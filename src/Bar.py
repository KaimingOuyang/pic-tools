
class Bar:
    def __init__(self, bar_cmd, index):
        self.set_default_settings()
        self.barindex = index
        self.register_funcs()
        self.parse_bar_cmd(bar_cmd)

    # Line class - list of functionalities
    def set_axes(self, axes):
        self.axes = axes
    
    def set_barcolors(self, barcolors):
        self.barcolors = barcolors
    
    def set_edgecolors(self, edgecolors):
        self.edgecolors = edgecolors

    def set_hatches(self, hatches):
        self.hatches = hatches

    def set_barlabels(self, barlabels):
        self.barlabels = barlabels

    def set_yvalues(self, yvalues):
        self.yvalues = yvalues

    def set_errorbars(self, errorbars):
        self.errorbars = errorbars

    def set_xticklabels(self, xticklabels):
        self.xticklabels = xticklabels

    def set_barwidth(self, barwidth):
        self.barwidth = barwidth

    def set_linewidth(self, linewidth):
        self.linewidth = linewidth
    
    def set_bar_offset(self, bar_offset):
        self.bar_offset = bar_offset

    def set_capsize(self, capsize):
        self.capsize = capsize

    def set_errorbars_capthick(self, errorbars_capthick):
        self.errorbars_capthick = errorbars_capthick

    def set_barindex(self, barindex):
        self.barindex = barindex

    # Line class - default attribute settings
    def set_default_settings(self):
        self.barcolors = None
        self.edgecolors = None
        self.hatches = None
        self.barlabels = None
        self.yvalues = None
        self.errorbars = None
        self.xticklabels = None
        self.axes = "major"
        self.barwidth = 3
        self.linewidth = 0.5
        self.bar_offset = 0.0
        self.barindex = 0
        self.capsize = 2
        self.errorbars_capthick = 1.3
        self.func_table = {}

    # Line class - register funcs for commands
    def register_funcs(self):
        self.func_table["axes"] = self.set_axes
        self.func_table["barcolors"] = self.set_barcolors
        self.func_table["edgecolors"] = self.set_edgecolors
        self.func_table["hatches"] = self.set_hatches
        self.func_table["barlabels"] = self.set_barlabels
        self.func_table["yvalues"] = self.set_yvalues
        self.func_table["errorbars"] = self.set_errorbars
        self.func_table["xticklabels"] = self.set_xticklabels
        self.func_table["barwidth"] = self.set_barwidth
        self.func_table["linewidth"] = self.set_linewidth
        self.func_table["bar_offset"] = self.set_bar_offset
        self.func_table["capsize"] = self.set_capsize
        self.func_table["errorbars_capthick"] = self.set_errorbars_capthick
        self.func_table["barindex"] = self.set_barindex
    
    def parse_bar_cmd(self, bar_cmd):
        for key in bar_cmd:
            self.func_table[key](bar_cmd[key])