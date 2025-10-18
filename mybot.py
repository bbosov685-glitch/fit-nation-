import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command  

# 🔑 Bot tokeningizni shu yerga yozing
API_TOKEN = "7486257227:AAFL2qmvkwNWJQeaWg5AykLzNbTe4rNfzM0"

# Bot va dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# ===================== 📋 30 kunlik rejalar =====================

ozish_plan = {
    1: "📆 *1-kun (Ozish)*\n🏃 2 km yugurish\n🏋️ 20 push-up\n🧘 10 daqiqa stretching",
    2: "📆 *2-kun*\n🚴 15 daqiqa velotrenajyor\n🏋️ 30 squat\n💪 3x20 plank",
    3: "📆 *3-kun*\n🏃 3 km yugurish\n🧘 10 daqiqa stretching\n💦 2L suv ichish",
    4: "📆 *4-kun*\n🏋️ 3x15 burpee\n🏋️ 20 push-up\n🚶 30 daqiqa yurish",
    5: "📆 *5-kun*\n🏋️ 3x20 jump squat\n🏃 15 daqiqa yugurish\n🧘 5 daqiqa meditatsiya",
    6: "📆 *6-kun*\n🚴 20 daqiqa kardio\n🏋️ 3x15 plank\n🏋️ 25 push-up",
    7: "📆 *7-kun*\n😴 Dam olish kuni\n🧘 Engil stretching",
    8: "📆 *8-kun*\n🏃 3 km yugurish\n🏋️ 3x20 squat\n💪 3x15 mountain climbers",
    9: "📆 *9-kun*\n🏋️ 4x10 push-up\n🏋️ 3x15 jumping jacks\n🚶 20 daqiqa yurish",
    10: "📆 *10-kun*\n🚴 25 daqiqa velotrenajyor\n🏋️ 3x20 burpee",
    11: "📆 *11-kun*\n🏋️ 4x15 squat\n💪 3x20 plank\n🧘 10 daqiqa stretching",
    12: "📆 *12-kun*\n🏃 4 km yugurish\n🏋️ 4x10 push-up\n🏋️ 3x15 sit-up",
    13: "📆 *13-kun*\n🚴 30 daqiqa kardio\n🧘 10 daqiqa yoga",
    14: "📆 *14-kun*\n😴 Dam olish kuni\n🚶 15 daqiqa sayr",
    15: "📆 *15-kun*\n🏋️ 3x20 squats\n🏋️ 4x15 burpee\n🏃 15 daqiqa yugurish",
    16: "📆 *16-kun*\n🏋️ 4x10 push-up\n💪 3x20 plank\n🚶 25 daqiqa yurish",
    17: "📆 *17-kun*\n🏋️ 3x20 jump squat\n🏋️ 3x15 mountain climbers",
    18: "📆 *18-kun*\n🚴 20 daqiqa kardio\n🏋️ 4x15 sit-up\n🧘 10 daqiqa yoga",
    19: "📆 *19-kun*\n🏃 4 km yugurish\n💦 2.5L suv ichish\n🍎 Sog‘lom ovqat",
    20: "📆 *20-kun*\n🏋️ 3x20 squat\n🏋️ 4x15 push-up\n🚴 25 daqiqa velotrenajyor",
    21: "📆 *21-kun*\n😴 Dam olish kuni\n🧘 15 daqiqa stretching",
    22: "📆 *22-kun*\n🏃 4 km yugurish\n🏋️ 3x20 burpee\n💪 3x15 plank",
    23: "📆 *23-kun*\n🏋️ 4x15 squat\n🚴 20 daqiqa kardio\n🧘 10 daqiqa yoga",
    24: "📆 *24-kun*\n🏋️ 3x20 push-up\n🏋️ 3x20 sit-up\n🚶 30 daqiqa yurish",
    25: "📆 *25-kun*\n🏋️ 4x15 burpee\n🏋️ 3x15 plank\n💪 3x20 squats",
    26: "📆 *26-kun*\n🚴 25 daqiqa velotrenajyor\n🧘 10 daqiqa stretching",
    27: "📆 *27-kun*\n🏋️ 3x25 push-up\n🏃 3 km yugurish",
    28: "📆 *28-kun*\n😴 Dam olish kuni\n🧘 Engil yoga",
    29: "📆 *29-kun*\n🏋️ 4x20 burpee\n🚴 30 daqiqa kardio",
    30: "📆 *30-kun (Ozish)*\n🔥 Yakuniy sinov:\n🏃 5 km yugurish\n🏋️ 60 push-up\n🏋️ 70 squat\n🧘 15 daqiqa stretching"
}

