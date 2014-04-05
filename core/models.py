from django.db import models
from django.utils.encoding import smart_unicode

from account.models import Student
from board.models import Board

# Create your models here.
class StudyGroup(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=300)

    user_set = models.ManyToManyField(Student, blank=True, null=True)
    event_set = models.ManyToManyField('Event', blank=True, null=True)
    tag_set = models.ManyToManyField('Tag', blank=True, null=True)
    board_set = models.ManyToManyField(Board, null=True)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=30)
    details = models.CharField(max_length=50)

    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)

    allDay = models.BooleanField(default=True)

    creator = models.ForeignKey(Student)

    def __unicode__(self):
        #return "[%] %s" % (smart_unicode(self.name), self.details)
        return smart_unicode(self.name)

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(Student)

    def __unicode__(self):
        return self.name
