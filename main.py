# Исходный список чисел
numbers = [5, 12, 7, 18, 3, 21, 8, 14, 6, 19]
# Переменная для хранения количества чисел, больших 10
count = 0
# Используем цикл for для обхода элементов списка
for number in numbers:
    if number > 10:
        count += 1
# Вывод результата
print("Количество чисел, больших 10:", count)
