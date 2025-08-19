
from typing import List, Tuple
from pyrogram.errors import UserNotParticipant
from pyrogram import Client
from config import FORCE_SUB_USERNAMES, FORCE_SUB_CHAT_IDS

async def check_user_subscriptions(app: Client, user_id: int) -> Tuple[List[str], List[int]]:
    """
    Returns (missing_usernames, missing_chat_ids) that the user still needs to join.
    Only USERNAMES and CHAT_IDS can be *verified*. Invite links cannot be verified by the Bot API.
    """
    missing_usernames = []
    for uname in FORCE_SUB_USERNAMES:
        if not uname:
            continue
        try:
            member = await app.get_chat_member(uname, user_id)
            if member.status not in ("member", "administrator", "creator"):
                missing_usernames.append(uname)
        except UserNotParticipant:
            missing_usernames.append(uname)
        except Exception:
            # If something goes wrong, be safe and require join
            missing_usernames.append(uname)

    missing_chat_ids = []
    for chat_id in FORCE_SUB_CHAT_IDS:
        try:
            member = await app.get_chat_member(chat_id, user_id)
            if member.status not in ("member", "administrator", "creator"):
                missing_chat_ids.append(chat_id)
        except UserNotParticipant:
            missing_chat_ids.append(chat_id)
        except Exception:
            missing_chat_ids.append(chat_id)

    return missing_usernames, missing_chat_ids
