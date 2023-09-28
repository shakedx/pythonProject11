import random

# Первое задание
my_tuple = (2,2,2,2,4,4,5,3,2,5,2,3,4,3,3,5,3,2,5,3,2,5,3)

a = my_tuple.count(5)

print("Кортеж:", my_tuple)
print("Количество цифр 5 в кортеже:", a)

#Второе задание

import random


def find_max_stroke(my_tuple2, a=3, а=3):
    максимальный_номер_строки = -1  # Начальное значение для максимального номера строки

    for number_of_stroke, stroke in enumerate(my_tuple2):
        # Проверерка на кратность числу "а"
        if all(element % а == 0 for element in stroke):
            максимальный_номер_строки = number_of_stroke

    return максимальный_номер_строки

size = 4
max_number = 10
my_tuple2 = tuple(tuple(random.randint(1, 10) for _ in range(size)) for _ in range(size))

# Выводим сгенерированный массив
print("Сгенерированный двумерный массив:")
for stroke in my_tuple2:
    print(stroke)

# Находим максимальный номер строки, состоящей только из элементов, кратных числу "а"
max_number = find_max_stroke(my_tuple2, a)

if max_number != -1:
    print(f"Максимальный номер строки, состоящей только из элементов, кратных {a}, равен {max_number}")
else:
    print(f"В массиве нет строк, удовлетворяющих условию")


#Третье задание

numbers = [int(x) for x in input("Введите список чисел через пробел: ").split()]

for i in range(1, len(numbers)):
    if (numbers[i] > 0 and numbers[i - 1] > 0) or (numbers[i] < 0 and numbers[i - 1] < 0):
        print(numbers[i - 1], numbers[i])
        break

#Четвертое задание

input_line = input("Введите последовательность чисел через пробел: ")
numbers = input_line.split()
input_line = set()

for число in numbers:
    if число in input_line:
        print("YES")
    else:
        print("NO")
        input_line.add(число)

#Пятое задание

number_of_strokes = int(input("Введите количество строк: "))
dictionary = {}


for _ in range(number_of_strokes):
    # _ - здесь это переменная "заглушка", потому что она не нужна внутри цикла
    stroke = input().split()
    for word in stroke:
        dictionary[word] = dictionary.get(word, 0) + 1

# Слово с максимальным количеством вхождений
max_word = max(dictionary.values())
most_use_words = [word for word, number in dictionary.items() if number == max_word]

# Выводим минимальное по порядку из самых частых слов
print(min(most_use_words))

