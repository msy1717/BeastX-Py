from .. import mrunal


def add_black_chat(chat_id):
    chat = eval(mrunal.get("BLACKLIST_CHATS"))
    if chat_id not in chat:
        chat.append(chat_id)
        mrunal.set("BLACKLIST_CHATS", str(chat))


def rem_black_chat(chat_id):
    chat = eval(mrunal.get("BLACKLIST_CHATS"))
    if chat_id in chat:
        chat.remove(chat_id)
        mrunal.set("BLACKLIST_CHATS", str(chat))
