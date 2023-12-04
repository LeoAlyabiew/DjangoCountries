import json
from django.shortcuts import render
from django.views import View
from MainApp.models import Country


# Create your views here.
def home(request):
    return render(request, 'index.html')


def countries_list(request):
    countries = Country.objects.all()

    return render(request, 'countries-list.html', {'countries': countries})


def countries_list_detail(request, country_name):
    with open('./country-by-languages.json', 'r') as countries:
        data = json.load(countries)
        result = []
        for item in data:
            if item['country'] == country_name:
                result = item['languages']
                break

    return render(request, 'countries-list-detail.html', {
        'country_name': country_name,
        'languages': result,
    })


def languages_list(request):
    with open('./country-by-languages.json', 'r') as countries:
        data = json.load(countries)
        result = []
        for item in data:
            result += item['languages']
        _result = set(result)
        result = list(_result)
        result = sorted(result)

    return render(request, 'languages-list.html', {'languages': result})
