"""This module concentrates

"""

# Function list:
#
#     DefaultPlots:
#         This class just has the default values for ploting
#
#     MakePlots(DefaultPlots, AlphaManagement):
#         This class concentrates all plots
#         - _get_default_width(self,width)
#         - _get_default_height(self,height)
#         - _get_default_export(self,export)
#         - _get_default_extension(self,extension)
#         - _get_default_dpi(self,dpi)
#         - _get_default_tight(self,tight)
#         - _get_default_transparent(self,transparent)
#         - _get_default_legend(self,legend)
#         - _get_default_x_label(self, x_label)
#         - _get_default_y_label(self, y_label)
#         - _get_default_decimal_separator(self, decimal_separator)
#         - _get_default_local(self, local)
#         - _get_default_legend_label(self, legend_label)
#         - draw_dot_plot(self, x_exp, *args)
#         - draw_density_function(self, x_exp, *args)
#
#
#########################################
################ Imports ################
#########################################

###### Standard ######
from collections import Counter
from itertools import takewhile

###### Third part ######
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde as parametric_gaussian

###### Home made ######
from pycafee.database_management import management
from pycafee.functions import functions
from pycafee.utils import checkers
from pycafee.utils import helpers
from pycafee.utils import general
from pycafee.utils.helpers import AlphaManagement



###########################################
################ Functions ################
###########################################

