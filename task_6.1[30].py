# Напишите программу, генерирующую элементы арифметической прогресии
# Программа принимает от пользователя три числа :
# - Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Напишите функцию
#     Аргументы: три указанных параметра
#     Возвращает: список элементов арифмитической прогрессии.

# Усложнение:
# - Для формирования списка внутри функции используйте Comprehension
# - Присвоение значений переменным a1,d,n запишите, используя только один input, в одну строку, 
#   вам понадобится распаковка и Comprehension или map

# Примеры/Тесты:
#     Ввод: 7 2 5
#     Вывод: [7 9 11 13 15]

#     Ввод: 2 3 12
#     Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]

a1, d, n = [int(el) for el in input("Введите a1, d, n ").split()]


def arithmetic_progression(start, step, lenght):
    return [start + step * idx for idx in range(lenght)]

print(arithmetic_progression(a1, d, n))