from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from photos.models import Photo
from photos.forms import PhotoForm

def index(request):
    photos = Photo.objects.all()

    return render_to_response(
        'photos/index.html',
        {'photos': photos},
        context_instance=RequestContext(request)
    )

@login_required
def new(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = Photo(
                title = form.cleaned_data['title'],
                image = request.FILES['image'],
            )
            photo.save()

            return HttpResponseRedirect(reverse('photos:index'))
    else:
        form = PhotoForm()

    return render_to_response(
        'photos/new.html',
        {'form': form},
        context_instance=RequestContext(request)
    )
