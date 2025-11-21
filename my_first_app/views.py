from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from my_first_app.models import Car, Author


# Create your views here.
def car_view(request):
    car_list = Car.objects.all()
    context = {
        "car_list": car_list
    }
    return render(request, "my_first_app/car_list.html", context)


class CarListView(TemplateView):
    template_name = "my_first_app/car_list.html"

    def get_context_data(self, **kwargs):
        car_list = Car.objects.all()
        return {
            "car_list": car_list
        }


def my_test_view(request, *args, **kwargs):
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
