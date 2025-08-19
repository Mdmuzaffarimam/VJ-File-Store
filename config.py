
import os

# --- Telegram credentials ---
API_ID = int(os.getenv("API_ID", "123456"))           # Get from my.telegram.org
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

# --- Force Subscribe configuration ---
# 1) Public usernames you can verify directly (e.g., "Mrn_Officialx")
FORCE_SUB_USERNAMES = [u.strip().lstrip("@") for u in os.getenv("FORCE_SUB_USERNAMES", "Mrn_Officialx").split(",") if u.strip()]

# 2) Private / invite-only channels -> use numeric chat IDs like -1001234567890
#    Tip: add the bot to your channel OR simply forward a message from that channel to the bot as admin,
#    then use /id to read the chat.id
FORCE_SUB_CHAT_IDS = [int(x.strip()) for x in os.getenv("FORCE_SUB_CHAT_IDS", "").split(",") if x.strip()]

# 3) Button links to show users (invite links or public links).
#    These links are just for the "Join" buttons UI. Membership check is only possible for USERNAMES/CHAT_IDS.
#    Put all links here (including the two invite links you shared).
FORCE_SUB_LINKS = [x.strip() for x in os.getenv("FORCE_SUB_LINKS",
    "https://t.me/+PArBpI-yLp5hMjQ1,https://t.me/+u6qe756hjylkNmE1,https://t.me/Mrn_Officialx").split(",") if x.strip()]

# Optional: list of admin user IDs who can use /id etc.
ADMINS = [int(x.strip()) for x in os.getenv("ADMINS", "").split(",") if x.strip()]
