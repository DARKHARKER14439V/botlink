from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔑 Paste your bot token here
TOKEN = "8653995384:AAEA9FHpi7viL-TMqy7KiGQZ1PslvKuZH4M"

# 📩 Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\nClick the link below:\n"
        "https://123movienow.cc/spa/videoPlayPage/movies/dhurandhar-2-hindi-cam-4EnNIyrN0G?id=568731759475578184&type=/movie/detail&detailSe=&detailEp=&lang=en"
    )

# 🔗 Custom command (/link)
async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📥 Download here:\n"
        "https://123movienow.cc/spa/videoPlayPage/movies/dhurandhar-2-hindi-cam-4EnNIyrN0G?id=568731759475578184&type=/movie/detail&detailSe=&detailEp=&lang=en"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("link", link))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()