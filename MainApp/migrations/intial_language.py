from django.db import migrations
import json
from MainApp.models import Country, Language


def save_data_to_db(param1, param2):
    with open("././country-by-languages.json", "r") as file:
        countries = json.load(file)

    for country_data in countries:
        country, _ = Country.objects.get_or_create(name=country_data['country'])
        for language_data in country_data["languages"]:
            language, _ = Language.objects.get_or_create(name=language_data)
            if language not in country.languages.all():
                country.languages.add(language)
        country.save()


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_language_country_languages')
    ]

    operations = [
        migrations.RunPython(save_data_to_db)
    ]
