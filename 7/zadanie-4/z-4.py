import pandas as pd

# Пути к файлам
input_file_path = "fourth_task.txt"  # Замените на полный путь к вашему файлу
calculations_file = "calculations.txt"
filtered_csv_file = "filtered.csv"

# Чтение исходного CSV-файла
data = pd.read_csv(input_file_path)

# Шаг 1: Удаление столбца "category"
data = data.drop(columns=["category"])

# Шаг 2: Вычисления
quantity_mean = data["quantity"].mean()  # Среднее по quantity
quantity_max = data["quantity"].max()    # Максимум по quantity
rating_min = data["rating"].min()        # Минимум по rating

# Сохранение вычислений в текстовый файл
with open(calculations_file, "w", encoding="utf-8") as calc_file:
    calc_file.write(f"{quantity_mean}\n")
    calc_file.write(f"{quantity_max}\n")
    calc_file.write(f"{rating_min}\n")

# Шаг 3: Фильтрация строк, где quantity < 40
filtered_data = data[data["quantity"] < 40]

# Сохранение отфильтрованных данных в CSV-файл
filtered_data.to_csv(filtered_csv_file, index=False, encoding="utf-8")

