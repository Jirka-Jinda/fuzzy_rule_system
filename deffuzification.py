import fuzzy_set as fs
import fuzzy_set_operations as fo

# creates "typical" value from output of inference procedure
# There are 3 basic approaches
def deffuzificate(fs: fs.fuzzy_set):
    return center_of_gravity(fs)
    #return center_of_maxima(fs)
    #return mean_of_maxima(fs)

# No. 1 - Center of gravity
def center_of_gravity(fs: fs.fuzzy_set):
    weighted_sum = 0
    degree_sum = 0
    for k in range(len(fs)):
        weighted_sum += fs.value(k) * fs.degree(k)
        degree_sum += fs.degree(k)
    return weighted_sum / degree_sum

# No. 2 - Mean of maxima
def mean_of_maxima(fs: fs.fuzzy_set):
    max_vals = []
    max_deg = fo.max_degree(fs)
    for k in range(len(fs)):
        if fs.degree(k) == max_deg:
            max_vals.append(fs.value(k))
    return sum(max_vals) / len(max_vals)

# No. 3 - Center of maxima
def center_of_maxima(fs: fs.fuzzy_set):
    max_deg = fo.max_degree(fs)
    min_deg = fo.min_degree(fs)
    min_val = 0
    max_val = 0
    for k in range(len(fs)):
        if fs.degree(k) == max_deg:
            max_val = fs.value(k)
        if fs.degree(k) == min_deg:
            min_val = fs.value(k)
    return (min_val + max_val) /2