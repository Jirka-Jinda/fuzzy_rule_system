import numpy as np
import fuzzy_set

def union(A: fuzzy_set, B: fuzzy_set):
    pass

def intersect(A: fuzzy_set, B: fuzzy_set):
    pass

def difference(A: fuzzy_set, B: fuzzy_set):
    pass

def complement(A: fuzzy_set):
    pass

def aggregation(A: fuzzy_set, B: fuzzy_set):
    pass

#####

def gen_union(A: fuzzy_set, B: fuzzy_set, operation):
    pass
def gen_intersect(A: fuzzy_set, B: fuzzy_set, operation):
    pass
def gen_difference(A: fuzzy_set, B: fuzzy_set, operation):
    pass
def gen_aggregation(A: fuzzy_set, B: fuzzy_set, operation):
    pass

def _union_Godel(x, y):
    return min(x, y)
def _union_Lukas(x, y):
    return max(0, x + y - 1)
def _union_Goguen(x, y):
    return x * y

