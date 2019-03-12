from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from photogur.models import Picture, Comment
from photogur.forms import LoginForm, PictureForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/home/')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/home/')
    else:
        form = UserCreationForm()
    html_response = render(request, 'signup.html', {'form': form})
    return HttpResponse(html_response)


@login_required
def picture_create(request):
    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            form.user = request.user
            form.save()
            return HttpResponseRedirect('/home')
    else:
        form = PictureForm()
    html_response = render(request, 'create_picture.html', {'form': form})
    return HttpResponse(html_response)
