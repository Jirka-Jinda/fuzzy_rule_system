import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import fuzzy_set as fs
import fuzzification as f

def draw_fuzzy_sets(sets: list[fs.fuzzy_set], x_label, y_label, set_labels):
    colors = ['b', 'r', 'c', 'k', 'g', 'm']
    for set_index in range(len(sets)):
        x = []
        y = []
        set = sets[set_index]
        for index in range(set.length()):
            x.append(set.value(index))
            y.append(set.degree(index))
        if set_labels[index] == []:
            name = "Set " + str(set_index + 1)
        else:
            name = set_labels[index]
        color = colors[set_index % len(colors)]
        if set.length() == 1:
            style = 'o' + color
        else:
            style = '-' + color
        plt.plot(x, y, style, label=name)
    ticks = [round(x*0.1, 1) for x in range(0,11)]
    plt.yticks(ticks, ticks)
    if x_label == "":
        plt.xlabel("Values in " + set.context.universum)
    else:
        plt.xlabel(x_label)
    if y_label == "":
        plt.ylabel("Degrees in " + set.context.degrees)
    else:
        plt.ylabel(y_label)
    plt.legend()
    plt.show()

def draw_graph(sets, x_label="", y_label="", set_labels=[]):
    temp = []
    for set in sets:
        if isinstance(set, fs.fuzzy_set):
            temp.append(set)
        elif isinstance(set, list):
            temp.append(f.create_crisp_fs(set))
        else:
            raise ValueError("Couldn't identify type of argument.")
    draw_fuzzy_sets(temp, x_label, y_label, set_labels)

# def draw_matrix():
#     ax = plt.axes(projection='3d')



#     ax.set_xlabel()
#     ax.set_ylabel()
#     ax.set_zlabel()
#     plt.show()
    