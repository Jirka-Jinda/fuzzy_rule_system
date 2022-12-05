# Before using, ensure following modules are present (in terminal):
# python -m pip install -U numpy
# python -m pip install -U matplotlib
import fuzzy_set
import fuzzy_set_operations
import fuzzification
import inference
import deffuzification
import rules
import graph_drawing
import numpy
import sys

# def controller(rules, input):
#     fuzzy_input = fuzzification.fuzzificate(input)
#     fuzzy_output = inference.infer(rules, fuzzy_input)
#     output = deffuzification.deffuzificate(fuzzy_output)
#     return output

res = rules.test_rules()
graph_drawing.draw_graph(res)
numpy.set_printoptions(threshold=sys.maxsize)
print(rules.create_relation_matrix(res[0],res[0]))
print()