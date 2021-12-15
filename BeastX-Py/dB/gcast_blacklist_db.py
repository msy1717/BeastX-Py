# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.
from .. import mrunal


def get_stuff():
    a = mrunal.get("GBLACKLISTS")
    if not a:
        return []
    try:
        return eval(a)
    except BaseException:
        mrunal.delete("GBLACKLISTS")
    return []


def get_gblacklists():
    return get_stuff()


def add_gblacklist(id):
    ok = get_gblacklists()
    if id not in ok:
        ok.append(id)
        mrunal.set("GBLACKLISTS", str(ok))


def rem_gblacklist(id):
    ok = get_gblacklists()
    if id in ok:
        ok.remove(id)
        mrunal.set("GBLACKLISTS", str(ok))


def is_gblacklisted(id):
    ok = get_gblacklists()
    return id in ok
