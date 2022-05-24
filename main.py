import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import matplotlib
os.system('cls')
print(">>>")

from pycafee.normalitycheck import KolmogorovSmirnov
from pycafee.normalitycheck import Lilliefors
import matplotlib as mpl
import numpy as np
mpl.rc('font', family = 'Times New Roman', size=12)
ks = KolmogorovSmirnov()
ks_table = ks.KOLMOGOROV_SMIRNOV_TABLE
lilliefors = Lilliefors(language='pt-br')
lilliefors_table = Lilliefors.LILLIEFORS_TABLE
abdi_molin_table = Lilliefors.ABDI_MOLIN_TABLE

plt.figure(figsize=(10,6))
# plt.plot(ks_table['n_rep'], ks_table[0.05], marker="o", color="k", label="Massey")
plt.plot(lilliefors_table['n_rep'], lilliefors_table[0.05], marker="o", color="r", label="Lilliefors")
plt.plot(abdi_molin_table['n_rep'], abdi_molin_table[0.05], marker="o", color="b", label="Abdi & Molin")
plt.legend()
# plt.ylim([0,1])
plt.xlabel("Número de observações")
plt.ylabel("Valor tabelado")
plt.tight_layout()
plt.savefig("lilliefors_abdi_molin_comparative.png", dpi=300, bbox_inches='tight')
plt.show()





# fig, ax = plt.subplots(figsize=(10,6))
# lilliefors.draw_abdi_molin_tabulated_values(ax=ax)
# plt.tight_layout()
# plt.savefig("abidi_molin_tabulated.png", dpi=300, bbox_inches='tight')
# plt.show()

# amostra_1 = np.array([0.8, 1, 2, 2.1, 5, 3.6, 5.6, 6, 3, 4.5, 5, 7, 8.5, 8.9, 8.4, 8.6, 9])
# lilliefors = Lilliefors()
# lilliefors_amostra_1, _ = lilliefors.fit(amostra_1)
# print(lilliefors_amostra_1)
# ks = KolmogorovSmirnov()
# ks_amostra_1, _ = ks.fit(amostra_1)
# print(ks_amostra_1)
# print('\n')
#
#
# amostra_2 = np.array([0.8, 1, 1.1, 1.15, 1.15, 1.2, 1.2, 1.2, 3, 4.5, 5, 2, 8.5, 8.9, 8.4, 8.6, 9])
# lilliefors = Lilliefors()
# lilliefors_amostra_2, _ = lilliefors.fit(amostra_2)
# print(lilliefors_amostra_2)
# ks = KolmogorovSmirnov()
# ks_amostra_2, _ = ks.fit(amostra_2)
# print(ks_amostra_2)
# print('\n')
#
#
# amostra_3 = np.array([0.8, 1, 1.1, 1.15, 1.15, 1.2, 1.2, 1.2, 1.2, 1.6, 1.8, 2, 8.5, 8.9, 8.4, 8.6, 9])
# lilliefors = Lilliefors()
# lilliefors_amostra_3, _ = lilliefors.fit(amostra_3)
# print(lilliefors_amostra_3)
# ks = KolmogorovSmirnov()
# ks_amostra_3, _ = ks.fit(amostra_3)
# print(ks_amostra_3)
# print('\n')
#
#
# plt.figure(figsize=(10,6))
# plt.plot(lilliefors_table['n_rep'], lilliefors_table[0.05], marker="o", color="k", label="Lilliefors")
# plt.plot(ks_table['n_rep'], ks_table[0.05], marker="o", color="r", label="Kolmogorov Smirnov")
# plt.scatter(amostra_1.size, lilliefors_amostra_1[0], marker='o', c='blue', label='Amostra 1')
# plt.scatter(amostra_2.size, lilliefors_amostra_2[0], marker='^', c='blue', label='Amostra 2')
# plt.scatter(amostra_3.size, lilliefors_amostra_3[0], marker='s', c='blue', label='Amostra 3')
# # plt.scatter(x=10, y = 0.5, marker='s', c='blue', label='Amostra 3')
# plt.xlabel("Número de observações")
# plt.ylabel("Valor tabelado")
# plt.legend()
# plt.ylim([0,1])
# plt.tight_layout()
# plt.savefig("ks_lilliefors_comparative.png", dpi=300, bbox_inches='tight')
# plt.show()
#
#
#
# print('ok')























#
#
# def draw_scatter_plot(x_exp, name, decimal_separator='.', local="pt_BR"):
#     """
#     """
#     checkers._check_is_str(name, "name")
#     plot_design = {
#         "scatter": ['o', 'None', 'k', 50],
#     }
#     default_locale = helpers._change_locale(decimal_separator, local)
#
#
#     fig, ax = plt.subplots(figsize=(8,6))
#     ax.scatter(np.arange(1, x_exp.size + 1), x_exp,
#             marker=plot_design["scatter"][0],
#             c=plot_design["scatter"][1],
#             edgecolors=plot_design["scatter"][2],
#             s=plot_design["scatter"][3],
#             label=name)
#
#     ax.set_xlabel("Unordered data")
#     ax.set_ylabel("Data")
#     ax.legend()
#     plt.show()
#
#     helpers._change_locale_back_to_default(default_locale)
#






























#
