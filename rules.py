import fuzzy_set as fs
import fuzzy_set_operations as fo
import numpy as np
import graph_drawing as gd

def weather_rules_set(discretion_factor=0):
    # hm/h
    wind_grades = fs.fuzzy_generator([0, 11, 29, 39, 49, 115], [0, 0.2, 0.4, 0.7, 1], discretion_factor)
    umbrella_wind = fs.fuzzy_set([(0,1),(1,0)])

    # mm/m^2 per hour, 1mm/m^2 =~ 1l per m^2
    rain_grades = fs.fuzzy_generator([0, 3, 8, 40, 100], [0, 0.3, 0.7, 1], discretion_factor)
    umbrella_rain = fs.fuzzy_set([(0,0),(1,1)])

    # Do i take an umbrella? Expert says:
    # IF [wind is STRONG or more] THEN [no]
    # IF [rain is MEDIUM or more] THEN [yes]

    gd.draw_graph([rain_grades, wind_grades], set_labels=["rain","wind"])

    #Rule set:
    R = [
        create_relation_matrix(wind_grades, umbrella_wind),
        create_relation_matrix(rain_grades, umbrella_rain),
    ]
    return R

def car_breaking_rules_set(discretion_factor=3):
    road_wetness = fs.fuzzy_generator([0, 25, 50, 75, 100], [0, 0.3, 0.6, 1], discretion_factor)
    wet_distance = fs.fuzzy_generator([0,100,200,300,400,500,600,700,800], [1,0.9,0.8,0.7,0.6,0.5,0.3,0.1], discretion_factor)

    car_speed = fs.fuzzy_generator([0, 50, 60, 90, 110, 130, 160], [0, 0.3, 0.5, 0.7, 0.9, 1], discretion_factor)
    speed_distance = fs.fuzzy_generator([0,100,200,300,400,500,600,700,800], [1,0.9,0.8,0.7,0.6,0.5,0.3,0.1], discretion_factor)

    car_weight = fs.fuzzy_generator([0, 700, 900, 1100, 1500], [0, 0.3, 0.6, 1], discretion_factor)
    weight_distance = fs.fuzzy_generator([0,100,200,300,400,500,600,700,800], [1,0.9,0.8,0.7,0.6,0.5,0.3,0.1], discretion_factor)

    R = [
    create_relation_matrix(road_wetness, wet_distance),
    create_relation_matrix(car_speed, speed_distance),
    #create_relation_matrix(car_weight, weight_distance),
    ]
    return R

def cars_rules_set(discretion_factor=0):
    rule = np.zeros(shape=(6,6))
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

    R = [rule]
    return R

########## Input-Output relation ############

def create_relation_matrix(input_set: fs.fuzzy_set, output_set: fs.fuzzy_set, operation=fo.tnorm_Lukas):
    input_size = input_set.length()
    output_size = output_set.length()
    result = np.zeros((input_size, output_size))

    for k in range(input_size):
        for i in range(output_size):
            result[k][i] = operation(input_set.degree(k), output_set.degree(i))

    return result

