# Фильтрация чисел: оставляем положительные, квадрат которых <= 2500
def filter_numbers(numbers):
    return [num for num in numbers if num > 0 and num**2 <= 2500]

# Функция для замены N/A на среднее арифметическое соседних чисел
def replace_na_with_average(numbers):
    for i, num in enumerate(numbers):
        if num is None:
            # Получаем список соседних значений (если есть)
            neighbors = [numbers[i - 1] if i > 0 else None, numbers[i + 1] if i < len(numbers) - 1 else None]
            neighbors = [n for n in neighbors if n is not None]
            # Считаем среднее арифметическое
            numbers[i] = sum(neighbors) / len(neighbors) if neighbors else 0
    return numbers

# Загрузка данных из файла
input_file_path = "third_task.txt"
with open(input_file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Обработка строк
result_sums = []
for line in lines:
    # Преобразуем строку в список чисел, заменяя "N/A" на None
    numbers = [float(num) if num != "N/A" else None for num in line.split()]
    
    # Применяем фильтрацию
    numbers_filtered = filter_numbers([num for num in numbers if num is not None])
    
    # Заменяем оставшиеся "N/A" на среднее
    numbers_final = replace_na_with_average(numbers_filtered)
    
    # Вычисляем сумму
    result_sums.append(sum(numbers_final))

# Сохранение результатов в файл
output_file_path = "result.txt"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    for result_sum in result_sums:
        output_file.write(f"{result_sum}\n")
