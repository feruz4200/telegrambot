from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes
import logging

logging.basicConfig(level=logging.INFO)

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    join_request = update.chat_join_request
    user_id = join_request.from_user.id

    await context.bot.send_message(
        chat_id=user_id,
        text="👋 Assalomu alaykum! QARINDOSH \nSiz kanalga qo‘shilish uchun so‘rov yubordingiz.\nZayavkangiz qabul qilinyapti!"
    )

    await context.bot.approve_chat_join_request(
        chat_id=join_request.chat.id,
        user_id=user_id
    )

async def main():
    application = ApplicationBuilder().token("8477466598:AAGfAxcxlZ2o0SKOQROMw3EyqmsVjXWnHLM").build()
    application.add_handler(ChatJoinRequestHandler(handle_join_request))
    print("✅ Bot ishga tushdi")
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
