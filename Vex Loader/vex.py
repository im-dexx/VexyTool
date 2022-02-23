#================================#
# █░█ █▀▀ ▀▄▀ ▄▄ █▀▄ █▀▀ █░█
# ▀▄▀ ██▄ █░█ ░░ █▄▀ ██▄ ▀▄▀

# https://github.com/im-dexx
#================================#

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

# Check 4 Updates
updater = open("vex.py", "r")
githubvex = requests.get("https://raw.githubusercontent.com/im-dexx/VexyTool/main/Vex%20Loader/vex.py").text

if updater.text != githubvex:
    print(f"{Fore.RED}* {Fore.WHITE} Vex is outdated, updating...")
    time.sleep(1)
    update = open("vex.py", "a+")
    update.write(githubvex)

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

def check4config():
    if not path.exists("config"):
        # Reinstall Config
        error("Configuration not found, re-installing.")
        os.mkdir("config")
        print("[1]: Input your DISCORD token // or leave empty")
        token = input(Fore.LIGHTBLACK_EX+f"Token%> {Fore.WHITE}")
        print("[2]: Creating token")
        newtoken = open("config/token.txt", 'a+')
        newtoken.write(token)
        newtoken.close()
        print("[3]: Installing Changelog")
        newlog = open("config/changelog.txt", 'a+')
        newlog.write(requests.get("https://raw.githubusercontent.com/im-dexx/VexyTool/main/changelog.txt").text)
        newlog.close()
        print("[/]: Installation finished, welcome "+os.getlogin())
        time.sleep(1)

        # Relaunch Vex
        cls()
        banner()
        vex()

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
def banner2():
    print(Fore.LIGHTBLACK_EX+"""
========================================
█░█ █▀▀ ▀▄▀ ░░▄▀ █░█ █▀█ █▀█ █▄▀ █▀▀ █▀▄
▀▄▀ ██▄ █░█ ▄▀░░ █▀█ █▄█ █▄█ █░█ ██▄ █▄▀
========================================
    """)

# OnStartup ======================+
cls()

# Check Files ====================+
exist = path.exists('config')
if exist == True:
    print(f"{Fore.GREEN}[-]: {Fore.WHITE}Configuration Found, starting.")
    time.sleep(1)
else:
        print(f"{Fore.RED}[#]: {Fore.WHITE}File not found\n[0]: Installing configuration")
        
        os.mkdir("config")
        print("[1]: Input your DISCORD token // or leave empty")
        token = input(Fore.LIGHTBLACK_EX+f"Token%> {Fore.WHITE}")
        print("[2]: Creating token")
        newtoken = open("config/token.txt", 'a+')
        newtoken.write(token)
        newtoken.close()
        print("[3]: Installing Changelog")
        newlog = open("config/changelog.txt", 'a+')
        newlog.write(requests.get("https://raw.githubusercontent.com/im-dexx/VexyTool/main/changelog.txt").text)
        newlog.close()
        print("[/]: Installation finished, welcome "+os.getlogin())
        time.sleep(1)

# Register Files ==================+


