# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.


import time

from .configs import Var
from .startup import *
from .startup.BaseClient import BeastXClient
from .startup.connections import (
    RedisConnection,
    session_file,
    vc_connection,
    where_hosted,
)
from .startup.exceptions import RedisError
from .startup.funcs import autobot

start_time = time.time()

HOSTED_ON = where_hosted()

mrunal = RedisConnection(
    host=Var.REDIS_URI or Var.REDISHOST,
    password=Var.REDIS_PASSWORD or Var.REDISPASSWORD,
    port=Var.REDISPORT,
    platform=HOSTED_ON,
    decode_responses=True,
    socket_timeout=5,
    retry_on_timeout=True,
)
if mrunal.ping():
    LOGS.info("Connected to Redis Database")


beastx_bot = BeastXClient(
    session_file(),
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    mrunal=mrunal,
    base_logger=TeleLogger,
)

beastx_bot.run_in_loop(autobot())

asst = BeastXClient(
    None,
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=mrunal.get("BOT_TOKEN"),
    mrunal=mrunal,
    base_logger=TeleLogger,
)

vcClient = vc_connection(mrunal, beastx_bot)

if not mrunal.get("SUDO"):
    mrunal.set("SUDO", "False")

if not mrunal.get("SUDOS"):
    mrunal.set("SUDOS", "")

if not mrunal.get("BLACKLIST_CHATS"):
    mrunal.set("BLACKLIST_CHATS", "[]")

HNDLR = mrunal.get("HNDLR") or "."
DUAL_HNDLR = mrunal.get("DUAL_HNDLR") or "/"
SUDO_HNDLR = mrunal.get("SUDO_HNDLR") or HNDLR
