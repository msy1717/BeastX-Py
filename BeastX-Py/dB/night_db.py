# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

from .. import mrunal


def get_stuff():
    a = mrunal.get("NIGHT_CHATS")
    if not a:
        return {}
    try:
        return eval(a)
    except BaseException:
        mrunal.delete("NIGHT_CHATS")
    return {}


def add_night(chat):
    chats = get_stuff()
    if chat not in chats:
        chats.append(chat)
        mrunal.set("NIGHT_CHATS", str(chats))
    return


def rem_night(chat):
    chats = get_stuff()
    if chat in chats:
        chats.remove(chat)
        mrunal.set("NIGHT_CHATS", str(chats))
    return


def night_grps():
    return get_stuff()
