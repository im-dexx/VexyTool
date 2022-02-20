# Libraries =======================+
import os
import time
import requests

import os.path as path
import sys
import webbrowser as wb
from dhooks import Webhook
import random

from colorama import Fore

# Variables ======================+
osys = ""
descs = [
    "vex is super good",
    "other multitools are mid",
    "imagine building token loggers",
    "youtube skids << vex",
    "hello "+os.getlogin(),
    "i think i have feelings for "+os.getlogin(),
    "wow you downloaded configurations"
        ]


# Functions
if sys.platform == "linux" or sys.platform == "linux2":
    osys = "linux"
elif sys.platform == "darwin":
    osys = "osx"
elif sys.platform == "win32":
    osys = "win"

def cls():
    if osys == "linux":
        os.system("clear")
    elif osys == "osx":
        os.system("clear")
    elif osys == "win":
        os.system("cls")

def error(string):
    print(f"\n{Fore.RED}[#]: {Fore.WHITE}{string}\n")
def warn(string):
    print(f"\n{Fore.YELLOW}[!]: {Fore.WHITE}{string}\n")
def check(string):
    print(f"\n{Fore.GREEN}[_]: {Fore.WHITE}{string}\n")

def banner():
    print(Fore.LIGHTBLACK_EX+f"""
==========================                        
█░█ █▀▀ ▀▄▀ ▄▄ █▀▄ █▀▀ █░█
▀▄▀ ██▄ █░█ ░░ █▄▀ ██▄ ▀▄▀
==========================
{random.choices(descs)}
    """)

# OnStartup ======================+
cls()

# Check Files ====================+
exist = path.exists('config')
if exist == True:
    print(f"{Fore.GREEN}[-]: {Fore.WHITE}Configuration Found, starting.")
else:
    print(f"{Fore.RED}[#]: {Fore.WHITE}File not found\n[0]: Installing configuration")
    
    # Create Directory
    os.mkdir("config")
    
    # Write Discord Token
    token = input(Fore.LIGHTBLACK_EX+f"Token%> {Fore.WHITE}")
    print("[1]: Creating token")
    newtoken = open("config/token.txt", 'a+')
    newtoken.write(token)
    newtoken.close()

    print("[/]: Installation finished, welcome "+os.getlogin())
    time.sleep(1)

# Register Files ==================+


# Load Vex ========================+
cls()
banner()
def vex():
    # Ask Input
    cmd = input(f"{Fore.LIGHTBLACK_EX}> {Fore.WHITE}")
    cmds = [""]

    # Register Commands
    if cmd.lower() == "help":
        cls()
        banner()
        print(f"""
{Fore.LIGHTBLACK_EX}General ==============================|
[0]: {Fore.WHITE}

{Fore.LIGHTBLACK_EX}Applications =========================|
[0]: {Fore.WHITE}
        """)
    else:
        error("Invalid Command, retry")

    # Loop
    if not path.exists("config"):
        error("Configuration not found, ending process.")
        time.sleep(1)
    else:
        vex()
vex()