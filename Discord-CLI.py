import os
import subprocess
import asyncio
import colorama
import datetime
import time

import random
import string

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from datetime import datetime

# - Terminal Color Definitions
RESET = '\033[0m'
# - Formatting Codes (Windows Incompatible)
BOLD = '\033[1m'
DIM = '\033[2m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'
INVERTED = '\033[7m'
HIDDEN = '\033[8m'
#-------------------------#
# - Background Colors
BDEFAULT = '\033[49m'
BWHITE = '\033[107m'
BLIGHTCYAN = '\033[106m'
BLIGHTMAGENTA = '\033[105m'
BLIGHTBLUE = '\033[104m'
BLIGHTYELLOW = '\033[103m'
BLIGHTGREEN = '\033[102m'
BLIGHTRED = '\033[101m'
BDARKGREY = '\033[100m'
BLIGHTGREY = '\033[47m'
BCYAN = '\033[46m'
BMAGENTA = '\033[45'
BBLUE = '\033[44m'
BYELLOW = '\033[43m'
BGREEN = '\033[42m'
BBLACK = '\033[40m'
BRED = '\033[41m'
#-------------------------#
# - Text Colors
CLEAR_SCREEN = '\033[2J'
WHITE = '\033[97m'
LIGHTCYAN = '\033[96m'
LIGHTMAGENTA = '\033[95m'
LIGHTBLUE = '\033[94m'
LIGHTYELLOW = '\033[93m'
LIGHTGREEN = '\033[92m'
LIGHTRED = '\033[91m'
DARKGREY = '\033[90m'
LIGHTGREY = '\033[37m'
CYAN = '\033[36m'
MAGENTA = '\033[35m'
BLUE = '\033[34m'
YELLOW = '\033[33m'
GREEN = '\033[32m'
BLACK = '\033[30m'
DEFAULT = '\033[39m'
RED = '\033[31m'
#
THEMECOLOR = LIGHTCYAN
colorama.init()

subprocess.call('cls',shell=True)

CLIENT_TOKEN = input("{}Client Token: ".format(THEMECOLOR))
VERSION = "0.5.0"
prefix = "qlxm)c}-][+I=s,<3UmN.k7;'aow#5G^"
client = commands.Bot(command_prefix = prefix)

Token_BYTE = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(8))
Token_WORD = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))
Token_DWORD = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(32))
Token_QWORD = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(64))

client.remove_command(name="help")

@client.event
async def on_ready():
    Header = '''
{}---------------------------------------------
- Discord CLI -
Version: {}
Author: WorldDstroyer
-
Client: {}
Token: [REDACTED]
Time | Date: {}
Session Nonce: {}
---------------------------------------------\
    '''
    BT = datetime.now()
    BT = BT.strftime("%m-%d-%y, %H:%M:%S")

    subprocess.call('cls',shell=True)

    print(Header.format(THEMECOLOR, VERSION, client.user, BT, Token_WORD))

    #
    Mode = input("Direct Message? (y/n) ")
    if Mode == "y":
        DM = True
    else:
        DM = False
    #

    if DM == True:
        Target = input("User ID: ")
        Channel = await client.fetch_user(int(Target))
    else:
        Target = input("Channel ID: ")
        Channel = client.get_channel(int(Target))

    print("")
    print("Listening for communications on target <{}>...".format(Target))
    print("")

    while True:
        CLI = input("{}: ".format(Channel))
        CLI = CLI.rstrip()

        if CLI == "":
            print("")

        else:
            await Channel.send(CLI)
            MT = datetime.now()
            MT = MT.strftime("%H:%M:%S")
            print("{}[{}] {}: {}{}".format(LIGHTYELLOW, MT, client.user, CLI, THEMECOLOR))
            print("")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.guild == None:
        MT = datetime.now()
        MT = MT.strftime("%H:%M:%S")
        print("\n[{}] {}: {}\n".format(MT, message.author, message.content))

#
client.run(CLIENT_TOKEN)
#