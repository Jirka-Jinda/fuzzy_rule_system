import numpy as np
import fuzzy_set

##### SET OPERATIONS #####

def union(A: fuzzy_set, B: fuzzy_set):
    result = []
    for k in range(len(A)):
        result.append(A.element(k))
    for k in range(len(B)):
        for i in range(len(result)):
            pass
            #dementni tuply v listech
    return fuzzy_set.fuzzy_set(result)

def intersection(A: fuzzy_set, B: fuzzy_set):
    result = []
    for k in range(len(A)):
        index = contains_value(B, A.value(k))
        if (index >= 0):
            result.append((A.value(k), max(B.degree(index), A.degree(k))))
    return fuzzy_set.fuzzy_set(result)

def negation(A: fuzzy_set):
    result = A
    for k in range(len(A)):
        result.set_degree(k, 1 - A.degree(k))
    return result

##### TRUTH OPERATIONS #####

def f_and(x: tuple, y: tuple):
    #methods: _union_Goguen, _union_Godel, _union_Lukas
    return gen_and(x, y, _union_Goguen)

def f_or(x: tuple, y: tuple):
    #methods:
    pass

def f_neg(x: tuple):
    #methods:
    pass

##### GENERAL FUNCS #####

def sum_values(A: fuzzy_set):
    result = 0
    for k in range(len(A)):
        result += A.value(k)
    return result

def max_degree(A: fuzzy_set):
    max_deg = A.degree(0)
    for k in range(len(A)):
        if A.degree(k) > max_deg:
            max_deg = A.degree(k)
    return max_deg

def min_degree(A: fuzzy_set):
    min_deg = A.degree(0)
    for k in range(len(A)):
        if A.degree(k) < min_deg:
            min_deg = A.degree(k)
    return min_deg

def contains_value(A: fuzzy_set, value):
    for k in range(len(A)):
        if A.value(k) == value:
            return k
    return -1

##### IMPLEMENTATION #####

def gen_and(x: tuple, y: tuple, operation):
    pass
def gen_or(x: tuple, y: tuple, operation):
    pass
def gen_neg(x: tuple, y: tuple, operation):
    pass

def _union_Godel(x, y):
    return min(x, y)
def _union_Lukas(x, y):
    return max(0, x + y - 1)
def _union_Goguen(x, y):
    return x * y


