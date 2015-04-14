from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from geoChat.models import Page, Comment, RegionCoordinates
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.generic import FormView
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate, models
from django.contrib.auth.forms import UserCreationForm
from models import ChatRoom
from django.utils import timezone

from django.contrib.auth.models import models



def index(request):
    chat_rooms = ChatRoom.objects.order_by('name')[:5]
    context = {
        'chat_rooms': chat_rooms,
    }
    return render(request,'chats/index.html', context)

def chat_room(request, chat_room_id):
    chat_rooms = ChatRoom.objects.order_by('name')[:6]
    first = get_object_or_404(ChatRoom, pk=chat_room_id)
    context = {
        'chat_rooms': chat_rooms,
        'first' : first,
    }
    return render(request, 'chats/chat_room.html', context)

def chat_room2(request):
    chat_rooms = ChatRoom.objects.order_by('name')[:8]
    first = get_object_or_404(ChatRoom, pk=request.POST.get('chat_room_id',False))

    context = {
        'chat_rooms': chat_rooms,
        'first' : first,
    }
    return render(request, 'chats/chat_room.html', context)

def showSettings(request):
	return render(request, 'settings.html')

def createNewChat(request):
    return render(request, 'chats/createChat.html')

def createRoom(request):
    c = ChatRoom(name= request.POST.get('chat_name',False), long = request.POST.get('long',False), lat = request.POST.get('lat',False))
    c.save()
    return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

class CreateRegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(CreateRegisterView, self).form_valid(form)

def create_chat_room(request):
    return HttpResponseRedirect('/')

#add view function to make new chat rooms
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