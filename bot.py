import asyncio
import os
import nest_asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes, MessageHandler, filters
)

nest_asyncio.apply()

# --- Bot Token ---
TOKEN = "7886373038:AAHwdjGys_nMyLsFpXaKcUIpjQze8s9glbI"  # Or paste your token directly for local testing

# --- Commands ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "\U0001F680 Welcome to *Space Exploration*! I'm Shiva 🚀\nUse /help to see all available commands.",
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "\U0001FA90 *Available Commands:*\n"
        "/isro - Indian Space Research Organisation\n"
        "/nasa - NASA details\n"
        "/esa - European Space Agency\n"
        "/roscosmos - Russian Space Agency\n"
        "/planets - Facts about planets\n"
        "/stars - Star life cycle\n"
        "/blackholes - Information on black holes\n"
        "/galaxies - Types of galaxies\n"
        parse_mode='Markdown'
    )

async def isro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "\U0001F1EE\U0001F1F3 *ISRO (Indian Space Research Organisation)*\n\n"
        "Founded: 1969\n"
        "HQ: Bengaluru\n"
        "Key Missions:\n"
        "- Aryabhata (1975): First satellite\n"
        "- Chandrayaan-1 & 2: Lunar missions\n"
        "- Mangalyaan: Mars Orbiter\n"
        "- Aditya-L1: Sun observation\n"
        "- Gaganyaan (Upcoming): Crewed mission\n\n"
        "[More Info](https://en.wikipedia.org/wiki/ISRO)",
        parse_mode='Markdown'
    )

async def nasa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "\U0001F1FA\U0001F1F8 *NASA (National Aeronautics and Space Administration)*\n\n"
        "Founded: 1958\n"
        "Key Missions: Apollo, Artemis, Voyager, Hubble, JWST\n"
        "[Visit NASA](https://www.nasa.gov)",
        parse_mode='Markdown'
    )

async def esa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "\U0001F1EA\U0001F1FA *ESA (European Space Agency)*\n\n"
        "Founded: 1975\n"
        "Programs: ExoMars, Gaia, Rosetta\n"
        "[Visit ESA](https://www.esa.int)",
        parse_mode='Markdown'
    )

async def roscosmos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "\U0001F1F7\U0001F1FA *Roscosmos (Russian Space Agency)*\n\n"
        "Founded: 1992\n"
        "Notable Missions: Soyuz, Luna, MIR\n"
        "[Visit Roscosmos](https://www.roscosmos.ru)",
        parse_mode='Markdown'
    )

async def planets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "\U0001FA90 *Planets in the Solar System:*\n\n"
        "- Mercury: Closest to the Sun\n"
        "- Venus: Hottest planet\n"
        "- Earth: Our home\n"
        "- Mars: The Red Planet\n"
        "- Jupiter: Largest gas giant\n"
        "- Saturn: Known for its rings\n"
        "- Uranus: Rotates sideways\n"
        "- Neptune: Windy and deep blue\n\n"
        "[Learn More](https://en.wikipedia.org/wiki/Planet)",
        parse_mode='Markdown'
    )

async def stars(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ *Lifecycle of Stars:*\n\n"
        "- Protostar\n"
        "- Main Sequence\n"
        "- Red Giant / Supergiant\n"
        "- Supernova\n"
        "- White Dwarf / Neutron Star / Black Hole\n\n"
        "[More Info](https://en.wikipedia.org/wiki/Star)",
        parse_mode='Markdown'
    )

async def blackholes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "\U0001F30D *Black Holes:*\n\n"
        "- Event Horizon\n"
        "- Singularity\n"
        "- Accretion Disk\n\n"
        "[Learn More](https://en.wikipedia.org/wiki/Black_hole)",
        parse_mode='Markdown'
    )

async def galaxies(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "\U0001F30C *Types of Galaxies:*\n\n"
        "- Spiral\n"
        "- Elliptical\n"
        "- Irregular\n\n"
        "Famous: Milky Way, Andromeda\n"
        "[Explore More](https://en.wikipedia.org/wiki/Galaxy)",
        parse_mode='Markdown'
    )

# --- Main Function ---
async def main():
    print("🚀 Bot is starting...")
    app = ApplicationBuilder().token(TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("isro", isro))
    app.add_handler(CommandHandler("nasa", nasa))
    app.add_handler(CommandHandler("esa", esa))
    app.add_handler(CommandHandler("roscosmos", roscosmos))
    app.add_handler(CommandHandler("planets", planets))
    app.add_handler(CommandHandler("stars", stars))
    app.add_handler(CommandHandler("blackholes", blackholes))
    app.add_handler(CommandHandler("galaxies", galaxies))

 # Run bot
    await app.run_polling(poll_interval=1.0)

# --- Run Bot ---
if __name__ == "__main__":
    asyncio.run(main())
