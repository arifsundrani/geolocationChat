from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.db import models
from django.contrib.auth.forms import User
from django.utils import timezone
from geoChat.models import Comment, ChatRoom
#testing
#added comment


class ChatRoomTest(TestCase):
    def test_room_was_made(self):
        a = ChatRoom.objects.create(name = 'Emory')
        a.save()
        self.assertEqual(a.name, 'Emory')
        self.assertEqual(a.active, True)

class CommentTest(TestCase):
    def test_comment_was_made(self):
        c = Comment.objects.create(text='This chat room is wicked cool.', postDate=timezone.now(), user_name='AnonymousUser')
        c.save()
        self.assertEqual(c.user_name, 'AnonymousUser')
        self.assertEqual(c.active, True)
        self.assertEqual(c.text, 'This chat room is wicked cool.')

class LoginTest(TestCase):
    def test_login(self):
        u = Client()
        response = u.post('/login/',{'username':'test','password':'nope'})
        response.status_code

class RegisterTest(TestCase):
    def test_register(self):
        v = Client()
        response = v.post('/register/',{'username':'arif','password1':'nope', 'password2': 'nope'})
        response.status_code