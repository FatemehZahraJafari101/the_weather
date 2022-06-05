from django.shortcuts import render,redirect

from .forms import WeatherForm
import requests





def index(request):
    
    form = WeatherForm()
    weather = ''
    
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            form.save()
            

            selected_project_id = form.cleaned_data["city"]
            request.session['selected_project_id'] = selected_project_id

            
            key = '9680a76846da5ac1bbf6dcebad08e200'
            url =  'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'.format(selected_project_id,key)
            r = requests.get(url).json()
            t = r
            

            
            weather = {
                'City' : t['name'],
                'Temperature' : t['main']['temp'],
                'Description' : t['weather'][0]['description'],
                'Icon' : t['weather'][0]['icon'],

            }
    
        
    context = {'form':form , 'Weather' : weather}

    return render(request, 'index.html',context)
