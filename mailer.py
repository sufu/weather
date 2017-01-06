import smtplib

def send_emails(emails, schedule, forecast):
    # connec to smtp server
    server = smtplib.SMTP('smtp.gmail.com', 587)

    #start TLS encryption
    server.starttls()

    try:
        password = open('password.txt', 'r').read()
        print(password)
    except FileNotFoundError as err:
        print(err)

    from_email = 'python.weather.forecast@gmail.com'
    server.login(from_email, password)

    for to_email in emails:
        message = 'Subject: Welcome to the Forecast!\n'
        message += 'Hi ' + emails[to_email] + '!\n\n'
        message += forecast + '\n\n'
        message += schedule + '\n\n'
        server.sendmail(from_email, to_email, message)
    server.quit()