ves_plan = {
    1: "📆 *1-kun (Ves olish)*\n🏋️ 5x5 bench press\n🏋️ 3x10 squat\n💪 3x10 biceps curl",
    2: "📆 *2-kun*\n🏋️ 5x5 deadlift\n🏋️ 3x12 pull-up\n🏋️ 3x10 military press",
    3: "📆 *3-kun*\n🍗 Kaloriyali ovqat + Dam olish\n🧘 Stretching 10 daqiqa",
    4: "📆 *4-kun*\n🏋️ 4x8 bench press\n🏋️ 4x10 barbell row\n💪 3x12 curls",
    5: "📆 *5-kun*\n🏋️ 4x10 squat\n🏋️ 3x10 lunges\n🍳 Proteinli nonushta",
    6: "📆 *6-kun*\n🏋️ 4x8 deadlift\n🏋️ 3x12 push-up\n🍖 Ko‘proq oqsil iste’moli",
    7: "📆 *7-kun*\n😴 Dam olish kuni\n🧘 Engil stretching",
    8: "📆 *8-kun*\n🏋️ 5x5 bench press\n🏋️ 4x10 biceps curl\n💪 3x12 shoulder press",
    9: "📆 *9-kun*\n🏋️ 4x8 squat\n🏋️ 4x10 triceps dips\n🍚 Guruch + tovuq go‘shti",
    10: "📆 *10-kun*\n🏋️ 5x5 deadlift\n🏋️ 3x10 pull-up\n🧘 10 daqiqa stretching",
    11: "📆 *11-kun*\n🏋️ 4x8 bench press\n🏋️ 3x12 curls\n🍳 Proteinli ovqat",
    12: "📆 *12-kun*\n🏋️ 4x10 squat\n🏋️ 3x12 lunges\n💪 3x15 sit-up",
    13: "📆 *13-kun*\n🚶 20 daqiqa yurish\n🍗 Kaloriyali kechki ovqat",
    14: "📆 *14-kun*\n😴 Dam olish kuni\n🧘 Engil yoga",
    15: "📆 *15-kun*\n🏋️ 5x5 bench press\n🏋️ 4x10 barbell row\n💪 3x10 curls",
    16: "📆 *16-kun*\n🏋️ 4x8 deadlift\n🏋️ 3x12 shoulder press\n🍚 Uglevodli taom",
    17: "📆 *17-kun*\n🏋️ 4x10 squat\n🏋️ 3x10 lunges\n🍖 Tovuq + sabzavot",
    18: "📆 *18-kun*\n🏋️ 5x5 bench press\n🏋️ 4x8 pull-up\n💪 3x12 curls",
    19: "📆 *19-kun*\n🚶 20 daqiqa yurish\n🍳 Ko‘p kaloriyali nonushta",
    20: "📆 *20-kun*\n🏋️ 4x8 deadlift\n🏋️ 3x12 biceps curl\n💪 3x10 military press",
    21: "📆 *21-kun*\n😴 Dam olish kuni\n🧘 Engil stretching",
    22: "📆 *22-kun*\n🏋️ 5x5 bench press\n🏋️ 3x10 barbell row\n🍗 Oqsilga boy taom",
    23: "📆 *23-kun*\n🏋️ 4x10 squat\n🏋️ 3x12 triceps dips\n🍚 Kaloriyali tushlik",
    24: "📆 *24-kun*\n🏋️ 5x5 deadlift\n🏋️ 3x12 pull-up\n🧘 10 daqiqa stretching",
    25: "📆 *25-kun*\n🏋️ 4x10 bench press\n🏋️ 3x12 curls\n🍖 Tovuq + guruch",
    26: "📆 *26-kun*\n🏋️ 4x8 squat\n🏋️ 4x10 shoulder press\n🍗 Kaloriyali ovqat",
    27: "📆 *27-kun*\n🏋️ 4x8 deadlift\n🏋️ 3x12 triceps dips\n🧘 5 daqiqa meditatsiya",
    28: "📆 *28-kun*\n😴 Dam olish kuni\n🧘 Stretching 15 daqiqa",
    29: "📆 *29-kun*\n🏋️ 4x10 squat\n🏋️ 4x10 push-up\n🍳 Proteinli nonushta",
    30: "📆 *30-kun (Ves olish)*\n🔥 Yakuniy sinov:\n🏋️ 5x5 deadlift\n🏋️ 5x5 bench press\n🏋️ 5x5 squat\n🍗 Sog‘lom kaloriyali taom"
}

# ===================== 🚀 Qo‘shimcha bo‘limlar =====================

ozish_food = (
    "🍽 *Ozish uchun ovqatlanish tavsiyalari:*\n\n"
    "• Ertalab: Yorma bo‘tqa, tuxum, yashil choy\n"
    "• Tushlik: Qaynatilgan tovuq, sabzavotlar, grechka\n"
    "• Kechki ovqat: Baliq yoki sabzavotli salat\n"
    "• Har kuni 2–2.5L suv ichish 💧\n"
    "• Shakarli ichimliklardan saqlaning 🚫"
)

