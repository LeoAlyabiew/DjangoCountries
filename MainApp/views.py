import json
from django.shortcuts import render
from django.views import View
from MainApp.models import Country, Language


# Create your views here.
def home(request):
    return render(request, 'index.html')


def countries_list(request):
    countries = Country.objects.all()

    return render(request, 'countries-list.html', {'countries': countries})


def countries_list_detail(request, country_name):
    country = Country.objects.get(name=country_name)
    languages = country.languages.all()

    return render(request, 'countries-list-detail.html', {
        'country_name': country_name,
        'languages': languages,
    })


def languages_list(request):
    result = Language.objects.all().order_by('name')

    return render(request, 'languages-list.html', {'languages': result})


def languages_list_detail(request, language_name):
    language = Language.objects.get(name=language_name)
    countries = language.country_set.all()

    return render(request, 'languages-list-detail.html', {
        'countries': countries,
        'language': language_name,
    })
