import os
os.system('cls')
print(">>>")




from pycafee.normalitycheck.densityplot import DensityPlot
import numpy as np
x_exp = np.array([
            5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7,
            5.1, 5.4, 5.1,4.6, 5.1, 4.8, 5.0, 5.0, 5.1, 5.2, 5.2, 4.7, 4.8, 5.4, 5.2, 5.5, 4.9, 5.0, 5.5, 4.9, 4.4,
            5.1, 5.0, 4.5, 4.4, 5.0, 5.1,4.8, 5.1, 4.6, 5.3, 5.0
            ])
densityplot = DensityPlot(language="pt-br")
densityplot.draw(x_exp, which="all", export=True, file_name="my_data", plot_design="colored", x_label="Comprimento das sépalas ($cm$)")
