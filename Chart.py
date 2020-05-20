from Line import Line
from Bar import Bar
import numpy as np
import Util
import matplotlib.pyplot as pyplot

class Chart:
    def __init__(self, chart_cmd):
        self.set_default_settings()
        self.register_funcs()
        self.parse_chart_cmd(chart_cmd)

    # Chart class - list of functionalities
    def set_title(self, title):
        self.title = title

    def set_xtitle(self, xtitle):
        self.xtitle = xtitle

    def set_ytitle(self, ytitle):
        self.ytitle = ytitle

    def set_major_ylim(self, major_ylim):
        self.major_ylim = major_ylim

    def set_minor_ylim(self, minor_ylim):
        self.minor_ylim = minor_ylim

    def set_xvalues(self, xvalues):
        self.xvalues = xvalues

    def set_xticklabels(self, xticklabels):
        self.xticklabels = xticklabels

    def set_plot_position(self, plot_position):
        self.plot_position = plot_position

    def set_sharex(self, flag):
        self.sharex = flag

    def set_sharey(self, flag):
        self.sharey = flag

    def parse_line_cmd(self, lines):
        index = 0
        for line_cmd in lines:
            line_obj = Line(line_cmd, index)
            self.line_objs.append(line_obj)
            index = index + 1

    def set_show_legend(self, show_legend):
        self.show_legend = show_legend

    def set_legend_loc(self, legend_loc):
        if legend_loc == "top":
            self.legend_loc = "lower left"
            self.bbox_to_anchor = (-0.02, 1.01)
        elif legend_loc == "right":
            self.legend_loc = "center left"
            self.bbox_to_anchor = (1.04, 0.5)
        elif legend_loc == "lower right":
            self.legend_loc = "lower left"
            self.bbox_to_anchor = (1.04, 0)
        elif legend_loc == "upper right":
            self.legend_loc = "upper left"
            self.bbox_to_anchor = (1.02, 1)
        elif legend_loc == "bottom right":
            self.legend_loc = "center"
            self.bbox_to_anchor = (1.04, -0.3)

    def set_legend_fontsize(self, legend_fontsize):
        self.legend_fontsize = legend_fontsize

    def set_legend_ncols(self, legend_ncols):
        self.legend_ncols = legend_ncols

    def set_legend_linewidth(self, legend_linewidth):
        self.legend_linewidth = legend_linewidth

    def set_xscale(self, xscale):
        self.xscale = xscale

    def set_major_yscale(self, major_yscale):
        self.major_yscale = major_yscale

    def set_minor_yscale(self, minor_yscale):
        self.minor_yscale = minor_yscale

    def set_title_fontsize(self, title_fontsize):
        self.title_fontsize = title_fontsize

    def set_label_fontsize(self, label_fontsize):
        self.label_fontsize = label_fontsize

    def set_ticklabel_fontsize(self, ticklabel_fontsize):
        self.ticklabel_fontsize = ticklabel_fontsize

    def set_xticklabel_angle(self, xticklabel_angle):
        self.xticklabel_angle = xticklabel_angle

    def parse_bar_cmd(self, bars):
        index = 0
        for bar_cmd in bars:
            bar_obj = Bar(bar_cmd, index)
            self.bar_objs.append(bar_obj)
            index = index + 1

    # Chart class - default attributes settings
    def set_default_settings(self):
        self.title = None
        self.xtitle = None
        self.ytitle = None
        self.major_ylim = None
        self.minor_ylim = None
        self.xvalues = None
        self.xticklabels = None
        self.major_axes = None
        self.minor_axes = None
        self.sharex = False
        self.sharey = False
        self.plot_position = [1, 1, 1]
        self.show_legend = True
        self.legend_loc = "best"
        self.bbox_to_anchor = None
        self.legend_fontsize = 16
        self.legend_ncols = 1
        self.legend_linewidth = 0.0
        self.xscale = None
        self.major_yscale = None
        self.minor_yscale = None
        self.title_fontsize = 16
        self.label_fontsize = 16
        self.ticklabel_fontsize = 15
        self.xticklabel_angle = 0
        self.grid_linewidth = 0.2
        self.grid_dashes = (5, 5)
        self.line_objs = []
        self.bar_objs = []
        self.func_table = {}

    # Chart class - register funcs for commands
    def register_funcs(self):
        self.func_table["title"] = self.set_title
        self.func_table["xtitle"] = self.set_xtitle
        self.func_table["ytitle"] = self.set_ytitle
        self.func_table["major_ylim"] = self.set_major_ylim
        self.func_table["minor_ylim"] = self.set_minor_ylim
        self.func_table["xvalues"] = self.set_xvalues
        self.func_table["xticklabels"] = self.set_xticklabels
        self.func_table["plot_position"] = self.set_plot_position
        self.func_table["sharex"] = self.set_sharex
        self.func_table["sharey"] = self.set_sharey
        self.func_table["lines"] = self.parse_line_cmd
        self.func_table["show_legend"] = self.set_show_legend
        self.func_table["legend_loc"] = self.set_legend_loc
        self.func_table["legend_fontsize"] = self.set_legend_fontsize
        self.func_table["legend_ncols"] = self.set_legend_ncols
        self.func_table["legend_linewidth"] = self.set_legend_linewidth
        self.func_table["xscale"] = self.set_xscale
        self.func_table["major_yscale"] = self.set_major_yscale
        self.func_table["minor_yscale"] = self.set_minor_yscale
        self.func_table["title_fontsize"] = self.set_title_fontsize
        self.func_table["label_fontsize"] = self.set_label_fontsize
        self.func_table["ticklabel_fontsize"] = self.set_ticklabel_fontsize
        self.func_table["xticklabel_angle"] = self.set_xticklabel_angle
        self.func_table["bars"] = self.parse_bar_cmd

    # Chart class - parse chart commands
    def parse_chart_cmd(self, chart_cmd):
        for key in chart_cmd:
            self.func_table[key](chart_cmd[key])

    # Chart class - plot subfigure
    def plot(self, figure):
        self.major_axes = figure.add_subplot(
            self.plot_position[0], self.plot_position[1], self.plot_position[2])

        legends = []
        # draw bars
        for i in range(0, len(self.bar_objs)):
            ret_legends = self.plot_bar(
                self.bar_objs[i], len(self.bar_objs), i)
            if i == 0 or len(ret_legends) == 1:
                legends = legends + ret_legends

        # specific for bar chart tick label settings
        if self.bar_objs != None:
            tick_len = len(self.bar_objs[0].yvalues[0])
            barwidth = self.bar_objs[0].barwidth
            linewidth = self.bar_objs[0].linewidth
            barcnt = len(self.bar_objs)

            major_ticks = np.arange(0, tick_len) * (barcnt + 1) * barwidth
            self.major_axes.set_xticks(major_ticks, minor=False)

            if self.xticklabels != None:
                self.xvalues = minor_ticks = (
                    np.arange(0, tick_len) * (barcnt + 1) + (barcnt + 1) / 2) * barwidth
            else:
                minor_ticks = []
                self.xticklabels = []
                for i in range(0, tick_len):
                    for j in range(0, barcnt):
                        minor_ticks.append(
                            (i * (barcnt + 1) + j + 1) * barwidth + (j + 1) * linewidth)
                        self.xticklabels.append(
                            self.bar_objs[j].xticklabels[i])

            self.major_axes.set_xticks(minor_ticks, minor=True)
            self.major_axes.set_xticklabels(self.xticklabels, minor=True, ha="right")
            self.major_axes.tick_params(
                axis='x', which='minor', color="w", labelsize=self.ticklabel_fontsize)
            self.major_axes.tick_params(
                axis='x', which='major', labelbottom=False, colors="#CCCCCC", width=1, length = 4.5)

        # draw lines
        for line_obj in self.line_objs:
            legends.append(self.plot_line(line_obj))

        # show legends
        if(self.show_legend == True):
            labels = [label.get_label() for label in legends]
            self.major_axes.legend(legends, labels, loc=self.legend_loc, bbox_to_anchor=self.bbox_to_anchor, fancybox=True,
                                   fontsize=self.legend_fontsize, ncol=self.legend_ncols, framealpha=1).get_frame().set_linewidth(self.legend_linewidth)

        # set x and (or) y axis property
        self.major_axes.set_title(self.title, fontsize=self.title_fontsize)
        self.major_axes.set_xlabel(self.xtitle, fontsize=self.label_fontsize)
        self.major_axes.set_ylabel(self.ytitle, fontsize=self.label_fontsize)

        self.major_axes.tick_params(
            axis='x', which='major', labelsize=self.ticklabel_fontsize)
        self.major_axes.tick_params(
            axis='y', which='major', labelsize=self.ticklabel_fontsize)

        self.major_axes.yaxis.grid(
            which='major', linestyle='--', linewidth=self.grid_linewidth, dashes=self.grid_dashes)

        if self.bar_objs == None:
            self.major_axes.xaxis.grid(
            which='major', linestyle='--', linewidth=self.grid_linewidth, dashes=self.grid_dashes)
            for tick in self.major_axes.get_xticklabels():
                tick.set_rotation(self.xticklabel_angle)
        else:
            for tick in self.major_axes.get_xticklabels(minor=True):
                tick.set_rotation(self.xticklabel_angle)

        if self.major_ylim != None:
            self.major_axes.set_ylim(self.major_ylim[0], self.major_ylim[1])
        if self.minor_ylim != None:
            self.minor_axes.set_ylim(self.minor_ylim[0], self.minor_ylim[1])

        if self.major_yscale != None:
            self.major_axes.set_yscale(
                self.major_yscale[0], basey=self.major_yscale[1])
        if self.minor_yscale != None:
            self.minor_axes.set_yscale(
                self.minor_yscale[0], basey=self.minor_yscale[1])

    # Chart class - add line to subfigure
    def plot_line(self, line_obj):
        if(line_obj.axes == "major"):
            axes = self.major_axes
        else:
            if(self.minor_axes == None):
                self.minor_axes = self.major_axes.twinx()
            axes = self.minor_axes

        if(line_obj.color != None):
            color = line_obj.color
        else:
            color = Util.get_default_line_colors(line_obj.lineindex)

        if(line_obj.linestyle != None):
            linestyle = line_obj.linestyle
        else:
            linestyle = Util.get_default_linestyle(line_obj.lineindex)

        if(line_obj.marker != None):
            marker = line_obj.marker
        else:
            marker = Util.get_default_markers(line_obj.lineindex)

        if(line_obj.errorbars != None):
            axes.errorbar(self.xvalues, line_obj.yvalues, yerr=line_obj.errorbars, fmt="none", ecolor=color,
                          elinewidth=line_obj.linewidth, capsize=line_obj.capsize, capthick=line_obj.errorbars_capthick)

        return axes.plot(self.xvalues, line_obj.yvalues, color=color, linestyle=linestyle, marker=marker, label=line_obj.linelabel, linewidth=line_obj.linewidth, markersize=line_obj.markersize)[0]

    def plot_bar(self, bar_obj, barcnt, id):
        if(bar_obj.axes == "major"):
            axes = self.major_axes
        else:
            if(self.minor_axes == None):
                self.minor_axes = self.major_axes.twinx()
            axes = self.minor_axes

        num_stack = len(bar_obj.yvalues[0])
        barcolors = []
        if(bar_obj.barcolors != None):
            barcolors = bar_obj.barcolors
        else:
            for i in range(0, num_stack):
                barcolors.append(
                    Util.get_default_bar_colors(bar_obj.barindex + i))

        edgecolors = []
        if(bar_obj.edgecolors != None):
            edgecolors = bar_obj.edgecolors
        else:
            for i in range(0, num_stack):
                edgecolors.append(
                    Util.get_default_bar_edgecolors(bar_obj.barindex + i))
                # print(i, edgecolors)

        hatches = []
        if(bar_obj.hatches != None):
            hatches = bar_obj.hatches
        else:
            for i in range(0, num_stack):
                hatches.append(Util.get_default_hatches(bar_obj.barindex + i))

        legends = []
        bottom = [0.0 for i in range(0, len(bar_obj.yvalues[0]))]
        for i in range(0, len(bar_obj.yvalues)):
            errorbar = None
            if bar_obj.errorbars != None:
                errorbar = bar_obj.errorbars[i]
            legends.append(axes.bar((np.arange(0, len(bar_obj.yvalues[i])) * (barcnt + 1) + id + 1) * bar_obj.barwidth + (id - 0.5) * bar_obj.linewidth, bar_obj.yvalues[i], width=bar_obj.barwidth, align="center", linewidth=bar_obj.linewidth, label=bar_obj.barlabels[i], hatch=hatches[i], color=barcolors[i], edgecolor=edgecolors[i], yerr=errorbar, capsize=bar_obj.capsize, bottom=bottom))
            bottom = [bottom[j] + bar_obj.yvalues[i][j]
                      for j in range(0, len(bar_obj.yvalues[i]))]

        return legends