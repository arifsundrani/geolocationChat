from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.db import models
from django.contrib.auth.forms import User
from django.utils import timezone
from geoChat.models import Comment

class CommentTest(TestCase):		
	def test_comment_was_made(self):
		c = Comment.objects.create(text = 'This chat room is wicked cool.', postDate = timezone.now(), name='AnonymousUser')
		c.save()
		self.assertEqual(c.name, 'AnonymousUser')
		self.assertEqual(c.text, 'This chat room is wicked cool.')
	
class LoginTest(TestCase):
	def test_login(self):
		u = Client()
		response = u.post('/login/',{'username':'arif','password':'nope'})
		response.status_code
	
class SignupViewTest(TestCase):
	def test_register(self):
		u = Client()
		response = u.post('/register/',{'username':'arif','password1':'nope', 'password2': 'nope'})
		response.status_code

#class ChatRoomViewTest(TestCase):
	