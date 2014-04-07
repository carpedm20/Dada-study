from django.db import models
from django.utils.encoding import smart_unicode

from account.models import Student
from board.models import Board
from tag.models import Tag

# Create your models here.
class StudyGroup(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=300)

    student_set = models.ManyToManyField(Student, blank=True, null=True)
    event_set = models.ManyToManyField('Event', blank=True, null=True)
    tag_set = models.ManyToManyField(Tag, blank=True, null=True)
    board_set = models.ManyToManyField(Board, null=True)

    creator = models.ForeignKey(Student, related_name='study_group_creator')
    leader = models.ManyToManyField(Student, related_name='leader')

    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=30)
    details = models.CharField(max_length=50)

    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)

    allDay = models.BooleanField(default=True)

    creator = models.ForeignKey(Student, related_name='event_creator')
    assigned_to = models.ManyToManyField(Student, related_name='assigned_to')

    tag_set = models.ManyToManyField(Tag, blank=True, null=True)

    def __unicode__(self):
        #return "[%] %s" % (smart_unicode(self.name), self.details)
        return smart_unicode(self.name)
