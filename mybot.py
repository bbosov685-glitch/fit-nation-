import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

# 🔑 Bot token
API_TOKEN = "7486257227:AAFL2qmvkwNWJQeaWg5AykLzNbTe4rNfzM0"

# Bot va dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# ===================== 📋 30 kunlik rejalar =====================

ozish_plan = {
    1: "Day 1 (Ozish):\n🏃 2 km yugurish\n🏋️ 20 push-up\n🧘 10 daqiqa stretching",
    2: "Day 2:\n🚴 15 daqiqa velotrenajyor\n🏋️ 30 squat\n💪 3x20 plank",
    3: "Day 3:\n🏃 3 km yugurish\n🧘 10 daqiqa stretching\n💦 Suv ichish 2L",
    4: "Day 4:\n🏋️ 3x15 burpee\n🏋️ 20 push-up\n🚶 30 daqiqa yurish",
    5: "Day 5:\n🏋️ 3x20 jump squat\n🏃 15 daqiqa yugurish\n🧘 5 daqiqa meditatsiya",
    6: "Day 6:\n🚴 20 daqiqa kardio\n🏋️ 3x15 plank\n🏋️ 25 push-up",
    7: "Day 7:\n😴 Dam olish kuni\n🧘 Engil stretching",
    8: "Day 8:\n🏃 3 km yugurish\n🏋️ 3x20 squat\n💪 3x15 mountain climbers",
    9: "Day 9:\n🏋️ 4x10 push-up\n🏋️ 3x15 jumping jacks\n🚶 20 daqiqa yurish",
    10: "Day 10:\n🚴 25 daqiqa velotrenajyor\n🏋️ 3x20 burpee",
    11: "Day 11:\n🏋️ 4x15 squat\n💪 3x20 plank\n🧘 10 daqiqa stretching",
    12: "Day 12:\n🏃 4 km yugurish\n🏋️ 4x10 push-up\n🏋️ 3x15 sit-up",
    13: "Day 13:\n🚴 30 daqiqa kardio\n🧘 10 daqiqa yoga",
    14: "Day 14:\n😴 Dam olish kuni\n🚶 15 daqiqa sayr",
    15: "Day 15:\n🏋️ 3x20 squats\n🏋️ 4x15 burpee\n🏃 15 daqiqa yugurish",
    16: "Day 16:\n🏋️ 4x10 push-up\n💪 3x20 plank\n🚶 25 daqiqa yurish",
    17: "Day 17:\n🏋️ 3x20 jump squat\n🏋️ 3x15 mountain climbers",
    18: "Day 18:\n🚴 20 daqiqa kardio\n🏋️ 4x15 sit-up\n🧘 10 daqiqa yoga",
    19: "Day 19:\n🏃 4 km yugurish\n💦 Suv 2.5L\n🍎 Sog‘lom ovqat",
    20: "Day 20:\n🏋️ 3x20 squat\n🏋️ 4x15 push-up\n🚴 25 daqiqa velotrenajyor",
    21: "Day 21:\n😴 Dam olish kuni\n🧘 15 daqiqa stretching",
    22: "Day 22:\n🏃 4 km yugurish\n🏋️ 3x20 burpee\n💪 3x15 plank",
    23: "Day 23:\n🏋️ 4x15 squat\n🚴 20 daqiqa kardio\n🧘 10 daqiqa yoga",
    24: "Day 24:\n🏋️ 3x20 push-up\n🏋️ 3x20 sit-up\n🚶 30 daqiqa yurish",
    25: "Day 25:\n🏋️ 4x15 burpee\n🏋️ 3x15 plank\n💪 3x20 squats",
    26: "Day 26:\n🚴 25 daqiqa velotrenajyor\n🧘 10 daqiqa stretching",
    27: "Day 27:\n🏋️ 3x25 push-up\n🏃 3 km yugurish",
    28: "Day 28:\n😴 Dam olish kuni\n🧘 Engil yoga",
    29: "Day 29:\n🏋️ 4x20 burpee\n🚴 30 daqiqa kardio",
    30: "Day 30 (Ozish):\n🔥 Yakuniy sinov:\n🏃 5 km yugurish\n🏋️ 60 push-up\n🏋️ 70 squat\n🧘 15 daqiqa stretching"
}

