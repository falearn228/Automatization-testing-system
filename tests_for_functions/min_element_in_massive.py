import json
from random import randint
import numpy as np


def test_1():
    return [a := np.random.randint(0, 100, size := randint(4, 20)).tolist(), size, min(a)]


def test_2():
    return [[], 0, -1]


def test_3():
    return [a := np.random.randint(-100, -1, size := randint(4, 20)).tolist(), size, min(a)]


def test_4():
    return [a := np.random.randint(0, 100, size := 1).tolist(), size, min(a)]


def test_5():
    return [a := np.random.randint(0, 100, size := randint(16400, 16600)).tolist(), size, min(a)]


def test_6():
    return [a := np.zeros((size := randint(4, 20)), dtype=int).tolist(), size, min(a)]


def test_7():
    a = np.random.randint(1, 100, size1 := randint(4, 10))
    d = np.random.randint(0, 1, 1)
    b = np.random.randint(-100, -1, size2 := randint(4, 10))
    size = size1 + size2 + 1
    a = np.union1d(a, d)
    return [c := np.union1d(a, b).tolist(), len(c), min(c)]


def test_8():
    a = [0]
    b = np.random.randint(1, 100, size := randint(4, 20))
    return [c := np.union1d(a, b).tolist(), len(c), min(c)]


def test_9():
    b = np.random.randint(1, 100, size := randint(4, 20))
    b = b.tolist()
    b.append(0)
    return [b, size + 1, min(b)]


arr1 = test_1()
arr2 = test_2()
arr3 = test_3()
arr4 = test_4()
arr5 = test_5()
arr6 = test_6()
arr7 = test_7()
arr8 = test_8()
arr9 = test_9()

massives = [
    {"stimulus": [str(arr1[0]), str(arr1[1])], "reactus": str(arr1[2])},
    {"stimulus": [str(arr2[0]), str(arr2[1])], "reactus": str(arr2[2])},
    {"stimulus": [str(arr3[0]), str(arr3[1])], "reactus": str(arr3[2])},
    {"stimulus": [str(arr4[0]), str(arr4[1])], "reactus": str(arr4[2])},
    {"stimulus": [str(arr5[0]), str(arr5[1])], "reactus": str(arr5[2])},
    {"stimulus": [str(arr6[0]), str(arr6[1])], "reactus": str(arr6[2])},
    {"stimulus": [str(arr7[0]), str(arr7[1])], "reactus": str(arr7[2])},
    {"stimulus": [str(arr8[0]), str(arr8[1])], "reactus": str(arr8[2])},
    {"stimulus": [str(arr9[0]), str(arr9[1])], "reactus": str(arr9[2])}
]

arr1 = test_1()
arr2 = test_2()
arr3 = test_3()
arr4 = test_4()
arr5 = test_5()
arr6 = test_6()
arr7 = test_7()
arr8 = test_8()
arr9 = test_9()

mas1 = [
    {"stimulus": [str(arr1[0]), str(arr1[1])], "reactus": str(arr1[2])},
    {"stimulus": [str(arr2[0]), str(arr2[1])], "reactus": str(arr2[2])},
    {"stimulus": [str(arr3[0]), str(arr3[1])], "reactus": str(arr3[2])},
    {"stimulus": [str(arr4[0]), str(arr4[1])], "reactus": str(arr4[2])},
    {"stimulus": [str(arr5[0]), str(arr5[1])], "reactus": str(arr5[2])},
    {"stimulus": [str(arr6[0]), str(arr6[1])], "reactus": str(arr6[2])},
    {"stimulus": [str(arr7[0]), str(arr7[1])], "reactus": str(arr7[2])},
    {"stimulus": [str(arr8[0]), str(arr8[1])], "reactus": str(arr8[2])},
    {"stimulus": [str(arr9[0]), str(arr9[1])], "reactus": str(arr9[2])}
]

arr1 = test_1()
arr2 = test_2()
arr3 = test_3()
arr4 = test_4()
arr5 = test_5()
arr6 = test_6()
arr7 = test_7()
arr8 = test_8()
arr9 = test_9()

mas2 = [
    {"stimulus": [str(arr1[0]), str(arr1[1])], "reactus": str(arr1[2])},
    {"stimulus": [str(arr2[0]), str(arr2[1])], "reactus": str(arr2[2])},
    {"stimulus": [str(arr3[0]), str(arr3[1])], "reactus": str(arr3[2])},
    {"stimulus": [str(arr4[0]), str(arr4[1])], "reactus": str(arr4[2])},
    {"stimulus": [str(arr5[0]), str(arr5[1])], "reactus": str(arr5[2])},
    {"stimulus": [str(arr6[0]), str(arr6[1])], "reactus": str(arr6[2])},
    {"stimulus": [str(arr7[0]), str(arr7[1])], "reactus": str(arr7[2])},
    {"stimulus": [str(arr8[0]), str(arr8[1])], "reactus": str(arr8[2])},
    {"stimulus": [str(arr9[0]), str(arr9[1])], "reactus": str(arr9[2])}
]

massives += mas1 + mas2
with open(r"C:\Users\falearn\source\repos\the_func\min_element_in_massive.json", "w") as outfile:
    json.dump(massives, outfile)
