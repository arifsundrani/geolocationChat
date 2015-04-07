from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.db import models
from django.contrib.auth.forms import User
from django.utils import timezone
from geoChat.models import Comment, ChatRoom, Page, RegionCoordinates

#Models
class RegionCoordinatesTest(TestCase):
    def test_region_was_made(self):
        z = RegionCoordinates.objects.create(x1 = 1, x2 = 2, y1 = 1, y2 = 2)
        z.save()
        self.assertEqual(z.x1, 1)
        self.assertEqual(z.x2, 2)
        self.assertEqual(z.y1, 1)
        self.assertEqual(z.y2, 2)

class ChatRoomTest(TestCase):
    def test_room_was_made(self):
        a = ChatRoom.objects.create(name = 'Emory')
        a.save()
        self.assertEqual(a.name, 'Emory')
        self.assertEqual(a.active, True)

class PageModelTest(TestCase):
    def test_page_was_made(self):
        b = Page.objects.create(createDate = timezone.now(), topic = 'Testing', location = RegionCoordinates.objects.create(x1 = 1, x2 = 2, y1 = 1, y2 = 2))
        b.save()
        self.assertEqual(b.topic, 'Testing')

class CommentTest(TestCase):
    def test_comment_was_made(self):
        c = Comment.objects.create(text='This chat room is wicked cool.', postDate=timezone.now(), user_name='AnonymousUser')
        c.save()
        self.assertEqual(c.user_name, 'AnonymousUser')
        self.assertEqual(c.active, True)
        self.assertEqual(c.text, 'This chat room is wicked cool.')

#Views
class IndexTest(TestCase):
    def test_index(self):
        x = Client()
        response = x.post('/index/',{'username':'arif','password1':'nope', 'password2': 'nope'})

class ChatRoomView(TestCase):
    def test_chat_room(self):
        y = Client()
        response = y.post('/chats/1/',{'username':'arif','password1':'nope', 'password2': 'nope'})

class SettingsTest(TestCase):
    def test_settings(self):
        w = Client()
        response = w.post('/showSettings/',{'username':'arif','password1':'nope', 'password2': 'nope'})

class CreateNewChatView(TestCase):
    def test_create_chat(self):
        z = Client()
        response = z.post('/createChat/',{'username':'arif','password1':'nope', 'password2': 'nope'})

#I don't think the test below is correct, need to do further testing.
class CreateRoomView(TestCase):
    def test_create_chat_room(self):
        a = Client()
        response = a.post('/createRoom/',{'username':'arif','password1':'nope', 'password2': 'nope'})

class RegisterTest(TestCase):
    def test_register(self):
        v = Client()
        response = v.post('/register/',{'username':'arif','password1':'nope', 'password2': 'nope'})

class LoginTest(TestCase):
    def test_login(self):
        u = Client()
        response = u.post('/login/',{'username':'test','password':'nope'})




