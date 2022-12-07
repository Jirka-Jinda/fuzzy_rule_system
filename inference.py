import fuzzy_set as fs
import fuzzy_set_operations as fo
import numpy as np

# slajdy I: http://belohlavek.inf.upol.cz/vyuka/flfs_I.pdf
# slajdy II, 42: http://belohlavek.inf.upol.cz/vyuka/flfs_II.pdf
# rukopis: http://belohlavek.inf.upol.cz/vyuka/UI-6-fuzzy-rules.pdf
# 3D grafy: https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

def infer(rules: list, inputs: list) -> fs.fuzzy_set:
    result = fs.fuzzy_set([])
    # apply rule for every set
    for k in range(len(inputs)):
        rule = rules[k]
        input = inputs[k]
        result_k = CRI(rule, input)
        # and append to results
        result = fo.union(result, result_k)
    return result

def CRI(rule: np.ndarray, input:fs.fuzzy_set, operation=fo.tnorm_Lukas):
    result = fs.fuzzy_set([])
    for k in range(input.length()):
        input_val = int(input.value(k))
        input_deg = input.degree(k)
        if input_deg == 0:
            continue
        else:
            fs_i = []
            for i in range(rule[input_val].size):
                fs_i.append((i, operation(input_deg, rule[input_val][i])))
            result = fo.union(result, fs.fuzzy_set(fs_i))
    return result