# Завдвння 1
from datetime import datetime

def get_days_from_today(date_str):
    try:
        # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' в об'єкт datetime
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        # Поточна дата
        today = datetime.today().date()
        # Різниця між поточною датою та заданою датою
        delta = date - today
        # Повернення різниці у днях як ціле число
        return delta.days
    except ValueError:
        return "Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'."

# Приклади
print(get_days_from_today("2021-09-29"))  # Приклад, коли дата у минулому
print(get_days_from_today("2023-07-09"))  # Приклад, коли дата у майбутньому
print(get_days_from_today("2024-01-01"))  # Приклад, коли дата у майбутньому
print(get_days_from_today("incorrect-format"))  # Повертає повідомлення про неправильний формат

# Завдвння 2
import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка параметрів
    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
        return []
    # Генерація унікальних випадкових чисел
    random_numbers = random.sample(range(min_num, max_num + 1), quantity)
    # Сортування чисел
    random_numbers.sort()
    return random_numbers

# Приклад 
lottery_numbers = get_numbers_ticket(7, 32, 9)
print("Ваші лотерейні числа:", lottery_numbers)