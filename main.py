import os
from decouple import config
from inst import download_video_from_inst_by_url
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = config("SECRET_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привіт! Відправ мені посилання на відео з інсти, а я відправлю тобі це відео😊")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_text = update.message.text
    if "https://www.instagram.com/" in user_text:
        download_video_from_inst_by_url(user_text)
        file_name = "your_vid.mp4"
    
        if os.path.isfile(file_name):
            await update.message.reply_document(document=open(file_name, "rb"))
            os.remove(file_name)
            print(f"{file_name} has been sent and deleted.")
        else:
            await update.message.reply_text("Невірне посилання🥺\nСпробуй знову😉")
    else:
        await update.message.reply_text("Невірне посилання🥺\nСпробуй знову😉")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()