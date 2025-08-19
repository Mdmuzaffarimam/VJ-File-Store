
# VJ File Store — Multi Force Subscribe (Deploy Ready)

This package adds **Multi Force Subscribe** to your bot. Users must join all required channels before using the bot.

> ⚠️ Telegram bots cannot verify private invite links directly. To *enforce* membership for private channels, you must provide their **numeric chat IDs** (like `-1001234567890`). Use `/id` helper below.

---

## Features
- Multi-channel Force Subscribe
- Hindi + English lock message
- Join buttons for each channel (invite links or public links)
- "✅ Try Again" callback
- Render / Railway deploy-ready

---

## Quick Start (Local)
1. Create a bot and get `BOT_TOKEN` from @BotFather.
2. Get `API_ID` and `API_HASH` from https://my.telegram.org/apps
3. Install deps:
   ```bash
   pip install -r requirements.txt
   ```
4. Export env vars (example):
   ```bash
   export API_ID=123456
   export API_HASH=xxxxxx
   export BOT_TOKEN=1234:abcd
   export FORCE_SUB_USERNAMES="Mrn_Officialx"
   export FORCE_SUB_CHAT_IDS="-1001234567890,-1002222222222"   # for private channels (optional)
   export FORCE_SUB_LINKS="https://t.me/+PArBpI-yLp5hMjQ1,https://t.me/+u6qe756hjylkNmE1,https://t.me/Mrn_Officialx"
   ```
5. Run:
   ```bash
   python app.py
   ```

---

## Getting Chat IDs for Private Channels
- Add the bot to your channel (no posting rights needed) **or**
- Forward any message from that channel to the bot (as an admin), then send `/id` replying to that forwarded message.
- The bot will show: `title` and `id`. Put that `id` in `FORCE_SUB_CHAT_IDS`.

> If you do not provide chat IDs, the bot will **show join buttons** for invite links but **cannot verify membership** for those links.

---

## Deploy to Render
- Create a new **Worker** service.
- Point to this repo/ZIP; Render will read `render.yaml`.
- Set the following Environment Variables on Render dashboard:
  - `API_ID`, `API_HASH`, `BOT_TOKEN`
  - `FORCE_SUB_USERNAMES` (comma-separated, e.g. `Mrn_Officialx`)
  - `FORCE_SUB_CHAT_IDS` (comma-separated numeric IDs for private channels, optional but recommended)
  - `FORCE_SUB_LINKS` (all your join/invite links; used for buttons)

## Deploy to Railway
- Create a new project from this ZIP/repo.
- Add variables in Project Settings → Variables:
  - `API_ID`, `API_HASH`, `BOT_TOKEN`
  - `FORCE_SUB_USERNAMES`
  - `FORCE_SUB_CHAT_IDS`
  - `FORCE_SUB_LINKS`
- Railway uses `Procfile` → `worker: python app.py`

---

## Notes
- Replace the placeholder media handler in `app.py` with your actual file-store logic.
- You can keep your own repository structure and just copy `force_subscribe.py` and the checking logic into your handlers.

Happy shipping! 🚀