ves_plan = {
    1: "Day 1 (Ves olish):\n🏋️ 5x5 bench press\n🏋️ 3x10 squat\n💪 3x10 biceps curl",
    2: "Day 2:\n🏋️ 5x5 deadlift\n🏋️ 3x12 pull-up\n🏋️ 3x10 military press",
    3: "Day 3:\n🍗 Kaloriyali ovqat + Dam olish\n🧘 Stretching 10 daqiqa",
    4: "Day 4:\n🏋️ 4x8 bench press\n🏋️ 4x10 barbell row\n💪 3x12 curls",
    5: "Day 5:\n🏋️ 4x10 squat\n🏋️ 3x10 lunges\n🍳 Proteinli nonushta",
    6: "Day 6:\n🏋️ 4x8 deadlift\n🏋️ 3x12 push-up\n🍖 Ko‘proq oqsil iste’moli",
    7: "Day 7:\n😴 Dam olish kuni\n🧘 Engil stretching",
    8: "Day 8:\n🏋️ 5x5 bench press\n🏋️ 4x10 biceps curl\n💪 3x12 shoulder press",
    9: "Day 9:\n🏋️ 4x8 squat\n🏋️ 4x10 triceps dips\n🍚 Guruch + tovuq go‘shti",
    10: "Day 10:\n🏋️ 5x5 deadlift\n🏋️ 3x10 pull-up\n🧘 10 daqiqa stretching",
    11: "Day 11:\n🏋️ 4x8 bench press\n🏋️ 3x12 curls\n🍳 Proteinli ovqat",
    12: "Day 12:\n🏋️ 4x10 squat\n🏋️ 3x12 lunges\n💪 3x15 sit-up",
    13: "Day 13:\n🚶 20 daqiqa yurish\n🍗 Kaloriyali kechki ovqat",
    14: "Day 14:\n😴 Dam olish kuni\n🧘 Engil yoga",
    15: "Day 15:\n🏋️ 5x5 bench press\n🏋️ 4x10 barbell row\n💪 3x10 curls",
    16: "Day 16:\n🏋️ 4x8 deadlift\n🏋️ 3x12 shoulder press\n🍚 Uglevodli taom",
    17: "Day 17:\n🏋️ 4x10 squat\n🏋️ 3x10 lunges\n🍖 Tovuq + sabzavot",
    18: "Day 18:\n🏋️ 5x5 bench press\n🏋️ 4x8 pull-up\n💪 3x12 curls",
    19: "Day 19:\n🚶 20 daqiqa yurish\n🍳 Ko‘p kaloriyali nonushta",
    20: "Day 20:\n🏋️ 4x8 deadlift\n🏋️ 3x12 biceps curl\n💪 3x10 military press",
    21: "Day 21:\n😴 Dam olish kuni\n🧘 Engil stretching",
    22: "Day 22:\n🏋️ 5x5 bench press\n🏋️ 3x10 barbell row\n🍗 Oqsilga boy taom",
    23: "Day 23:\n🏋️ 4x10 squat\n🏋️ 3x12 triceps dips\n🍚 Kaloriyali tushlik",
    24: "Day 24:\n🏋️ 5x5 deadlift\n🏋️ 3x12 pull-up\n🧘 10 daqiqa stretching",
    25: "Day 25:\n🏋️ 4x10 bench press\n🏋️ 3x12 curls\n🍖 Tovuq + guruch",
    26: "Day 26:\n🏋️ 4x8 squat\n🏋️ 4x10 shoulder press\n🍗 Kaloriyali ovqat",
    27: "Day 27:\n🏋️ 4x8 deadlift\n🏋️ 3x12 triceps dips\n🧘 5 daqiqa meditatsiya",
    28: "Day 28:\n😴 Dam olish kuni\n🧘 Stretching 15 daqiqa",
    29: "Day 29:\n🏋️ 4x10 squat\n🏋️ 4x10 push-up\n🍳 Proteinli nonushta",
    30: "Day 30 (Ves olish):\n🔥 Yakuniy sinov:\n🏋️ 5x5 deadlift\n🏋️ 5x5 bench press\n🏋️ 5x5 squat\n🍗 Sog‘lom kaloriyali taom"
}

