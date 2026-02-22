import smtplib
from datetime import datetime
import pandas
import random
import os

my_email = os.environ.get("MY_EMAIL")
passowrd = os.environ.get("MY_PASSWORD")


today = (datetime.now().month, datetime.now().day)
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    filepath = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(filepath) as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=passowrd)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject:BirthDay Wish from TALIB\n\n {content}")
