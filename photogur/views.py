from django.http import HttpResponse
from django.shortcuts import render
from photogur.models import Picture


def pictures(request):
    context = {'pictures': Picture.objects.all()}
    response = render(request, 'pictures.html', context)
    return HttpResponse(response)
