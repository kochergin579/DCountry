from django.shortcuts import render, HttpResponse, redirect
import json
from MainApp.models import Country
from django.http import HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from MainApp.models import Language


# Create your views here.
def home(request):
    return render(request, "index.html")

def name(request):

    return render(request, "name.html")



def countries_list(request):
    countries = Country.objects.all()
    context = {
        "countries": countries

    }
    return render(request, "countries_list.html", context)



def languages_list(request):
    with open('countries.json') as f:
        country = json.load(f)
        

    context = {
       "country" : country

            }
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
            










