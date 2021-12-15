# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.

from .. import mrunal


def str_to_list(text):  # Returns List
    return text.split(" ")


def list_to_str(list):  # Returns String
    str = "".join(f"{x} " for x in list)
    return str.strip()


def are_all_nums(list):  # Takes List , Returns Boolean
    return all(item.isdigit() for item in list)


def get_channels():  # Returns List
    channels = mrunal.get("BROADCAST")
    if channels is None or channels == "":
        return [""]
    else:
        return str_to_list(channels)


def get_no_channels():  # Returns List
    channels = mrunal.get("BROADCAST")
    if channels is None or channels == "":
        return 0
    else:
        a = channels.split(" ")
    return len(a)


def is_channel_added(id):
    channels = get_channels()
    return str(id) in channels


def add_channel(id):  # Take int or str with numbers only , Returns Boolean
    id = str(id)
    try:
        channels = get_channels()
        channels.append(id)
        mrunal.set("BROADCAST", list_to_str(channels))
        return True
    except Exception as e:
        print(f"BeastX LOG : // functions/broadcast_db/add_channel : {e}")
        return False


def rem_channel(id):
    try:
        channels = get_channels()
        channels.remove(str(id))
        mrunal.set("BROADCAST", list_to_str(channels))
        return True
    except Exception as e:
        print(f"BeastX LOG : // functions/broadcast_db/rem_channel : {e}")
        return False
