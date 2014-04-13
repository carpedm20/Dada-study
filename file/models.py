from django.db import models
from django.core.files.storage import FileSystemStorage

from board.models import Board, Post

fs = FileSystemStorage(location='/media/photos')

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to=fs)
    slug = models.SlugField(max_length=50, blank=True)

    post = models.ForeignKey(Post, blank=True, null=True)

    def __unicode__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(File, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.file.delete(False)
        super(File, self).delete(*args, **kwargs)
