import json
import sys
from Figure import Figure
import matplotlib

if __name__ == "__main__":
    matplotlib.rcParams['ps.useafm'] = True
    matplotlib.rcParams['pdf.use14corefonts'] = True
    matplotlib.rcParams['text.usetex'] = True   
    matplotlib.rcParams['font.sans-serif'] = ["Helvetica"]
    # matplotlib.rcParams['font.family'] = "sans-serif"
    filename = sys.argv[1]
    with open(filename, "r") as jfile:
        figs_dict = json.load(jfile)
        if "figures" in figs_dict:
            for fig_cmd in figs_dict["figures"]:
                fig_obj = Figure(fig_cmd)
                fig_obj.plot()
        else:
            print("[Error] Not define 'figures' objects")
            exit(1)
