from django.db import migrations
import json
from MainApp.models import Country


def save_data_to_db(param1, param2):
    with open("././country-by-languages.json", "r") as file:
        countries = json.load(file)

    for country_data in countries:
        country, _ = Country.objects.get_or_create(name=country_data['country'])


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial')
    ]

    operations = [
        migrations.RunPython(save_data_to_db)
    ]
