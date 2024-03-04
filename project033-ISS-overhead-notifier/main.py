import requests
import datetime as dt
import pytz
import smtplib
import time

MY_LAT = 2.943140
MY_LONG = 101.719002

EMAIL = "XXX@gmail.com"
PASSWORD = "abc123"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()["results"]
    timezone_my = pytz.timezone('Asia/Kuala_Lumpur')

    sunrise_utc = data["sunrise"]
    sunrise_my = dt.datetime.fromisoformat(sunrise_utc).astimezone(timezone_my)
    sunrise_my_hour = int(str(sunrise_my).split()[1].split(":")[0])

    sunset_utc = data["sunset"]
    sunset_my = dt.datetime.fromisoformat(sunset_utc).astimezone(timezone_my)
    sunset_my_hour = int(str(sunset_my).split()[1].split(":")[0])

    hour_now = dt.datetime.now().hour

    if hour_now > sunset_my_hour or hour_now < sunrise_my_hour:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            email_message = (f"Subject:ISS Overhead Notification Alert !!! \n\n"
                             f"Look up !! ISS is above you in the sky!!")
            connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=email_message)
            print(dt.datetime.now())
            print(email_message)
