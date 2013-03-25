from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response

from photos.models import Photo
from photos.forms import PhotoForm

def index(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = Photo(image = request.FILES['image'])
            photo.save()

            return HttpResponseRedirect(reverse('photos:index'))
    else:
        form = PhotoForm()

    photos = Photo.objects.all()

    return render_to_response(
        'photos/index.html',
        {'photos': photos, 'form': form},
        context_instance=RequestContext(request)
    )
