from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChatJoinRequestHandler
import logging

# Logging sozlash
logging.basicConfig(level=logging.INFO)

# Bot tokeni
TOKEN = "8477466598:AAGfAxcxlZ2o0SKOQROMw3EyqmsVjXWnHLM"

# ChatJoin so'rovini qayta ishlovchi
async def join_request_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.chat_join_request.from_user.id
    chat_id = update.chat_join_request.chat.id

    # 1. Salomlashuv
    await context.bot.send_message(
        chat_id=user_id,
        text="👋 Assalomu alaykum QARINDOSH!\nSiz kanalda qatnashish uchun so'rov yubordingiz.\nZayavkangiz qabul qilinmoqda!"
    )

    # 2. Video + caption yuborish
    await context.bot.send_video(
        chat_id=user_id,
        video="BAACAgIAAxkBAAMLaJRnvDASPPGq9v6ujXCYU-UTDuwAAjdyAAKuaKFIHA_Ac0_i5NQ2BA",
        caption=(
            "SALOM SALOM QARINDOOSHIM!\n\n"
            "📢 2 kunlik BEPUL darslikda nimalar o‘rgatiladi?\n\n"
            "1) Xitoyning ichki va tashqi marketplace'lari farqlari\n"
            "2) Pinduoduo (ichki marketplace) dan to'g'ri ro'yxatdan o'tish\n"
            "3) Kargo turlari: Avto va Avia kargo farqlari\n"
            "4) Yuanni so'mga qanday qilib to'g'ri hisoblash kerak\n\n"
            "Eslatma:\n"
            "Bu 30 kunlik to‘liq kursning atigi 2 KUNI!\n"
            "Agar darslar sizga yoqsa, qolgan kunlarni to‘lab davom ettirishingiz mumkin.\n\n"
            "✅ 23-24 AVGUST KUNLARI darslar shu yopiq kanalda bo‘ladi:\n"
            "https://t.me/+_Xpi9AEla5hkNjhi"
        )
    )

    # 3. Avtomatik qabul qilish
    await context.bot.approve_chat_join_request(
        chat_id=chat_id,
        user_id=user_id
    )


# Asosiy ishga tushirish
async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(join_request_handler))

    # polling ishga tushirish
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await app.updater.idle()

import asyncio
asyncio.run(main())
