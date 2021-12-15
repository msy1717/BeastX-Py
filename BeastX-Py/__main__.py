# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

import os
import sys
import time

from . import *
from .functions.helper import time_formatter, updater
from .startup.funcs import autopilot, customize, plug, ready, startup_stuff
from .startup.loader import load_other_plugins

# Option to Auto Update On Restarts..
if mrunal.get("UPDATE_ON_RESTART") and os.path.exists(".git") and updater():
    os.system("git pull -f -q && pip3 install --no-cache-dir -U -q -r requirements.txt")
    os.execl(sys.executable, "python3", "-m", "BeastX-Py")

startup_stuff()


beastx_bot.me.phone = None
beastx_bot.first_name = beastx_bot.me.first_name

if not beastx_bot.me.bot:
    mrunal.set("OWNER_ID", beastx_bot.uid)


LOGS.info("Initialising...")


beastx_bot.run_in_loop(autopilot())

pmbot = mrunal.get("PMBOT")
manager = mrunal.get("MANAGER")
addons = mrunal.get("ADDONS") or Var.ADDONS
vcbot = mrunal.get("VCBOT") or Var.VCBOT

# Railway dont allow Music Bots
if HOSTED_ON == "railway" and not vcbot:
    vcbot = "False"

load_other_plugins(addons=addons, pmbot=pmbot, manager=manager, vcbot=vcbot)

suc_msg = """
            ----------------------------------------------------------------------
                Beast has been deployed! Visit @BeastX_Userbot for updates!!
            ----------------------------------------------------------------------
"""

# for channel plugins
plugin_channels = mrunal.get("PLUGIN_CHANNEL")

# Customize BeastX Assistant...
beastx_bot.run_in_loop(customize())

# Load Addons from Plugin Channels.
if plugin_channels:
    beastx_bot.run_in_loop(plug(plugin_channels))

# Send/Ignore Deploy Message..
if not mrunal.get("LOG_OFF"):
    beastx_bot.run_in_loop(ready())

cleanup_cache()

if __name__ == "__main__":
    LOGS.info(
        f"Took {time_formatter((time.time() - start_time)*1000)} to start •BeastX•"
    )
    LOGS.info(suc_msg)
    beastx_bot.run()
