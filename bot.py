import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.environ["8868878965:AAEKfxSQc71Su8Q36w-a1rCrIz-vXi6fO44"]

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سڵاو! لینکی ڤیدیۆی TikTok بنێرە."
    )

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = (update.message.text or "").strip()

    if "tiktok.com/" not in url:
        await update.message.reply_text("تکایە لینکی دروستی TikTok بنێرە.")
        return

    await update.message.reply_text(
        "لینکەکەت وەرگیرا. بەشی داگرتنی ڤیدیۆ هێشتا پێویستی بە زیادکردنە."
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
    app.run_polling()

if __name__ == "__main__":
    main()
