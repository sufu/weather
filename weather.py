import requests
#cities = ['San Jose', 'Milpitas', 'Santa Clara']
def get_weather_forcast(cities):
    forecasts = []

    # Connecting to weather api
    try:
        api_id = open('./info/appid.txt', 'r').read().strip()
        print(api_id)
    except FileNotFoundError as err:
        print(err)

    # for each city
    for city in cities:
        city_format = "".join(city.split())

        url = 'http://api.openweathermap.org/data/2.5/weather?q='
        url += city_format
        url += '&units=metric'
        url += api_id
        print(url)

        weather_request = requests.get(url)
        weather_json = weather_request.json()
        print(weather_json)

        # Parsing JSON
        description = weather_json['weather'][0]['description']
        temp_min = weather_json['main']['temp_min']
        temp_max = weather_json['main']['temp_max']

        # Creating the forecast
        forecast = city + ':  ' + description + ', '
        forecast += str(int(temp_min)) + ' ~ '+ str(int(temp_max)) + ' C\n'

        forecasts.append(forecast)

    return forecasts

#print(get_weather_forcast(cities))
