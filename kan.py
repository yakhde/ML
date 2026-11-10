import asyncio
import math
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

# --- SOZLAMALAR ---
API_TOKEN = '8539329523:AAFaq9AkiJBtIFejvNCu3IPDChHm26uslt0'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# --- BOSQICHLARNI ANIQLASH (FSM) ---
class CalcState(StatesGroup):
    waiting_for_num1 = State()
    waiting_for_operation = State()
    waiting_for_num2 = State()

# --- START BUYRUG'I ---
@dp.message(Command("start"))
async def start_cmd(message: types.Message, state: FSMContext):
    await state.set_state(CalcState.waiting_for_num1)
    await message.answer("🤖 **Kalkulyator botga xush kelibsiz!**\n\nBirinchi sonni kiriting:")

# --- BEKOR QILISH BUYRUG'I ---
@dp.message(Command("cancel"))
async def cancel_cmd(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("❌ Amaliyot bekor qilindi. Qaytadan boshlash uchun /start bosing.")

# Birinchi sonni qabul qilish
@dp.message(CalcState.waiting_for_num1)
async def process_num1(message: types.Message, state: FSMContext):
    try:
        num1 = float(message.text)
        await state.update_data(num1=num1)
        
        await state.set_state(CalcState.waiting_for_operation)
        await message.answer(
            "Amalni tanlang yoki yozing:\n"
            "➕ `+` , ➖ `-` , ✖️ `*` , ➗ `/` , 📊 `%` , 📐 `ildiz`\n\n"
            "*(Agar amalingiz 'ildiz' bo'lsa, ikkinchi son shart emas)*",
            parse_mode="Markdown"
        )
    except ValueError:
        await message.answer("⚠️ Iltimos, faqat son kiriting!")

# Amalni qabul qilish
@dp.message(CalcState.waiting_for_operation)
async def process_operation(message: types.Message, state: FSMContext):
    operation = message.text.strip().lower()
    valid_ops = ["+", "-", "*", "/", "%", "ildiz"]

    if operation not in valid_ops:
        await message.answer("⚠️ Noma'lum amal! Iltimos, ulardan birini kiriting: +, -, *, /, %, ildiz")
        return

    await state.update_data(operation=operation)

    # Agar amal ildiz bo'lsa, ikkinchi sonni so'rab o'tirmaymiz
    if operation == "ildiz":
        data = await state.get_data()
        a = data['num1']
        if a >= 0:
            res = f"√{a} = {math.sqrt(a)}"
        else:
            res = "Manfiy sondan ildiz chiqarib bo'lmaydi!"
        
        await message.answer(f"✅ Natija: {res}\n\nYangi hisob-kitob uchun birinchi sonni kiriting:")
        await state.set_state(CalcState.waiting_for_num1)
    else:
        await state.set_state(CalcState.waiting_for_num2)
        await message.answer("Ikkinchi sonni kiriting:")

# 3-BOSQICH: Ikkinchi sonni qabul qilish va hisoblash
@dp.message(CalcState.waiting_for_num2)
async def process_num2(message: types.Message, state: FSMContext):
    try:
        num2 = float(message.text)
        data = await state.get_data()
        a = data['num1']
        op = data['operation']
        result = None

        if op == "+":
            result = a + num2
        elif op == "-":
            result = a - num2
        elif op == "*":
            result = a * num2
        elif op == "/":
            result = a / num2 if num2 != 0 else "Nolga bo'lish xatosi!"
        elif op == "%":
            result = (a * num2) / 100

        await message.answer(f"✅ Natija: {result}\n\nYangi hisob-kitob uchun birinchi sonni kiriting:")
        
        # Ketma-ket davom etish uchun yana 1-bosqichga qaytaramiz
        await state.set_state(CalcState.waiting_for_num1)

    except ValueError:
        await message.answer("⚠️ Iltimos, faqat son kiriting!")

# --- BOTNI ISHGA TUSHIRISH ---
async def main():
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())