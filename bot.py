import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import nest_asyncio

nest_asyncio.apply()

TOKEN = "7886373038:AAHwdjGys_nMyLsFpXaKcUIpjQze8s9glbI"# Use environment variable

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Welcome to *Space Exploration*! I'm Shiva.\nUse /help to see commands.", parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🪐 Available Commands:\n/start - Welcome message\n/help - This help guide", parse_mode='Markdown')

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
