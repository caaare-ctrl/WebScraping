from selenium import webdriver
import csv
import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep

column_name = ["Date","Horoscopes","Overview","Love","Dating","Work","Bonus"]
astrology = ["taurus", "aries", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn",
             "aquarius", "pisces"]
days = ["Monday", "Tueday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
data = []

# for a in astrology:
#     for day in days:
#         chrome_driver_path = "C:\Development\chromedriver.exe"
#         driver = webdriver.Chrome(executable_path=chrome_driver_path)
#         url = f"https://www.astrology.com/horoscope/daily/{a}.html#{day}"
#         driver.get(url)
#         html = driver.page_source
#         soup = BeautifulSoup(html, 'html.parser')
#         driver.close()
#         date = soup.find(id='content-date').get_text()
#         overview = soup.find(id='content').get_text()
#         love = soup.find(id="content-love").get_text()
#         daily_dating = soup.find(id="content-dating").get_text()
#         work = soup.find(id="content-work").get_text()
#         extra = soup.find(id="content-bonus").get_text()
#         row = {"Date": date,
#                "Horoscopes": a.capitalize(),
#                "Overview": overview,
#                "Love": love,
#                "Dating": daily_dating,
#                "Work": work,
#                "Bonus": extra}
#         data.append(row)
#     with open('astrology.csv', 'w', encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=column_name)
#         writer.writeheader()
#         for d in data:
#             writer.writerow(d)
#



# for a in astrology:
#     for day in days:
#         row = {}
#         scrap_url = f"https://www.astrology.com/horoscope/daily/{a}.html#{day}"
#         response = requests.get(scrap_url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         print(a.capitalize())
#         date = soup.find(id='content-date').get_text()
#         print(date)
#         overview = soup.find(id='content').get_text()
#         love = soup.find(id="content-love").get_text()
#         daily_dating = soup.find(id="content-dating").get_text()
#         work = soup.find(id="content-work").get_text()
#         extra = soup.find(id="content-bonus").get_text()
#         row = {"Date": date,
#                "Horoscopes": a.capitalize(),
#                "Overview": overview,
#                "Love": love,
#                "Dating": daily_dating,
#                "Work": work,
#                "Bonus": extra}
#         data.append(row)
#     with open('astrology.csv', 'w', encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=column_name)
#         writer.writeheader()
#         for d in data:
#             writer.writerow(d)

df = pd.read_csv("astrology.csv")
print(df)