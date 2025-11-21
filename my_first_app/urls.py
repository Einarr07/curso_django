"""
URL configuration for curso_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path

from my_first_app.models import Author


def my_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("Hello, world.")


def author_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    author = Author.objects.get(id=kwargs['id'])
    profile = author.profile
    return HttpResponse(
        f"Author: {author.name} - Birth Date: {author.birth_date} -\nWebsite: {profile.website} - Biography: {profile.biography}")


urlpatterns = [
    path('listado/', my_view),
    path('detalle/<int:id>', my_view),
    path('marcas/<str:brand>', my_view),

    path('autor/<int:id>', author_view),
]
