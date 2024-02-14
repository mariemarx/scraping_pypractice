import re
from bs4 import BeautifulSoup 
import requests 

# select interpreter 3.9

page = "https://weather.com/en-IE/weather/tenday/l/bf217d537cc1c8074ec195ce07fb74de3c1593caa6033b7c3be4645ccc5b01de"
response = requests.get(page)
soup = BeautifulSoup(response.content,"html.parser")

d = soup.find_all('details', {'id': re.compile(r'^detailIndex')})

for row in d:
    date = row.find("h3", attrs={'data-testid': "daypartName"}).get_text()
    weather_icon = row.find("div", attrs={'data-testid': "weatherIcon"}).get_text()
    phrase = row.find("p", class_="DailyContent--narrative--3Ti6_", attrs={'data-testid': "wxPhrase"}).get_text()
    temp = row.find("span", attrs={'data-testid': "TemperatureValue"}).get_text()
    rain_chance = row.find("div", attrs={'data-testid': "Precip"}).get_text()
    wind_speed = row.find("div", attrs={'data-testid': "wind"}).get_text()
    humidity = row.find("div", class_="DetailsTable--field--CPpc_").get_text()
    
    print(date, weather_icon, temp, rain_chance, wind_speed, humidity)
    print(phrase)
    print()