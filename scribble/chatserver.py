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
        self.current_room_id = None

    def connectionMade(self):
        print "User connected"
        packet = {'type': "message", 'content': "Welcome!", 'sender': "system"}

        self.message(json.dumps(packet))
        self.factory.clients.append(self)

    def connectionLost(self, reason):
        print "User disconnected"
        if self.current_room is not None:
            packet = {'type': "leave", 'content': self.user_name, 'sender': "system"}
            json_dump = json.dumps(packet)

            for c in self.factory.live_rooms[self.current_room_id].clients:
                c.message(json_dump)

            self.factory.live_rooms[self.current_room_id].clients.remove(self)
        else:
            self.factory.clients.remove(self)

    def dataReceived(self, data):

        print "data: ", data
        packet = json.loads(data)  # parse json to python dict

        print "packet "+str(packet)
        print packet['type']

        # check to see what type of message it is
        if packet['type'] == "join":
            self.set_user_and_room(packet['content'])
            self.enter_room()

            # send existing messages to newly joined user
            for item in self.factory.live_rooms[self.current_room_id].messages:
                self.message(item)
            return

            # message: sanitize and send message to each user in same room
        if packet['type'] == "message":
            packet['content'] = escape(packet['content'])
            if self.current_room is not None:
                self.factory.live_rooms[self.current_room_id].messages.append(data)
                for c in self.factory.live_rooms[self.current_room_id].clients:
                    c.message(data)
                return
            else:
                self.transport.write("Error, room not found")
                self.transport.write("Disconnecting")
                self.factory.users.remove(self)
                return

        if packet['type'] == 'flag':
            print packet['sender'] + 'to flag user' + packet['content']

    def message(self, message):
        self.transport.write(message)

    def set_user_and_room(self, content):
        self.user_name = content['userName']
        self.current_room = ChatRoom.objects.get(pk=content['room'])
        self.current_room_id = content['room']
        self.factory.clients.remove(self)
        print(content['userName'] + ' joining ' + self.current_room_id)

    def enter_room(self):
        # access count increase
        if self.factory.access_count == 200:
            self.delete_unused_rooms()
            self.factory.live_rooms[self.current_room_id] = self.resize_chat_messages(self.factory.live_rooms[self.current_room_id], 50)
        else:
            self.factory.access_count += 1

        if self.current_room_id not in self.factory.live_rooms:
            self.factory.live_rooms[self.current_room_id] = LiveRoom()

        self.factory.live_rooms[self.current_room_id].clients.append(self)

        # packet to send to other users (this user entered your room)
        packet = {'type': "join", 'content': {'userName': self.user_name, 'room': self.current_room_id},
                  'sender': "system"}
        json_packet_send = json.dumps(packet)

        # packet to send to self (these people are already in your room)
        packet2 = {'type': "join", 'content': {'userName': self.user_name, 'room': self.current_room_id},
                   'sender': "system"}

        for c in self.factory.live_rooms[self.current_room_id].clients:
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

    # method to clear rooms
    def delete_unused_rooms(self):
        for key, value in self.factory.live_rooms:
            try:
                ChatRoom.objects.get(pk=key)
            except:
                del self.factory.live_rooms[key]




# Twisted imports
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
    access_count = 0
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

