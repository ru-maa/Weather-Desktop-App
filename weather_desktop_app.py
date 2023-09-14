import PySimpleGUI as sg
import requests
import setting

# GUI設定
sg.theme("Dark Grey 13")

# ウィンドウに配置するコンポーネント
layout = [  [sg.Text("気温の知りたい市を入力してください!"), sg.InputText()],
            [sg.Button("検索", key=("-SEARCH-"))],
            [sg.Output(size=(80, 20), key=("-LOG-"))],
            [sg.Button("Exit"), sg.Button("Clear", key="-CLEAR-")]
]

# ウィンドウの生成
window = sg.Window("天気プログラム", layout)

# 天気情報を取得する都市名とAPIキー
def weather_data_get(city_name):
    city_name = city_name
    API_KEY = setting.AP
    api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"
    # 天気情報を取得するAPIにアクセスしてデータを取得
    url = api.format(city=city_name, key=API_KEY)
    response = requests.get(url)
    weather_data_get = response.json()
    return  weather_data_get


# 天気情報を整形してMessageを作成
def weather_date(data, city_name):
    temp = data['main']['temp']
    message = f"{city_name}の気温は{temp}℃です。\n体感温度は{data['main']['feels_like']}℃です。"
    if temp > 30:
        message += "\n今日はとても暑いです。熱中症に気をつけましょう！"
    elif temp < 5:
        message += "\n今日はとても寒いです。防寒対策をしましょう！"

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    try:
        rain = data['rain']['1h']
        message += f"\n降水確率は{rain}%です。"
    except KeyError:
        message += "\n降水確率は不明です。"

    message += f"\n湿度は{humidity}%で、気圧は{pressure} hPaです。"
    return message


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "-SEARCH-":
        weather_data = weather_data_get(values[0])
        temp = weather_data["main"], ["temp"]
        message = weather_date(weather_data, values[0])
        print(message)
    #　「Clear」ボタンを押したときの処理
    elif event == "-CLEAR-":
        #　「-OUTPUT-」領域を、空白で更新します。
        window["-LOG-"].update("")

window.close()

