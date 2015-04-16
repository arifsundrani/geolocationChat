from django.contrib.auth import logout
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
import geoChat.views

#REST
from django.conf.urls import url, include
from django.contrib import auth

from django.contrib.auth.models import User
#from rest_framework import routers, serializers, viewsets

#twisted
from django.views.generic import RedirectView
from django.contrib.auth.views import password_change, password_change_done


'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'location',)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
'''

urlpatterns = patterns('',
    url(r'^(/)?$', RedirectView.as_view(url='/chats/1/')),
    url('^home/', CreateView.as_view(
    	template_name='home.html',
    	form_class=UserCreationForm,
    	success_url='/'
    	), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', geoChat.views.logout_view, name="logout"),
    #url('^register/', CreateView.as_view(
    #	template_name='registration/register.html',
    #	form_class=UserCreationForm,
    #	success_url='/' #have a login_redirect that logs people in? if you dont have the right data redirect people to login page?
    #	), name='register'),
    url('^register/', geoChat.views.CreateRegisterView.as_view(),name='register'),
    #url(r'^password_reset/$', password_reset, {'template_name': 'registration/pass.html'}),

    url(r'^password_change/$', password_change, {'template_name':'registration/pass.html'}, name='password_change'),
    url(r'^password_change_done/', password_change_done,
            {'template_name':'registration/success.html'}, name = 'password_change_done'),



    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^chats/', include('geoChat.urls')),
    url(r'^chat_room/', geoChat.views.chat_room, name ='chat_room'),
    url(r'^chat_room2/', geoChat.views.chat_room2, name ='chat_room2'),
    url(r'^createChat/', geoChat.views.createNewChat, name ='createNewChat'),
    url(r'^chatRoom/', geoChat.views.createRoom, name ='createRoom'),
)




