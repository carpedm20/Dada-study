from django.db import models

from core.models import StudyGroup
from account.models import Student
from tag.models import Tag

class Event(models.Model):
    name = models.CharField(max_length=30)
    details = models.CharField(max_length=50, blank=True)

    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)

    allDay = models.BooleanField(default=True)

    creator = models.ForeignKey(Student, related_name='event_creator')
    assigned_to = models.ManyToManyField(Student, related_name='assigned_to')
    finished_student = models.ManyToManyField(Student, related_name='finished_student')

    study_group = models.ForeignKey(StudyGroup, null=True)
    tag_set = models.ManyToManyField(Tag, blank=True, null=True)

    def __unicode__(self):
        #return "%s : %s ~ %s" % (self.name, self.start, self.end)
        return "%s" % (self.name)
