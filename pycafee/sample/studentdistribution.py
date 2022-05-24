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
from collections import namedtuple


###### Third part ######
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


###### Home made ######
from pycafee.database_management import management
from pycafee.functions import functions
from pycafee.utils.helpers import PlotsManagement, AlphaManagement, NDigitsManagement
from pycafee.utils import checkers
from pycafee.utils import general
from pycafee.utils import helpers
###########################################
################ Functions ################
###########################################


class StudentDistribution(PlotsManagement, AlphaManagement, NDigitsManagement):

    def __init__(self, language=None, alfa=None, n_digits=None, **kwargs):
        super().__init__(language=language, alfa=alfa, n_digits=n_digits,**kwargs)


    # with tests, with databse (but at StudentDistribution), with docstring
    def draw(self, gl, tcalc, alfa=None, ax=None, which=None, interval=None, legend=None, x_label=None, y_label=None, width='default', height='default', export=None, file_name=None, extension=None, dpi=None, tight=None, transparent=None, plot_design='gray', decimal_separator=None, local=None):
        """This function draws a graph with the Student's t distribution (one-sided or two-sided) for a given degree of freedom, combined with the calculated value of the statistic of this test for a sample with an alpha level of significance.

        Parameters
        ----------
        gl : ``int``, higher than 1
            The degree of freedom of the sample
        tcalc : ``float`` or ``int``
            The calculated value of the Student's t-test statistic
        alfa : ``float``
            The level of significance, ``0.0 < alfa < 1.0``.
        ax : ``None`` or ``matplotlib.axes.SubplotBase``, optional
            * If ``ax`` is ``None``, a figure is created with a preset design. The other parameters can be used to edit and export the graph.
            * If ``ax`` is a ``matplotlib.axes.SubplotBase``, the function returns a ``matplotlib.axes.SubplotBase`` with the StudentDistribution axis. In this case, the parameters related to graph export will not influence the generated axis.

        which : ``str``, optional
            The parameter which controls the t distribution to be ploted. The options are:

                - ``None`` or ``"two-side"`` (default): two-side
                - ``"one-side"``: one-side

        interval : ``None`` or ``list``, optional
            The interval

            * If it is ``None``, it tries to find a suitable range to plot the graph.
            * If it is a ``list``, the ``list`` must contain 2 positive numeric elements, where the first element defines the lower limit of the interval, and the second element defines the upper limit of the interval.

        legend : ``bool``, optional
            Whether the legend should be added into the chart (``True``) or not (``False``). The default value is ``None``, which implies ``True``.
        x_label : ``str``, optional
            The label to be displayed on x label. Default is ``None``, which results in ``"Student's t"``.
        y_label : ``str``, optional
            The label to be displayed on y label. Default is ``None``, which results in ``"Probability density"``.
        width : ``"default"``, ``int`` or ``float`` (positive), optional
            The width of the figure. If it is ``"default"``, it uses a pre-defined value. If it is a number, it defines the ``width`` of the chart (in inches).
        height : ``"default"``, ``int`` or ``float`` (positive), optional
            The height of the figure. If it is ``"default"``, it uses a pre-defined value. If it is a number, it defines the ``height`` of the chart (in inches).
        export : ``bool``, optional
            Whether the graph should be exported (``True``) or not (``False``). The default value is ``None``, which implies ``False``.
        file_name : ``str``, optional
            The file name. Default is ``None`` which results in a file named ``"student_distribution"``.
        extension : ``str``, optional
            The file extension without a dot. Default is ``None`` which results in a ``".png"`` file.
        dpi : ``int`` or ``float`` (positive), optional
            The figure pixel density. The default is ``None``, which results in a ``100 dpis`` picture. This parameter must be a number higher than zero.
        tight : ``bool``, optional
            Whether the graph should be tight (``True``) or not (``False``). The default value is ``None``, which implies ``True``.
        transparent : ``bool``, optional
            Whether the background of the graph should be transparent (``True``) or not (``False``). The default value is ``None``, which implies ``False`` (white).
        plot_design : ``str`` or ``dict``, optional
            The plot desing. If ``"gray"``, uses a gray-scale desing (default). If ``"colored"``, uses a colored desing. If ``dict``, it must have four ``keys`` (``"distribution"``, ``"area-rejection"``, ``"area-acceptance"``, ``"tcalc"``), where each one defines the design of each element added to the chart.
        decimal_separator : ``str``, optional
            The decimal separator symbol used in the chart. It can be the dot (``None`` or ``'.'``) or the comma (``','``).
        local : ``str``, optional
            The alias for the desired locale. Only used if ``decimal_separator = ','`` to set the matplolib's default ``locale``. Its only function is to change the decimal separator symbol and should be changed only if the ``"pt_BR"`` option is not available.


        Returns
        -------
        axes : ``matplotlib.axes._subplots.AxesSubplot``
            The axis of the graph.
        output : ``dict``
            A dictionary with the data used to plot the graph.

            * If ``which = "two-side"``
            * If ``which = "one-side"``


        See Also
        --------
        pycafee.normalitycheck.shapirowilk.ShapiroWilk.fit


        Notes
        -----

        The ``plot_design`` parameter must be a dict where the ``values`` for all ``keys`` must be a ``list``. The ``list`` of the key ``"distribution"`` must have:

            * the first element must be a ``str`` with the color name;
            * the second element must be a ``str`` with line style;
            * the third element must be a number (``int`` or ``float``, positive) with the line thickness;

        The ``list`` of the key ``"tcalc"`` must have:

            * the first element must be a ``str`` with the color name;
            * the second element must be a ``str`` with the marker;
            * the third element must be a number (``int`` or ``float``, positive) with size of the marker;

        The ``area-rejection`` and ``area-acceptance`` ``lists`` must have a single element, which is a ``str`` with the name of the color that fills the area between the distribution line and the line ``y = 0``. For example:

        .. code-block:: python

            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['white'],
                "tcalc": ['k', 'o', 50],
            }


        A list of color names can be found at `matplotlib's documentation <https://matplotlib.org/stable/_images/sphx_glr_named_colors_003.png>`_.

        A list of linestyles can be found `here <https://raw.githubusercontent.com/andersonmdcanteli/matplotlib-course/main/auxiliary-scripts/matplotli-all-linestyles/matplotlib_linestyles.png>`_.

        A list of makers can be found `on this link <https://raw.githubusercontent.com/andersonmdcanteli/matplotlib-course/main/auxiliary-scripts/matplotlib-all-markers/matplotlib_markers.png>`_.


        The critical values for the sample are obtained using the scipy percent point function [1]_:

        .. code-block:: python

            stats.t.ppf(1-alfa/2, gl) or stats.t.ppf(alfa/2, gl) # for the two-side distribution
            stats.t.ppf(1-alfa, gl) or stats.t.ppf(alfa, gl) # for the one-side distribution


        The density values are estimated using the scipy probability density function [1]_:

        .. code-block:: python

            stats.t.pdf(x,gl)


        References
        ----------
        .. [1] SCIPY. scipy.stats.t. Available at: `www.scipy.org <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html>`_. Access on: 10 May. 2022.


        Examples
        --------

        >>> from pycafee.sample.studentdistribution import StudentDistribution
        >>> student = StudentDistribution()
        >>> axes, output = student.draw(gl=4,tcalc=3.15, export=True)
            The 'student_distribution.png' file was exported!

        .. image:: img/student_distribution.png
           :alt: Graph showing the student's plot
           :align: center


        >>> from pycafee.sample.studentdistribution import StudentDistribution
        >>> student = StudentDistribution()
        >>> axes, output = student.draw(gl=4,tcalc=-3.15, export=True, plot_design='colored', file_name='my_data')
            The 'my_data.png' file was exported!

            .. image:: img/my_data.png
               :alt: Graph showing the student's plot
               :align: center


        >>> from pycafee.sample.studentdistribution import StudentDistribution
        >>> student = StudentDistribution(language='pt-br')
        >>> axes, output = student.draw(gl=4,tcalc=1.15, which='one-side', export=True, plot_design='colored', file_name='meus_dados')
            O arquivo 'meus_dados.png' foi exportado!


            .. image:: img/meus_dados.png
               :alt: Graph showing the student's plot
               :align: center

        """

        ### Checking the input parameters ###

        ## gl ##
        checkers._check_is_integer(gl, param_name="gl", language=self.language)
        checkers._check_value_is_equal_or_higher_than(gl, 'gl', 1, self.language)

        ## tcalc ##
        checkers._check_is_float_or_int(tcalc, param_name="tcalc", language=self.language)

        ## alfa ##
        if alfa is None:
            alfa = self.alfa
        else:
            checkers._check_is_float(alfa, alfa, self.language)
            checkers._check_data_in_range(alfa, "alfa", 0.0, 1.0, self.language)


        ### quering ###
        func_name = "StudentDistribution"
        fk_id_function = management._query_func_id(func_name)
        messages = management._get_messages(fk_id_function, self.language, func_name)


        ## which ##
        if which is None:
            which = "two-side"
        else:
            checkers._check_is_str(which, "which", self.language)
            which_keys = ["two-side", "one-side"]
            which = _check_which_param(which, self.language)

        ## y_label ##
        if y_label is None:
            y_label = messages[3][0][0]
        else:
            y_label = self._get_default_y_label(y_label)

        ## x_label ##
        if x_label is None:
            x_label = messages[4][0][0]
        else:
            x_label = self._get_default_x_label(x_label)


        ## width ##
        width = self._get_default_width(width)

        ## height ##
        height = self._get_default_height(height)

        ## export ##
        export = self._get_default_export(export)

        ## file_name ##
        if file_name is None:
            file_name = "student_distribution"
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
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['white'],
                "tcalc": ['k', 'o', 50],
            }
        elif plot_design == "colored":
            plot_design = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gray'],
                "area-acceptance": ['snow'],
                "tcalc": ['red', 'o', 80],
            }
        else:
            plot_design_default = {
                "distribution": ['k', '-', 1.5],
                "area-rejection": ['gainsboro'],
                "area-acceptance": ['white'],
                "tcalc": ['k', 'o', 50],
            }
            plot_design_example = {
                "distribution": "['color name', 'line style', number]",
                "area-rejection": "['color name']",
                "area-acceptance": "['color name']",
                "tcalc": "['color name', 'marker type', number]",
            }
            helpers._check_plot_design(plot_design, "plot_design", plot_design_default, plot_design_example, self.language)

        ## Legend ##
        legend = self._get_default_legend(legend)

        ## decimal_separator ##
        decimal_separator = self._get_default_decimal_separator(decimal_separator)

        ## local ##
        local = self._get_default_local(local)


        ### cheking the decimal_separator ###
        default_locale = helpers._change_locale(self.language, decimal_separator, local)


        ### cheking the interval ###

        if interval is None: # if None, try to find a good interval based on tcalc and Studen's t
            if which == "two-side":
                t_student = stats.t.ppf(1-alfa/2, gl)
                if tcalc > t_student:
                    interval = [-1.2*tcalc, 1.2*tcalc]
                else:
                    interval = [-1.8*t_student, 1.8*t_student]
            else:
                # if tcalc is poisitive, get the positive t value; else, get the negative tvalue
                if tcalc > 0:
                    t_student = stats.t.ppf(1-alfa, gl)
                    if tcalc > t_student:
                        interval = [-1.2*tcalc, 1.2*tcalc]
                    else:
                        interval = [-1.8*t_student, 1.8*t_student]
                else:
                    t_student = stats.t.ppf(alfa, gl)
                    if np.abs(tcalc) > np.abs(t_student):
                        interval = [1.2*tcalc, -1.2*tcalc]
                    else:
                        interval = [1.8*t_student, -1.8*t_student]


        else: # if not None, checks if is a list
            checkers._check_is_list(interval, "interval", self.language)
            # check if the list has correct size
            checkers._check_list_length(interval, 2, "interval", self.language)
            # then check if each element is float or int
            for i in range(len(interval)):
                checkers._check_is_float_or_int(interval[i], f"interval[{i}]", self.language)

            # Raise error if the lower is higher than the higher value
            if interval[0] > interval[1]:
                try:
                    error = messages[5][0][0]
                    raise ValueError(error)
                except ValueError:
                    msg = f"{messages[6][0][0]} 'interval' {messages[6][2][0]}: interval[0] = ({interval[0]}) > interval[1] = ({interval[1]})"
                    general._display_one_line_attention(msg)
                    raise
            # Raise error if the values are equal
            elif interval[0] == interval[1]:
                try:
                    error = messages[5][0][0]
                    raise ValueError(error)
                except ValueError:
                    msg = f"{messages[7][0][0]} 'interval' {messages[7][2][0]}: interval[0] = ({interval[0]}) == interval[1] = ({interval[1]})"
                    general._display_one_line_attention(msg)
                    raise
            # Warn user that the values are not oposit
            elif np.abs(interval[0]) != np.abs(interval[1]):
                general._display_warn(
                    messages[8][0][0],
                    messages[9][0][0],
                )
            else:
                pass

        ### drawing the plot ###
        if which == "two-side":
            # gerando dados de x dentro do intervalo estabelacido
            x_pred = np.arange(interval[0],interval[1],0.01)
            # gerando dados de y para cada x_pred
            y_pred = stats.t.pdf(x_pred,gl)
            output = {"curve": [x_pred, y_pred]}
            # adicionando região de rejeição à esquerda
            t_student_esquerda = stats.t.ppf(alfa/2, gl)
            y_t_student_esquerda = stats.t.pdf(t_student_esquerda, gl)
            x_esquerda = np.arange(interval[0],t_student_esquerda, 0.01)
            y_esquerda = stats.t.pdf(x_esquerda, gl)
            # adicionando o tcalculado
            y_tcalc = stats.t.pdf(tcalc, gl)
            tcalc = helpers._truncate(tcalc, self.language, decs=self.n_digits)
            output["tcalc"] = [tcalc, y_tcalc]
            output["t_left"] = [t_student_esquerda, y_t_student_esquerda]
            # adicionando região de rejeição à direita
            t_student_direita = stats.t.ppf(1 - alfa/2, gl)
            y_t_student_direita = stats.t.pdf(t_student_direita, gl)
            x_direita = np.arange(t_student_direita, interval[1],0.01)
            y_direita = stats.t.pdf(x_direita, gl)
            output["t_right"] = [t_student_direita, y_t_student_direita]


            if ax is None:
                fig, axes = plt.subplots(figsize=(width,height))
                # adicionando a distribuição t
                axes.plot(x_pred, y_pred,
                            label=r'$gl=%i$' % (gl),
                            c=plot_design['distribution'][0],
                            ls=plot_design['distribution'][1],
                            lw=plot_design['distribution'][2],
                        )

                axes.scatter(tcalc, y_tcalc,  label = r'$t_{calc} = $' + str(tcalc), zorder=10,
                                    color=plot_design['tcalc'][0],
                                    marker=plot_design['tcalc'][1],
                                    s=plot_design['tcalc'][2],
                                    )

                axes.fill_between(x_esquerda, y_esquerda, interpolate=True, zorder=-1,
                                    label=messages[10][0][0],
                                    color=plot_design['area-rejection'][0],
                                    )

                axes.fill_between(x_direita, y_direita, interpolate=True, zorder=-1,
                                    color=plot_design['area-rejection'][0]
                                    )


                if plot_design['area-acceptance'][0] != "white":
                    # dicionando área de aceitação
                    x_centro = np.arange(t_student_esquerda, t_student_direita, 0.01)
                    y_centro = stats.t.pdf(x_centro, gl)
                    axes.fill_between(x_centro, y_centro, interpolate=True, zorder=-1,
                                        label=messages[11][0][0],
                                        color=plot_design['area-acceptance'][0],
                                        )
                # adicionando reta em y = 0
                axes.hlines(0, xmin=interval[0], xmax=interval[1], color='k')

                # legend #
                if legend:
                    axes.legend()

                # x label #
                axes.set_xlabel(x_label)
                # y label #
                axes.set_ylabel(y_label)
                # axes.set_ylim(bottom=0, top=None) # limiting to start at y = 0

                # leaving the graph "tight" #
                if tight:
                    tight = 'tight'
                    fig.tight_layout()
                else:
                    tight = None

                # exporting the plot #
                if export:
                    plt.savefig(file_name, dpi=dpi, transparent=transparent, bbox_inches=tight)
                    fk_id_function = management._query_func_id('draw_density_function')
                    messages = management._get_messages(fk_id_function, self.language, 'draw_density_function')
                    general._display_one_line_success(f"{messages[1][0][0]} '{file_name}' {messages[1][2][0]}")

                plt.show()
            else:
                checkers._check_is_subplots(ax, "ax", self.language)
                axes = ax
                # adicionando a distribuição t
                axes.plot(x_pred, y_pred,
                            label=r'$gl=%i$' % (gl),
                            c=plot_design['distribution'][0],
                            ls=plot_design['distribution'][1],
                            lw=plot_design['distribution'][2],
                        )

                axes.scatter(tcalc, y_tcalc,  label = r'$t_{calc} = $' + str(tcalc), zorder=10,
                                    color=plot_design['tcalc'][0],
                                    marker=plot_design['tcalc'][1],
                                    s=plot_design['tcalc'][2],
                                    )

                axes.fill_between(x_esquerda, y_esquerda, interpolate=True, zorder=-1,
                                    label=messages[10][0][0],
                                    color=plot_design['area-rejection'][0],
                                    )

                axes.fill_between(x_direita, y_direita, interpolate=True, zorder=-1,
                                    color=plot_design['area-rejection'][0]
                                    )

                if plot_design['area-acceptance'][0] != "white":
                    # dicionando área de aceitação
                    x_centro = np.arange(t_student_esquerda, t_student_direita, 0.01)
                    y_centro = stats.t.pdf(x_centro, gl)
                    axes.fill_between(x_centro, y_centro, interpolate=True, zorder=-1,
                                        label=messages[11][0][0],
                                        color=plot_design['area-acceptance'][0],
                                        )
                # adicionando reta em y = 0
                axes.hlines(0, xmin=interval[0], xmax=interval[1], color='k')

                # legend #
                if legend:
                    axes.legend()
                # x label #
                axes.set_xlabel(x_label)
                # y label #
                axes.set_ylabel(y_label)
                # axes.set_ylim(bottom=0, top=None) # limiting to start at y = 0


        else:
            # gerando dados de x dentro do intervalo estabelacido
            x_pred = np.arange(interval[0],interval[1],0.01)
            # gerando dados de y para cada x_pred
            y_pred = stats.t.pdf(x_pred,gl)
            output = {"curve": [x_pred, y_pred]}

            # adicionando o tcalculado
            y_tcalc = stats.t.pdf(tcalc, gl)
            tcalc = helpers._truncate(tcalc, self.language, decs=self.n_digits)
            output["tcalc"] = [tcalc, y_tcalc]


            if tcalc < 0:
                # adicionando região de rejeição à esquerda
                t_student = stats.t.ppf(alfa, gl)
                y_t_student = stats.t.pdf(t_student, gl)
                x = np.arange(interval[0],t_student, 0.01)
                y = stats.t.pdf(x, gl)
                output["t_student"] = [t_student, y_t_student]
            else:
                # adicionando região de rejeição à direita
                t_student = stats.t.ppf(1 - alfa, gl)
                y_t_student = stats.t.pdf(t_student, gl)
                x = np.arange(t_student, interval[1],0.01)
                y = stats.t.pdf(x, gl)
                output["t_student"] = [t_student, y_t_student]

            if ax is None:
                fig, axes = plt.subplots(figsize=(width,height))
                # adicionando a distribuição t
                axes.plot(x_pred, y_pred,
                            label=r'$gl=%i$' % (gl),
                            c=plot_design['distribution'][0],
                            ls=plot_design['distribution'][1],
                            lw=plot_design['distribution'][2],
                        )

                axes.scatter(tcalc, y_tcalc,  label = r'$t_{calc} = $' + str(tcalc), zorder=10,
                                    color=plot_design['tcalc'][0],
                                    marker=plot_design['tcalc'][1],
                                    s=plot_design['tcalc'][2],
                                    )

                axes.fill_between(x, y, interpolate=True, zorder=-1,
                                    label=messages[10][0][0],
                                    color=plot_design['area-rejection'][0],
                                    )


                if plot_design['area-acceptance'][0] != "white":
                    # dicionando área de aceitação
                    if t_student > 0:
                        x_centro = np.arange(x_pred[0], t_student, 0.01)
                    else:
                        x_centro = np.arange(t_student, x_pred[-1], 0.01)
                    y_centro = stats.t.pdf(x_centro, gl)
                    axes.fill_between(x_centro, y_centro, interpolate=True, zorder=-1,
                                        label=messages[11][0][0],
                                        color=plot_design['area-acceptance'][0],
                                        )
                # adicionando reta em y = 0
                axes.hlines(0, xmin=interval[0], xmax=interval[1], color='k')

                # legend #
                if legend:
                    axes.legend()

                # x label #
                axes.set_xlabel(x_label)
                # y label #
                axes.set_ylabel(y_label)
                # axes.set_ylim(bottom=0, top=None) # limiting to start at y = 0

                # leaving the graph "tight" #
                if tight:
                    tight = 'tight'
                    fig.tight_layout()
                else:
                    tight = None

                # exporting the plot #
                if export:
                    plt.savefig(file_name, dpi=dpi, transparent=transparent, bbox_inches=tight)
                    fk_id_function = management._query_func_id('draw_density_function')
                    messages = management._get_messages(fk_id_function, self.language, 'draw_density_function')
                    general._display_one_line_success(f"{messages[1][0][0]} '{file_name}' {messages[1][2][0]}")

                plt.show()
            else:
                checkers._check_is_subplots(ax, "ax", self.language)
                axes = ax
                # adicionando a distribuição t
                axes.plot(x_pred, y_pred,
                            label=r'$gl=%i$' % (gl),
                            c=plot_design['distribution'][0],
                            ls=plot_design['distribution'][1],
                            lw=plot_design['distribution'][2],
                        )

                axes.scatter(tcalc, y_tcalc,  label = r'$t_{calc} = $' + str(tcalc), zorder=10,
                                    color=plot_design['tcalc'][0],
                                    marker=plot_design['tcalc'][1],
                                    s=plot_design['tcalc'][2],
                                    )

                axes.fill_between(x, y, interpolate=True, zorder=-1,
                                    label=messages[10][0][0],
                                    color=plot_design['area-rejection'][0],
                                    )


                if plot_design['area-acceptance'][0] != "white":
                    # dicionando área de aceitação
                    x_centro = np.arange(t_student, t_student, 0.01)
                    y_centro = stats.t.pdf(x_centro, gl)
                    axes.fill_between(x_centro, y_centro, interpolate=True, zorder=-1,
                                        label=messages[11][0][0],
                                        color=plot_design['area-acceptance'][0],
                                        )
                # adicionando reta em y = 0
                axes.hlines(0, xmin=interval[0], xmax=interval[1], color='k')

                # legend #
                if legend:
                    axes.legend()
                # x label #
                axes.set_xlabel(x_label)
                # y label #
                axes.set_ylabel(y_label)
                # axes.set_ylim(bottom=0, top=None) # limiting to start at y = 0


        helpers._change_locale_back_to_default(default_locale)

        return axes, output

    # with tests, with databse (but at StudentDistribution), with docstring
    def get_critical_value(self, gl, alfa=None, which=None):
        """This function returns the critical value of the two-side or one-side Student's t distribution. This is just a wrapper around ``stats.t.ppf`` [1]_.


        Parameters
        ----------
        gl : ``int``, higher than ``1``
            The degree of freedom of the sample
        alfa : ``float``
            The level of significance, ``0.0 < alfa < 1.0``.
        which : ``str``, optional
            The parameter which controls the t distribution to be ploted. The options are:

                - ``None`` or ``"two-side"`` (default): two-side
                - ``"one-side"``: one-side

        Returns
        -------
        result : ``tuple``
            The critical values for a par ``gl`` and ``alpha``, where

            * The first element is the higher critical value;
            * The second element is the lower critical value;
            * The third element is the corresponding alpha value;
            * The fourth element is the distribution used from the which parameter;

        t_student : ``list``
            A ``list`` of two elements containing the lower critical value in the first element and the higher critical value in the second element, without truncating their values.



        See Also
        --------
        draw


        Notes
        -----

        The critical values for the sample are obtained using the scipy percent point function [1]_:

        .. code-block:: python

            stats.t.ppf(1-alfa/2, gl) or stats.t.ppf(alfa/2, gl) # for the two-side distribution
            stats.t.ppf(1-alfa, gl) or stats.t.ppf(alfa, gl) # for the one-side distribution



        References
        ----------
        .. [1] SCIPY. scipy.stats.t. Available at: `www.scipy.org <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html>`_. Access on: 10 May. 2022.


        Examples
        --------

        **Getting the critical values for 4 degrees of freedom at 95% of confidence level (two-side)**

        >>> from pycafee.sample.studentdistribution import StudentDistribution
        >>> student = StudentDistribution()
        >>> result, t_student = student.get_critical_value(4)
        >>> print(result)
        Student(Higher=2.776, Lower=-2.776, Alpha=0.05, Distribution='two-side')
        >>> print(t_student)
        [-2.7764451051977996, 2.7764451051977987]


        **Getting the critical values for 5 degrees of freedom at 90% of confidence level (two-side)**

        >>> from pycafee.sample.studentdistribution import StudentDistribution
        >>> student = StudentDistribution()
        >>> result, t_student = student.get_critical_value(5, alfa=0.1)
        >>> print(result)
        Student(Higher=2.015, Lower=-2.015, Alpha=0.1, Distribution='two-side')
        >>> print(t_student)
        [-2.0150483726691575, 2.015048372669157]



        **Getting the critical values for 4 degrees of freedom at 95% of confidence level (one-side)**

        >>> from pycafee.sample.studentdistribution import StudentDistribution
        >>> student = StudentDistribution()
        >>> result, t_student = student.get_critical_value(4, which="one-side")
        >>> print(result)
        Student(Higher=2.131, Lower=-2.131, Alpha=0.05, Distribution='one-side')
        >>> print(t_student)
        [-2.1318467813362907, 2.13184678133629]



        **Getting the critical values for 5 degrees of freedom at 90% of confidence level (one-side)**

        >>> from pycafee.sample.studentdistribution import StudentDistribution
        >>> student = StudentDistribution()
        >>> result, t_student = student.get_critical_value(5, which="one-side", alfa=0.1)
        >>> print(result)
        Student(Higher=1.475, Lower=-1.475, Alpha=0.1, Distribution='one-side')
        >>> print(t_student)
        [-1.475884048782027, 1.4758840487820273]




        """

        ### Checking the input parameters ###

        ## gl ##
        checkers._check_is_integer(gl, param_name="gl", language=self.language)
        checkers._check_value_is_equal_or_higher_than(gl, 'gl', 1, self.language)


        ## alfa ##
        if alfa is None:
            alfa = self.alfa
        else:
            checkers._check_is_float(alfa, alfa, self.language)
            checkers._check_data_in_range(alfa, "alfa", 0.0, 1.0, self.language)

        ## which ##
        if which is None:
            which = "two-side"
        else:
            checkers._check_is_str(which, "which", self.language)
            which_keys = ["two-side", "one-side"]
            which = _check_which_param(which, self.language)

        if which == "two-side":
            t_student = [stats.t.ppf(alfa/2, gl), stats.t.ppf(1 - alfa/2, gl)]
        else:
            t_student = [stats.t.ppf(alfa, gl), stats.t.ppf(1 - alfa, gl)]

        fk_id_function = management._query_func_id("StudentDistribution")
        messages = management._get_messages(fk_id_function, self.language)

        result = namedtuple(messages[13][0][0], (messages[13][1][0], messages[13][2][0], messages[13][3][0], messages[13][4][0]))

        return result(helpers._truncate(t_student[1], self.language, decs=self.n_digits), helpers._truncate(t_student[0], self.language, decs=self.n_digits), alfa, which), t_student


    def __str__(self):
        fk_id_function = management._query_func_id("StudentDistribution")
        messages = management._get_messages(fk_id_function, self.language)
        return messages[12][0][0]

    def __repr__(self):
        fk_id_function = management._query_func_id("StudentDistribution")
        messages = management._get_messages(fk_id_function, self.language)
        return messages[12][0][0]






