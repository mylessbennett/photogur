from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from photogur.models import Picture, Comment


def root(request):
    return HttpResponseRedirect('home')


def home(request):
    context = {'pictures': Picture.objects.all()}
    response = render(request, 'index.html', context)
    return HttpResponse(response)


def picture_show(request, id):
    picture = get_object_or_404(Picture, pk=id)
    context = {'picture': picture}
    response = render(request, 'picture.html', context)
    return HttpResponse(response)


def picture_search(request):
    query = request.GET['query']
    search_results = Picture.objects.filter(artist=query)
    context = {
        'pictures': search_results,
        'query': query
    }
    response = render(request, 'search_page.html', context)
    return HttpResponse(response)


def create_comment(request):

    Comment.objects.create(
        name=request.POST['name'],
        message=request.POST['message'],
        picture=Picture.objects.get(pk=request.POST['picture_id'])
    )
    return HttpResponseRedirect('/pictures/' + request.POST['picture_id'])