# ===================== 🍽 Ovqatlanish bo‘limi =====================

ozish_food = (
    "🥗 *Ozish uchun ovqatlanish bo‘limi:*\n\n"
    "🍳 Nonushta: 2 dona tuxum, sabzavot, qora non\n"
    "🍗 Tushlik: tovuq go‘shti, salat, limonli suv\n"
    "🥦 Kechki ovqat: baliq yoki sabzavotli taom\n"
    "💧 Har kuni kamida 2L suv iching\n"
    "🚫 Shakar, non va fastfoodni cheklang"
)

ves_food = (
    "🍛 *Ves olish uchun ovqatlanish bo‘limi:*\n\n"
    "🍳 Nonushta: tuxum, yong‘oq, sutli bo‘tqa\n"
    "🍗 Tushlik: guruch + tovuq yoki mol go‘shti\n"
    "🍞 Kechki ovqat: kartoshka pyuresi + baliq\n"
    "🥤 Oraliq: banan, yogurt, yeryong‘oq moyi\n"
    "💪 Har kuni 5 mahal ovqatlaning va suv iching"
)

# ===================== 💡 Tavsiyalar bo‘limi =====================

ozish_tips = (
    "💡 *Ozish uchun tavsiyalar:*\n\n"
    "1️⃣ Har kuni ertalab 15 daqiqa yuguring\n"
    "2️⃣ Har 3 soatda yengil ovqatlaning\n"
    "3️⃣ 7–8 soat uxlashga e’tibor bering\n"
    "4️⃣ Fastfood, shakar va gazli ichimliklardan saqlaning\n"
    "5️⃣ Kunda kamida 2L suv iching"
)

ves_tips = (
    "💡 *Ves olish uchun tavsiyalar:*\n\n"
    "1️⃣ Katta porsiyada ovqatlaning\n"
    "2️⃣ Oqsil va uglevodli taomlar ko‘proq iste’mol qiling\n"
    "3️⃣ Har kuni 7–8 soat uxlash\n"
    "4️⃣ Mashqdan so‘ng proteinli ichimlik iching\n"
    "5️⃣ Stressdan saqlaning va sabrli bo‘ling 💪"
)

# ===================== 🚀 Commands =====================

@dp.message(Command("start"))
async def start_command(message: Message):
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Ozish 📉", callback_data="ozish"),
            types.InlineKeyboardButton(text="Ves olish 📈", callback_data="ves")
        ],
        [
            types.InlineKeyboardButton(text="ℹ️ Help", callback_data="help"),
            types.InlineKeyboardButton(text="📌 Join", callback_data="join")
        ]
    ])
    await message.answer("👋 Salom! Fit Nation botga xush kelibsiz!\n\nMaqsadingizni tanlang:", reply_markup=keyboard)

@dp.callback_query(F.data == "help")
async def help_menu(callback: CallbackQuery):
    text = (
        "ℹ️ *Yordam bo‘limi:*\n\n"
        "👉 Botdan foydalanish uchun quyidagilarni bajaring:\n"
        "- Ozish yoki Ves olish bo‘limini tanlang.\n"
        "- Ovqatlanish, Mashqlar yoki Tavsiyalarni tanlang.\n"
        "- 30 kunlik rejalar bilan mashg‘ulotni boshlang.\n\n"
        "❓ Savol va yordam uchun 👉 [@b_islomkhoja](https://t.me/b_islomkhoja)"
    )
    await callback.message.answer(text, parse_mode="Markdown", disable_web_page_preview=True)

@dp.callback_query(F.data == "join")
async def join_menu(callback: CallbackQuery):
    text = (
        "📌 Bizning rasmiy kanalimizga qo‘shiling:\n"
        "👉 [Fit Nation Kanal](https://t.me/fitnationuz)\n\n"
        "Bu yerda qo‘shimcha maslahatlar, sport yangiliklari va motivatsiya postlari bo‘ladi!"
    )
    await callback.message.answer(text, parse_mode="Markdown", disable_web_page_preview=True)

