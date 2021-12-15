# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

from .. import mrunal


def get_stuff():
    a = mrunal.get("SNIP")
    if not a:
        return {}
    try:
        return eval(a)
    except BaseException:
        mrunal.delete("SNIP")
    return {}


def add_snip(word, msg, media, button):
    ok = get_stuff()
    ok.update({word: {"msg": msg, "media": media, "button": button}})
    mrunal.set("SNIP", str(ok))


def rem_snip(word):
    ok = get_stuff()
    if ok.get(word):
        ok.pop(word)
        mrunal.set("SNIP", str(ok))


def get_snips(word):
    ok = get_stuff()
    if ok.get(word):
        return ok[word]
    return False


def list_snip():
    ok = get_stuff()
    return "".join(f"👉 ${z}\n" for z in ok)
