import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render

from MainApp.models import Country
from MainApp.models import Language

# Create your views here.
def home(request):
    return render(request, "index.html")


def name(request):
    return render(request, "name.html")


def countries_list(request):
    # with open('countries.json') as f:
    #     country = json.load(f)
    country = Country.objects.all()
    context = {
        "country": country

    }
    return render(request, "countries_list.html", context)



def languages_list(request):
    # with open('countries.json') as f:
    #     country = json.load(f)
    language = Language.objects.all()


    context = {
        "language": language
    }
    # def f(country):
    #     n = []
    #     for i in country:
    #         if i not in n:
    #             n.append(i)
              
    #     context = {
    #          "country": country
    #
    # }
    return render(request, "languages_list.html", context)


def country_page(request, id):
    try:
        country = Country.objects.get(id=id)
        languages = country.languages.all()
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Товар с id {id} не найден")
    context = {
        "country": country,
        "languages": languages
    }
    return render(request, "country_page.html", context)
