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


def get_logger():  # Returns List
    pmperm = mrunal.get("LOGUSERS")
    if pmperm is None or pmperm == "":
        return [""]
    else:
        return str_to_list(pmperm)


def is_logger(id):  # Take int or str with numbers only , Returns Boolean
    if not str(id).isdigit():
        return False
    pmperm = get_logger()
    return str(id) in pmperm


def log_user(id):  # Take int or str with numbers only , Returns Boolean
    id = str(id)
    if not id.isdigit():
        return False
    try:
        pmperm = get_logger()
        pmperm.append(id)
        mrunal.set("LOGUSERS", list_to_str(pmperm))
        return True
    except Exception as e:
        print(f"BeastX LOG : // functions/logusers_db/log_user : {e}")
        return False


def nolog_user(id):  # Take int or str with numbers only , Returns Boolean
    id = str(id)
    if not id.isdigit():
        return False
    try:
        pmperm = get_logger()
        pmperm.remove(id)
        mrunal.set("LOGUSERS", list_to_str(pmperm))
        return True
    except Exception as e:
        print(f"BeastX LOG : // functions/loguser_db/nolog_user : {e}")
        return False
