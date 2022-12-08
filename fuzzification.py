import fuzzy_set as fs
import fuzzy_set_operations as fo

# concrete approach of fuzzification of a singleton
# No. 1 - Singleton
def create_singleton(input):
    input = int(input)
    degree = 1
    return fs.fuzzy_set([(input, degree)])

# No. 2 - Narrow fuzzy set
def create_narrow_fs(input):
    input = int(input)
    degree = 1
    factor = 0.5
    return fs.fuzzy_set([
        (input - 1, degree * factor),
        (input, degree),
        (input + 1, degree * factor)])

# method of transforming arbitrary inputs into fuzzy set
def fuzzificate(input: list, method=create_singleton) -> fs.fuzzy_set:
    # if input is singleton create singleton fuzzy set
    if len(input) == 1:
        return method(input[0])
    # else we have a set, consider every value a singleton and union results
    else:
        result = fs.fuzzy_set([])
        for singleton in input:
            result = fo.union(result, fuzzificate([singleton]))
        return result

# creates crisp fuzzy set from regular set, used for drawing
def create_crisp_fs(set):
    return fuzzificate(set, create_singleton)