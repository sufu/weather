import requests
def get_weather_forcast():
    # Connecting to weather api
    try:
        api_id = open('appid.txt', 'r').read().strip()
        print(api_id)
    except FileNotFoundError as err:
        print(err)

    url = 'http://api.openweathermap.org/data/2.5/weather?q=SanJose&units=metric'
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
    forecast = 'The foreast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min)) + '.'

    return forecast
