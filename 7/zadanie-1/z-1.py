from collections import Counter
import re

# Функция для подсчета частоты слов
def count_word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())  # Находим все слова (приводим к нижнему регистру)
    return Counter(words)

# Функция для подсчета предложений в каждом абзаце
def count_sentences_per_paragraph(text):
    paragraphs = [p for p in text.split("\n") if p.strip()]  # Разделяем на абзацы, пропуская пустые строки
    sentence_counts = [len(re.findall(r'[.!?]+', paragraph)) for paragraph in paragraphs]
    return sentence_counts

# Загрузка текста из файла
file_path = "first_task.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Обработка общей части
word_frequency = count_word_frequency(text)

# Обработка вариантной части
sentences_per_paragraph = count_sentences_per_paragraph(text)

# Сохранение результатов
# Результаты частоты слов
general_output_path = "word_frequency.txt"
with open(general_output_path, "w", encoding="utf-8") as general_file:
    for word, freq in word_frequency.most_common():
        general_file.write(f"{word}:{freq}\n")

# Результаты по вариантной части
variant_output_path = "sentences_per_paragraph.txt"
with open(variant_output_path, "w", encoding="utf-8") as variant_file:
    for count in sentences_per_paragraph:
        variant_file.write(f"{count}\n")
