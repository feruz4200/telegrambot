from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes
import logging

logging.basicConfig(level=logging.INFO)

# --- Join request function ---
async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    join_request = update.chat_join_request
    user_id = join_request.from_user.id
    chat_id = join_request.chat.id

    # 1. Salomlashuv xabari
    await context.bot.send_message(
        chat_id=user_id,
        text="👋 Assalomu alaykum! QARINDOSH\nSiz kanalga qo‘shilish uchun so‘rov yubordingiz.\nZayavkangiz qabul qilinmoqda!"
    )

    # 2. Video yuborish (file_id orqali)
    await context.bot.send_video(
        chat_id=user_id,
        video="BAACAgIAAxkBAAMLaJRnvDASPPGq9v6ujXCYU-UTDuwAAjdyAAKuaKFIHA_Ac0_i5NQ2BA",
        caption = (
    "SALOM SALOM QARINDOOSHIM!\n\n"
    "📢 2 kunlik BEPUL darslikda nimalar o‘rgatiladi?\n\n"
    "1) Xitoyning ichki va tashqi marketplace'lari farqlari\n"
    "2) Pinduoduo (ichki marketplace) dan to'g'ri ro'yxatdan o'tish\n"
    "3) Kargo turlari: Avto va Avia kargo farqlari\n"
    "4) Yuanni so'mga qanday qilib to'g'ri hisoblash kerak\n\n"
    "Eslatma:\n"
    "Bu 30 kunlik to‘liq kursning atigi 2 KUNI!\n"
    "Agar darslar sizga yoqsa, qolgan kunlarni to‘lab davom ettirishingiz mumkin.\n\n"
    "✅ 23-24 AVGUST KUNLARI darslar aynan mana shu yopiq kanalda bo‘ladi:\n"
    " https://t.me/+_Xpi9AEla5hkNjhi "
)    )

    # 3. Zayavkani avtomatik qabul qilish
    await context.bot.approve_chat_join_request(
        chat_id=chat_id,
        user_id=user_id
    )

# --- Asosiy ishga tushirish funksiyasi ---
async def main():
    application = ApplicationBuilder().token("8477466598:AAGfAxcxlZ2o0SKOQROMw3EyqmsVjXWnHLM").build()
    application.add_handler(ChatJoinRequestHandler(handle_join_request))
    print("✅ Bot ishga tushdi!")
    await application.run_polling()

# --- Run ---
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
