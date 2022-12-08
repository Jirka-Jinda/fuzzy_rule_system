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
import numpy
import sys

#                     ### FUZZY PRAVIDLOVÉ SYSTÉMY ###
#    
#                           ┌────────────────┐
#                           │                │
#             Output ◄──┬───┤   Controlled   │◄──────── Input
#                       │   │    process     │     ▲
#                       │   │                │     │
#                       │   └────────────────┘     │
#                       │                          │
#                       │     ┌────────────┐       │
#                       │     │ Controller │       │
#                       ▼─────┤            ├───────┘
#                             └────────────┘

#                        ### FUZZY CONTROLLER ###
#
#                      ┌─────────────────────────────┐
# ┌────────────────┐   │                             │   ┌──────────────────┐
# │                │   │         Controller          │   │                  │
# │ Fuzzification  ├──►├──────────────┬──────────────┼──►│ Deffuzification  │
# │                │   │              │              │   │                  │
# └────────────────┘   │  Inference   │    Rules     │   └──────────────────┘
#                      │  procedure   │              │
#                      │              │              │
#                      └──────────────┴──────────────┘

def fuzzification_procedure(input):
    return fuzzification.fuzzificate(input)

def inference_procedure(rules, fuzzy_input):
    return inference.infer(rules, fuzzy_input)

def defuzzufication_procedure(fuzzy_ouput):    
    return deffuzification.deffuzificate(fuzzy_ouput)




#---------------- Auta z hodiny ---------------

# input = fuzzy_set.fuzzy_set([(4,1),(2,0.4)])

#------------------- Destnik -------------------
# Mam si vzit destnik?

# vitr = 5 km/h, dest = 40 mm/h, slunce = 10000 lx (denni svetlo)
umbrella_input = [[35]]
umbrella_fuzzy_input = []
# fuzzifikace
for input in umbrella_input:
    umbrella_fuzzy_input.append([fuzzification_procedure(input)])
# inference
weather_rules = rules.weather_rules_set()
umbrella_fuzzy_output = inference_procedure(weather_rules, umbrella_fuzzy_input)
print(umbrella_fuzzy_output.all_elements())
# deffuzifikace
umbrella_output = defuzzufication_procedure(umbrella_fuzzy_output)
print("Vem si destnik na", umbrella_output*10, "%.")

#----------- Nelinearni fce ~ interpolace ------

#

# input = fuzzy_set.fuzzy_set([(4,1),(2,0.4)])
# print(input.all_elements())
# temp = inference.infer([rule],[input])
# res = temp.all_elements()
# print(res)

