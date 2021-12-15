# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

from .. import mrunal


def get_stuff():
    a = mrunal.get("NOTE")
    if not a:
        return {}
    try:
        return eval(a)
    except BaseException:
        mrunal.delete("NOTE")
    return {}


def add_note(chat, word, msg, media, button):
    ok = get_stuff()
    if ok.get(chat):
        ok[chat].update({word: {"msg": msg, "media": media, "button": button}})
    else:
        ok.update({chat: {word: {"msg": msg, "media": media, "button": button}}})
    mrunal.set("NOTE", str(ok))


def rem_note(chat, word):
    ok = get_stuff()
    if ok.get(chat) and ok[chat].get(word):
        ok[chat].pop(word)
        mrunal.set("NOTE", str(ok))


def rem_all_note(chat):
    ok = get_stuff()
    if ok.get(chat):
        ok.pop(chat)
        mrunal.set("NOTE", str(ok))


def get_notes(chat, word):
    ok = get_stuff()
    if ok.get(chat) and ok[chat].get(word):
        return ok[chat][word]
    return False


def list_note(chat):
    ok = get_stuff()
    if ok.get(chat):
        return "".join(f"👉 #{z}\n" for z in ok[chat])
    return False
