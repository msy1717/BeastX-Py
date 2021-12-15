# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

from .. import mrunal


def get_stuff(key=None):
    kk = mrunal.get(key)
    if not kk:
        return {}
    try:
        return eval(kk)
    except BaseException:
        mrunal.delete(key)
    return {}


def add_welcome(chat, msg, media, button):
    ok = get_stuff("WELCOME")
    ok.update({chat: {"welcome": msg, "media": media, "button": button}})
    return mrunal.set("WELCOME", str(ok))


def get_welcome(chat):
    ok = get_stuff("WELCOME")
    wl = ok.get(chat)
    if wl:
        return wl
    return


def delete_welcome(chat):
    ok = get_stuff("WELCOME")
    wl = ok.get(chat)
    if wl:
        ok.pop(chat)
        return mrunal.set("WELCOME", str(ok))
    return


def add_goodbye(chat, msg, media, button):
    ok = get_stuff("GOODBYE")
    ok.update({chat: {"goodbye": msg, "media": media, "button": button}})
    return mrunal.set("GOODBYE", str(ok))


def get_goodbye(chat):
    ok = get_stuff("GOODBYE")
    wl = ok.get(chat)
    if wl:
        return wl
    return


def delete_goodbye(chat):
    ok = get_stuff("GOODBYE")
    wl = ok.get(chat)
    if wl:
        ok.pop(chat)
        return mrunal.set("GOODBYE", str(ok))
    return


def add_thanks(chat):
    x = get_stuff("THANK_MEMBERS")
    x.update({chat: True})
    return mrunal.set("THANK_MEMBERS", str(x))


def remove_thanks(chat):
    x = get_stuff("THANK_MEMBERS")
    if x.get(chat):
        x.pop(chat)
        return mrunal.set("THANK_MEMBERS", str(x))
    return


def must_thank(chat):
    x = get_stuff("THANK_MEMBERS")
    try:
        return x[chat]
    except KeyError:
        return False
