from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from geoChat.models import Page, Comment, RegionCoordinates
from django.core.urlresolvers import reverse
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class HomeView(RegionCoordinates):
    model = RegionCoordinates
    template_name = 'base.html'

class  ChatView(object):
	"""docstring for  ChatView"""
	def __init__(self, arg):
		super( ChatView, self).__init__()
		self.arg = arg

class ProfileView(object):
	"""docstring for ProfileView"""
	def __init__(self, arg):
		super(ProfileView, self).__init__()
		self.arg = arg
		
class ChatListView(object):
	"""docstring for ChatListView"""
	def __init__(self, arg):
		super(ChatListView, self).__init__()
		self.arg = arg

class SettingsView(object):
			"""docstring for SettingsView"""
			def __init__(self, arg):
				super(SettingsView, self).__init__()
				self.arg = arg

class CreateChatView(object):
	"""docstring for CreateChatView"""
	def __init__(self, arg):
		super(CreateChatView, self).__init__()
		self.arg = arg