from twisted.protocols import basic
from twisted.web.websockets import WebSocketsResource, WebSocketsProtocol, lookupProtocolForFactory
import os
import json
from django.utils.html import escape


class MyChat(basic.LineReceiver):

    def __init__(self):
        self.user_name = None
        self.current_room = None
        self.live_room = None

    def connectionMade(self):
        print "User connected"
        packet = {'type': "message", 'content': "Welcome!", 'sender': "system"}

        self.transport.write(packet)
        self.factory.clients.append(self)

    def connectionLost(self, reason):
        print "User disconnected"
        if self.current_room is not None:
            packet = {'type': "leave", 'content': self.user_name, 'sender': "system"}
            json_dump = json.dumps(packet)

            for c in self.factory.live_rooms[self.current_room.name].clients:
                c.message(json_dump)

            self.factory.live_rooms[self.current_room.name].clients.remove(self)
        else:
            self.factory.clients.remove(self)

    def dataReceived(self, data):

        packet = json.dumps(data)

        if packet['type'] == "join":
            self.set_user_and_room(packet['content'])
            self.enter_room()

            for item in self.factory.live_rooms[self.current_room.name].messages:
                self.message(item)
            return

        if packet['type'] == "message":
            packet['message'] = escape(packet['message'])
            if self.current_room is not None:
                self.factory.live_rooms[self.current_room.name].messages.append(data)
            else:
                self.transport.write("Error, room not found")
                self.transport.write("Disconnecting")

        for c in self.factory.live_rooms[self.current_room.name].clients:
            c.message(data)

        if packet['type'] == 'flag':
            print 'to flag user'

    def message(self, message):
        self.transport.write(message)

    def set_user_and_room(self, content):

        self.user_name = content['userName']
        self.current_room = ChatRoom.objects.get(pk=content['room'])
        self.factory.clients.remove(self)
        print(content['userName'] + ' joining ' + content['room'])

    def enter_room(self):
        if self.current_room.name not in self.factory.live_rooms:
            self.factory.live_rooms[self.current_room.name] = LiveRoom()

        self.factory.live_rooms[self.current_room.name].clients.append(self)

        packet = {'type': "join", 'content': {'userName': self.user_name, 'room': self.current_room.name},
                  'sender': "system"}
        json_packet_send = json.dumps(packet)

        packet2 = {'type': "join", 'content': {'userName': self.user_name, 'room': self.current_room.name},
                   'sender': "system"}

        for c in self.factory.live_rooms[self.current_room.name].clients:
            c.message(json_packet_send)
            if c is not self:
                packet2['content']['userName'] = c.user_name
                self.message(json.dumps(packet2))

    @staticmethod
    def resize_chat_messages(messages, start):
        temp = []
        for x in range(start, len(messages)):
            temp.append(messages[x])
        return temp



#Twisted imports
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.internet import protocol
from twisted.application import service, internet
from twisted.internet.protocol import Factory

#Django environment integration
os.environ['DJANGO_SETTINGS_MODULE'] = 'scribble.settings'
import django
django.setup()
from geoChat.models import ChatRoom
from django.contrib.auth.forms import User


print(ChatRoom.objects.all())

class LiveRoom(object):
    def __init__(self):
        self.messages = []
        self.clients = []

class ChatFactory(Factory):
    protocol = MyChat
    clients = []
    live_rooms = {}
    rooms = ChatRoom.objects.all()
    print "initializing groups: " + str(rooms)

resource = WebSocketsResource(lookupProtocolForFactory(ChatFactory()))
root = Resource()

root.putChild("ws", resource)

application = service.Application("chatserver")

internet.TCPServer(8026, Site(root)).setServiceParent(application)

