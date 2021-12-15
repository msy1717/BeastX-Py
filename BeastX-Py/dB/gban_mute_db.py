# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

from .. import mrunal


def get_gban_stuff():
    a = mrunal.get("GBAN")
    if not a:
        return {}
    try:
        return dict(eval(a))
    except BaseException:
        mrunal.delete("GBAN")
    return {}


ge = mrunal.get("GMUTE")
if ge:
    try:
        if "list" not in str(type(eval(ge))):
            mrunal.set("GMUTE", "[]")
    except BaseException:
        mrunal.set("GMUTE", "[]")


def gban(user, reason):
    ok = list_gbanned()
    ok.update({user: reason or "No Reason. "})
    mrunal.set("GBAN", str(ok))


def ungban(user):
    ok = list_gbanned()
    if ok.get(user):
        del ok[user]
        mrunal.set("GBAN", str(ok))


def is_gbanned(user):
    ok = list_gbanned()
    if ok.get(user):
        return ok[user]
    return False


def list_gbanned():
    return get_gban_stuff()


def gmute(user):
    ok = list_gmuted()
    ok.append(user)
    mrunal.set("GMUTE", str(ok))


def ungmute(user):
    ok = list_gmuted()
    if user in ok:
        ok.remove(user)
        mrunal.set("GMUTE", str(ok))


def is_gmuted(user):
    ok = list_gmuted()
    return user in ok


def list_gmuted():
    if mrunal.get("GMUTE"):
        return eval(mrunal.get("GMUTE"))
    return []
