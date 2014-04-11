from django.db import models
from django.core.files.storage import FileSystemStorage

from board.models import Board, Post, 

fs = FileSystemStorage(location='/media/photos')

# Create your models here.
def File(models.Model):
    name = models.CharField(max_length=200)

    post = models.ForeignKey(Post, blank=True, null=True)

    
