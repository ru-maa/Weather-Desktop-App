import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'weather_api.env')
load_dotenv(dotenv_path)

AP = os.environ.get("API_KEY") # 環境変数の値をAPに代入
