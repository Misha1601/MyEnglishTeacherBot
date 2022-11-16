from main import dp, bot
from app.generator import Generate
from app.translate import Translate

async def play(message: types.Message):
    word = Generate().offer()
    word_translate = Translate(word=word).perevod()
    mes = await message.answer(f"{word}\n"
                                f"||{word_translate}||",
                                parse_mode='MarkdownV2',
                                reply_markup=buttons_answer())
    mes1 = await message.answer(f"В любом обучении главное практика на постоянной основе!",
                                   reply_markup=buttons_no_menu())
    await message.delete()
    await del_old_messege(mes)
    await save_info_messege(mes)
    await save_info_messege(mes1)
    await statistics(message=mes, quest=True)