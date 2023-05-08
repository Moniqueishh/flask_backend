from app import app
# from .models import User
from flask import render_template, request
from .auth.forms import SearchCity
import requests, json



@app.route('/', methods=['GET', 'POST'])
def homePage():
    form = SearchCity()
    if request.method == "POST":
        print("Button workss!")
        if form.validate():
            cityName = form.cityName.data
            print(cityName)

            return render_template('index.html', form=form)
        else:
            return "The city you're looking for does not exist."
    return render_template('index.html', form=form)

#We can add the search route here since no authentication is needed to search

@app.route('/search', methods=["GET", "POST"])
def searchPage():
    form = SearchCity()
    if request.method == "POST":
        # print("Button workss!")
        if form.validate():
            cityName = form.cityName.data
            print(cityName)

            url = 'https://api.openweathermap.org/data/2.5/weather?units=imperial&q={cityName}&appid=dc3ef453ab3d9fcae3c05cb7809a765b'
            response = requests.get(url)
            if response.ok:
                my_weather_dict = response.json()
                weather_dict = {}
                weather_dict["Temp"] = my_weather_dict["main"]["temp"]


                return render_template("results.html", form = form, weather_dict = weather_dict)


            else:
                return "The city you're looking for does not exist."

    return render_template('search.html', form = form)

#But we need to add authorization to be able to save trips only to users signed in. 
# @login_required for the heart button to show up to save trips
#So the HTML jinja needs to reflect:
#if user is authorized...... show heart or "save trip"
