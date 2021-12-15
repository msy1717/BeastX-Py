# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

from .. import mrunal


def get_stuff():
    a = mrunal.get("ECHO")
    if not a:
        return {}
    try:
        return eval(a)
    except BaseException:
        mrunal.delete("ECHO")
    return {}


def add_echo(chat, user):
    x = get_stuff()
    try:
        k = x[chat]
        if user not in k:
            k.append(user)
        x.update({chat: k})
    except BaseException:
        x.update({chat: [user]})
    return mrunal.set("ECHO", str(x))


def rem_echo(chat, user):
    x = get_stuff()
    try:
        k = x[chat]
        if user in k:
            k.remove(user)
        x.update({chat: k})
    except BaseException:
        pass
    return mrunal.set("ECHO", str(x))


def check_echo(chat, user):
    x = get_stuff()
    try:
        k = x[chat]
        if user in k:
            return True
        return
    except BaseException:
        return


def list_echo(chat):
    x = get_stuff()
    try:
        return x[chat]
    except BaseException:
        return
