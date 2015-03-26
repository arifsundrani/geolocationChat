from twisted.protocols import basic
from twisted.web.websockets import WebSocketsResource, WebSocketsProtocol, lookupProtocolForFactory
import os


class MyChat(basic.LineReceiver):

    def __init__(self):
        self.user_name = None
        self.current_room = None
        self.live_room = None

    def connectionMade(self):
        print "User connected"
        self.transport.write('Welcome! \n')
        self.factory.clients.append(self)

    def connectionLost(self, reason):
        print "User disconnected"
        if self.current_room is not None:
            self.factory.live_rooms[self.current_room.name].clients.remove(self)
        else:
            self.factory.clients.remove(self)

    def dataReceived(self, data):

        if data[0:3] != '<b>':
            self.set_user_and_room(data)
            self.enter_room()

            for item in self.factory.live_rooms[self.current_room.name].messages:
                self.message(item)
            return

        if self.current_room is not None:
            self.factory.live_rooms[self.current_room.name].messages.append(data)
        else:
            self.transport.write("Error, room not found")
            self.transport.write("Disconnecting")

        for c in self.factory.live_rooms[self.current_room.name].clients:
            c.message(data)

    def message(self, message):
        self.transport.write(message + '\n')

    def set_user_and_room(self, data):
        split = data.split(':-:')
        self.user_name = split[0]
        self.current_room = ChatRoom.objects.get(name=split[1])
        self.factory.clients.remove(self)
        print(split[0] + ' joining ' + split[1])

    def enter_room(self):
        if self.current_room.name in self.factory.live_rooms:
            self.factory.live_rooms[self.current_room.name].clients.append(self)
        else:
            self.factory.live_rooms[self.current_room.name] = LiveRoom()
            self.factory.live_rooms[self.current_room.name].clients.append(self)


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

internet.TCPServer(1025, Site(root)).setServiceParent(application)

