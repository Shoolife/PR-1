from bs4 import BeautifulSoup
import pandas as pd

# Чтение HTML-файла
with open("fifth_task.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Парсинг HTML с помощью BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Нахождение таблицы
table = soup.find("table", {"id": "product-table"})

# Извлечение заголовков таблицы
headers = [header.text.strip() for header in table.find("thead").find_all("th")]

# Извлечение данных из строк таблицы
rows = []
for row in table.find("tbody").find_all("tr"):
    cells = [cell.text.strip() for cell in row.find_all("td")]
    rows.append(cells)

# Создание DataFrame
df = pd.DataFrame(rows, columns=headers)

# Сохранение в CSV
df.to_csv("result.csv", index=False, encoding="utf-8")

print("Данные успешно сохранены в output.csv")
