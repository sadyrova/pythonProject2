from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет!")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton('Площадь квадрата', callback_data='math_start'))
    await message.answer("text", reply_markup=markup)


@dp.message_handler(commands=['mem'])
async def mem_command(message: types.Message):
    await bot.send_photo(admin_id, types.InputFile('C:\Users\user\PycharmProjects\Project_27-01'))



@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "Какой национальный цветок Японии?"
    answer = [
        "Фиалка",
        "Роза",
        "Сакура",
        "Сирень",

    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Какая валюта Дании??"
    answer = [
        "Тенге",
        "Сум",
        "Крона",
        "Лир",

    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
    )

@dp.message_handler()
async def echo(message: types.Message):
    if message.text == "python":
        await message.answer("I love it!")
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"Саламалекум хозяин {message.from_user.full_name}"
        )
        await message.answer(f"This is an answer method! {message.message_id}")
        await message.reply("This is a reply method!")

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)