from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


#REST
from django.conf.urls import url, include
from django.contrib.auth.models import User
#from rest_framework import routers, serializers, viewsets

#twisted
from django.views.generic import RedirectView

from views import index, chat_room

urlpatterns = patterns('',
        url(r'^$', index, name='index'),
        url(r'^(?P<chat_room_id>\d+)/$', chat_room, name='chat_room'),
)