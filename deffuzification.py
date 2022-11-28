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
    pass

# No. 2 - Center of maxima
def center_of_maxima(fs: fs.fuzzy_set):
    pass

# No. 3 - Mean of maxima
def mean_of_maxima(fs: fs.fuzzy_set):
    pass