# with tests, with docstring, with database but at StudentDistribution
def _check_which_param(which, language):
    """This function checks whether the parameter which is ``"two-side"`` or ``"one-side"``

    Parameters
    ----------

    which : ``str``
        The ``which`` parameter for Student's t distribution
    language : ``str``
        The language code

    Notes
    -----
    The parameter ``language`` isn't checked if it is a ``str``.

    Returns
    -------

        * If ``which`` is ``"two-side"`` or ``"one-side"``, the function returns ``"two-side"`` or ``"one-side"``
        * Else, the function raises ``ValueError``.


    """

    ### quering ###
    func_name = "StudentDistribution"
    fk_id_function = management._query_func_id(func_name)
    messages = management._get_messages(fk_id_function, language, func_name)
    ## which ##
    if which is None:
        which = "two-side"
    else:
        checkers._check_is_str(which, "which", language)
        which_keys = ["two-side", "one-side"]
        if which not in which_keys:
            try:
                error = messages[1][0][0]
                raise ValueError(error)
            except ValueError:
                msg = f"{messages[2][0][0]} 'which' {messages[2][2][0]} 'two-side' {messages[2][4][0]} 'one-side' {messages[2][6][0]} '{which}'"
                general._display_one_line_attention(msg)
                raise
    return which








#
