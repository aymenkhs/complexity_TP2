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
    hue_data["temps d'execution"] = initial_data["T_part1"].tolist() + \
        initial_data["T_part2"].tolist() + initial_data["T_part3"].tolist()
    hue_data["Partie"] = ["partie1"] * 12 + ["partie2"] * 12 + ["partie3"] * 12
    return hue_data


def graph_langage(data, language):
    ax =  sns.lineplot(data=data, x="nb", y="T_part1")
    ax.legend(["T(n)"])
    ax.set_xlim(1000000, 2050000000)
    ax.set(xlabel='n', ylabel='Temps d\'execution en secondes', title='Gt partie 1 \'{}\''.format(language))
    plt.tight_layout()
    file_save_path = os.path.join("graphes_figures" ,"{}_part1.png".format(language))
    plt.savefig(file_save_path)
    plt.close()

    ax =  sns.lineplot(data=data, x="nb", y="T_part2")
    ax.legend(["T(n)"])
    ax.set_xlim(1000000, 2050000000)
    ax.set(xlabel='n', ylabel='Temps d\'execution en secondes', title='Gt partie 2 \'{}\''.format(language))
    plt.tight_layout()
    file_save_path = os.path.join("graphes_figures" ,"{}_part2.png".format(language))
    plt.savefig(file_save_path)
    plt.close()

    ax =  sns.lineplot(data=data, x="nb", y="T_part3")
    ax.legend(["T(n)"])
    ax.set_xlim(1000000, 2050000000)
    ax.set(xlabel='n', ylabel='Temps d\'execution en secondes', title='Gt partie 3 \'{}\''.format(language))
    plt.tight_layout()
    file_save_path = os.path.join("graphes_figures" ,"{}_part3.png".format(language))
    plt.savefig(file_save_path)
    plt.close()

    hue_data = create_hue_data(data)
    ax =  sns.lineplot(data=hue_data, x="n", y="temps d'execution", hue="Partie")
    ax.legend(["partie 1", "partie 2", "partie3"])
    ax.set_xlim(1000000, 2050000000)
    ax.set(xlabel='n', ylabel='Temps d\'execution en secondes', title='comparatif des 3 partie \'{}\''.format(language))
    plt.tight_layout()
    file_save_path = os.path.join("graphes_figures" ,"{}_global_comparaison.png".format(language))
    plt.savefig(file_save_path)
    plt.close()


def graph_function(list_values):
    result = [6*value-10 for value in list_values]
    ax =  sns.lineplot(x=list_values, y=list_values)
    ax.legend(["ctp(n)"])
    ax.set(xlabel='n', ylabel='nombre d\'iterations', title='Gp partie 1')
    plt.tight_layout()
    file_save_path = os.path.join("graphes_figures" ,"ctp_part1.png")
    plt.savefig(file_save_path)
    plt.close()

    result = [3*value-4 for value in list_values]
    ax =  sns.lineplot(x=list_values, y=result)
    ax.legend(["ctp(n)"])
    ax.set(xlabel='n', ylabel='nombre d\'iterations', title='Gp partie 2')
    plt.tight_layout()
    file_save_path = os.path.join("graphes_figures" ,"ctp_part2.png")
    plt.savefig(file_save_path)
    plt.close()

    result = [6*math.sqrt(value)-4 for value in list_values]
    ax =  sns.lineplot(x=list_values, y=result)
    ax.legend(["ctp(n)"])
    ax.set(xlabel='n', ylabel='nombre d\'iterations', title='Gp partie 3')
    plt.tight_layout()
    file_save_path = os.path.join("graphes_figures" ,"ctp_part3.png")
    plt.savefig(file_save_path)
    plt.close()

    cm = [10] * 12
    ax =  sns.lineplot(x=list_values, y=cm)
    ax.legend(["ctm(n)"])
    ax.set(xlabel='n', ylabel='nombre d\'iterations', title='Gm partie 1')
    ax.set_xlim(1000000, 2050000000)
    file_save_path = os.path.join("graphes_figures" ,"ctm_part1.png")
    plt.savefig(file_save_path)
    plt.close()

    ax =  sns.lineplot(x=list_values, y=cm)
    ax.legend(["ctm(n)"])
    ax.set(xlabel='n', ylabel='nombre d\'iterations', title='Gm partie 2')
    ax.set_xlim(1000000, 2050000000)
    file_save_path = os.path.join("graphes_figures" ,"ctm_part2.png")
    plt.savefig(file_save_path)
    plt.close()

    ax =  sns.lineplot(x=list_values, y=cm)
    ax.legend(["ctm(n)"])
    ax.set(xlabel='n', ylabel='nombre d\'iterations', title='Gm partie 3')
    ax.set_xlim(1000000, 2050000000)
    file_save_path = os.path.join("graphes_figures" ,"ctm_part3.png")
    plt.savefig(file_save_path)
    plt.close()


def main():
    # reading JAVA data
    java = pd.read_csv("csv_files/JAVA_TP2.csv")
    # preare JAVA data
    java["T_part1"] = [value/1000000000 for value in java["T_part1"].tolist()]
    java["T_part2"] = [value/1000000000 for value in java["T_part2"].tolist()]
    java["T_part3"] = [value/1000000000 for value in java["T_part3"].tolist()]
    graph_langage(java, "JAVA")
    c = pd.read_csv("csv_files/C_TP2.csv")
    graph_langage(c, "C")
    graph_function(c["nb"].tolist())

if __name__ == '__main__':
    main()
