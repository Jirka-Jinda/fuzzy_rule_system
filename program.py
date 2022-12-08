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
# # Mam si vzit destnik?
# # 0-11 low; 12-29 medium; 30-39 strong; 49-50 very_strong_wind; 50-115 storm - km/h
# # 0-2.5 low; 2.6-8 medium; 8.1-40 high; 40-100 drowning - mm/m2
# umbrella_input = [[],[]]
# umbrella_fuzzy_input = []
# # fuzzifikace
# for input in umbrella_input:
#     umbrella_fuzzy_input.append([fuzzification_procedure(input)])
# # inference
# weather_rules = rules.weather_rules_set()
# umbrella_fuzzy_output = inference_procedure(weather_rules, umbrella_fuzzy_input)
# # deffuzifikace
# print(umbrella_fuzzy_output.all_elements())
# umbrella_output = defuzzufication_procedure(umbrella_fuzzy_output)
# if umbrella_output < 0.5:
#     print("Destnik bych si nebral.")
# elif umbrella_output >= 0.5:
#     print("Vzal bych si destnik.")
# print(umbrella_output)

#----------- Brzdeni na silnici ------

# mokra silnice = 10%, rychlost = 55 km/h
road_input = [[10],[150]]
road_fuzzy_input = []
# fuzzifikace
for input in road_input:
    road_fuzzy_input.append([fuzzification_procedure(input)])
# inference
car_rules = rules.car_breaking_rules_set()
car_fuzzy_output = inference_procedure(car_rules, road_fuzzy_input)
# deffuzifikace
gd.draw_graph([car_fuzzy_output])
car_output = defuzzufication_procedure(car_fuzzy_output)
print("Zacni brzdit zhruba:", car_output, "metru pred prekazkou.")


# input = fuzzy_set.fuzzy_set([(4,1),(2,0.4)])
# print(input.all_elements())
# temp = inference.infer([rule],[input])
# res = temp.all_elements()
# print(res)

