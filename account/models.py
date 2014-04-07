from django.db import models
from django.contrib.auth.models import User

import hashlib

from school.models import * # School, Course
from core.models import * # 

class Student(models.Model):
    user = models.OneToOneField(User)

    school = models.ForeignKey(School, null=True)
    friends = models.ManyToManyField('self', symmetrical=True, null=True)

    def __unicode__(self):
        return self.user.username

    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.username).hexdigest()

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

class StudentGroup(models.Model):
    name = models.CharField(max_length=200)
    student_set = models.ManyToManyField(Student, null=True)

    def __unicode__(self):
        return self.name
