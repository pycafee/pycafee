"""
Este módulo concentra os métodos de comparação entre os diferentes métodos numéricos de verificar normalidade dos dados
"""

##########################################
################ Summmary ################
##########################################



#########################################
################ Imports ################
#########################################

###### Standard ######



###### Third part ######
import matplotlib.pyplot as plt




###### Home made ######
from pycafee.normalitycheck.lilliefors import Lilliefors
from pycafee.normalitycheck.kolmogorovsmirnov import KolmogorovSmirnov

from pycafee.utils.helpers import AlphaManagement, NDigitsManagement, PlotsManagement

###########################################
################ Functions ################
###########################################


class Comaparison(AlphaManagement, NDigitsManagement, PlotsManagement):

    def __init__(self):
        # print("Anderson Darling")
        pass

    def tabulated_comparison(self, which):
        """
        """

        if 'lilliefors' in which:
            lilli = Lilliefors()
            lilli_table = lilli.LILLI_TABLE

        if 'abdi' in which:
            abdi_molin = Lilliefors()
            abdi_molin_table = abdi_molin.ABDI_MOLIN_TABLE


        if 'kolmogorov' in which:
            ks = KolmogorovSmirnov()
            ks_table = ks.KS_TABLE



























#
