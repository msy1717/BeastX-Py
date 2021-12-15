# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

from .. import mrunal


def get_stuff():
    a = mrunal.get("PMPERMIT")
    if not a:
        return []
    try:
        return eval(a)
    except BaseException:
        try:
            # Transferring stuff From old format to new
            x, y = [], mrunal.get("PMPERMIT").split()
            for z in y:
                x.append(int(z))
            mrunal.set("PMPERMIT", str(x))
            return x
        except BaseException:
            pass
    return []


def get_approved():
    return get_stuff()


def approve_user(id):
    ok = get_approved()
    if id not in ok:
        ok.append(id)
        mrunal.set("PMPERMIT", str(ok))


def disapprove_user(id):
    ok = get_approved()
    if id in ok:
        ok.remove(id)
        mrunal.set("PMPERMIT", str(ok))


def is_approved(id):
    ok = get_approved()
    return id in ok
