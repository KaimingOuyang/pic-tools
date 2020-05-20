import json
import sys
from Figure import Figure

if __name__ == "__main__":
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
