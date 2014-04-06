from django.db import models

from core.models import Student

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=200)
    details = models.CharField(max_length=300)

    post_set = models.ManyToManyField('Post', blank=True, null=True)

    creator = models.ForeignKey(Student)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(blank=False)

    tag_set = models.ManyToManyField('PostTag', blank=True, null=True)

    creator = models.ForeignKey(Student)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(blank=False)

    creator = models.ForeignKey(Student)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

class PostTag(models.Model):
    name = models.CharField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