ves_food = (
    "🍗 *Ves olish uchun ovqatlanish:*\n\n"
    "• Ertalab: Tuxum + yogurt + non\n"
    "• Tushlik: Guruch + tovuq + sabzavot\n"
    "• Kechki ovqat: Baliq, yong‘oq, sutli mahsulotlar\n"
    "• Har kuni 3–4 marta to‘yimli ovqatlaning 🍚"
)

ozish_tips = (
    "💡 *Ozish bo‘yicha tavsiyalar:*\n\n"
    "✅ Har kuni 7-8 soat uxlang\n"
    "✅ Stressdan uzoq bo‘ling\n"
    "✅ Tez ovqatlanmang — sekin chaynang\n"
    "✅ Harakatni ko‘paytiring (yurish, zinadan chiqish)"
)

ves_tips = (
    "💡 *Ves olish uchun tavsiyalar:*\n\n"
    "✅ Har 3 soatda ovqatlaning\n"
    "✅ Ko‘proq protein iste’mol qiling\n"
    "✅ Mashqdan so‘ng oqsilli taom yeng\n"
    "✅ Yetarlicha uxlang (kamida 8 soat)"
)

ozish_sport = (
    "🏋️ *Ozish uchun mashqlar:*\n\n"
    "- Yugurish (20–30 daqiqa)\n"
    "- Jump squat (3x15)\n"
    "- Burpee (3x10)\n"
    "- Plank (3 daqiqa)\n"
    "- Engil stretching"
)

ves_sport = (
    "🏋️ *Ves olish uchun mashqlar:*\n\n"
    "- Bench press (5x5)\n"
    "- Squat (4x10)\n"
    "- Deadlift (4x8)\n"
    "- Biceps curls (3x12)\n"
    "- Stretching 10 daqiqa"
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
        "ℹ️ *Help bo‘limi:*\n\n"
        "👉 Botdan foydalanish juda oson:\n"
        "- Ozish yoki Ves olishni tanlang.\n"
        "- Kategoriya ichidan Ovqatlanish, Mashqlar yoki Tavsiyalarni ko‘ring.\n"
        "- 30 kunlik rejalardan foydalaning.\n\n"
        "Savollar uchun: @b_islomkhoja"
    )
    await callback.message.answer(text, parse_mode="Markdown")

@dp.callback_query(F.data == "join")
async def join_menu(callback: CallbackQuery):
    await callback.message.answer(
        "📌 Bizning rasmiy kanal: [Fit Nation](https://t.me/fitnationuz)\n"
        "Qo‘shimcha maslahatlar, yangiliklar va motivatsiya uchun bizga qo‘shiling 💪",
        parse_mode="Markdown",
        disable_web_page_preview=True
    )

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
    title = "📉 Ozish bo‘yicha kategoriya tanlang:" if goal == "ozish" else "📈 Ves olish bo‘yicha kategoriya tanlang:"
    await callback.message.answer(title, reply_markup=keyboard)

@dp.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
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
    await callback.message.answer("🔙 Asosiy menyuga qaytdingiz.", reply_markup=keyboard)

# ✅ Ovqatlanish, mashqlar, tavsiyalar funksiyalari
@dp.callback_query(F.data == "ozish_food")
async def ozish_food_menu(callback: CallbackQuery):
    await callback.message.answer(ozish_food, parse_mode="Markdown")

@dp.callback_query(F.data == "ves_food")
async def ves_food_menu(callback: CallbackQuery):
    await callback.message.answer(ves_food, parse_mode="Markdown")

@dp.callback_query(F.data == "ozish_tips")
async def ozish_tips_menu(callback: CallbackQuery):
    await callback.message.answer(ozish_tips, parse_mode="Markdown")

@dp.callback_query(F.data == "ves_tips")
async def ves_tips_menu(callback: CallbackQuery):
    await callback.message.answer(ves_tips, parse_mode="Markdown")

@dp.callback_query(F.data == "ozish_sport")
async def ozish_sport_menu(callback: CallbackQuery):
    await callback.message.answer(ozish_sport, parse_mode="Markdown")

@dp.callback_query(F.data == "ves_sport")
async def ves_sport_menu(callback: CallbackQuery):
    await callback.message.answer(ves_sport, parse_mode="Markdown")

@dp.callback_query(F.data == "ozish_plan")
async def ozish_plan_menu(callback: CallbackQuery):
    plan_text = "\n\n".join([ozish_plan[d] for d in ozish_plan])
    await callback.message.answer(f"📅 *Ozish uchun 30 kunlik reja:*\n\n{plan_text}", parse_mode="Markdown")

@dp.callback_query(F.data == "ves_plan")
async def ves_plan_menu(callback: CallbackQuery):
    plan_text = "\n\n".join([ves_plan[d] for d in ves_plan])
    await callback.message.answer(f"📅 *Ves olish uchun 30 kunlik reja:*\n\n{plan_text}", parse_mode="Markdown")

# ===================== 🚀 Run =====================
async def main():
    print("🤖 Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