class DefaultPlots:
    """
    This class just instantiates the default values for ploting. This may be used for database parameters.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # enviar estes valores para a database e permiter a alteração(?)
        self.width = 12
        self.height = 6
        self.export = False
        self.extension = "png"
        self.dpi = 100
        self.tight = True
        self.transparent = False
        self.legend = True
        self.decimal_separator = "."
        self.local = "pt_BR"
        self.legend_label = "data"
        self.x_label = "data"
        self.y_label = "data"





class MakePlots(DefaultPlots, AlphaManagement):
    """This class instantiates an object to make plots with pre-defined layout.

    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _get_default_width(self,width):
        if width == 'default':
            width = self.width
        else:
            checkers._check_is_float_int(width, "width", self.language)
        return width

    def _get_default_height(self,height):
        if height == 'default':
            height = self.height
        else:
            checkers._check_is_float_int(height, "height", self.language)
        return height

    def _get_default_export(self,export):
        if export is None:
            export = self.export
        else:
            checkers._check_is_bool(export, "export", self.language)
        return export

    def _get_default_extension(self, extension):
        if extension is None:
            extension = self.extension
        else:
            checkers._check_is_str(extension, "extension", self.language)
            helpers._check_forbidden_character(extension, "extension", self.language)
            helpers._check_figure_extension(extension, "extension", self.language)
        return extension

    def _get_default_dpi(self,dpi):
        if dpi is None:
            dpi = self.dpi
        else:
            checkers._check_is_float_int(dpi, "dpi", self.language)
            checkers._chek_is_positive(dpi, "dpi", self.language)
        return dpi

    def _get_default_tight(self,tight):
        if tight is None:
            tight = self.tight
        else:
            checkers._check_is_bool(tight, "tight", self.language)
        return tight

    def _get_default_transparent(self,transparent):
        if transparent is None:
            transparent = self.transparent
        else:
            checkers._check_is_bool(transparent, "transparent", self.language)
        return transparent

    def _get_default_legend(self,legend):
        if legend is None:
            legend = self.legend
        else:
            checkers._check_is_bool(legend, "legend", self.language)
        return legend

    def _get_default_x_label(self, x_label):
        if x_label is None:
            x_label = self.x_label
        else:
            checkers._check_is_str(x_label, "x_label", self.language)
        return x_label

    def _get_default_y_label(self, y_label):
        if y_label is None:
            y_label = self.y_label
        else:
            checkers._check_is_str(y_label, "y_label", self.language)
        return y_label

    def _get_default_decimal_separator(self, decimal_separator):
        if decimal_separator is None:
            decimal_separator = self.decimal_separator
        else:
            pass # o controle é feito em outra função
        return decimal_separator

    def _get_default_local(self, local):
        if local is None:
            local = self.local
        else:
            pass # o controle é feito em outra função
        return local

    def _get_default_legend_label(self, legend_label):
        if legend_label is None:
            legend_label = self.legend_label
        else:
            checkers._check_is_str(legend_label, "legend_label", self.language)
        return legend_label

    # Experimental, with text, with database, NO test
    def draw_dot_plot(self, x_exp, legend_label=None, x_label=None, width='auto', height='auto', export=None, file_name=None, extension=None, dpi=None, tight=None, transparent=None, n_ticks=None, legend=None, decimal_separator=None, local=None):
        """This function draws a dot plot with a predefined design

        Parameters
        ----------
        x_exp : 1D :doc:`numpy array <numpy:reference/generated/numpy.array>`
            A 1 dimension numpy array with the dataset
        legend_label : ``str``, optional
            The label to be displayed on the legend. Default is ``None``, which results in ``"data"``.
        x_label : ``str``, optional
            The label to be displayed on x label. Default is ``None``, which results in a blank label.
        width : ``'auto'``, ``'default'``, ``int`` or ``float`` (positive), optional
            The ``width`` of the figure. If it is ``'auto'``, it tries to figure out a nice width for the plot using the data range. If it is ``'default'``, it uses a pre-defined value. If it is a number, it defines the width of the chart (in inches).
        height : ``'auto'``, ``'default'``, ``int`` or ``float`` (positive), optional
            The ``height`` of the figure. If it is ``'auto'``, it tries to figure out a nice height for the plot using the data range. If it is ``'default'``, it uses a pre-defined value. If it is a number, it defines the height of the chart (in inches).
        export : ``bool``, optional
            Whether the graph should be exported (``True``) or not (``False``). The default value is ``None``, which implies ``False``.
        file_name : ``str``, optional
            The file name. Default is ``None`` which results in a file named ``"dot_plot"``.
        extension : ``str``, optional
            The file extension without a dot. Default is ``None`` which results in a ``".png"`` file.
        dpi : ``int`` or ``float``, optional
            The figure pixel density. The default is ``None``, which results in a ``100 dpis`` picture. This parameter must be a number higher than zero.
        n_ticks : ``int``, optional
            The number of evenly spaced ticks to be drawn on the x-axis. The default is ``None``, which uses matplotlib default parameter.
        tight : ``bool``, optional
            Whether the graph should be tight (``True``) or not (``False``). The default value is ``None``, which implies ``True``.
        transparent : ``bool``, optional
            Whether the background of the graph should be transparent (``True``) or not (``False``). The default value is ``None``, which implies not transparent (white).
        legend : ``bool``, optional
            Whether the legend should be inserted into the chart (``True``) or not (``False``). The default value is ``None``, which does not insert the legend into the plot (``False``).
        decimal_separator : ``str``, optional
            The decimal separator symbol used in the chart. It can be the dot (``None`` or ``'.'``) or the comma (``','``).
        local : ``str``, optional
            The alias for the desired locale. Only used if ``decimal_separator=','`` to set the matplolib's default locale. Its only function is to change the decimal separator symbol and should be changed only if the ``"pt_BR"`` option is not available.


        Returns
        -------
        x : :doc:`numpy array <numpy:reference/generated/numpy.array>`
            The x values used to plot the graph.
        y : :doc:`numpy array <numpy:reference/generated/numpy.array>`
            The y values used to plot the graph.

        Notes
        -----

        .. admonition:: \u2615

            To obtain which extensions the figure can be exported, use the following script:

            >>> from matplotlib import pyplot as plt
            >>> suported_types = plt.gcf().canvas.get_supported_filetypes()
            >>> for key, value in suported_types.items():
                    print(key, ":", value)
            >>> plt.close()


        References
        ----------
        .. [1] Inspired by https://stackoverflow.com/a/64943404/17872198


        Examples
        --------

        >>> from easy_stat.functions.plots import MakePlots
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7,
                        5.1, 5.4, 5.1,4.6, 5.1, 4.8, 5.0, 5.0, 5.2, 5.2, 4.7, 4.8, 5.4, 5.2, 5.5, 4.9, 5.0, 5.5, 4.9, 4.4,
                        5.1, 5.0, 4.5, 4.4, 5.0, 5.1,4.8, 5.1, 4.6, 5.3, 5.0
                        ])
        >>> plots = MakePlots()
        >>> plots.draw_dot_plot(x)


        .. image:: img/dot_plot.png
           :alt: Graph showing the dot plot
           :align: center

        """
        general._display_warn(
            aviso = "    UserWarning",
            texto = "This function is experimental"
        )
        ### Checking the input parameters ###

        ## x_exp ##
        checkers._check_is_numpy_1_D(x_exp, "x_exp", self.language)

        ## legend_label ##
        legend_label = self._get_default_legend_label(legend_label)

        ## width ##
        if width == 'auto':
            width = None
        else:
            width = self._get_default_width(width)

        ## height ##
        if height == 'auto':
            height = None
        else:
            height = self._get_default_height(height)

        ## export ##
        export = self._get_default_export(export)

        ## file name ##
        if file_name is None:
            file_name = "dot_plot"
        else:
            checkers._check_is_str(file_name, "file_name", self.language)
            helpers._check_forbidden_character(file_name, "file_name")

        ## extension ##
        extension = self._get_default_extension(extension)


        ### Baptism of Fire ###
        file_name = helpers._check_conflicting_filename(file_name, extension, self.language)

        ## dpi ##
        dpi = self._get_default_dpi(dpi)

        ## n_ticks ##
        if n_ticks is not None:
            checkers._check_is_integer(n_ticks, "n_ticks", self.language)

        ## tight ##
        tight = self._get_default_tight(tight)

        ## transparent ##
        transparent = self._get_default_transparent(transparent)

        ## Legend ##
        if legend is None:
            legend = False
        else:
            legend = self._get_default_legend(legend)

        ## decimal_separator ##
        decimal_separator = self._get_default_decimal_separator(decimal_separator)

        ## local ##
        local = self._get_default_local(local)


        ### drawing the graph ###
        ## counting the number of unique values within x_exp ##
        values, counts = np.unique(x_exp, return_counts=True)

        ## formatting the chart according to the data ##
        data_range = max(values) - min(values)

        # width #
        if width is None:
            if data_range < 10:
                width = 4
            elif data_range < 30:
                width = data_range/2
            else:
                width = 8
        else:
            pass

        # height #
        if height is None:
            if data_range < 50:
                height = max(counts)/4
            else:
                height = max(counts)/2
        else:
            pass

        if width is not None or height is not None:
            if data_range < 50:
                marker_size = 40
            else:
                marker_size = np.ceil(200 / (data_range//10))
        else:
            marker_size = None

        # cheking the decimal_separator #
        default_locale = helpers._change_locale(decimal_separator, local, self.language)

        ## Createing the dot plot with format ##
        fig, ax = plt.subplots(figsize=(width, height))

        # lists to export the data #
        axis_x = []
        axis_y = []

        # making the data #
        for value, count in zip(values, counts):
            axis_x.append([value]*count)
            axis_y.append(list(range(count)))

        # flating the data into one dimension array #
        x = np.array(helpers._flat_list_of_lists(axis_x, "axis_x"))
        y = np.array(helpers._flat_list_of_lists(axis_y, "axis_y"))

        # ploting the data #
        ax.scatter(x, y, marker='o', c="None", edgecolors="k",  s=marker_size, label=legend_label)

        # removing spines #
        for spine in ['top', 'right', 'left']:
            ax.spines[spine].set_visible(False)

        # improving y axis #
        ax.yaxis.set_visible(False)
        ax.set_ylim(-1, max(counts))

        # formatting the axes #
        if n_ticks is None:
            pass
        else:
            ticks = np.linspace(min(values), max(values), n_ticks)#, dtype=int)
            ax.set_xticks(ticks)
        ax.tick_params(axis='x', length=5, pad=5)

        # legend #
        if legend:
            ax.legend()

        # x label #
        if x_label is not None:
            ax.set_xlabel(x_label)


        # making the graph "tight" #
        if tight:
            tight = 'tight'
            fig.tight_layout()
        else:
            tight = None

        # exporting the plot #
        if export:
            plt.savefig(file_name, dpi=dpi, transparent=transparent, bbox_inches=tight)
            ### quering ###
            func_name = "draw_dot_plot"
            fk_id_function = management._query_func_id(func_name)
            messages = management._get_messages(fk_id_function, self.language, func_name)
            general._display_one_line_attention(f"{messages[1][0][0]} '{file_name}' {messages[1][2][0]}")

        # showing the plot #
        plt.show()

        helpers._change_locale_back_to_default(default_locale)

        return x, y

    # Experimental, with text, with database, NO test
    def draw_density_function(self, x_exp, bw_method=None, which=None, legend_label=None, x_label=None, y_label=None, width='default', height='default', export=None, file_name=None, extension=None, dpi=None, tight=None, transparent=None, plot_design='default', legend=None, decimal_separator=None, local=None):
        """This function draws the non-parametric density plot with the central tendency measurements

        Parameters
        ----------
        x_exp : 1D :doc:`numpy array <numpy:reference/generated/numpy.array>`
            The data to be fitted
        bw_method : ``str``, optional
            The method used to calculate the estimator bandwidth. This can be ``'scott'`` or ``'silverman'``. If ``None`` (default), the scott method is used. This is the ``bw_method`` from ``scipy.stats.gaussian_kde()``, but limited to ``'scott'`` or ``'silverman'`` options. For other options, use the original method [1]_.
        which : ``str``, optional
            The parameter which controls which measures of central tendency should be added to the graph. The options are:
                - ``None`` (default): no measures of central tendency are included;
                - ``'mean'``: adds the mean;
                - ``'median'``: adds the median;
                - ``'mode'``: adds the mode(s);
                - ``'all'``: adds the mean, median and the mode(s);

            To add two measures of central tendency, combine their names separated by a comma (``','``). For example, to add the mean and median, use ``which = "mean,median"``.
        legend_label : ``str``, optional
            The label to be displayed on the legend. Default is ``None``, which results in ``"Non parametric density"``.
        x_label : ``str``, optional
            The label to be displayed on x label. Default is ``None``, which results in ``"data"``.
        y_label : ``str``, optional
            The label to be displayed on y label. Default is ``None``, which results in ``"Non-parametric density"``.
        width : ``'auto'``, ``'default'``, ``int`` or ``float`` (positive), optional
            The width of the figure. If it is ``'auto'``, it tries to figure out a nice width for the plot using the data range. If it is ``'default'``, it uses a pre-defined value. If it is a number, it defines the width of the chart (in inches).
        height : ``'auto'``, ``'default'``, ``int`` or ``float`` (positive), optional
            The height of the figure. If it is ``'auto'``, it tries to figure out a nice height for the plot using the data range. If it is ``'default'``, it uses a pre-defined value. If it is a number, it defines the height of the chart (in inches).
        export : ``bool``, optional
            Whether the graph should be exported (``True``) or not (``False``). The default value is ``None``, which implies ``False``.
        file_name : ``str``, optional
            The file name. Default is ``None`` which results in a file named ``"kernal_density"``.
        extension : ``str``, optional
            The file extension without a dot. Default is ``None`` which results in a ``".png"`` file.
        dpi : ``int`` or ``float``, optional
            The figure pixel density. The default is ``None``, which results in a ``100 dpis`` picture. This parameter must be a number higher than zero.
        tight : ``bool``, optional
            Whether the graph should be tight (``True``) or not (``False``). The default value is ``None``, which implies ``True``.
        transparent : ``bool``, optional
            Whether the background of the graph should be transparent (``True``) or not (``False``). The default value is ``None``, which implies not transparent (white).
        plot_design : ``str`` or ``dict``, optional
            The plot desing. If ``'default'``, uses a simple desing (default). If ``'colored'``, uses a colored desing. If ``dict``, it must have five ``keys`` (``"kde"``, ``"Mean"``, ``"Median"``, ``"Mode"``, ``"Area"``), where each one defines the design of each element added to the chart.

            The ``values`` for all ``keys`` must be a ``list``. The lists of the keys ``"kde"``, ``"Mean"``, ``"Median"``, and ``"Mode"`` must have:
                - the first element must be a ``str`` with the name of the color;
                - the second element must be a ``str`` with the style of the line;
                - the third element must be a number (``int`` or ``float``) with the thickness of the line.

            The ``Area`` list must have a single element, which is a ``str`` with the name of the color that fills the area between the fit and the line ``y = 0``.

            For example:

            .. code-block:: python

                plot_design = {
                    "kde": ['k', '-', 1.5],
                    "Mean": ['dimgray', '--', 1.5],
                    "Median": ['darkgray', '--', 1.5],
                    "Mode": ['lightgray', '--', 1.5],
                    "Area": ['white'],
                }


        legend : ``bool``, optional
            Whether the legend should be inserted into the chart (``True``) or not (``False``). The default value is ``None``, which does not insert the legend into the plot (``False``).
        decimal_separator : ``str``, optional
            The decimal separator symbol used in the chart. It can be the dot (``None`` or ``'.'``) or the comma (``','``).
        local : ``str``, optional
            The alias for the desired locale. Only used if ``decimal_separator = ','`` to set the matplolib's default ``locale``. Its only function is to change the decimal separator symbol and should be changed only if the ``"pt_BR"`` option is not available.


        Returns
        -------
        kde_x : :doc:`numpy array <numpy:reference/generated/numpy.array>`
            The x values used to plot the graph
        kde_y : :doc:`numpy array <numpy:reference/generated/numpy.array>`
            The y values used to plot the graph
        central_tendency : ``dict``
            A dictionary with the measures of central tendency of the data with respective value estimated by the kde function.

        Notes
        -----

        .. admonition:: \u2615

            To obtain which extensions the figure can be exported, use the following script:

            >>> from matplotlib import pyplot as plt
            >>> suported_types = plt.gcf().canvas.get_supported_filetypes()
            >>> for key, value in suported_types.items():
                    print(key, ":", value)
            >>> plt.close()


        The mode is calculated using the multimode function.

        A list of color names can be found at matplotlib reference [2]_.

        A list of linestyles can be found at reference [3]_.

        References
        ----------
        .. [1] https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html
        .. [2] https://matplotlib.org/stable/_images/sphx_glr_named_colors_003.png
        .. [3] https://raw.githubusercontent.com/andersonmdcanteli/matplotlib-course/main/auxiliary-scripts/matplotli-all-linestyles/matplotlib_linestyles.png

        Examples
        --------

        >>> from easy_stat.functions.plots import MakePlots
        >>> import numpy as np
        >>> x = np.array([5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7,
                        5.1, 5.4, 5.1,4.6, 5.1, 4.8, 5.0, 5.0, 5.2, 5.2, 4.7, 4.8, 5.4, 5.2, 5.5, 4.9, 5.0, 5.5, 4.9, 4.4,
                        5.1, 5.0, 4.5, 4.4, 5.0, 5.1,4.8, 5.1, 4.6, 5.3, 5.0
                        ])
        >>> plots = MakePlots()
        >>> plots.draw_density_function(x, export=True, which="all", plot_design='colored')

        .. image:: img/kernal_density.png
           :alt: Graph showing the dot plot
           :align: center





        """
        general._display_warn(
            aviso = "    UserWarning",
            texto = "This function is experimental"
        )
        ### Checking the input parameters ###

        ## x_exp ##
        checkers._check_is_numpy_1_D(x_exp, param_name="x_exp", language=self.language)

        ## bw_method ##
        if bw_method is None:
            bw_method = "scott"
        else:
            checkers._check_is_str(bw_method, "bw_method")
            if bw_method not in ["scott", "silverman"]:
                try:
                    raise ValueError("Not allowed key")
                except ValueError:
                    general._display_one_line_attention(
                        f"The parameter 'bw_method' only accepts 'scott' or 'silverman' as key, but we got: {bw_method}",
                    )
                    raise

        ## which ##
        if which is None:
            which = "None"
        else:
            checkers._check_is_str(which, "which", self.language)
            which = helpers._check_which_density_gaussian_kernal_plot(which)

        ## legend_label ##
        if legend_label is None:
            legend_label = "Non-parametric density"
        else:
            legend_label = self._get_default_legend_label(legend_label)

        ## x_label ##
        x_label = self._get_default_x_label(x_label)

        if y_label is None:
            y_label = "Non-parametric density"
        else:
            y_label = self._get_default_y_label(y_label)

        ## width ##
        width = self._get_default_width(width)

        ## height ##
        height = self._get_default_height(height)

        ## export ##
        export = self._get_default_export(export)

        ## file_name ##
        if file_name is None:
            file_name = "kernal_density"
        else:
            checkers._check_is_str(file_name, "file_name", self.language)
            helpers._check_forbidden_character(file_name, "file_name")

        ## extension ##
        extension = self._get_default_extension(extension)

        ## Baptism of fire ##
        file_name = helpers._check_conflicting_filename(file_name, extension, self.language)

        ## dpi ##
        dpi = self._get_default_dpi(dpi)

        ## tight ##
        tight = self._get_default_tight(tight)

        ## transparent ##
        transparent = self._get_default_transparent(transparent)

        ## plot design ##
        if plot_design == 'default':
            plot_design = {
                "kde": ['k', '-', 1.5],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', '--', 1.5],
                "Mode": ['lightgray', '--', 1.5],
                "Area": ['white'],
            }
        elif plot_design == "colored":
            plot_design = {
                "kde": ['k', '-', 1.5],
                "Mean": ['red', '--', 1.5],
                "Median": ['blue', '--', 1.5],
                "Mode": ['green', '--', 1.5],
                "Area": ['gainsboro'],
            }
        else:
            plot_design_default = {
                "kde": ['k', '-', 1.5],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', '--', 1.5],
                "Mode": ['lightgray', '--', 1.5],
                "Area": ['white'],
            }
            plot_design_example = {
                "kde": "['color name', 'line style', number]",
                "Mean": "['color name', 'line style', number]",
                "Median": "['color name', 'line style', number]",
                "Mode": "['color name', 'line style', number]",
                "Area": "['color name']",
            }
            helpers._check_plot_design(plot_design, "plot_design", plot_design_default, plot_design_example)

        ## Legend ##
        legend = self._get_default_legend(legend)

        ## decimal_separator ##
        decimal_separator = self._get_default_decimal_separator(decimal_separator)

        ## local ##
        local = self._get_default_local(local)

        ### Getting the measures of central tendency ###
        mean = np.mean(x_exp)
        median = np.median(x_exp)
        modas = functions.multimode(x_exp)
        modas = list(modas.items())


        ### estimating the kde ###
        kde = parametric_gaussian(x_exp, bw_method = bw_method)


        ### getting generic values to use on the x axis ###
        kde_x = np.linspace(min(x_exp), max(x_exp), 1000)


        ### calculating nonparametric density values ###
        kde_y = kde(kde_x)

        ### cheking the decimal_separator ###
        default_locale = helpers._change_locale(decimal_separator, local, self.language)

        ### plotando o gráfico ##
        fig, ax = plt.subplots(figsize=(width,height))

        ## adding the predicted values ##
        ax.plot(kde_x, kde_y,
            color=plot_design["kde"][0],
            ls = plot_design["kde"][1],
            lw=plot_design["kde"][2],
            label=legend_label
        )
        ## adding background color ##
        ax.fill_between(kde_x, kde_y, color=plot_design["Area"][0])
        ## adding measures of central tendency ##
        central_tendency = {}
        if which[0] == "all":
            ax.vlines(mean, 0, kde(mean),
                        color=plot_design["Mean"][0],
                        label="Mean",
                        ls=plot_design["Mean"][1],
                        lw=plot_design["Mean"][2]
                    )
            central_tendency["mean"] = [mean, kde(mean)[0]]
            ax.vlines(median, 0, kde(median),
                        color=plot_design["Median"][0],
                        label="Median",
                        ls=plot_design["Median"][1],
                        lw=plot_design["Median"][2]
                    )
            central_tendency["median"] = [median, kde(median)[0]]
            # adding mode #
            if None in modas[0]:
                print("\n")
                print("    ---> UserWarning: The data does not have a mode (all values are unique)")
                print("\n")
            else:
                if len(modas) > 1:
                    print("\n")
                    print("    ---> UserWarning: The data has more than one mode")
                    print("         Bimodal or multi-modal distributions tend to be oversmoothed")
                    print("\n")
                moda_aux = []
                for i in range(len(modas)):
                    moda_aux.append([modas[i][0], kde(modas[i][0])[0]])

                    if i != len(modas)-1:
                        ax.vlines(modas[i][0], 0, kde(modas[i][0]), color=plot_design["Mode"][0], ls=plot_design["Mode"][1], lw=plot_design["Mode"][2])
                    else:
                        ax.vlines(modas[i][0], 0, kde(modas[i][0]), color=plot_design["Mode"][0], label="Mode", ls=plot_design["Mode"][1], lw=plot_design["Median"][2])
                central_tendency["mode"] = moda_aux
        else:
            if "mean" in which:
                ax.vlines(mean, 0, kde(mean),
                        color=plot_design["Mean"][0], label="Mean", ls=plot_design["Mean"][1], lw=plot_design["Mean"][2])
                central_tendency["mean"] = [mean, kde(mean)[0]]
            if "median" in which:
                ax.vlines(median, 0, kde(median),
                        color=plot_design["Median"][0], label="Median", ls=plot_design["Median"][1], lw=plot_design["Median"][2])
                central_tendency["median"] = [median, kde(median)[0]]
            if "mode" in which:
                if None in modas[0]:
                    print("\n")
                    print("    ---> UserWarning: The data does not have a mode (all values are unique)")
                    print("\n")
                else:
                    if len(modas) > 1:
                        print("\n")
                        print("    ---> UserWarning: The data has more than one mode")
                        print("         Bimodal or multi-modal distributions tend to be oversmoothed")
                        print("\n")
                    moda_aux = []
                    for i in range(len(modas)):
                        if i != len(modas)-1:
                            ax.vlines(modas[i][0], 0, kde(modas[i][0]),
                                    color=plot_design["Mode"][0], ls=plot_design["Mode"][1], lw=plot_design["Mode"][2])
                        else:
                            ax.vlines(modas[i][0], 0, kde(modas[i][0]),
                                    color=plot_design["Mode"][0], label="Mode", ls=plot_design["Mode"][1], lw=plot_design["Mode"][2])
                    central_tendency["mode"] = moda_aux

        # legend #
        if legend:
            ax.legend()

        # x label #
        ax.set_xlabel(x_label)

        # y label #
        ax.set_ylabel(y_label)
        ax.set_ylim(bottom=0, top=None) # limiting to start at y = 0

        # leaving the graph "tight" #
        if tight:
            tight = 'tight'
            fig.tight_layout()
        else:
            tight = None

        # exporting the plot #
        if export:
            plt.savefig(file_name, dpi=dpi, transparent=transparent, bbox_inches=tight)
            ### quering ###
            func_name = "draw_density_function"
            fk_id_function = management._query_func_id(func_name)
            messages = management._get_messages(fk_id_function, self.language, func_name)
            general._display_one_line_attention(f"{messages[1][0][0]} '{file_name}' {messages[1][2][0]}")

        plt.show()
        helpers._change_locale_back_to_default(default_locale)
        return kde_x, kde_y, central_tendency







# We live in every moment but this one... Why don't we recognize the faces loving us so https://youtu.be/kAFxLXqP8UM?t=45
