import matplotlib.pyplot as plt
import fuzzy_set as fs
import fuzzification as f

def draw_fuzzy_sets(sets: list[fs.fuzzy_set]):
    colors = ['b', 'r', 'c', 'k', 'g', 'm']
    for set_index in range(len(sets)):
        x = []
        y = []
        set = sets[set_index]
        for index in range(set.length()):
            x.append(set.value(index))
            y.append(set.degree(index))
        name = "Set " + str(set_index + 1)
        color = colors[set_index % len(colors)]
        if set.length() == 1:
            style = 'o' + color
        else:
            style = '-' + color
        plt.plot(x, y, style, label=name)
    ticks = [round(x*0.1, 1) for x in range(0,11)]
    plt.yticks(ticks, ticks)
    plt.xlabel("Values in " + set.context.universum)
    plt.ylabel("Degrees in " + set.context.degrees)
    plt.legend()
    plt.show()

def draw_graph(sets):
    temp = []
    for set in sets:
        if isinstance(set, fs.fuzzy_set):
            temp.append(set)
        elif isinstance(set, list):
            temp.append(f.create_crisp_fs(set))
        else:
            raise ValueError("Couldn't identify type of param")
    draw_fuzzy_sets(temp)