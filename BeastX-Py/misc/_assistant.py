# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

import inspect
import re

from telethon import Button
from telethon.events import CallbackQuery, InlineQuery, NewMessage
from telethon.tl.types import InputWebDocument
from telethon.utils import get_display_name

from .. import LOGS, asst, beastx_bot
from . import append_or_update, owner_and_sudos

BeastX_PIC = "https://telegra.ph/file/4a1e0ee716f805cf66777.jpg"
OWNER = get_display_name(beastx_bot.me)

MSG = f"""
**BeastX - UserBot**
➖➖➖➖➖➖➖➖➖➖
**Owner**: [{OWNER}](tg://user?id={beastx_bot.uid})
**Support**: @BeastX_Bots
➖➖➖➖➖➖➖➖➖➖
"""

IN_BTTS = [
    [
        Button.url(
            "Repository",
            url="https://github.com/msy1717/Beast-X",
        ),
        Button.url("Support", url="https://t.me/BeastX_Support"),
    ]
]


# decorator for assistant


def asst_cmd(pattern=None, load=None, **kwargs):
    """Decorator for assistant's command"""
    name = inspect.stack()[1].filename.split("/")[-1].replace(".py", "")

    def ult(func):
        if pattern:
            kwargs["pattern"] = re.compile("^/" + pattern)
        asst.add_event_handler(func, NewMessage(**kwargs))
        if load is not None:
            append_or_update(load, func, name, kwargs)

    return ult


def callback(data=None, owner=False, **kwargs):
    """Assistant's callback decorator"""

    def ultr(func):
        async def wrapper(event):
            if owner and not str(event.sender_id) in owner_and_sudos():
                return await event.answer(f"This is {OWNER}'s bot!!")
            try:
                await func(event)
            except Exception as er:
                LOGS.exception(er)

        asst.add_event_handler(wrapper, CallbackQuery(data=data, **kwargs))

    return ultr


def in_pattern(pattern=None, owner=False, **kwargs):
    """Assistant's inline decorator."""

    def don(func):
        async def wrapper(event):
            if owner and not str(event.sender_id) in owner_and_sudos():
                res = [
                    await event.builder.article(
                        title="BeastX Userbot",
                        url="https://t.me/TheBeastX",
                        description="(c) msy1717",
                        text=MSG,
                        thumb=InputWebDocument(BeastX_PIC, 0, "image/jpeg", []),
                        buttons=IN_BTTS,
                    )
                ]
                return await event.answer(
                    res,
                    switch_pm=f"🤖: Assistant of {OWNER}",
                    switch_pm_param="start",
                )
            try:
                await func(event)
            except Exception as er:
                LOGS.exception(er)

        asst.add_event_handler(wrapper, InlineQuery(pattern=pattern, **kwargs))

    return don
