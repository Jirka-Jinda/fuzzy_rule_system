import fuzzy_set as fs
import fuzzy_set_operations as fo
import numpy as np

# Inference procedure
def infer(rules: list, inputs: list) -> fs.fuzzy_set:
    result = fs.fuzzy_set([])
    # apply use correspoding input and rule
    for k in range(len(inputs)):
        rule = rules[k]
        input = inputs[k]
        # apply Compositional rule of inference
        result_k = CRI(rule, input)
        # and append to results
        result = fo.union(result, result_k)
    return result

# Applying Compositional Rule of Inferece
def CRI(rule: np.ndarray, input:fs.fuzzy_set, operation=fo.tnorm_Goguen) -> fs.fuzzy_set:
    result = fs.fuzzy_set([])
    if isinstance(input, list):
        input = input[0]
    for k in range(input.length()):
        input_val = int(input.value(k))
        input_deg = input.degree(k)
        if input_deg == 0:
            continue
        else:
            fs_i = []
            for i in range(rule[input_val].size):
                fs_i.append((i+1, operation(input_deg, rule[input_val][i])))
            result = fo.union(result, fs.fuzzy_set(fs_i))
    return result