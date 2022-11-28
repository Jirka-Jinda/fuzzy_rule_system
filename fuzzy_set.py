import numpy as np

class context:
    def __init__(self, U='R', L='[0,1]'):
        self.universum = U
        self.degrees = L

class fuzzy_set:
    def __init__(self, list_of_tuples, context=context()):
        self.context = context
        self.elements = np.array(list_of_tuples)

    ##### GET #####
    def U(self):
        return self.context.universum
    def L(self):
        return self.context.degrees
    def element(self, index):
        return self.elements[index]
    def value(self, index):
        return self.elements[index][0]
    def degree(self, index):
        return self.elements[index][1]
    def length(self):
        return int(self.elements.size / 2)

    ##### SET #####
    def set_value(self, index, value):
        self.elements[index] = (value, self.degree(index))
    def set_degree(self, index, value):
        self.elements[index] = (self.value(index), value)

    ##### FUNCS #####
    def is_singleton(self):
        if self.length() == 1:
            return True
        else:
            return False

    def aplha_cut(self, threshold):
        pass

