import numpy as np
import fuzzy_set

##### SET OPERATIONS #####

def union(A: fuzzy_set, B: fuzzy_set):
    result = []
    for k in range(A.length()):
        result.append(A.element(k))
    for k in range(B.length()):
        found = False
        for i in range(len(result)):
            if B.value(k) == result[i][0]:
                found = True
                result[i] = (B.value(k), max(B.degree(k), result[i][1]))
                break
        if not found:
            result.append(B.element(k))      
    return fuzzy_set.fuzzy_set(result)

def intersection(A: fuzzy_set, B: fuzzy_set):
    result = []
    for k in range(A.length()):
        index = contains_value(B, A.value(k))
        if (index >= 0):
            result.append((A.value(k), max(B.degree(index), A.degree(k))))
    return fuzzy_set.fuzzy_set(result)

def negation(A: fuzzy_set):
    result = A
    for k in range(A.length()):
        result.set_degree(k, 1 - A.degree(k))
    return result

##### GENERAL FUNCS #####

def sum_values(A: fuzzy_set):
    result = 0
    for k in range(A.length()):
        result += A.value(k)
    return result

def max_degree(A: fuzzy_set):
    max_deg = A.degree(0)
    for k in range(A.length()):
        if A.degree(k) > max_deg:
            max_deg = A.degree(k)
    return max_deg

def min_degree(A: fuzzy_set):
    min_deg = A.degree(0)
    for k in range(A.length()):
        if ((A.degree(k) < min_deg) and A.degree(k) != 0) or min_deg == 0:
            min_deg = A.degree(k)
    return min_deg

def contains_value(A: fuzzy_set, value):
    for k in range(A.length()):
        if A.value(k) == value:
            return k
    return -1

    
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


