"""
desc
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
import numpy as np



###### Home made ######
from pycafee.database_management import management
from pycafee.utils.helpers import PlotsManagement, LanguageManagement
from pycafee.utils import checkers
from pycafee.utils import general
from pycafee.utils import helpers
###########################################
################ Functions ################
###########################################


class DotPlot(PlotsManagement, LanguageManagement):

    def __init__(self, language=None, **kwargs):
        super().__init__(language=language,**kwargs)

    # with tests, with text, with docstring, with database
    def draw(self, x_exp, ax=None, legend_label=None, x_label=None, width='auto', height='auto', export=None, file_name=None, extension=None, dpi=None, tight=None, transparent=None, n_ticks=None, legend=None, decimal_separator=None):
        """This function draws a dot plot with a predefined design

        Parameters
        ----------
        x_exp : 1D :doc:`numpy array <numpy:reference/generated/numpy.array>`
            A ``1`` dimension numpy array with the dataset
        ax : ``None`` or ``matplotlib.axes.SubplotBase``

            * If ``ax`` is ``None``, a figure is created with a preset design. The other parameters can be used to edit and export the graph.
            * If ``ax`` is a ``matplotlib.axes.SubplotBase``, the function returns a ``matplotlib.axes.SubplotBase`` with the dotplot axis. In this case, parameters relatd to wht ``fig`` will not affect the graph.

        legend : ``bool``, optional
            Whether the legend should be add into the chart (``True``) or not (``False``). The default value is ``None``, which implies ``False``.
        legend_label : ``str``, optional
            The label to be displayed on the legend. Default is ``None``, which results in ``"data"``. Only valid if ``legend = True``.
        x_label : ``str``, optional
            The label to be displayed on x label. Default is ``None``, which results in a blank label.
        width : ``"auto"``, ``"default"``, ``int`` or ``float`` (positive), optional
            The ``width`` of the figure.

            * If it is ``"auto"``, it tries to figure out a nice ``width`` for the plot using the data range.
            * If it is ``"default"``, it uses a pre-defined value.
            * If it is a number, it defines the ``width`` of the chart (in inches).

        height : ``"auto"``, ``"default"``, ``int`` or ``float`` (positive), optional
            The ``height`` of the figure.

            * If it is ``"auto"``, it tries to figure out a nice height for the plot using the data range.
            * If it is ``"default"``, it uses a pre-defined value.
            * If it is a number, it defines the height of the chart (in inches).

        export : ``bool``, optional
            Whether the graph should be exported (``True``) or not (``False``). The default value is ``None``, which implies ``False``.
        file_name : ``str``, optional
            The file name. Default is ``None`` which results in a file named ``"dot_plot"``.
        extension : ``str``, optional
            The file extension without a dot. Default is ``None`` which results in a ``".png"`` file.
        dpi : ``int`` or ``float`` (positive), optional
            The figure pixel density. The default is ``None``, which results in a ``100 dpis`` picture. This parameter must be a positive number.
        n_ticks : ``int`` (positive), optional
            The number of evenly spaced ticks to be drawn on the x-axis. The default is ``None``, which uses matplotlib default parameter.
        tight : ``bool``, optional
            Whether the graph should be tight (``True``) or not (``False``). The default value is ``None``, which implies ``True``.
        transparent : ``bool``, optional
            Whether the background of the graph should be transparent (``True``) or not (``False``). The default value is ``None``, which implies ``False`` (e.g, white background).
        decimal_separator : ``str``, optional
            The decimal separator symbol used in the chart. It can be the dot (``None`` or ``"."``) or the comma (``","``).



        Returns
        -------
        x : :doc:`numpy array <numpy:reference/generated/numpy.array>`
            The ``x`` values used to plot the graph.
        y : :doc:`numpy array <numpy:reference/generated/numpy.array>`
            The ``y`` values used to plot the graph.
        axes : ``matplotlib.axes._subplots.AxesSubplot``
            The axis of the graph.


        See Also
        --------
        pycafee.normalitycheck.densityplot.DensityPlot.draw


        References
        ----------
        .. [1] Inspired by FITZGERALD, P. How to create a “dot plot” in Matplotlib? (not a scatter plot). Available at: `stackoverflow.com <https://stackoverflow.com/questions/49703938/how-to-create-a-dot-plot-in-matplotlib-not-a-scatter-plot/64943404#64943404>`_. Access on: 10 May. 2022.


        Examples
        --------

        **Drawing a dot plot with default parameters**

        >>> from pycafee.normalitycheck.dotplot import DotPlot
        >>> import numpy as np
        >>> x = np.array([
                    5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7,
                    5.1, 5.4, 5.1,4.6, 5.1, 4.8, 5.0, 5.0, 5.2, 5.2, 4.7, 4.8, 5.4, 5.2, 5.5, 4.9, 5.0, 5.5, 4.9, 4.4,
                    5.1, 5.0, 4.5, 4.4, 5.0, 5.1,4.8, 5.1, 4.6, 5.3, 5.0
                    ])
        >>> dotplot = DotPlot()
        >>> x, y, axes = dotplot.draw(x, ax=None, export=True)
            The 'dot_plot.png' file was exported!

        .. image:: img/dot_plot.png
           :alt: Graph showing the dot plot
           :align: center


        |

        **Drawing a dot plot**

        >>> from pycafee.normalitycheck.dotplot import DotPlot
        >>> import numpy as np
        >>> x = np.array([
                    5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7,
                    5.1, 5.4, 5.1,4.6, 5.1, 4.8, 5.0, 5.0, 5.2, 5.2, 4.7, 4.8, 5.4, 5.2, 5.5, 4.9, 5.0, 5.5, 4.9, 4.4,
                    5.1, 5.0, 4.5, 4.4, 5.0, 5.1,4.8, 5.1, 4.6, 5.3, 5.0
                    ])
        >>> dotplot = DotPlot()
        >>> x, y, axes = dotplot.draw(x, ax=None, export=True, file_name="my_data", decimal_separator=",", n_ticks=6, x_label='comprimento das sépalas ($cm$)')
            The 'my_data.png' file was exported!

        .. image:: img/my_data.png
           :alt: Graph showing the dot plot
           :align: center


        |

        **Drawing a dot plot using a previously created figure**

        >>> from pycafee.normalitycheck.dotplot import DotPlot
        >>> import numpy as np
        >>> import matplotlib.pyplot as plt
        >>> x = np.array([
                    5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7,
                    5.1, 5.4, 5.1,4.6, 5.1, 4.8, 5.0, 5.0, 5.2, 5.2, 4.7, 4.8, 5.4, 5.2, 5.5, 4.9, 5.0, 5.5, 4.9, 4.4,
                    5.1, 5.0, 4.5, 4.4, 5.0, 5.1,4.8, 5.1, 4.6, 5.3, 5.0
                    ])
        >>> dotplot = DotPlot()
        >>> fig, ax = plt.subplots(figsize=(8,4))
        >>> x, y, ax = dotplot.draw(x, ax=ax)
        >>> plt.savefig("new_plot.png")
        >>> plt.show()

        .. image:: img/new_plot.png
           :alt: Graph showing the dot plot
           :align: center


        """
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
            helpers._check_forbidden_character(file_name, "file_name", self.language)

        ## extension ##
        extension = self._get_default_extension(extension)


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
        checkers._check_is_str(decimal_separator, "decimal_separator", self.language)
        helpers._check_decimal_separator(decimal_separator, self.language)

        ## This was removed due to local issue on colab ##
        ## local ##
        # local = self._get_default_local(local)


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

        ## This was removed due to local issue on colab ##
        # cheking the decimal_separator #
        # default_locale = helpers._change_locale(self.language, decimal_separator, local)

        # lists to export the data #
        axis_x = []
        axis_y = []

        # making the data #
        for value, count in zip(values, counts):
            axis_x.append([value]*count)
            axis_y.append(list(range(count)))

        # flating the data into one dimension array #
        x = np.array(helpers._flat_list_of_lists(axis_x, "axis_x", self.language))
        y = np.array(helpers._flat_list_of_lists(axis_y, "axis_y", self.language))

        ## Createing the dot plot with format ##
        if ax is None:
            fig, axes = plt.subplots(figsize=(width, height))
        else:
            checkers._check_is_subplots(ax, "ax", self.language)
            axes = ax
        # ploting the data #
        axes.scatter(x, y, marker='o', c="None", edgecolors="k",  s=marker_size, label=legend_label)
        # removing spines #
        for spine in ['top', 'right', 'left']:
            axes.spines[spine].set_visible(False)
        # improving y axis #
        axes.yaxis.set_visible(False)
        axes.set_ylim(-1, max(counts))
        # formatting the axes #
        if n_ticks is None:
            pass
        else:
            ticks = np.linspace(min(values), max(values), n_ticks)#, dtype=int)
            axes.set_xticks(ticks)
        axes.tick_params(axis='x', length=5, pad=5)
        # legend #
        if legend:
            axes.legend()

        # decimal separator
        if ax is None:
            axes = helpers._change_decimal_separator_x_axis(fig, axes, decimal_separator)

        # x label #
        if x_label is not None:
            axes.set_xlabel(x_label)

        if ax is None:
            # making the graph "tight" #
            if tight:
                tight = 'tight'
                fig.tight_layout()
            else:
                tight = None

            # exporting the plot #
            if export:
                ### Baptism of Fire ###
                exits, file_name = helpers._check_conflicting_filename(file_name, extension, self.language)

                plt.savefig(file_name, dpi=dpi, transparent=transparent, bbox_inches=tight)
                ### quering ###
                if exits == False:
                    func_name = "draw_density_function" # reaproveitando database
                    fk_id_function = management._query_func_id(func_name)
                    messages = management._get_messages(fk_id_function, self.language, func_name)
                    general._display_one_line_success(f"{messages[1][0][0]} '{file_name}' {messages[1][2][0]}")
            # showing the plot #
            plt.show()


        ## This was removed due to local issue on colab ##
        # helpers._change_locale_back_to_default(default_locale)

        return x, y, axes



























#
