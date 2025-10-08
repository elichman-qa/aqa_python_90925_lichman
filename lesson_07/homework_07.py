# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
from lesson_06.homework_05 import print_people_30years
from lesson_06.homework_06 import search_ch_in_word, sum_pare_value, print_str_value


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    limit_value = 25
    # Complete the while loop condition.
    while multiplier <= limit_value:
        result = number * multiplier
        if result < limit_value:
            print(str(number) + "x" + str(multiplier) + "=" + str(result))
            pass
        multiplier += 1


multiplication_table(2)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_two_value(number1, number2):
    """
    Функція, яка обчислює суму двох чисел.
    :param number1: Перший доданок
    :param number2: Другий доданок
    :return: Добуток доданків
    """
    result = number1 + number2
    print("The sum of your two values is: ", result)


sum_two_value(5, 6)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def middle_value(list_of_nums):
    """
    Функцію, яка розрахує середнє арифметичне списку чисел.
    :param list_of_nums: Тут треба використовувати список чисел
    :return: Кінцеве значення
    """
    result = sum(list(list_of_nums)) / len(list(list_of_nums))
    print("The middle value for your list nums is: ", round(result, 2))


my_list_nums = list(range(1, 5))
my_list_nums2 = (1, 2.5, 0.85, 42)
middle_value(my_list_nums)
middle_value(my_list_nums2)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
new_row = "Написати функцію, яка приймає рядок та повертає його у зворотному порядку."


def reverse_sort_row(some_row):
    """
    функція, яка приймає рядок та повертає його у зворотному порядку.
    """
    enumerate_some_row = dict(enumerate(list(some_row)))
    sorted_some_row = sorted(enumerate_some_row.items(), key=lambda index: index[0], reverse=True)
    print("".join(ch for index, ch in sorted_some_row))


reverse_sort_row(new_row)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def tolong_word (list_words):
    """
    функція, яка приймає список слів та повертає найдовше слово у списку
    """
    sorted_list_words = sorted(list_words, key=lambda word: len(word), reverse=True)
    print(sorted_list_words[0])

line = "Написати функцію, яка приймає список слів та повертає найдовше слово у списку"
lines = line.split()
tolong_word(lines)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
print_people_30years()
# task 8
search_ch_in_word('h')
# task 9
sum_pare_value(my_list_nums2)
# task 10
print_str_value(lines)
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
