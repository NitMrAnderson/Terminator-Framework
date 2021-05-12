import glob
import random
import pathlib
import os
import configparser
import toml

config = configparser.ConfigParser()
config_file = "banner.conf"

def colored(hex_color, message):
    r, g, b = [int(hex_color[i:i + 2], 16) for i in range(1, len(hex_color), 2)]
    print("\x1b[38;2;{r};{g};{b}m{message}\x1b[0m".format(**vars()))

def banner():
    workpath = (pathlib.Path(__file__).parent.absolute())
    path = str(workpath) + "/Banners"
    # Return all banner paths
    banner_paths = []
    for dirs in os.walk(path):
        for file in glob.glob(os.path.join(dirs[0], '*.txt')):
            banner_paths.append(file)
    # Select random banner path
    banner = random.choice(banner_paths)
    # Get file content
    file = open(banner, 'r')
    message = file.read()
    file.close()
    # Colored print of the banner
    colored("#ff0000", message)

# OnLoad function is needed to run code when program start
# but code in OnLoad function will not run in other situations unlike just code which not in any function
def OnLoad():
    banner()

# Code in OnCall function will run when you enter plugin command in Terminator promt
def OnCall(*args):
    banner()

# Code in OnExit function will run when you exit from terminator.
def OnExit():
    colored("#00ff00", "Goodbay from Banner!")

# Code in this function will run when you enter about <plugin command> in Terminator promt
def Info():
    print("""
    It's simple pre-installed plugin which return Banner
    We made it to test our plugin system.
    """)

# Code in this function will run when you enter help <plugin command> in Terminator promt
def Help():
    print("""
    It's actually don't need any args.
    It have a config in /core/bin/Banner/
    You can add Your banners! Just put any .txt file to the /core/bin/Banner/Banners
    To don't see our banners anymore you can just delete /core/bin/Banner/ folder
    """)
