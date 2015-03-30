from django.db import models
from django.contrib.auth.forms import User


# Create your models here.

class RegionCoordinates(models.Model):
    x1 = models.FloatField()
    y1 = models.FloatField()
    x2 = models.FloatField()
    y2 = models.FloatField()

class Page(models.Model):
    createDate = models.DateTimeField('date created')
    topic = models.CharField(max_length = 60)
    createUser = models.ForeignKey(User, blank=True, null=True)
    #createUser = models.User('created this user')
    location = models.ForeignKey(RegionCoordinates)

class Comment(models.Model):
    text = models.TextField()
    postDate = models.DateTimeField('date published')
    name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    spam = models.BooleanField(default=False)
    def __unicode__ (self):
        return self.text
    #poster = models.ForeignKey(User, blank=True, null=True)

#chat room


class ChatRoom(models.Model):

    name = models.CharField(max_length=50)
    chat_list = [Comment()]*200
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name
