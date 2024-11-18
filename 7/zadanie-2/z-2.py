# Загрузка данных из файла
input_file_path = "second_task.txt"
with open(input_file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Функция для обработки строк
def process_line(line):
    numbers = map(int, line.split())  # Преобразование строки в список чисел
    # Суммируем абсолютные значения чисел, квадрат которых больше 100000
    return sum(abs(num) for num in numbers if num**2 > 100000)

# Применение операции к каждой строке
column = [process_line(line) for line in lines]

# Сортировка по убыванию
column_sorted = sorted(column, reverse=True)

# Сохранение топ-10 значений
top_10 = column_sorted[:10]

# Сохранение результатов в файл
output_file_path = "result.txt"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    for value in top_10:
        output_file.write(f"{value}\n")
