class Line:
    def __init__(self, line_cmd, index):
        self.set_default_settings()
        self.lineindex = index
        self.register_funcs()
        self.parse_line_cmd(line_cmd)
        

    # Line class - list of functionalities
    def set_axes(self, axes):
        self.axes = axes

    def set_color(self, color):
        self.color = color

    def set_linelabel(self, linelabel):
        self.linelabel = linelabel

    def set_yvalues(self, yvalues):
        self.yvalues = yvalues

    def set_errorbars(self, errorbars):
        self.errorbars = errorbars
    
    def set_linestyle(self, linestyle):
        self.linestyle = linestyle
    
    def set_marker(self, marker):
        self.marker = marker

    def set_linewidth(self, linewidth):
        self.linewidth = linewidth

    def set_capsize(self, capsize):
        self.capsize = capsize

    def set_errorbars_capthick(self, errorbars_capthick):
        self.errorbars_capthick = errorbars_capthick

    def set_markersize(self, markersize):
        self.markersize = markersize

    def set_lineindex(self, lineindex):
        self.lineindex = lineindex
        
    # Line class - default attribute settings
    def set_default_settings(self):
        self.color = None
        self.linelabel = None
        self.yvalues = None
        self.errorbars = None
        self.linestyle = None
        self.marker = None
        self.axes = "major"
        self.linewidth = 1
        self.capsize = 2
        self.errorbars_capthick = 1.3
        self.markersize = 10.0
        self.lineindex = 0
        self.func_table = {}

    # Line class - register funcs for commands
    def register_funcs(self):
        self.func_table["axes"] = self.set_axes
        self.func_table["color"] = self.set_color
        self.func_table["linelabel"] = self.set_linelabel
        self.func_table["yvalues"] = self.set_yvalues
        self.func_table["errorbars"] = self.set_errorbars
        self.func_table["linestyle"] = self.set_linestyle
        self.func_table["marker"] = self.set_marker
        self.func_table["linewidth"] = self.set_linewidth
        self.func_table["capsize"] = self.set_capsize
        self.func_table["errorbars_capthick"] = self.set_errorbars_capthick
        self.func_table["markersize"] = self.set_markersize
        self.func_table["lineindex"] = self.set_lineindex
    
    def parse_line_cmd(self, line_cmd):
        for key in line_cmd:
            self.func_table[key](line_cmd[key])