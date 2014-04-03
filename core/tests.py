from django.test import TestCase
from django.contrib.auth.models import User

from .models import StudentGroup, Tag
from account.models import Student
from school.models import School

class StudnetGroupTestCase(TestCase):
    def setUp(self):
        unist = School(name="UNIST")
        kaist = School(name="KAIST")
        postech = School(name="POSTECH")

        user = User(username="hello@gmail.com", password="123")
        Student.objects.create(user=user, school=unist)

        user = User(username="serious@gmail.com", password="123")
        Student.objects.create(user=user, school=postech)

        user = User(username="kaist@gmail.com", password="123")
        Student.objects.create(user=user, school=kaist)

        user = User(username="unist@gmail.com", password="123")
        Student.objects.create(user=user, school=unist)

        group = StudentGroup(name="TOEIC study", details="over 990")
        group.save()

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
# Create your tests here.
