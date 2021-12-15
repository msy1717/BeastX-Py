# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

from .. import mrunal


def get_stuff(key="USERNAME_DB"):
    kk = mrunal.get(key)
    if not kk:
        return {}
    try:
        return eval(kk)
    except BaseException:
        mrunal.delete(key)
    return {}


def update_username(id, uname):
    ok = get_stuff()
    ok.update({id: uname})
    mrunal.set("USERNAME_DB", str(ok))


def get_username(id):
    ok = get_stuff()
    if ok.get(id):
        return ok[id]
    return None
