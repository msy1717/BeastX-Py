# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

from .. import mrunal


def get_stuff():
    a = mrunal.get("MUTE")
    if not a:
        return {}
    try:
        return eval(a)
    except BaseException:
        mrunal.delete("MUTE")
    return {}


def mute(chat, id):
    ok = get_stuff()
    if ok.get(chat):
        if id not in ok[chat]:
            ok[chat].append(id)
    else:
        ok.update({chat: [id]})
    mrunal.set("MUTE", str(ok))


def unmute(chat, id):
    ok = get_stuff()
    if ok.get(chat) and id in ok[chat]:
        ok[chat].remove(id)
    mrunal.set("MUTE", str(ok))


def is_muted(chat, id):
    ok = get_stuff()
    return bool(ok.get(chat) and id in ok[chat])
