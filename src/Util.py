
def get_default_line_colors(index):
    colors = []
    colors.append((0.266, 0.447, 0.768))
    colors.append((0.929, 0.490, 0.192))
    colors.append("#651854")
    colors.append("#ce2b37")
    colors.append("#008000")
    colors.append((0.149, 0.266, 0.470))
    colors.append((0.619, 0.282, 0.054))
    return colors[index % len(colors)]

def get_default_markers(index):
    markers = []
    markers.append("o")
    markers.append("x")
    markers.append("+")
    markers.append("^")
    markers.append("s")
    markers.append("2")
    markers.append("v")
    markers.append("1")
    markers.append("D")
    markers.append("s")
    markers.append("<")
    markers.append(">")
    markers.append("*")
    markers.append("d")
    return markers[index % len(markers)]

def get_default_linestyle(index):
    lines = []
    lines.append('-')
    lines.append('-')
    lines.append('-')
    lines.append('-')
    lines.append('-.')
    lines.append(':')
    lines.append('dashdot')
    lines.append('--')
    lines.append('-')
    return lines[index]

def get_default_bar_colors(index):
    colors = []
    colors.append("#003366")
    colors.append("#E67E22")
    colors.append("#5F005F")
    colors.append("#A2A5C8")
    colors.append("#684D71")
    colors.append("#206783")

    colors.append((0.929, 0.490, 0.192))
    colors.append((1.000, 0.752, 0.000))
    colors.append((0.356, 0.607, 0.835))
    colors.append((0.439, 0.678, 0.278))
    colors.append((0.619, 0.282, 0.054))
    colors.append((0.647, 0.647, 0.647))
    return colors[index % len(colors)]

def get_default_bar_edgecolors(index):
    edgecolors = []
    edgecolors.append("#003366")
    edgecolors.append("#E67E22")
    edgecolors.append("#8E44AD")
    edgecolors.append("#313566")
    edgecolors.append("#993300")
    edgecolors.append("#474C51")
    edgecolors.append("#D73041")
    edgecolors.append((0.266, 0.447, 0.768))
    edgecolors.append((0.929, 0.490, 0.192))
    edgecolors.append((1.000, 0.752, 0.000))
    edgecolors.append((0.356, 0.607, 0.835))
    edgecolors.append((0.439, 0.678, 0.278))
    edgecolors.append((0.149, 0.266, 0.470))
    edgecolors.append((0.619, 0.282, 0.054))
    edgecolors.append((0.647, 0.647, 0.647))
    return edgecolors[index % len(edgecolors)]

def get_default_hatches(index):
    hatches = []
    density = 5
    hatches.append(None)
    hatches.append(None)
    hatches.append("\\\\" * density)
    hatches.append("/////")
    hatches.append("....")
    hatches.append(None)
    hatches.append("+++")
    hatches.append("x" * density)
    hatches.append("." * density)
    hatches.append("x" * density)
    hatches.append("\\" * (density + 2))
    hatches.append("/" * (density + 2))
    hatches.append("+" * density)
    hatches.append("-" * (density + 2))
    hatches.append("|" * (density + 2) + "x" * density)
    hatches.append("-" * (density + 2) + "x" * density)
    hatches.append("-" * density + "/" * density)
    hatches.append("-" * density + "\\" * density)
    hatches.append("|" * (density + 2) + "/" * density)
    hatches.append("|" * (density + 2) + "\\" * density)
    hatches.append("x" * density + "+" * density)
    hatches.append("****")
    hatches.append("o")
    hatches.append("O")
    return hatches[index % len(hatches)]