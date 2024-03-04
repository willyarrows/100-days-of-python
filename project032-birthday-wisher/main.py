import datetime as dt
import random
import smtplib

import pandas as pd

EMAIL = "XXX@gmail.com"
PASSWORD = "abc123"

today = dt.datetime.today()
current_month, current_day = today.month, today.day

df_birthday = pd.read_csv("birthdays.csv")
for index, row in df_birthday.iterrows():
    if current_month == row['month'] and current_day == row['day']:
        random_letter = f"letter_{random.randint(1, 3)}.txt"
        with open(f"letter_templates/{random_letter}") as letter_file:
            birthday_letter = letter_file.read().replace('[NAME]', row['name'])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            email_message = (f"Subject:Happy Birthday !!! \n\n"
                             f"{birthday_letter}")
            connection.sendmail(from_addr=EMAIL, to_addrs=row['email'], msg=email_message)
