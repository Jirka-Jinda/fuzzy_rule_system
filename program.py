# Before using, ensure following modules are present (in terminal):
# python -m pip install -U numpy
# python -m pip install -U matplotlib
import fuzzy_set
import fuzzy_set_operations
import fuzzification
import inference
import deffuzification
import rules
import graph_drawing as gd

# def controller(rules, input):
#     fuzzy_input = fuzzification.fuzzificate(input)
#     fuzzy_output = inference.infer(rules, fuzzy_input)
#     output = deffuzification.deffuzificate(fuzzy_output)
#     return output

init = []
init.append((5, 0.3))
init.append((6, 0.5))
init.append((7, 0.8))
init.append((8, 1))
init.append((9, 1))
init.append((10, 0.9))
init.append((11, 0.8))
init.append((12, 0.5))
init.append((13, 0.2))

init2 = []
init2.append((6, 1))
init2.append((7, 1))
init2.append((8, 0.3))
init2.append((9, 0.2))
init2.append((10, 0.1))
init2.append((11, 0.5))
init2.append((12, 0.5))

f_set1 = fuzzy_set.fuzzy_set(init)
f_set2 = fuzzy_set.fuzzy_set(init2)
f_sets = [f_set1, f_set2]
gd.draw_graph(f_sets)

# fuzz = fuzzification.fuzzificate([5,6,8,10,11,17])
# defuzz = deffuzification.deffuzificate(fuzz)
# gd.draw_graph([fuzz, defuzz])