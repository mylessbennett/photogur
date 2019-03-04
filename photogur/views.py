from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from photogur.models import Picture


def pictures(request):
    context = {'pictures': Picture.objects.all()}
    response = render(request, 'pictures.html', context)
    return HttpResponse(response)


def picture_show(request, id):
    picture = get_object_or_404(Picture, pk=id)
    context = {'picture': picture}
    response = render(request, 'picture.html', context)
    return HttpResponse(response)
