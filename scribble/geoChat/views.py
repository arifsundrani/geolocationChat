from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from geoChat.models import Page, Comment, RegionCoordinates
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.generic import FormView
<<<<<<< HEAD
from django.core.exceptions import ValidationError
from django import forms
=======
>>>>>>> origin/master
import sys
from django.template import Context, Template
from django.db.models import F
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
    #chat_rooms = ChatRoom.objects.filter(lat1__lte= float(request.POST.get('lat',False))).filter(long1__lte= request.POST.get('long',False)).filter(lat2__gte= request.POST.get('lat',False)).filter(long2__gte= request.POST.get('long',False)).order_by('name')
    chat_rooms1 = ChatRoom.objects.all()
    chat_rooms = []
    print float(request.POST.get('lat',False))
    for e in chat_rooms1:
        # print str(e.name) + '  ' + str(e.lat1)
        # print str(e.name) + '  ' + str(e.lat2)
        if e.lat1 <= float(request.POST.get('lat',False)) and e.lat2 >= float(request.POST.get('lat',False)) and e.long1 <= float(request.POST.get('long',False)) and e.long2 >= float(request.POST.get('long',False)):
            chat_rooms.append(e)



    #chat_rooms = ChatRoom.objects.order_by('name')[:8]
    if chat_rooms.__len__() == 0:
        list=[1,2]
        bools = {
            'noChat': list
        }
        return render(request, 'chats/createChat.html', bools)
    first = get_object_or_404(ChatRoom, pk=request.POST.get('chat_room_id',False))
    context = {
        'chat_rooms': chat_rooms,
        'first': first,
    }
    return render(request, 'chats/chat_room.html', context)

def showSettings(request):
	return render(request, 'settings.html')

def createNewChat(request):
    bools = {
    }
    return render(request, 'chats/createChat.html',bools)

def createRoom(request):
    RA = request.POST.copy()
    a = float(RA.get('lat',False))
    a1 = a - 1.0

    b = float(RA.get('long', False))
    b1 = b - 1

    c =  float(RA.get('lat',False))
    a2 = c +1

    d = float(RA.get('long',False))
    b2 = d + 1
    c = ChatRoom(name= request.POST.get('chat_name',False), lat1 = a1, long1 = b1, lat2 = a2,long2 = b2,)
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
<<<<<<< HEAD
        login(self.request, user)
        return super(CreateRegisterView, self).form_valid(form)


=======
        if validateEmail(self.request.POST['email']):
            login(self.request, user)
            return super(CreateRegisterView, self).form_valid(form)
        else:
            raise ValidationError("Email address is not real")

        return super(CreateRegisterView, self)
>>>>>>> origin/master

def create_chat_room(request):
    return HttpResponseRedirect('/')

def validateEmail(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
<<<<<<< HEAD
        return False

def password_reset(request):
    return password_reset(request)
=======
        return False
>>>>>>> origin/master
