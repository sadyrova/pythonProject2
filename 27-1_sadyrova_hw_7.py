# Функция bubble_sort
from typing import Any


def bubble_sort(list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]

                swapped = True


list = [6, 3, 13, 8, 4, 9, 11]
bubble_sort(list)
print(list)

# Функция selection_sort

def selection_sort(list):
    for i in range(len(list)):

        lowest_value_index = i

        for j in range(i + 1, len(list)):
            if list[j] < list[lowest_value_index]:
                lowest_value_index = j

        list[i], list[lowest_value_index] = list[lowest_value_index], list[i]


list = [22, 18, 27, 14, 17]
selection_sort(list)
print(list)


# Функция binary_search

def binary_search(list, number):

    first = 0
    last = len(list) - 1
    while first < last:
        middle = (first + last) // 2
        if list[middle] == number:
            return middle
        elif list[middle] < number:
            first = middle + 1
        else:
            last = middle - 1
    return -1

list = sorted([15, 6, 9, 2, 23, 7, 13, 10, 25])
number = 7
print(list)
print(binary_search(list, number))