# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

from .. import mrunal


def get_stuff():
    a = mrunal.get("CHATBOT_USERS")
    if not a:
        return {}
    try:
        return eval(a)
    except BaseException:
        mrunal.delete("CHATBOT_USERS")
    return {}


def get_all_added(chat):
    ok = get_stuff()
    if ok.get(chat):
        return ok[chat]
    return False


def chatbot_stats(chat, id):
    ok = get_stuff()
    return bool(ok.get(chat) and id in ok[chat])


def add_chatbot(chat, id):
    ok = get_stuff()
    if not ok.get(chat):
        ok.update({chat: [id]})
    elif id not in ok[chat]:
        ok[chat].append(id)
    return mrunal.set("CHATBOT_USERS", str(ok))


def rem_chatbot(chat, id):
    ok = get_stuff()
    if ok.get(chat) and id in ok[chat]:
        ok[chat].remove(id)
    return mrunal.set("CHATBOT_USERS", str(ok))
