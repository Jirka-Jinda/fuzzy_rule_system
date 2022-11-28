import fuzzy_set as fs
import fuzzy_set_operations as fo

# method to transform arbitrary inputs into fuzzy set
def fuzzificate(input: list[int]) -> fs.fuzzy_set:
    # if input is singleton create singleton fuzzy set
    if len(input) == 1:
        return fuzzificate_singleton(input[0])
    # else we have a set, consider every value a singleton and union results
    else:
        result = fs.fuzzy_set([])
        for singleton in input:
            fo.union(result, fuzzificate(singleton))
        return result

# concrete approach to fuzzification of a singleton
def fuzzificate_singleton(input):
    return create_narrow_fs(input)
    #return create_singleton(input)

# No. 1 - Singleton
def create_singleton(input):
    degree = 1
    return fs.fuzzy_set((input, degree))

# No. 2 - Narrow fuzzy set
def create_narrow_fs(input):
    degree = 1
    factor = 0.3
    return fs.fuzzy_set([
        (input - 1, degree * factor),
        (input, degree),
        (input + 1, degree * factor)])
