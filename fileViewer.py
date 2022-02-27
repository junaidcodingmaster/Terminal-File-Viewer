import pyfiglet
import time
import datetime
from tqdm import tqdm
from simple_chalk import chalk
import inquirer
import os

# * viewer component.
from viewer import *

os.system("cls")
rawLogo = pyfiglet.figlet_format("Terminal File Viewer")
logo = chalk.bold.blue(rawLogo)

# Display
print(logo)

print("\nWelcome to Terminal File Viewer , Made by Junaid.")
print("\n")

# Interface
try:
    file = input("Enter your File name or File path : ")
except KeyboardInterrupt:
    print("User exited")
    os._exit(0)
else:
    pass

interface = [
    inquirer.List(
        "mode",
        message="What you want to do with your file",
        choices=["Open Viewer", "Open Copier"],
    )
]

viewerMode = inquirer.prompt(interface)["mode"]

# Loader
for i in tqdm(range(100), desc="Processesing… ", ascii=False, ncols=100):
    time.sleep(0.02)
    if i == 100:
        break

# condition for viewer class
if viewerMode == "Open Viewer":
    Viewer.view(file)
elif viewerMode == "Open Copier":
    Viewer.copier(file,rawLogo)
else:
    Viewer.error()

copyRight = "Terminal File Viewer Copyright © " + str(datetime.datetime.now().year) + " Junaid"

# Giving a line for Credits
print("\n")
# Credits
print("This app is made by Junaid.")
print(chalk.bgWhite.black(copyRight))
