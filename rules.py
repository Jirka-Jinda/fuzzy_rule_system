import fuzzy_set as fs
import fuzzy_set_operations as fo
import numpy as np

def weather_rules_set(discretion_factor=0):
    # 0-11 low; 12-29 meduium; 30-39 strong; 49-50 very_strong_wind; 50-115 storm
    # hm/h, [1, 0.7, 0.5, 0.7, 1]
    wind_grades = fs.fuzzy_generator([0, 11, 29, 39, 49, 115], [0, 0.2, 0.4, 0.7, 1], discretion_factor)
    # 0-2.5 low; 2.6-8 medium; 8.1-40 high; 40-100 drowning
    # mm/m^2 per hour, 1mm/m^2 =~ 1l per m^2
    rain_grades = fs.fuzzy_generator([0, 3, 8, 40, 100], [0, 0.3, 0.7, 1], discretion_factor)
    # 400-sunrise,sunset; 1000-overcast; 10000-full daylight; 32000-direct sunlight
    # lux * 10^2 = lumen/m2
    sun_grades = fs.fuzzy_generator([0, 4, 10, 100, 320], [0, 0.4, 0.8, 1], discretion_factor)

    # Do i take an umbrella? Expert says:
    # IF [wind is STRONG or more] THEN [no]
    # IF [rain is MEDIUM or more] THEN [yes]
    # IF [sun is DIRECT SUNLIGHT] THEN [yes]

    # Output space:
    umbrella_grades = fs.fuzzy_set([(1,0)])
    #umbrella_grades = fs.fuzzy_generator([0,1,2,3,4,5,6,7,8,9], [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], discretion_factor)
    
    #Rule set:
    R = [
        create_relation_matrix(wind_grades, umbrella_grades)
        #create_relation_matrix(rain_grades, umbrella_grades),
        #create_relation_matrix(sun_grades, umbrella_grades)
    ]
    # for item in R:
    #     print(item)
    return R

def nonlinear_rules_set(discretion_factor=0):
    pass

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

