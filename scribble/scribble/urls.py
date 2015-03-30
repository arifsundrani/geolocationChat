from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
import geoChat.views

#REST
from django.conf.urls import url, include
from django.contrib.auth.models import User
#from rest_framework import routers, serializers, viewsets

#twisted
from django.views.generic import RedirectView

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
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url('^register/', CreateView.as_view(
    	template_name='registration/register.html',
    	form_class=UserCreationForm,
    	success_url='/login' #have a login_redirect that logs people in? if you dont have the right data redirect people to login page?
    	), name='register'),
    url(r'^settings/$', geoChat.views.showSettings, name = 'settings'),#.as_view(), name = 'settings'),
    url('^changepass/', CreateView.as_view(
    	template_name='settings/password.html',
    	form_class=PasswordChangeForm,
    	success_url='/'
    	), name='password'),

    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^chats/', include('geoChat.urls')),
)




