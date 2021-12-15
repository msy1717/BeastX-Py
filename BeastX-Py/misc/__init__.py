# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.


from .. import *

CMD_HELP = {}
# ----------------------------------------------#


def sudoers():
    from .. import mrunal

    if mrunal.get("SUDOS"):
        return mrunal["SUDOS"].split()
    return []


def should_allow_sudo():
    from .. import mrunal

    return mrunal.get("SUDO") == "True"


def owner_and_sudos(castint=False):
    from .. import mrunal, beastx_bot

    data = [str(beastx_bot.uid), *sudoers()]
    if castint:
        return [int(a) for a in data]
    return data


# ------------------------------------------------ #


def append_or_update(load, func, name, arggs):
    if isinstance(load, list):
        return load.append(func)
    if isinstance(load, dict):
        if load.get(name):
            return load[name].append((func, arggs))
        return load.update({name: [(func, arggs)]})
