# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

from .. import mrunal


def is_clean_added(chat):
    k = mrunal.get("CLEANCHAT")
    if k:
        if str(chat) in k:
            return True
        return
    return


def add_clean(chat):
    if not is_clean_added(chat):
        k = mrunal.get("CLEANCHAT")
        if k:
            return mrunal.set("CLEANCHAT", k + " " + str(chat))
        return mrunal.set("CLEANCHAT", str(chat))
    return


def rem_clean(chat):
    if is_clean_added(chat):
        k = mrunal.get("CLEANCHAT")
        mrunal.set("CLEANCHAT", k.replace(str(chat), ""))
        return True
    return
