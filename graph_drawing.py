import matplotlib.pyplot as plt
import fuzzy_set as fs

def draw_set(set, style='o'):
    x = []
    y = []
    for value in set:
        x.append(value)
        y.append(1)
    plt.plot(x, y, style)
    plt.xlabel("Set values")
    plt.show()

def draw_fuzzy_set(set: fs.fuzzy_set):
    draw_fuzzy_sets([set])

def draw_fuzzy_sets(sets: list[fs.fuzzy_set]):
    for set_index in range(len(sets)):
        x = []
        y = []
        set = sets[set_index]
        for index in range(set.length()):
            x.append(set.value(index))
            y.append(set.degree(index))
        name = "Set " + str(set_index + 1)
        plt.plot(x, y, label=name)
    plt.xlabel("Values in " + set.context.universum)
    plt.ylabel("Degrees in " + set.context.degrees)
    plt.legend()
    plt.show()