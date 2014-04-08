import uuid
import base64

from django.db import models
from django.utils.encoding import smart_unicode

from account.models import Student
from board.models import Board
from tag.models import Tag
from event.models import Event

# Create your models here.
class StudyGroup(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=300)

    student_set = models.ManyToManyField(Student, blank=True, null=True, related_name='studygroup_set')
    bookmarked_student_set = models.ManyToManyField(Student, blank=True, null=True, related_name='bookmarked_student_set')

    event_set = models.ManyToManyField(Event, blank=True, null=True)
    tag_set = models.ManyToManyField(Tag, blank=True, null=True)
    board_set = models.ManyToManyField(Board, null=True)

    creator = models.ForeignKey(Student, related_name='study_group_creator')
    leader = models.ManyToManyField(Student, related_name='leader')

    unique_id = models.CharField(max_length=100, null=True, blank=True, unique=True)

    #def __init__(self, *args, **kwargs):
    #    super(StudyGroup, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.unique_id = base64.b64encode(str(uuid.uuid4()))[:10]
        super(StudyGroup, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