# Load Vex ========================+
cls()
banner()
def vex():
    # Ask Input
    check4config()
    cmd = input(f"{Fore.LIGHTBLACK_EX}> {Fore.WHITE}")
    gcmds = [""]
    acmds = ["webhooks"]
    apicmds = ["ipfind"]
    vcmds = ["changetoken", "changelog"]

    # Register Commands
    if cmd.lower() == "help" or cmd.lower() == "cmds" or cmd.lower() == "commands":
        cls()
        banner()
        print(f"""
{Fore.LIGHTBLACK_EX}General ==============================|
[0]: {gcmds[0]}{Fore.WHITE}

{Fore.LIGHTBLACK_EX}Applications =========================|
[0]: {acmds[0]}{Fore.WHITE} webhook api

{Fore.LIGHTBLACK_EX}Api Commands =========================|
[0]: {apicmds[0]}{Fore.WHITE} locate an ip

{Fore.LIGHTBLACK_EX}Vex Commands =========================|
[0]: {vcmds[0]}{Fore.WHITE} change your token
{Fore.LIGHTBLACK_EX}[1]: {vcmds[1]}{Fore.WHITE} display changelog
        """)
    elif cmd.lower() == "clear" or cmd.lower() == "cls":
        cls()
        banner()
    elif cmd.lower() == apicmds[0]:
        try:
            ip2locate = input(f"{Fore.LIGHTBLACK_EX}IP to locate\n> {Fore.LIGHTBLUE_EX}")
            api = requests.get(f"http://ip-api.com/json/{ip2locate}").json()
            print(Fore.MAGENTA+"General Info ===============================|"+Fore.LIGHTMAGENTA_EX)
            print("Query: "+api["query"])
            print("Country: "+api["country"]+" - "+api["countryCode"])
            print("Region: "+api["regionName"]+" - "+api["region"])
            print("City: "+api["city"])
            print("Zip: "+api["zip"])

            print(Fore.MAGENTA+"\nExtra Info ================================|"+Fore.LIGHTMAGENTA_EX)
            print("ISP: "+api["isp"])
            print("ORG: "+api["org"])
            print("AS: "+api["as"])
            print("\n")
            newip = open("config/ips.txt", 'a+')
            newip.write(f"\n"+ip2locate+" : "+api["country"] +" - "+ api["city"])
            newip.close()
        except:
            error("Error with IP API")
    elif cmd.lower() == acmds[0]:
        cls()
        banner2()
        check("type 'cancel' to end vex/hooked")
        def vhooked():
            # Command Input
            cmd = input(f"{Fore.LIGHTBLACK_EX}Vex/Hooked%> {Fore.WHITE}")
            vhcmds = ["chat", "raid"]

            # Register Command
            if cmd.lower() == "help" or cmd.lower() == "cmds" or cmd.lower() == "commands":
                print(f"""
{Fore.LIGHTBLACK_EX}Commands ==============================|
{Fore.LIGHTBLACK_EX}[0]: {vhcmds[0]}{Fore.WHITE} - send messages to a webhook via dhooks library
{Fore.LIGHTBLACK_EX}[1]: {vhcmds[1]}{Fore.WHITE} - being reworked
                """)
                vhooked()
            elif cmd.lower() == vhcmds[0]:
                try:
                    newhook = input(Fore.LIGHTBLACK_EX+f"Webhook URL: {Fore.LIGHTBLUE_EX}\n")
                    check("cancel or end to stop")
                    def hookchat():
                        hook = Webhook(newhook)
                        chat = input(f"{Fore.WHITE}Message: {Fore.LIGHTBLUE_EX}")
                        if chat == "end" or chat == "cancel":  
                            pass
                        else:
                            hook.send(chat)
                            hookchat()
                    hookchat()
                except:
                    error("Invalid Webhook")
                    time.sleep(1)
                    cls()
                    banner2()
                    vhooked()
            elif cmd.lower() == "cancel":
                pass
            else:
                error("[VexHook]: Unknown command.")
                vhooked()
        vhooked()
    elif cmd.lower() == vcmds[0]:
        check4config()
        if not path.exists("config/token.txt"):
            print("[1]: Old token not found, continuing.")
        else:
            os.remove("config/token.txt")
            print("[1]: Old token removed")
        token = input(Fore.LIGHTBLACK_EX+f"Token%> {Fore.WHITE}")
        print("[2]: Changing token")
        newtoken = open("config/token.txt", 'a+')
        newtoken.write(token)
        newtoken.close()
        print("[/]: Token Changed\n")
    elif cmd.lower() == vcmds[1]:
        cls()
        banner()
        print(f"{Fore.LIGHTBLACK_EX}VexyTool Changelog:")
        print(requests.get("https://raw.githubusercontent.com/im-dexx/VexyTool/main/changelog.txt").text)
    else:
        error("Invalid Command, retry")

    # Loop
    check4config()
    vex()
vex()
