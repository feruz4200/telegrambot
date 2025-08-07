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
        caption="SALOM SALOM QARINDOOSHIM 👋

📢 2 kunlik BEPUL darslikda nimalar o‘rgatiladi?

1️⃣ 🇨🇳Xitoyning Ichki va tashqi marketplace ning farqi
2️⃣ Pinduoduo (ichki marketplace) dan to’g’ri ro‘yxatdan o‘tish tartibi
3️⃣ Kargo turlari – avto va avia kargoning farqi
4️⃣ Xitoyning Yuannini so‘mga hisoblash usuli

🟡 ESLATMA:
Bu — Xitoydan tovar zakaz qilish bo‘yicha 30 KUNLIK to‘liq darslikning atigi 2 KUNIgina!

📌 DARSLARIMIZ  sizga yoqsa, qolgan darslarni pul to’lab davom  ettirishingiz mumkin.

✅ DARSLAR 23-24 AVGUST KUNLARI  AYNAN MANASHU 👇

👉 https://t.me/+_Xpi9AEla5hkNjhi 👈 YOPIQ  KANALDA  BÒLIB ÒTADI"
    )

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
