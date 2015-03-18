from django.conf.urls import patterns, include, url
from django.contrib import admin

#REST
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

#twisted
from django.views.generic import RedirectView


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'location',)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = patterns('',
    url(r'^(/)?$', RedirectView.as_view(url='/chat/')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^chat/', include('geoChat.urls')),
)
