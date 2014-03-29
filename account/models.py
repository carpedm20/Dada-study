from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

from school.models import * # School, Course
from study.models import * # 

class StudentManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
           email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

# Create your models here.
class Student(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    school = models.ForeignKey(School, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = StudentManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return self.username

class Group(models.Model):
    name = models.CharField(max_length=200)
    user_set = models.ManyToManyField(Student, null=True)

    def __unicode__(self):
        return self.name
