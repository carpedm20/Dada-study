import os
from django.conf import settings
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.decorators.http import require_POST
from jfu.http import upload_receive, UploadResponse, JFUResponse

from .models import File
from board.models import Post

@require_POST
def upload(request, study_group_id=None):
    file = upload_receive( request )

    instance = File(file=file)
    instance.save()

    basename = os.path.basename( instance.file.path )

    file_dict = {
        'name' : basename,
        'size' : file.size,

        'url': settings.MEDIA_URL + basename,
        'thumbnailUrl': settings.MEDIA_URL + basename,

        'deleteUrl': reverse('jfu_delete', kwargs = { 'pk': instance.pk }),
        'deleteType': 'POST',
    }

    return UploadResponse( request, file_dict )

@require_POST
def upload_delete( request, study_group_id=None, pk=None ):
    success = True
    try:
        instance = File.objects.get( pk = pk )
        os.unlink( instance.file.path )
        instance.delete()
    except File.DoesNotExist:
        success = False

    return JFUResponse( request, success )