@dp.callback_query(F.data.in_(["ozish", "ves"]))
async def process_goal(callback: CallbackQuery):
    goal = callback.data
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="🍽 Ovqatlanish", callback_data=f"{goal}_food"),
            types.InlineKeyboardButton(text="🏋️ Mashqlar", callback_data=f"{goal}_sport"),
            types.InlineKeyboardButton(text="ℹ️ Tavsiyalar", callback_data=f"{goal}_tips")
        ],
        [types.InlineKeyboardButton(text="📅 30 kunlik reja", callback_data=f"{goal}_plan")],
        [types.InlineKeyboardButton(text="🔙 Orqaga", callback_data="back")]
    ])
    await callback.message.answer(
        "📋 Kategoriya tanlang:" if goal == "ozish" else "📈 Ves olish bo‘yicha kategoriya:",
        reply_markup=keyboard
    )

@dp.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    await start_command(callback.message)

# ===================== 📅 Rejalar =====================
@dp.callback_query(F.data == "ozish_plan")
async def ozish_plan_menu(callback: CallbackQuery):
    plan_text = "\n\n".join([ozish_plan[d] for d in ozish_plan])
    await callback.message.answer(f"📅 *Ozish uchun 30 kunlik reja:*\n\n{plan_text}", parse_mode="Markdown")

@dp.callback_query(F.data == "ves_plan")
async def ves_plan_menu(callback: CallbackQuery):
    plan_text = "\n\n".join([ves_plan[d] for d in ves_plan])
    await callback.message.answer(f"📅 *Ves olish uchun 30 kunlik reja:*\n\n{plan_text}", parse_mode="Markdown")

# ===================== 🍽 Ovqatlanish callbacklari =====================
@dp.callback_query(F.data == "ozish_food")
async def ozish_food_menu(callback: CallbackQuery):
    await callback.message.answer(ozish_food, parse_mode="Markdown")

@dp.callback_query(F.data == "ves_food")
async def ves_food_menu(callback: CallbackQuery):
    await callback.message.answer(ves_food, parse_mode="Markdown")

# ===================== 💡 Tavsiyalar callbacklari =====================
@dp.callback_query(F.data == "ozish_tips")
async def ozish_tips_menu(callback: CallbackQuery):
    await callback.message.answer(ozish_tips, parse_mode="Markdown")

@dp.callback_query(F.data == "ves_tips")
async def ves_tips_menu(callback: CallbackQuery):
    await callback.message.answer(ves_tips, parse_mode="Markdown")

# ===================== 🚀 Run =====================
# ===================== ⏰ Mashg‘ulot eslatmasi =====================

from datetime import datetime, timedelta

user_reminders = {}  # foydalanuvchi ID va vaqtni saqlaydi

@dp.message(Command("eslatma"))
async def set_reminder_command(message: Message):
    await message.answer(
        "⏰ Mashg‘ulot eslatmasini o‘rnatish uchun vaqtni kiriting (masalan: 18:30)\n\n"
        "Namuna: `18:00` yoki `07:45`", parse_mode="Markdown"
    )

@dp.message(F.text.regexp(r"^\d{1,2}:\d{2}$"))
async def save_reminder_time(message: Message):
    user_id = message.from_user.id
    time_str = message.text.strip()
    try:
        hour, minute = map(int, time_str.split(":"))
        now = datetime.now()
        remind_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if remind_time < now:
            remind_time += timedelta(days=1)  # ertangi kunga o‘tadi

        user_reminders[user_id] = remind_time
        await message.answer(f"✅ Eslatma o‘rnatildi: {time_str}\nBot sizga o‘sha vaqtda eslatadi ⏰")
    except Exception:
        await message.answer("❌ Noto‘g‘ri format. Masalan, 18:00 deb yozing.")

async def reminder_checker():
    while True:
        now = datetime.now().replace(second=0, microsecond=0)
        for user_id, remind_time in list(user_reminders.items()):
            if now == remind_time:
                await bot.send_message(user_id, "⏰ Mashg‘ulot vaqti keldi! Harakatga tushamiz 💪")
                user_reminders[user_id] = remind_time + timedelta(days=1)  # keyingi kunga o‘tadi
        await asyncio.sleep(30)
async def main():
    print("🤖 Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())  