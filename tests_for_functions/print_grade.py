import json
from random import randint, uniform
import numpy as np


def test_1():
    a = 110
    return [a, "Incorrect"]

def test_2():
    a = 90
    return [a, "Great"]

def test_3():
    a = 85
    return [a, "Good"]

def test_4():
    a = 65
    return [a, "Satisfactory"]

def test_5():
    a = 45
    return [a, "Unsatisfactory"]

def test_6():
    a = -124
    return [a, "Incorrect"]

arr1 = test_1()
arr2 = test_2()
arr3 = test_3()
arr4 = test_4()
arr5 = test_5()
arr6 = test_6()

massives = [
    {"stimulus": [str(arr1[0])], "reactus": str(arr1[1])},
    {"stimulus": [str(arr2[0])], "reactus": str(arr2[1])},
    {"stimulus": [str(arr3[0])], "reactus": str(arr3[1])},
    {"stimulus": [str(arr4[0])], "reactus": str(arr4[1])},
    {"stimulus": [str(arr5[0])], "reactus": str(arr5[1])},
    {"stimulus": [str(arr6[0])], "reactus": str(arr6[1])}
]

with open(r"C:\Users\falearn\source\repos\the_func\print_grade.json", "w", encoding="utf-8") as outfile:
    json.dump(massives, outfile, ensure_ascii=False)