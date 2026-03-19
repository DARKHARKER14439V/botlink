import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔐 Token from environment
TOKEN = os.getenv("BOT_TOKEN")

# 🌐 Flask app (for Render port)
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)

# 📩 Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\nClick the link below:\n"
        "https://123movienow.cc/spa/videoPlayPage/movies/dhurandhar-2-hindi-cam-4EnNIyrN0G?id=568731759475578184&type=/movie/detail&detailSe=&detailEp=&lang=en"
    )

# 🔗 Custom command
async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📥 Download here:\n"
        "https://123movienow.cc/spa/videoPlayPage/movies/dhurandhar-2-hindi-cam-4EnNIyrN0G?id=568731759475578184&type=/movie/detail&detailSe=&detailEp=&lang=en"
    )

def main():
    # Flask thread start
    threading.Thread(target=run_web).start()

    # Telegram bot
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("link", link))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
