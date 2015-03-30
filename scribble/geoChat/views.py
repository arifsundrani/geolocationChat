from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from geoChat.models import Page, Comment, RegionCoordinates
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from models import ChatRoom



def index(request):
    chat_rooms = ChatRoom.objects.order_by('name')[:5]
    context = {
        'chat_list': chat_rooms,
    }
    return render(request,'chats/index.html', context)

def chat_room(request, chat_room_id):
    chat = get_object_or_404(ChatRoom, pk=chat_room_id)
    return render(request, 'chats/chat_room.html', {'chat': chat})

def showSettings(request):
	return render(request, 'settings.html')
	
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

'''
class showSettings(View):
    def get(self, request):
        return render(request, 'settings.html')


class HomeView(CreateView):
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
'''