from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔐 PASTE YOUR *NEW* BOTFATHER TOKEN BETWEEN THE QUOTES
token = 8262841351:AAFQB_zXKXaliVw8dlQNS1DNPZAhPW36RAU

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Your Telegram bot is now LIVE and working!")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Type /start to test the bot.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
