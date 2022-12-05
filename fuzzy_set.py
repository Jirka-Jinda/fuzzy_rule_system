import numpy as np

class context:
    def __init__(self, U='Z', L='[0,1]'):
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
        return (self.value(index), self.degree(index))
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

    def cut(self, threshold):
        for i in range(self.length()):
            if self.degree(i) > threshold:
                self.set_degree(i, threshold) 

    ############## GENERATOR #####################

def fuzzy_generator(thresholds_values: list, thresholds_degrees: list, discretion_factor):
    result = []
    rounding_mistake = 0
    values_range = thresholds_values[len(thresholds_values) - 1] - thresholds_values[0]

    for k in range(len(thresholds_values)):
        smoothing = False

        if k == 0:
            if len(thresholds_degrees) == len(thresholds_values) - 1:
                continue
            else:
                raise ValueError("Wrong number of values to degrees")
        else:
            semi_res = []
            deg_dif_from_prev = 0
            begin_val = thresholds_values[k-1]
            end_val = thresholds_values[k]
            interval_degree = thresholds_degrees[k-1]
            interval_size = end_val - begin_val

            if k == len(thresholds_values) - 1:
                interval_size = values_range - rounding_mistake
            else:
                rounding_mistake += interval_size

            if k > 1 and discretion_factor > 0:
                smoothing = True
                deg_dif_from_prev = interval_degree - thresholds_degrees[k-2]

            generated_vals = [x + begin_val  for x in range(interval_size)]
            for i in range(len(generated_vals)):
                if smoothing and i < interval_size * (1 / discretion_factor):
                    semi_res.append((generated_vals[i], round(interval_degree - deg_dif_from_prev / 2, 2)))
                else:
                    semi_res.append((generated_vals[i], interval_degree))

            result.extend(semi_res)
    return fuzzy_set(result)
    

