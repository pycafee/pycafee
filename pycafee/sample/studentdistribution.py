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
from scipy.stats import ttest_1samp as one_sample_comparison
from scipy.stats import t as t_student

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
    def draw(self, gl, tcalc, alfa=None, ax=None, which=None, interval=None, legend=None, x_label=None, y_label=None, width='default', height='default', export=None, file_name=None, extension=None, dpi=None, tight=None, transparent=None, plot_design='gray', decimal_separator=None):
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
            checkers._check_is_float(alfa, "alfa", self.language)
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
        # file_name = helpers._check_conflicting_filename(file_name, extension, self.language)

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
        checkers._check_is_str(decimal_separator, "decimal_separator", self.language)
        helpers._check_decimal_separator(decimal_separator, self.language)


        ## local ##
        # local = self._get_default_local(local)


        ### cheking the decimal_separator ###
        # default_locale = helpers._change_locale(self.language, decimal_separator, local)


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

            if ax is None:
                axes = helpers._change_decimal_separator_x_axis(fig, axes, decimal_separator)
                axes = helpers._change_decimal_separator_y_axis(fig, axes, decimal_separator)
                # leaving the graph "tight" #
                if tight:
                    tight = 'tight'
                    fig.tight_layout()
                else:
                    tight = None

                # exporting the plot #
                if export:
                    exits, file_name = helpers._check_conflicting_filename(file_name, extension, self.language)
                    plt.savefig(file_name, dpi=dpi, transparent=transparent, bbox_inches=tight)
                    fk_id_function = management._query_func_id('draw_density_function')
                    messages = management._get_messages(fk_id_function, self.language, 'draw_density_function')
                    general._display_one_line_success(f"{messages[1][0][0]} '{file_name}' {messages[1][2][0]}")

                plt.show()

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
            if ax is None:
                axes = helpers._change_decimal_separator_x_axis(fig, axes, decimal_separator)
                axes = helpers._change_decimal_separator_y_axis(fig, axes, decimal_separator)
                # leaving the graph "tight" #
                if tight:
                    tight = 'tight'
                    fig.tight_layout()
                else:
                    tight = None

                # exporting the plot #
                if export:
                    exits, file_name = helpers._check_conflicting_filename(file_name, extension, self.language)
                    plt.savefig(file_name, dpi=dpi, transparent=transparent, bbox_inches=tight)
                    fk_id_function = management._query_func_id('draw_density_function')
                    messages = management._get_messages(fk_id_function, self.language, 'draw_density_function')
                    general._display_one_line_success(f"{messages[1][0][0]} '{file_name}' {messages[1][2][0]}")

            plt.show()


        # helpers._change_locale_back_to_default(default_locale)

        return axes, output

    # with tests, with databse (but at StudentDistribution), with docstring
    def _get_p_value(self, t_calc, gl, which=None):
        """
        Returns the p-value of Student's t-distribution based on test statistic, degree of freedom, and type of distribution. This function is a wrapper around the `scipy.stats.t.cdf()` function [1]_, which returns the probability of the t distribution.

        Parameters
        ----------
        tcalc : ``float`` or ``int``
            The t statistic
        gl : ``int``, higher than ``1``
            The degree of freedom of the sample
        which : ``str``, optional
            The type of the distribution.

            * If ``which = "two-side"`` (or ``None``, e.g, the default), the p-value is calculated with the two-sided Student's distribution.
            * If ``which = "one-side"``, the p-value is calculated with the one-sided Student's distribution.

        Returns
        -------
        result : ``tuple``, with

            p_value : ``float``
                The estimated probability for the test statistic
            which : ``str``
                The type of distribution that was used to obtain the ``p_value``

        See Also
        --------
        get_critical_value


        Notes
        -----
        If ``which = "one-side"``, the ``p_value`` is estimated using the ``scipy.stats.t.cdf()`` function as follows:

        .. code:: python

           p_value = (1 - scipy.stats.t.cdf(np.abs(t_calc), gl))


        If ``which = "two-side"``, the ``p_value`` is estimated using the ``scipy.stats.t.cdf()`` function as follows:

        .. code:: python

           p_value = 2*(1 - scipy.stats.t.cdf(np.abs(t_calc), gl))



        References
        ----------
        .. [1] SCIPY. scipy.stats.t. Available at: `www.scipy.org <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html>`_. Access on: 10 May. 2022.


        Examples
        --------

        **Getting p-value for two side distribution**

        >>> from pycafee.sample import StudentDistribution
        >>> teste = StudentDistribution()
        >>> result = teste._get_p_value(1.19, 5)
        >>> print(result)
        Student(p_value=0.2874641347924176, which='two-side')


        **Getting p-value for one side distribution**

        >>> from pycafee.sample import StudentDistribution
        >>> teste = StudentDistribution()
        >>> result = teste._get_p_value(1.19, 5, which="one-side")
        >>> print(result)
        Student(p_value=0.1437320673962088, which='one-side')


        """

        ## tcalc ##
        checkers._check_is_float_or_int(t_calc, "t_calc", self.language)

        ## gl ##
        checkers._check_is_integer(gl, param_name="gl", language=self.language)
        checkers._check_value_is_equal_or_higher_than(gl, 'gl', 1, self.language)

        ## which ##
        if which is None:
            which = "two-side"
        else:
            checkers._check_is_str(which, "which", self.language)
            which_keys = ["two-side", "one-side"]
            which = _check_which_param(which, self.language)


        # ------ getting from scipy ------ #
        if which == "two-side":
            p_value = 2*(1 - t_student.cdf(np.abs(t_calc), gl))
        else:
            p_value = (1 - t_student.cdf(np.abs(t_calc), gl))

        fk_id_function = management._query_func_id("StudentDistribution")
        messages = management._get_messages(fk_id_function, self.language, "StudentDistribution")

        result = namedtuple(messages[13][0][0], (messages[21][3][0], "which"))

        return result(p_value, which)



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
        >>> result = student.get_critical_value(4)
        >>> print(result)
        Student(Upper=2.7764451051977996, Lower=-2.7764451051977996, Alpha=0.05, Distribution='two-side')


        **Getting the critical values for 5 degrees of freedom at 90% of confidence level (two-side)**

        >>> from pycafee.sample.studentdistribution import StudentDistribution
        >>> student = StudentDistribution()
        >>> result = student.get_critical_value(5, alfa=0.1)
        >>> print(result)
        Student(Upper=2.0150483726691575, Lower=-2.0150483726691575, Alpha=0.1, Distribution='two-side')


        **Getting the critical values for 4 degrees of freedom at 95% of confidence level (one-side)**

        >>> from pycafee.sample.studentdistribution import StudentDistribution
        >>> student = StudentDistribution()
        >>> result = student.get_critical_value(4, which="one-side")
        Student(Upper=2.13184678133629, Lower=-2.13184678133629, Alpha=0.05, Distribution='one-side')


        **Getting the critical values for 5 degrees of freedom at 90% of confidence level (one-side)**

        >>> from pycafee.sample.studentdistribution import StudentDistribution
        >>> student = StudentDistribution()
        >>> result = student.get_critical_value(5, which="one-side", alfa=0.1)
        >>> print(result)
        Student(Upper=1.4758840487820273, Lower=-1.475884048782027, Alpha=0.1, Distribution='one-side')

        """

        ### Checking the input parameters ###

        ## gl ##
        checkers._check_is_integer(gl, param_name="gl", language=self.language)
        checkers._check_value_is_equal_or_higher_than(gl, 'gl', 1, self.language)


        ## alfa ##
        if alfa is None:
            alfa = self.alfa
        else:
            checkers._check_is_float(alfa, "alfa", self.language)
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
        messages = management._get_messages(fk_id_function, self.language, "StudentDistribution")

        result = namedtuple(messages[13][0][0], (messages[13][1][0], messages[13][2][0], messages[13][3][0], messages[13][4][0]))

        return result(t_student[1], t_student[0], alfa, which)

    # with tests, with databse (but at StudentDistribution), with docstring
    def compare_with_constant(self, x_exp=None, params=None, value=None, alfa=None, which=None, comparison=None, details=None):
        """This function checks if a sample is equal to a constant through Student's t test.

        Parameters
        ----------
        x_exp : ``numpy array``, optional
            One dimension :doc:`numpy array <numpy:reference/generated/numpy.array>` with at least 2 sample data.
        value : ``int`` or ``float``, optional
            The value that will be used as a reference. This value is treated as a constant. Default is ``0``.
        params : ``list``, optional
            A ``list`` with three elements, where each one represents a parameter of the sample

             * First element corresponds to the sample mean;
             * Second element corresponds to the standard deviation of the sample;
             * Third element corresponds to the sample size;

        alfa : ``float``, optional
            The level of significance (``ɑ``). Default is ``None`` which results in ``0.05`` (``ɑ = 5%``).
        which : ``str``, optional
            The kind of comparison to perform.

            * If ``which = "two-side"`` (or ``None``, e.g, the default), the comparison test is performed with the two-sided Student's distribution.
            * If ``which = "one-side"``, the comparison test is performed with the one-sided Student's distribution.

        comparison : ``str``, optional
            This parameter determines how to perform the comparison test between the means.

            * If ``comparison = "critical"`` (or ``None``, e.g, the default), the comparison test is made between the critical value (with ``ɑ`` significance level) and the calculated value of the test statistic.
            * If ``"p-value"``, the comparison test is performed between the p-value and the adopted significance level (``ɑ``).

            **Both results should lead to the same conclusion.**

        details : ``str``, optional
            The ``details`` parameter determines the amount of information presented about the hypothesis test.

            * If ``details = "short"`` (or ``None``, e.g., the default), a simplified version of the test result is returned.
            * If ``details = "full"``, a detailed version of the hypothesis test result is returned.
            * if ``details = "binary"``, the conclusion will be ``1`` (:math:`H_0` is rejected) or ``0`` (:math:`H_0` is accepted).

        Returns
        -------
        result : ``tuple`` with
            statistic : ``float``
                The test statistic.
            critical : ``list`` of two ``floats``
                The critical values for the adopted significance level, where:

                * ``critical[0]`` is the upper critical value (always positive);
                * ``critical[1]`` is the lower critical value (always negative);

            p_value : ``float``
                The p-value for the hypothesis test.
            which : ``str``
                The kind of comparison that was performed.
            alpha : ``float``
                The adopted level of significance.
        conclusion : ``str`` or ``int``
            The test conclusion (e.g, Normal/ not Normal).


        See Also
        --------
        get_critical_value


        Notes
        -----

        * Parameters ``x_exp`` and ``param`` can not be ``None`` at the same time;
        * If ``x_exp!=None``, the parameter ``params`` has no influence on the test. In this case, the test statistic is estimated using ``scipy.stats.ttest_1samp`` [1]_:

        .. code:: python

                statistic, p_value = scipy.stats.ttest_1samp(x_exp, value, axis=None)

        * If ``param!=None``, the parameter ``x_exp`` has no influence on the test. In this case, the test statistic is estimated through the following relation:

        .. math::

                t_{calc}=\\frac{\\overline{x}-\\mu}{s_x/ \\sqrt{n}}


        The parameter ``comparison`` uses the hypothesis test to compare the means as follows:

        .. admonition:: \u2615

           :math:`H_0:` the mean is equal to constant

           :math:`H_1:` the mean is different from the constant ``(1)``

           :math:`H_1:` the mean is lower than the constant ``(2)``

           :math:`H_1:` the mean is greater than the constant ``(3)``


        The parameter ``which`` controls which alternative hypothesis will be used. If ``which = "two-side"`` the relation ``(1)`` will be used as the alternative hypothesis. In this case, when ``comparison = "critical"``, the comparison is performed between the calculated test ``statistic`` and the ``critical`` values (at alpha significance level) as follows:


        .. code:: python

           if critical.Lower <= statistic <= critical.Upper:
               The mean is equal to the constant
           else:
               The mean is different from the constant

        The lower critical value is obtained with ``alfa/2`` and the upper critical value is obtained with ``1 - alfa/2`` significance level (e.g., two side distribution).

        When ``comparison = "p-value"``, the comparison is performed between the calculated ``p-value`` and the adopted significance level) as follows:


        .. code:: python

           if p-value >= ɑ:
               The mean is equal to the constant
           else:
               The mean is different from the constant

        If ``which = "one-side"`` the relation ``(2)`` or ``(3)`` will be used as the alternative hypothesis, which will depend on the difference between the sample ``mean`` and the value of the ``constant``. If this difference is lower than zero (negative), the alternative hypothesis ``(2)`` will be used. In this case, when ``comparison = "critical"``, the comparison is performed between the calculated test ``statistic`` and the lower ``critical`` value (at alpha significance level) as follows:


        .. code:: python

           if critical.Lower <= statistic:
               The mean is equal to the constant
           else:
               The mean is lower than the constant

        The lower critical value is obtained with ``alfa`` significance level (one side distribution).


        When ``comparison = "p-value"``, the comparison is performed between the calculated ``p-value`` and the adopted significance level) as follows:


        .. code:: python

           if p-value >= ɑ:
               The mean is equal to the constant
           else:
               The mean is lower than the constant


        If the difference between the sample ``mean`` and the value of the ``constant`` is higher than zero (positive), the alternative hypothesis ``(3)`` will be used. In this case, when ``comparison = "critical"``, the comparison is performed between the calculated test ``statistic`` and the upper ``critical`` value (at alpha significance level) as follows:


        .. code:: python

           if statistic <= critical.Upper:
               The mean is equal to the constant
           else:
               The mean is higher than the constant

        The upper critical value is obtained with ``1 - alfa`` significance level (one side distribution).


        When ``comparison = "p-value"``, the comparison is performed between the calculated ``p-value`` and the adopted significance level) as follows:


        .. code:: python

           if p-value >= ɑ:
               The mean is equal to the constant
           else:
               The mean is higher than the constant


        References
        ----------
        .. [1] SCIPY. scipy.stats.ttest_1samp. Available at: `https://docs.scipy.org <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html>`_. Access on: 10 May. 2022.


        Examples
        --------

        **Two side t test**

        >>> from pycafee.sample import StudentDistribution
        >>> import numpy as np
        >>> x = np.array([3.335, 3.328, 3.288, 3.198, 3.254])
        >>> constant = 3.2
        >>> comparison_test = StudentDistribution()
        >>> result, conclusion = comparison_test.compare_with_constant(x_exp=x, value=constant)
        >>> print(result)
        OneSampleStudentComparison(statistic=3.187090493341284, critical=[2.7764451051977987, -2.7764451051977996], p_value=0.03330866140058606, which='two-side', alpha=0.05)
        >>> print(conclusion)
        The mean (3.28) is different from the constant (3.2) (with 95.0% confidence).



        >>> from pycafee.sample import StudentDistribution
        >>> import numpy as np
        >>> x = np.array([3.335, 3.328, 3.288, 3.198, 3.254])
        >>> constant = 3.2
        >>> comparison_test = StudentDistribution()
        >>> result, conclusion = comparison_test.compare_with_constant(x_exp=x, value=constant, comparison='p-value', details='full')
        >>> print(result)
        OneSampleStudentComparison(statistic=3.187090493341284, critical=[2.7764451051977987, -2.7764451051977996], p_value=0.03330866140058606, which='two-side', alpha=0.05)
        >>> print(conclusion)
        Since the p-value (0.033) is lower than the adopted significance level (0.05), we have evidence to reject the null hypothesis of equality of means, and we can say that the mean (3.28) is different from the constant (3.2) (with 95.0% confidence).


        ** Two side t test using sample parameters**

        >>> from pycafee.sample import StudentDistribution
        >>> mean = 3.4
        >>> std = 0.35
        >>> n = 6
        >>> constant = 3.2
        >>> comparison_test = StudentDistribution()
        >>> result, conclusion = comparison_test.compare_with_constant(params=[mean, std, n], value=constant, comparison='p-value', details='full')
        >>> print(result)
        OneSampleStudentComparison(statistic=1.3997084244475284, critical=[2.5705818366147395, -2.57058183661474], p_value=0.22048596679416987, which='two-side', alpha=0.05)
        >>> print(conclusion)
        Since the p-value (0.22) is higher than the adopted significance level (0.05), we do not have evidence to reject the hypothesis of equality between the means, and we can say that the mean (3.4) is equal to the constant (3.2) (with 95.0% confidence).




        **One side t test**

        >>> from pycafee.sample import StudentDistribution
        >>> import numpy as np
        >>> x = np.array([3380, 3500, 3600, 3450, 3490, 3390])
        >>> constant = 3450
        >>> comparison_test = StudentDistribution()
        >>> result, conclusion = comparison_test.compare_with_constant(x_exp=x, value=constant, which="one-side")
        >>> print(result)
        OneSampleStudentComparison(statistic=0.5520741745513498, critical=[2.015048372669157, -2.0150483726691575], p_value=0.3023326513892771, which='one-side', alpha=0.05)
        >>> print(conclusion)
        The mean (3468.333) is equal to the constant (3450) (with 95.0% confidence).



        >>> from pycafee.sample import StudentDistribution
        >>> import numpy as np
        >>> x = np.array([3380, 3500, 3600, 3450, 3490, 3390])
        >>> constant = 3450
        >>> comparison_test = StudentDistribution()
        >>> result, conclusion = comparison_test.compare_with_constant(x_exp=x, value=constant, which="one-side", alfa=0.01, details='full')
        >>> print(result)
        OneSampleStudentComparison(statistic=0.5520741745513498, critical=[3.3649299989072743, -3.3649299989072756], p_value=0.3023326513892771, which='one-side', alpha=0.01)
        >>> print(conclusion)
        Since the test statistic (0.552) is lower than the upper critical value (3.364), we have no evidence to reject the null hypothesis of equality between the means, and we can say that the mean (3468.333) is equal to the constant (3450) (with 99.0% confidence)


        ** One side t test using sample parameters**


        >>> from pycafee.sample import StudentDistribution
        >>> import numpy as np
        >>> mean = 3440
        >>> std = 100
        >>> n = 10
        >>> constant = 3450
        >>> comparison_test = StudentDistribution()
        >>> result, conclusion = comparison_test.compare_with_constant(params=[mean, std, n], value=constant, which="one-side", alfa=0.01, details='full')
        >>> print(result)
        OneSampleStudentComparison(statistic=-0.31622776601683794, critical=[2.8214379233005493, -2.8214379233005498], p_value=0.37952032723207196, which='one-side', alpha=0.01)
        >>> print(conclusion)
        Since the test statistic (-0.316) is higher than the lower critical value (-2.821), we have no evidence to reject the null hypothesis of equality between the means, and we can say that the mean (3440) is equal to the constant (3450) (with 99.0% confidence)


        """
        fk_id_function = management._query_func_id("StudentDistribution")
        messages = management._get_messages(fk_id_function, self.language, "StudentDistribution")

        ### Checking the input parameters ###

        ## x_exp ##
        if x_exp is not None:
            checkers._check_is_numpy_1_D(x_exp, "x_exp", self.language)
            checkers._check_array_lower_size(x_exp, 2, "x_exp", self.language)

        ## param
        if params is not None:
            checkers._check_is_list(params, "params", self.language)
            checkers._check_is_float_or_int(params[0], "params[0]", self.language)
            checkers._check_is_float_or_int(params[1], "params[1]", self.language)
            checkers._check_is_integer(params[2], "params[2]", self.language)
            checkers._check_value_is_equal_or_higher_than(params[2], 'params[2]', 2, self.language)

        ## conflicting x_exp and param
        if x_exp is None and params is None:
            try:
                error = messages[33][0][0]
                raise ValueError(error)
            except ValueError:
                general._display_one_line_attention(messages[34][0][0])
                raise


        ## value ##
        if value is None:
            value = 0
        else:
            checkers._check_is_float_or_int(value, param_name="value", language=self.language)

        ## alfa ##
        if alfa is None:
            alfa = self.alfa
        else:
            checkers._check_is_float(alfa, "alfa", self.language)
            checkers._check_data_in_range(alfa, "alfa", 0.0, 1.0, self.language)


        ### checking the conclusion parameter ###
        if comparison is None:
            comparison = "critical"
        else:
            checkers._check_is_str(comparison, "comparison", self.language)
            if comparison == "critical":
                comparison = "critical"
            elif comparison == "p-value":
                comparison = "p-value"
            else:
                try:
                    error = messages[1][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(f"{messages[31][0][0]} 'comparison' {messages[31][2][0]} 'critical' {messages[31][4][0]} 'p-value', {messages[31][6][0]}: '{comparison}'")
                    raise

        ### checking the details parameter ###
        if details == None:
            details = "short"
        else:
            checkers._check_is_str(details, "details", self.language)
            if details == "short":
                details = "short"
            elif details == "full":
                details = "full"
            elif details == "binary":
                details = "binary"
            else:
                try:
                    error = messages[1][0][0]
                    raise ValueError(error)
                except ValueError:
                    general._display_one_line_attention(f"{messages[31][0][0]} 'details' {messages[31][2][0]} 'short', 'full' {messages[31][4][0]} 'binary', {messages[31][6][0]}: '{details}'")
                    raise


        ## which ##
        if which is None:
            which = "two-side"
        else:
            checkers._check_is_str(which, "which", self.language)
            which_keys = ["two-side", "one-side"]
            which = _check_which_param(which, self.language)


        aceita = 0
        rejeita = 1

        if which == "two-side":
            if x_exp is not None:
                statistic, p_value = one_sample_comparison(x_exp, value, axis=None)
                media = x_exp.mean()
                gl = x_exp.size - 1
            else:
                media = params[0]
                gl = params[2]-1
                statistic = _compare_with_constant_func(
                                value=value,
                                mean=media,
                                std=params[1],
                                n=params[2])
                p_value = self._get_p_value(
                                t_calc=statistic,
                                gl=gl,
                                which=which)[0]
            critical = self.get_critical_value(gl=gl, alfa=alfa)
            if comparison == 'critical':
                if critical[1] <= statistic <= critical[0]:
                    if details == 'short':
                        conclusion = f"{messages[14][0][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[14][2][0]}{value}{messages[14][4][0]} {100*(1-alfa)}{messages[14][6][0]}."
                    elif details == "full":
                        conclusion = f"{messages[15][0][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[15][2][0]}{helpers._truncate(critical[1], self.language, decs=self.n_digits)}, {helpers._truncate(critical[0], self.language, decs=self.n_digits)}{messages[15][4][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[15][6][0]}{value}{messages[15][8][0]} {100*(1-alfa)}{messages[15][10][0]}"
                    else:
                        # aceita
                        conclusion = aceita
                else:
                    if details == 'short':
                        conclusion = f"{messages[16][0][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[16][2][0]}{value}{messages[16][4][0]} {100*(1-alfa)}{messages[16][6][0]}."
                    elif details == "full":
                        if statistic > 0:
                            conclusion = f"{messages[17][0][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[17][2][0]}{helpers._truncate(critical[0], self.language, decs=self.n_digits)}{messages[17][4][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[17][6][0]}{value}{messages[17][8][0]} {100*(1-alfa)}{messages[17][10][0]}."
                        else:
                            conclusion = f"{messages[18][0][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[18][2][0]}{helpers._truncate(critical[1], self.language, decs=self.n_digits)}{messages[18][4][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[18][6][0]}{value}{messages[18][8][0]} {100*(1-alfa)}{messages[18][10][0]}."
                    else:
                        # rejeita
                        conclusion = rejeita
            else:
                if p_value < alfa:
                    if details == 'short':
                        conclusion = f"{messages[16][0][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[16][2][0]}{value}{messages[16][4][0]} {100*(1-alfa)}{messages[16][6][0]}."
                    elif details == "full":
                        conclusion = f"{messages[19][0][0]}{helpers._truncate(p_value, self.language, decs=self.n_digits)}{messages[19][2][0]}{alfa}{messages[19][4][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[19][6][0]}{value}{messages[19][8][0]} {100*(1-alfa)}{messages[19][10][0]}."
                    else:
                        # rejeita
                        conclusion = rejeita
                else:
                    if details == "short":
                        conclusion = f"{messages[14][0][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[14][2][0]}{value}{messages[14][4][0]} {100*(1-alfa)}{messages[14][6][0]}."
                    elif details == "full":
                        conclusion = f"{messages[20][0][0]}{helpers._truncate(p_value, self.language, decs=self.n_digits)}{messages[20][2][0]}{alfa}{messages[20][4][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[20][6][0]}{value}{messages[20][8][0]} {100*(1-alfa)}{messages[20][10][0]}."
                    else:
                        # aceita
                        conclusion = aceita


        else:
            if x_exp is not None:
                statistic, p_value = one_sample_comparison(x_exp, value, axis=None)
                p_value = p_value/2 # corrigindo o valor de p
                media = x_exp.mean()
                gl = x_exp.size - 1
            else:
                media = params[0]
                gl = params[2]-1
                statistic = _compare_with_constant_func(
                                value=value,
                                mean=media,
                                std=params[1],
                                n=params[2])
                p_value = self._get_p_value(
                                t_calc=statistic,
                                gl=gl,
                                which=which)[0]
            critical = self.get_critical_value(gl=gl, alfa=alfa, which=which)
            # Teste Unilateral a ESQUERDA #
            if value < media:
                # a constante é menor do que a média, a estatistica é positiva
                if comparison == "critical":
                    if statistic > critical[0]:
                        if details == "short":
                            conclusion = f"{messages[22][0][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[22][2][0]}{value}{messages[22][4][0]} {100*(1-alfa)}{messages[22][6][0]}."
                        elif details == "full":
                            conclusion = f"{messages[32][0][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[32][2][0]}{helpers._truncate(critical[0], self.language, decs=self.n_digits)}{messages[32][4][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[32][6][0]}{value}{messages[32][8][0]} {100*(1-alfa)}{messages[32][10][0]}"
                        else:
                            # rejeita
                            conclusion = rejeita
                    else:
                        if details == "short":
                            conclusion = f"{messages[14][0][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[14][2][0]}{value}{messages[14][4][0]} {100*(1-alfa)}{messages[14][6][0]}."
                        elif details == "full":
                            conclusion = f"{messages[24][0][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[24][2][0]}{helpers._truncate(critical[0], self.language, decs=self.n_digits)}{messages[24][4][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[24][6][0]}{value}{messages[24][8][0]} {100*(1-alfa)}{messages[24][10][0]}"
                        else:
                            # aceita
                            conclusion = aceita
                else:
                    if p_value < alfa:
                        if details == "short":
                            conclusion = f"{messages[22][0][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[22][2][0]}{value}{messages[22][4][0]} {100*(1-alfa)}{messages[22][6][0]}."
                        elif details == "full":
                            conclusion = f"{messages[25][0][0]}{helpers._truncate(p_value, self.language, decs=self.n_digits)}{messages[25][2][0]}{alfa}{messages[25][4][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[25][6][0]}{value}{messages[25][8][0]} {100*(1-alfa)}{messages[25][10][0]}"
                        else:
                            # rejeita
                            conclusion = rejeita
                    else:

                        if details == "short":
                            conclusion = f"{messages[14][0][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[14][2][0]}{value}{messages[14][4][0]} {100*(1-alfa)}{messages[14][6][0]}."
                        elif details == "full":
                            conclusion = f"{messages[26][0][0]}{helpers._truncate(p_value, self.language, decs=self.n_digits)}{messages[26][2][0]}{alfa}{messages[26][4][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[26][6][0]}{value}{messages[26][8][0]} {100*(1-alfa)}{messages[26][10][0]}."
                        else:
                            # aceita
                            conclusion = aceita


            elif value == media:
                if details == "binary":
                    # aceita
                    conclusion = aceita
                else:
                    conclusion = f"{messages[27][0][0]}{value}{messages[27][2][0]}{media}{messages[27][4][0]}"

            else:

                # Teste Unilateral a DIREITA #
                # Se a constante é maior do que a média, a estatistica é negativa
                if comparison == "critical":
                    if statistic < critical[1]:
                        if details == "short":
                            conclusion = f"{messages[28][0][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[28][2][0]}{value}{messages[28][4][0]} {100*(1-alfa)}{messages[28][6][0]}."
                        elif details == "full":
                            conclusion = f"{messages[29][0][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[29][2][0]}{helpers._truncate(critical[1], self.language, decs=self.n_digits)}{messages[29][4][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[29][6][0]}{value}{messages[29][8][0]} {100*(1-alfa)}{messages[29][10][0]}"
                        else:
                            # rejeita
                            conclusion = rejeita
                    else:
                        if details == "short":
                            conclusion = f"{messages[14][0][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[14][2][0]}{value}{messages[14][4][0]} {100*(1-alfa)}{messages[14][6][0]}."
                        elif details == "full":
                            conclusion = f"{messages[23][0][0]}{helpers._truncate(statistic, self.language, decs=self.n_digits)}{messages[23][2][0]}{helpers._truncate(critical[1], self.language, decs=self.n_digits)}{messages[23][4][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[23][6][0]}{value}{messages[23][8][0]} {100*(1-alfa)}{messages[23][10][0]}"
                        else:
                            # aceita
                            conclusion = aceita
                else:
                    if p_value < alfa:
                        if details == "short":
                            conclusion = f"{messages[28][0][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[28][2][0]}{value}{messages[28][4][0]} {100*(1-alfa)}{messages[28][6][0]}."
                        elif details == "full":
                            conclusion = f"{messages[30][0][0]}{helpers._truncate(p_value, self.language, decs=self.n_digits)}{messages[30][2][0]}{alfa}{messages[30][4][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[30][6][0]}{value}{messages[30][8][0]} {100*(1-alfa)}{messages[30][10][0]}"
                        else:
                            # rejeita
                            conclusion = rejeita
                    else:
                        if details == "short":
                            conclusion = f"{messages[14][0][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[14][2][0]}{value}{messages[14][4][0]} {100*(1-alfa)}{messages[14][6][0]}."
                        elif details == "full":
                            conclusion = f"{messages[26][0][0]}{helpers._truncate(p_value, self.language, decs=self.n_digits)}{messages[26][2][0]}{alfa}{messages[26][4][0]}{helpers._truncate(media, self.language, decs=self.n_digits)}{messages[26][6][0]}{value}{messages[26][8][0]} {100*(1-alfa)}{messages[26][10][0]}."
                        else:
                            # aceita
                            conclusion = aceita


        result = namedtuple(messages[21][0][0], (messages[21][1][0], messages[21][2][0], messages[21][3][0], "which", messages[21][4][0]))
        # print(critical)
        return result(statistic, [critical[0], critical[1]], p_value, which, alfa), conclusion




    def compare_pairs(self, x_exp_1, x_exp_2, alfa=None, which=None, comparison=None, details=None):

        pass



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



def _compare_with_constant_func(value, mean, std, n):
    """This function calculates the value of the Student's t test statistic that compares a sample with a constant, using the sample parameters.

    Parameters
    ----------
    value : ``int`` or ``float``
        The value that will be used as a reference. This value is treated as a constant.
    mean : ``int`` or ``float``
        The sample mean
    std : ``int`` or ``float``
        The sample standard deviation
    n : ``int``
         The sample size (higher than 1);


    Returns
    -------
    tcalc : ``float``
        The test statistic

    Notes
    -----

    The statistic is estimated through the following relation:

    .. math::

            t_{calc}=\\frac{\\overline{x}-\\mu}{s_x/ \\sqrt{n}}

    """
    t_calc = (mean - value)/(std/np.sqrt(n))
    return t_calc







#
