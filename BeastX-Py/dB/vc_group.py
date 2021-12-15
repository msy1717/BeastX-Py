# BeastX - UserBot
# Copyright (C) 2021 msy1717
#
# This file is a part of < https://github.com/msy1717/BeastX/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/msy1717/BeastX-Py/blob/main/LICENSE>.


from .. import mrunal


def get_chats():
    cha = mrunal.get("VC_AUTH_GROUPS")
    if not cha:
        cha = "{}"
    return eval(cha)


def add_vcauth(chat_id, admins=False):
    omk = get_chats()
    omk.update({chat_id: {"admins": admins}})
    mrunal.set("VC_AUTH_GROUPS", str(omk))
    return True


def check_vcauth(chat_id):
    omk = get_chats()
    if omk.get(chat_id):
        return omk[chat_id], omk[chat_id]["admins"]
    return None, None


def rem_vcauth(chat_id):
    omk = get_chats()
    if chat_id in omk.keys():
        try:
            del omk[chat_id]
            mrunal.set("VC_AUTH_GROUPS", str(omk))
            return True
        except KeyError:
            return False
    return None
