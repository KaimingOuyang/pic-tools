from Chart import Chart
import matplotlib.pyplot as pyplot

class Figure:
    def __init__(self, fig_cmd):
        self.set_default_settings()
        self.register_funcs()
        self.parse_fig_cmd(fig_cmd)

    # Figure class - list of functionalities
    def set_outfile(self, outfile):
        self.outfile = outfile

    def set_nrows(self, nrows):
        self.nrows = nrows

    def set_ncols(self, ncols):
        self.ncols = ncols

    def set_charts(self, chart_list):
        self.chart_list = chart_list

    def set_figsize(self, figsize):
        self.figsize = figsize

    # Figure class - default attributes settings
    def set_default_settings(self):
        # list of keys
        self.outfile = "figure.pdf"
        self.nrows = 1
        self.ncols = 1
        self.sharex = False
        self.sharey = False
        self.chart_list = None
        self.figsize = [5.7, 3.5]
        self.func_table = {}

    # Figure class - register funcs for commands
    def register_funcs(self):
        self.func_table["outfile"] = self.set_outfile
        self.func_table["nrows"] = self.set_nrows
        self.func_table["ncols"] = self.set_ncols
        self.func_table["charts"] = self.set_charts
        self.func_table["figsize"] = self.set_figsize

    # Figure class - parse figure commands
    def parse_fig_cmd(self, fig_cmd):
        for key in fig_cmd.keys():
            self.func_table[key](fig_cmd[key])

    # Figure class - plot figure
    def plot(self):
        figure = pyplot.figure(figsize=self.figsize, dpi=200)
        for chart_cmd in self.chart_list:
            chart = Chart(chart_cmd)
            chart.plot(figure)
        pyplot.savefig(self.outfile, bbox_inches='tight',
                       dpi=200, transparent=True)
        pyplot.close(figure)