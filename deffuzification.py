import fuzzy_set as fs
import fuzzy_set_operations as fo

# No. 1 - Center of gravity
def center_of_gravity(fs: fs.fuzzy_set):
    weighted_sum = 0
    degree_sum = 0
    for k in range(fs.length()):
        weighted_sum += (fs.value(k) * fs.degree(k))
        degree_sum += fs.degree(k)
    if degree_sum == 0:
        return 0
    else:
        return weighted_sum / degree_sum

# No. 2 - Mean of maxima
def mean_of_maxima(fs: fs.fuzzy_set):
    max_vals = []
    max_deg = fo.max_degree(fs)
    for k in range(fs.length()):
        if fs.degree(k) == max_deg:
            max_vals.append(fs.value(k))
    return sum(max_vals) / len(max_vals)

# No. 3 - Center of maxima
def center_of_maxima(fs: fs.fuzzy_set):
    max_deg = fo.max_degree(fs)
    max_vals = []
    for k in range(fs.length()):
        if fs.degree(k) == max_deg:
            max_vals.append(fs.value(k))
    return (min(max_vals + max(max_vals))) / 2

# creates "typical" value from output of inference procedure
# There are 3 basic approaches
def deffuzificate(fs: fs.fuzzy_set, method=center_of_gravity):
    return method(fs)