#Тест на натуральные числа
#Тест на натуральные числа и нуль
#Тест на отрицательные числа
#Тест на натуральные и отрицательные числа, и нуль
#Тест на ввод одинаковых чисел

import json
import random
from statistics import mean

def test_natural_numbers():
    numbers = [random.randint(1, 100) for _ in range(5)]
    average = mean(numbers)
    return [numbers, average]

def test_natural_numbers_and_zero():
    numbers = [random.randint(0, 100) for _ in range(4)]
    numbers.append(0)
    average = mean(numbers)
    return [numbers, average]

def test_negative_numbers():
    numbers = [random.randint(-100, -1) for _ in range(5)]
    average = mean(numbers)
    return [numbers, average]

def test_mixed_numbers():
    numbers = [random.randint(-100, 100) for _ in range(5)]
    average = mean(numbers)
    return [numbers, average]

def test_same_numbers():
    number = random.randint(-100, 100)
    numbers = [number] * 5
    average = mean(numbers)
    return [numbers, average]

# Пример использования

arr1 = test_natural_numbers()
arr2 = test_natural_numbers_and_zero()
arr3 = test_negative_numbers()
arr4 = test_mixed_numbers()
arr5 = test_same_numbers()

massives = [
    {"stimulus": [str(arr1[0][0]), str(arr1[0][1]),str(arr1[0][2]),str(arr1[0][3]),str(arr1[0][4])], "reactus": str(arr1[1])},
    {"stimulus": [str(arr2[0][0]), str(arr2[0][1]),str(arr2[0][2]),str(arr2[0][3]),str(arr2[0][4])], "reactus": str(arr2[1])},
    {"stimulus": [str(arr3[0][0]), str(arr3[0][1]),str(arr3[0][2]),str(arr3[0][3]),str(arr3[0][4])], "reactus": str(arr3[1])},
    {"stimulus": [str(arr4[0][0]), str(arr4[0][1]),str(arr4[0][2]),str(arr4[0][3]),str(arr4[0][4])], "reactus": str(arr4[1])},
    {"stimulus": [str(arr5[0][0]), str(arr5[0][1]),str(arr5[0][2]),str(arr5[0][3]),str(arr5[0][4])], "reactus": str(arr5[1])},
]


with open(r"C:\Users\falearn\source\repos\the_func\read_and_calculate_average.json", "w") as outfile:
    json.dump(massives, outfile)
