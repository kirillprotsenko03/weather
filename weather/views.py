from django.shortcuts import render
from .forms import CityForm
from .models import City
import requests

# Create your views here.


def index(request):

    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=0bbd03de432dd3b7016b590f24bb1f72'
        r = requests.get(url.format(city), timeout=5).json()
        city_weather = {
            'city': city.city,
            'temperature': r['main']['temp'],
            'icon': r['weather'][0]['icon'],
            'description': r['weather'][0]['description']
        }
        weather_data.append(city_weather)
    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/index.html', context)
