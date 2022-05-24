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
from scipy.stats import gaussian_kde as parametric_gaussian


###### Home made ######
from pycafee.database_management import management
from pycafee.functions import functions
from pycafee.utils.helpers import PlotsManagement, LanguageManagement
from pycafee.utils import checkers
from pycafee.utils import general
from pycafee.utils import helpers
###########################################
################ Functions ################
###########################################


class DensityPlot(PlotsManagement, LanguageManagement):

    def __init__(self, language=None, **kwargs):
        super().__init__(language=language,**kwargs)

    # with tests, with text, with docstring, with database
    def draw(self, x_exp, ax=None, bw_method=None, which=None, x_label=None, y_label=None, width='default', height='default', export=None, file_name=None, extension=None, dpi=None, tight=None, transparent=None, plot_design='gray', legend=None, decimal_separator=None, local=None):
        """This function draws the non-parametric density plot with the option to add the central tendency measurements

        Parameters
        ----------
        x_exp : 1D :doc:`numpy array <numpy:reference/generated/numpy.array>`
            The data to be fitted
        ax : ``None`` or ``matplotlib.axes.SubplotBase``
            * If ``ax`` is ``None``, a figure is created with a preset design. The other parameters can be used to edit and export the graph.
            * If ``ax`` is a ``matplotlib.axes.SubplotBase``, the function returns a ``matplotlib.axes.SubplotBase`` with the DensityPlot axis. In this case, only the ``which`` and ``bw_method`` parameters affect the plot.
        bw_method : ``str``, optional
            The method used to calculate the estimator bandwidth. This can be ``"scott"`` or ``"silverman"``. If ``None`` (default), the ``"scott"`` method is used. This is the ``bw_method`` parameter from ``scipy.stats.gaussian_kde()``, but limited to ``"scott"`` or ``"silverman"`` options. For other options, use the original method [1]_.
        which : ``str``, optional
            The parameter which controls which measures of central tendency should be added to the graph. The options are:

                - ``None`` (default): no measures of central tendency are included;
                - ``"mean"``: adds the mean;
                - ``"median"``: adds the median;
                - ``"mode"``: adds the mode(s) (only if the data has a mode);
                - ``"all"``: adds the mean, median and the mode(s) (if the data das a mode);

            To add two measures of central tendency, combine their names separated by a comma (``","``). For example, to add the mean and the median, use ``which = "mean,median"``.
        legend : ``bool``, optional
            Whether the legend should be added into the chart (``True``) or not (``False``). The default value is ``None``, which implies ``True``.
        x_label : ``str``, optional
            The label to be displayed on x label. Default is ``None``, which results in ``"data"``.
        y_label : ``str``, optional
            The label to be displayed on y label. Default is ``None``, which results in ``"Non-parametric density"``.
        width : ``"default"``, ``int`` or ``float`` (positive), optional
            The width of the figure. If it is ``"default"``, it uses a pre-defined value. If it is a number, it defines the ``width`` of the chart (in inches).
        height : ``"default"``, ``int`` or ``float`` (positive), optional
            The height of the figure. If it is ``"default"``, it uses a pre-defined value. If it is a number, it defines the ``height`` of the chart (in inches).
        export : ``bool``, optional
            Whether the graph should be exported (``True``) or not (``False``). The default value is ``None``, which implies ``False``.
        file_name : ``str``, optional
            The file name. Default is ``None`` which results in a file named ``"kernal_density"``.
        extension : ``str``, optional
            The file extension without a dot. Default is ``None`` which results in a ``".png"`` file.
        dpi : ``int`` or ``float`` (positive), optional
            The figure pixel density. The default is ``None``, which results in a ``100 dpis`` picture. This parameter must be a number higher than zero.
        tight : ``bool``, optional
            Whether the graph should be tight (``True``) or not (``False``). The default value is ``None``, which implies ``True``.
        transparent : ``bool``, optional
            Whether the background of the graph should be transparent (``True``) or not (``False``). The default value is ``None``, which implies ``False`` (white).
        plot_design : ``str`` or ``dict``, optional
            The plot desing. If ``"gray"``, uses a gray-scale desing (default). If ``"colored"``, uses a colored desing. If ``dict``, it must have five ``keys`` (``"kde"``, ``"Mean"``, ``"Median"``, ``"Mode"``, ``"Area"``), where each one defines the design of each element added to the chart.
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
        axes : ``matplotlib.axes._subplots.AxesSubplot``
            The axis of the graph.

        See Also
        --------
        pycafee.normalitycheck.dotplot.DotPlot.draw


        Notes
        -----

        The ``plot_design`` paramter must be a dict where the ``values`` for all ``keys`` must be a ``list``. The lists of the keys ``"kde"``, ``"Mean"``, ``"Median"``, and ``"Mode"`` must have:

            * the first element must be a ``str`` with the color name;
            * the second element must be a ``str`` with line style;
            * the third element must be a number (``int`` or ``float``, positive) with the line thickness.

        The ``Area`` list must have a single element, which is a ``str`` with the name of the color that fills the area between the fit and the line ``y = 0``. For example:

        .. code-block:: python

            plot_design = {
                "kde": ['k', '-', 1.5],
                "Mean": ['dimgray', '--', 1.5],
                "Median": ['darkgray', '--', 1.5],
                "Mode": ['lightgray', '--', 1.5],
                "Area": ['white'],
            }

        .. admonition:: \u2615

            To obtain which extensions the figure can be exported, use the following script:

            >>> from matplotlib import pyplot as plt
            >>> suported_types = plt.gcf().canvas.get_supported_filetypes()
            >>> for key, value in suported_types.items():
                    print(key, ":", value)
            >>> plt.close()


        The mode is calculated using the :ref:`multimode <multimode>` function.

        A list of color names can be found at `matplotlib's documentation <https://matplotlib.org/stable/_images/sphx_glr_named_colors_003.png>`_.

        A list of linestyles can be found `here <https://raw.githubusercontent.com/andersonmdcanteli/matplotlib-course/main/auxiliary-scripts/matplotli-all-linestyles/matplotlib_linestyles.png>`_.

        References
        ----------
        .. [1] SCIPY. scipy.stats.gaussian_kde. Available at: `www.scipy.org <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.html>`_. Access on: 10 May. 2022.


        Examples
        --------

        **Nonparametric density plot with default parameters plus the measures of central tendency.**

        >>> from pycafee.normalitycheck.densityplot import DensityPlot
        >>> import numpy as np
        >>> x_exp = np.array([
                    5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7,
                    5.1, 5.4, 5.1,4.6, 5.1, 4.8, 5.0, 5.0, 5.1, 5.2, 5.2, 4.7, 4.8, 5.4, 5.2, 5.5, 4.9, 5.0, 5.5, 4.9, 4.4,
                    5.1, 5.0, 4.5, 4.4, 5.0, 5.1,4.8, 5.1, 4.6, 5.3, 5.0
                    ])
        >>> densityplot = DensityPlot()
        >>> densityplot.draw(x_exp, which="all", export=True)
            The 'kernal_density.png' file was exported!


        .. image:: img/kernal_density.png
           :alt: Graph showing the dot plot
           :align: center


        |

        **Nonparametric density with some editing**

        >>> from pycafee.normalitycheck.densityplot import DensityPlot
        >>> import numpy as np
        >>> x_exp = np.array([
                    5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 5.4, 4.8, 4.8, 4.3, 5.8, 5.7, 5.4, 5.1, 5.7,
                    5.1, 5.4, 5.1,4.6, 5.1, 4.8, 5.0, 5.0, 5.1, 5.2, 5.2, 4.7, 4.8, 5.4, 5.2, 5.5, 4.9, 5.0, 5.5, 4.9, 4.4,
                    5.1, 5.0, 4.5, 4.4, 5.0, 5.1,4.8, 5.1, 4.6, 5.3, 5.0
                    ])
        >>> densityplot = DensityPlot(language="pt-br")
        >>> densityplot.draw(x_exp, which="all", export=True, file_name="my_data", plot_design="colored", x_label="Comprimento das sépalas ($cm$)")
            O arquivo 'my_data.png' foi exportado!


        .. image:: img/my_data.png
           :alt: Graph showing the dot plot
           :align: center



        """

        ### Checking the input parameters ###

        ## x_exp ##
        checkers._check_is_numpy_1_D(x_exp, param_name="x_exp", language=self.language)

        ### quering ###
        func_name = "draw_density_function"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, self.language, func_name)


        ## bw_method ##
        if bw_method is None:
            bw_method = "scott"
        else:
            checkers._check_is_str(bw_method, "bw_method", self.language)
            if bw_method not in ["scott", "silverman"]:
                try:
                    error = messages[2][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(
                        f"{messages[3][0][0]} 'bw_method' {messages[3][2][0]} 'scott' {messages[3][4][0]} 'silverman' {messages[3][6][0]} '{bw_method}'",
                    )
                    raise

        ## which ##
        if which is None:
            which = "None" # importante, pois None não é subscritable
        else:
            checkers._check_is_str(which, "which", self.language)
            which = helpers._check_which_density_gaussian_kernal_plot(which, self.language)


        ## x_label ##
        x_label = self._get_default_x_label(x_label)

        if y_label is None:
            y_label = messages[5][0][0]
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
            helpers._check_forbidden_character(file_name, "file_name", self.language)

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
        if plot_design == 'gray':
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
            helpers._check_plot_design(plot_design, "plot_design", plot_design_default, plot_design_example, self.language)

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
        default_locale = helpers._change_locale(self.language, decimal_separator, local)

        ### plotando o gráfico ##
        if ax is None:
            fig, axes = plt.subplots(figsize=(width,height))

            ## adding the predicted values ##
            axes.plot(kde_x, kde_y,
                color=plot_design["kde"][0],
                ls = plot_design["kde"][1],
                lw=plot_design["kde"][2],
                label=messages[4][0][0]
            )
            ## adding background color ##
            axes.fill_between(kde_x, kde_y, color=plot_design["Area"][0])
            ## adding measures of central tendency ##
            central_tendency = {}
            if which[0] == "all":
                axes.vlines(mean, 0, kde(mean),
                            color=plot_design["Mean"][0],
                            label=messages[4][1][0],
                            ls=plot_design["Mean"][1],
                            lw=plot_design["Mean"][2]
                        )
                central_tendency["mean"] = [mean, kde(mean)[0]]
                axes.vlines(median, 0, kde(median),
                            color=plot_design["Median"][0],
                            label=messages[4][2][0],
                            ls=plot_design["Median"][1],
                            lw=plot_design["Median"][2]
                        )
                central_tendency["median"] = [median, kde(median)[0]]
                # adding mode #
                if None in modas[0]:
                    general._display_warn(
                        aviso = messages[6][0][0],
                        texto = messages[7][0][0],
                    )
                else:
                    if len(modas) > 1:
                        general._display_warn(
                            aviso = messages[6][0][0],
                            texto = messages[8][0][0],
                        )
                    moda_aux = []
                    for i in range(len(modas)):
                        moda_aux.append([modas[i][0], kde(modas[i][0])[0]])

                        if i != len(modas)-1:
                            axes.vlines(modas[i][0], 0, kde(modas[i][0]),
                            color=plot_design["Mode"][0],
                            ls=plot_design["Mode"][1],
                            lw=plot_design["Mode"][2])
                        else:
                            axes.vlines(modas[i][0], 0, kde(modas[i][0]),
                            color=plot_design["Mode"][0],
                            label=messages[4][3][0],
                            ls=plot_design["Mode"][1],
                            lw=plot_design["Mode"][2])

                    central_tendency["mode"] = moda_aux
            else:
                if "mean" in which:
                    axes.vlines(mean, 0, kde(mean),
                            color=plot_design["Mean"][0],
                            label=messages[4][1][0],
                            ls=plot_design["Mean"][1],
                            lw=plot_design["Mean"][2])
                    central_tendency["mean"] = [mean, kde(mean)[0]]
                if "median" in which:
                    axes.vlines(median, 0, kde(median),
                            color=plot_design["Median"][0],
                            label=messages[4][2][0],
                            ls=plot_design["Median"][1],
                            lw=plot_design["Median"][2])
                    central_tendency["median"] = [median, kde(median)[0]]
                if "mode" in which:
                    if None in modas[0]:
                        general._display_warn(
                            aviso = messages[6][0][0],
                            texto = messages[7][0][0],
                        )
                    else:
                        if len(modas) > 1:
                            general._display_warn(
                                aviso = messages[6][0][0],
                                texto = messages[8][0][0],
                            )
                        moda_aux = []
                        for i in range(len(modas)):
                            moda_aux.append([modas[i][0], kde(modas[i][0])[0]])
                            if i != len(modas)-1:
                                axes.vlines(modas[i][0], 0, kde(modas[i][0]),
                                        color=plot_design["Mode"][0],
                                        ls=plot_design["Mode"][1],
                                        lw=plot_design["Mode"][2])
                            else:
                                axes.vlines(modas[i][0], 0, kde(modas[i][0]),
                                        color=plot_design["Mode"][0],
                                        label=messages[4][3][0],
                                        ls=plot_design["Mode"][1],
                                        lw=plot_design["Mode"][2])
                        central_tendency["mode"] = moda_aux

            # legend #
            if legend:
                axes.legend()

            # x label #
            axes.set_xlabel(x_label)

            # y label #
            axes.set_ylabel(y_label)
            axes.set_ylim(bottom=0, top=None) # limiting to start at y = 0

            # leaving the graph "tight" #
            if tight:
                tight = 'tight'
                fig.tight_layout()
            else:
                tight = None

            # exporting the plot #
            if export:
                plt.savefig(file_name, dpi=dpi, transparent=transparent, bbox_inches=tight)
                general._display_one_line_success(f"{messages[1][0][0]} '{file_name}' {messages[1][2][0]}")

            plt.show()
        else:
            checkers._check_is_subplots(ax, "ax", self.language)
            axes = ax
            axes.plot(kde_x, kde_y)
            ## adding background color ##
            axes.fill_between(kde_x, kde_y)
            ## adding measures of central tendency ##
            central_tendency = {}
            if which[0] == "all":
                axes.vlines(mean, 0, kde(mean),)
                central_tendency["mean"] = [mean, kde(mean)[0]]
                axes.vlines(median, 0, kde(median))
                central_tendency["median"] = [median, kde(median)[0]]
                # adding mode #
                if None in modas[0]:
                    general._display_warn(
                        aviso = messages[6][0][0],
                        texto = messages[7][0][0],
                    )
                else:
                    if len(modas) > 1:
                        general._display_warn(
                            aviso = messages[6][0][0],
                            texto = messages[8][0][0],
                        )
                    moda_aux = []
                    for i in range(len(modas)):
                        moda_aux.append([modas[i][0], kde(modas[i][0])[0]])

                        if i != len(modas)-1:
                            axes.vlines(modas[i][0], 0, kde(modas[i][0]))
                        else:
                            axes.vlines(modas[i][0], 0, kde(modas[i][0]))

                    central_tendency["mode"] = moda_aux
            else:
                if "mean" in which:
                    axes.vlines(mean, 0, kde(mean))
                    central_tendency["mean"] = [mean, kde(mean)[0]]
                if "median" in which:
                    axes.vlines(median, 0, kde(median))
                    central_tendency["median"] = [median, kde(median)[0]]
                if "mode" in which:
                    if None in modas[0]:
                        general._display_warn(
                            aviso = messages[6][0][0],
                            texto = messages[7][0][0],
                        )
                    else:
                        if len(modas) > 1:
                            general._display_warn(
                                aviso = messages[6][0][0],
                                texto = messages[8][0][0],
                            )
                        moda_aux = []
                        for i in range(len(modas)):
                            moda_aux.append([modas[i][0], kde(modas[i][0])[0]])
                            if i != len(modas)-1:
                                axes.vlines(modas[i][0], 0, kde(modas[i][0]))
                            else:
                                axes.vlines(modas[i][0], 0, kde(modas[i][0]))
                        central_tendency["mode"] = moda_aux



        helpers._change_locale_back_to_default(default_locale)
        return kde_x, kde_y, central_tendency, axes




























#
