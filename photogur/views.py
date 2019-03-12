from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from photogur.models import Picture, Comment
from photogur.forms import LoginForm
from django.contrib.auth import authenticate, login


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


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()

    context = {'form': form}
    http_response = render(request, 'login.html', context)
    return HttpResponse(http_response)
