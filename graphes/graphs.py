import os
import math

import pandas as pd
import seaborn as sns
sns.set_theme(style="darkgrid")

import matplotlib
import matplotlib.pyplot as plt

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 22}

matplotlib.rc('font', **font)


def create_hue_data(initial_data):
    hue_data = pd.DataFrame(columns = ["n", "Partie", "temps d'execution"])
    hue_data["n"] = initial_data["nb"].tolist() * 3
    hue_data["temps d'execution"] = initial_data["T_part1"].tolist() +
        initial_data["T_part2"].tolist() + initial_data["T_part3"].tolist()
    hue_data["Partie"] = ["partie1"] * 12 + ["partie2"] * 12 + ["partie3"] * 12
    return hue_data


def graph_langage(data, language):
    ax =  sns.lineplot(data=data, x="nb", y="T_part1")
    ax.legend(["T(n)"])
    ax.set_xlim(1000000, 2050000000)
    ax.set(xlabel='n', ylabel='Temps d\'execution en secondes', title='partie 1 \'{}\''.format(language))
    plt.show()

    ax =  sns.lineplot(data=java, x="nb", y="T_part2")
    ax.legend(["T(n)"])
    ax.set_xlim(1000000, 2050000000)
    ax.set(xlabel='n', ylabel='Temps d\'execution en secondes', title='partie 2 \'{}\''.format(language))
    plt.show()

    ax =  sns.lineplot(data=java, x="nb", y="T_part3")
    ax.legend(["T(n)"])
    ax.set_xlim(1000000, 2050000000)
    ax.set(xlabel='n', ylabel='Temps d\'execution en secondes', title='partie 3 \'{}\''.format(language))
    plt.show()

    hue_data = create_hue_data(data)
    ax =  sns.lineplot(data=hue_data, x="n", y="temps d'execution", hue="Partie")
    ax.legend(["partie 1", "partie 2", "partie3"])
    ax.set_xlim(1000000, 2050000000)
    ax.set(xlabel='n', ylabel='Temps d\'execution en secondes', title='comparatif des 3 partie \'{}\''.format(language))
    plt.show()


def graph_function(list_values):
    ax =  sns.lineplot(x=list_values, y=list_values)
    ax.legend(["ctp(n)"])
    ax.set(xlabel='n', ylabel='nombre d\'iterations', title='partie 1')
    plt.show()

    result = [value//2 for value in list_values]
    ax =  sns.lineplot(x=list_values, y=list_values)
    ax.legend(["ctp(n)"])
    ax.set(xlabel='n', ylabel='nombre d\'iterations', title='partie 2')
    plt.show()

    result = [int(math.sqrt(value)) for value in list_values]
    ax =  sns.lineplot(x=list_values, y=list_values)
    ax.legend(["ctp(n)"])
    ax.set(xlabel='n', ylabel='nombre d\'iterations', title='partie 3')
    plt.show()

    cm = [1] * 12
    ax =  sns.lineplot(x=list_values, y=cm)
    ax.legend(["ctm(n)"])
    ax.set(xlabel='n', ylabel='nombre d\'iterations', title='partie 1')
    plt.show()

    ax =  sns.lineplot(x=list_values, y=cm)
    ax.legend(["ctm(n)"])
    ax.set(xlabel='n', ylabel='nombre d\'iterations', title='partie 2')
    plt.show()

    ax =  sns.lineplot(x=list_values, y=cm)
    ax.legend(["ctm(n)"])
    ax.set(xlabel='n', ylabel='nombre d\'iterations', title='partie 3')
    plt.show()





def main():
    java = pd.read_csv("csv_files/JAVA_TP2.csv")
    c = pd.read_csv("csv_files/C_TP2.csv")

if __name__ == '__main__':
    main()
