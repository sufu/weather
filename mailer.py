import smtplib
from datetime import date

today = date.today().strftime("%m/%d/%y")

#def send_emails(emails, schedule, forecast):
def send_emails(emails, forecasts):
    # connec to smtp server
    server = smtplib.SMTP('smtp.gmail.com', 587)

    #start TLS encryption
    server.starttls()

    try:
        password = open('./info/password.txt', 'r').read()
        print(password)
    except FileNotFoundError as err:
        print(err)

    from_email = 'python.weather.forecast@gmail.com'
    server.login(from_email, password)

    for to_email in emails:
        message = 'Subject: Weather Forecasts today!\n'
        message += 'Hi ' + emails[to_email] + '!\n\n'
        message += 'Weather forecasts for today ' + today +':\n\n\n'
        for forecast in forecasts:
            message += forecast + '\n'
        message += '\n\nInfo provided by Robert Fu'
        #message += schedule + '\n\n'
        #print(message)
        server.sendmail(from_email, to_email, message)
    server.quit()
