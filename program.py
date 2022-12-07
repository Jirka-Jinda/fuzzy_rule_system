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

rule = numpy.zeros(shape=(6,6))
rule[0][0] = 1
rule[0][1] = 0.5
rule[0][2] = 0.6
rule[1][0] = 0.5
rule[1][1] = 1
rule[1][2] = 0.9
rule[2][0] = 0.6
rule[2][1] = 0.9
rule[2][2] = 1 
rule[3][3] = 1
rule[3][4] = 0.9
rule[3][5] = 0.8
rule[4][3] = 0.9 
rule[4][4] = 1 
rule[4][5] = 0.8 
rule[5][3] = 0.8
rule[5][4] = 0.8
rule[5][5] = 1

print(rule)
input = fuzzy_set.fuzzy_set([(4,1),(2,0.4)])
print(input.all_elements())
temp = inference.infer([rule],[input])
res = temp.all_elements()
print(res)
print("pls")

