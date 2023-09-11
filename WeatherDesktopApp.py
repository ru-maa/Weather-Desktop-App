import tkinter
import requests

# 天気情報を取得する都市名とAPIキー
city_name = ""
API_KEY = ""
api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"
