from django.db import models
from account.models import Student

# Create your models here.
class StudyGroup(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=300)

    user_set = models.ManyToManyField(Student, null=True)

    tag_set = models.ManyToManyField('Tag', null=True)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
