import fuzzy_set as fs
import fuzzy_set_operations as fo
import numpy as np

def weather_rules_set(discretion_factor=0):
    # 0-11 low; 12-29 meduium; 30-39 strong; 49-50 very_strong_wind; 50-115 storm
    # hm/h, [1, 0.7, 0.5, 0.7, 1]
    # wind_grades = fs.fuzzy_generator([0, 11, 29, 39, 49, 115], [1, 0.7, 0.4, 0.2, 0], discretion_factor)
    wind_grades = fs.fuzzy_generator([0, 2, 3], [0,1], discretion_factor)
    # 0-2.5 low; 2.6-8 medium; 8.1-40 high; 40-100 drowning
    # mm/m^2 per hour, 1mm/m^2 =~ 1l per m^2
    rain_grades = fs.fuzzy_generator([0, 3, 8, 40, 100], [1, 0.7, 0.3, 0], discretion_factor)
    # 400-sunrise,sunset; 1000-overcast; 10000-full daylight; 32000-direct sunlight
    # lux * 10^2 = lumen/m2
    sun_grades = fs.fuzzy_generator([0, 4, 10, 100, 320], [0, 0.4, 0.8, 1], discretion_factor)

    # Do i take an umbrella? Expert says:
    # IF [wind is STRONG or more] THEN [no]
    # IF [rain is MEDIUM or more] THEN [yes]
    # IF [sun is DIRECT SUNLIGHT] THEN [yes]

    # Output space:
    umbrella_grades = fs.fuzzy_set([(0,1)])
    # umbrella_grades = fs.fuzzy_generator([0,1], [1], discretion_factor)
    
    #Rule set:
    R = [
        create_relation_matrix(wind_grades, umbrella_grades),
        create_relation_matrix(rain_grades, umbrella_grades),
        create_relation_matrix(sun_grades, umbrella_grades)
    ]
    return R

def room_temperature_rules_set(discretion_factor=0):
    pass

########## Input-Output relation ############

def create_relation_matrix(input_set: fs.fuzzy_set, output_set: fs.fuzzy_set, operation=fo.tnorm_Lukas):
    input_size = input_set.length()
    output_size = output_set.length()
    result = np.zeros((input_size, output_size))

    for k in range(input_size):
        for i in range(output_size):
            result[k][i] = operation(input_set.degree(k), output_set.degree(i))

    return result

