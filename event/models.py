from django.db import models

from account.models import Student
from tag.models import Tag

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
