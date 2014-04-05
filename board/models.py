from django.db import models

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=300)
    foo = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea
