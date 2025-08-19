
import asyncio
from typing import List
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_ID, API_HASH, BOT_TOKEN, FORCE_SUB_LINKS, ADMINS
from force_subscribe import check_user_subscriptions

app = Client("vj_file_store_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def build_force_sub_keyboard() -> InlineKeyboardMarkup:
    rows = []
    # Make a row per link
    for idx, link in enumerate(FORCE_SUB_LINKS, start=1):
        rows.append([InlineKeyboardButton(f"📢 Join Channel {idx}", url=link)])
    rows.append([InlineKeyboardButton("✅ Try Again", callback_data="check_subscribe")])
    return InlineKeyboardMarkup(rows)

FORCE_SUB_MESSAGE = (
    "🔒 *Access Locked*
"
    "Bot use karne se pehle neeche diye gaye sabhi channels join karna *zaroori* hai.

"
    "🔹 *Join all channels, then press* _Try Again_

"
    "— Hindi + English —
"
    "Please join *all* the required channels below to unlock the bot.
"
)

@app.on_message(filters.private & filters.command("start"))
async def start_handler(client, message):
    missing_usernames, missing_chat_ids = await check_user_subscriptions(client, message.from_user.id)

    if missing_usernames or missing_chat_ids:
        await message.reply_text(
            FORCE_SUB_MESSAGE,
            reply_markup=build_force_sub_keyboard(),
            disable_web_page_preview=True
        )
        return

    await message.reply_text("🎉 *Welcome!* Aap ab bot use kar sakte ho.
Send any file to store it.", quote=True)

# Simple /id helper to fetch chat/user IDs for configuration
@app.on_message(filters.private & filters.command("id"))
async def id_handler(client, message):
    uid = message.from_user.id
    text_lines = [f"👤 Your ID: `{uid}`"]
    if message.reply_to_message and message.reply_to_message.forward_from_chat:
        chat = message.reply_to_message.forward_from_chat
        text_lines.append(f"🔎 Forwarded chat info -> title: *{chat.title}*, id: `{chat.id}`")
    await message.reply_text("\n".join(text_lines))

@app.on_callback_query(filters.regex(r"^check_subscribe$"))
async def recheck_callback(client, callback_query):
    user_id = callback_query.from_user.id
    missing_usernames, missing_chat_ids = await check_user_subscriptions(client, user_id)
    if missing_usernames or missing_chat_ids:
        await callback_query.answer("Still locked. Please join all channels.", show_alert=True)
        try:
            await callback_query.message.edit_text(
                FORCE_SUB_MESSAGE, reply_markup=build_force_sub_keyboard(),
                disable_web_page_preview=True
            )
        except Exception:
            pass
    else:
        await callback_query.answer("Unlocked! 🎉", show_alert=True)
        await callback_query.message.edit_text("🎉 *Unlocked!* You can now use the bot.")

# Minimal echo to keep the bot functional for now (you can replace with file-store logic)
@app.on_message(filters.private & filters.media)
async def receive_media(client, message):
    # Placeholder for your file-store logic; we just acknowledge
    await message.reply_text("✅ File received. (Demo placeholder — integrate with your file store logic.)")

if __name__ == "__main__":
    app.run()
