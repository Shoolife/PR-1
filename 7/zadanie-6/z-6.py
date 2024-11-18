import requests

# URL публичного API
api_url = "https://api.open-meteo.com/v1/forecast"

# Указываем широту и долготу Екатеринбурга
latitude = 56.8389
longitude = 60.6057

# Указываем диапазон дат
start_date = "2024-11-15"
end_date = "2024-11-25"

# Параметры запроса
params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": "temperature_2m",
    "start_date": start_date,
    "end_date": end_date,
    "timezone": "auto"  # Устанавливает часовой пояс автоматически
}

# Запрос к API
response = requests.get(api_url, params=params)
if response.status_code == 200:
    data = response.json()
else:
    print("Ошибка запроса:", response.status_code)
    exit()

# Пример обработки данных (создаем HTML-таблицу)
html_content = "<html><head><title>Weather Data for Yekaterinburg</title></head><body>"
html_content += f"<h1>Прогноз погоды в Екатеринбурге с {start_date} по {end_date}</h1>"

# Добавляем данные прогноза в таблицу
html_content += "<h2>Прогноз по часам</h2>"
html_content += "<table border='1'><tr><th>Дата и время</th><th>Температура (°C)</th></tr>"
for hour, temp in zip(data["hourly"]["time"], data["hourly"]["temperature_2m"]):
    html_content += f"<tr><td>{hour}</td><td>{temp}</td></tr>"
html_content += "</table>"

html_content += "</body></html>"

# Сохранение в HTML-файл
with open("yekaterinburg_weather_15_25_november.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML-таблица успешно создана: yekaterinburg_weather_15_25_november.html")
