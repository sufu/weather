import smtplib
import weather
import mailer

def get_emails():
    emails = {}

    try:
        emails_file = open('./info/emails.txt', 'r')

        for line in emails_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err)

    return emails

def get_cities():
    cities = []

    try:
        cities_file = open('./info/cities.txt', 'r')

        for line in cities_file:
            cities.append(line.strip())
    except FileNotFoundError as err:
        print(err)

    return cities


def get_schedule():
    try:
        schedule_file = open('./info/schedule.txt', 'r')
        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)

    return schedule


def main():
    emails = get_emails()
    print(emails)

    cities = get_cities()
    print(cities)
    #schedule = get_schedule()
    #print(schedule)

    forecasts = weather.get_weather_forcast(cities)
    print(forecasts)

    #mailer.send_emails(emails, schedule, forecast)
    mailer.send_emails(emails, forecasts)

main()
