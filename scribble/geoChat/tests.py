from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.db import models
from django.contrib.auth.forms import User
from django.utils import timezone
from geoChat.models import Comment

class CommentTest(TestCase):
	#def setUp(self):
		
	def test_comment_was_made(self):
		c = Comment.objects.create(text = 'This chat room is wicked cool.', postDate = timezone.now(), name='AnonymousUser')
		c.save()
		self.assertEqual(c.name, 'AnonymousUser')
		self.assertEqual(c.text, 'This chat room is wicked cool.')
	
#class LoginTest(TestCase):
#	c = Client()
#	response = c.post('/login/',{'username':'arif','password':'nope'})
#	response.status_code
	
#class SignupViewTest(TestCase):

#class ChatRoomViewTest(TestCase):
	