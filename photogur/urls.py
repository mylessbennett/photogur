"""photogur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from photogur.views import home, picture_show, root, picture_search, create_comment, login_view, logout_view, signup, picture_create, edit_picture

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root),
    path('home/', home, name='home_page'),
    path('pictures/<int:id>', picture_show, name='picture_details'),
    path('pictures/<int:id>/edit', edit_picture, name='edit'),
    path('search', picture_search, name='picture_search'),
    path('comments/new', create_comment, name='create_comment'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('create_picture', picture_create, name='create_picture'),
]
