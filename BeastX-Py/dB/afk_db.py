# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

from datetime import datetime as dt

from .. import mrunal


def get_stuff():
    a = mrunal.get("AFK_DB")
    if not a:
        return []
    try:
        return eval(a)
    except BaseException:
        mrunal.delete("AFK_DB")
    return []


def add_afk(msg, media_type, media):
    time = dt.now().strftime("%b %d %Y %I:%M:%S%p")
    mrunal.set("AFK_DB", str([msg, media_type, media, time]))
    return


def is_afk():
    afk = get_stuff()
    if afk:
        start_time = dt.strptime(afk[3], "%b %d %Y %I:%M:%S%p")
        afk_since = str(dt.now().replace(microsecond=0) - start_time)
        return afk[0], afk[1], afk[2], afk_since
    return False


def del_afk():
    return mrunal.set("AFK_DB", "[]")
