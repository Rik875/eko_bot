import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

color = {"Серый" : "Несортированные отходы",
         "Коричневый" : "Бумага",
         "Синий" : "Пластик",
         "Зеленый" : "Стекло",
         "Черный" : "Пищевые отходы",
         "Желтый" : "Ртутьсодержащие",
         "Оранжевый" : "Элементы питания",
        }

@bot.command()
async def bak(ctx, text_bak):
    if text_bak not in color:
        await ctx.send("Такого цвета нет у меня")
        return
    
    await ctx.send(color[text_bak])

@bot.command()
async def channels(ctx):
    await ctx.send("Вот некоторые каналы про экологию: https://t.me/ecomisli \n https://t.me/recyclemagru \n https://t.me/greenpeaceru")

@bot.command()
async def sites(ctx):
    await ctx.send("Вот несколько сайтов и форумов, посвященных экологии: https://ecoforum.paradigma.center/ \n  https://www.ecosociety.ru/ \n https://wwf.ru/ \n https://greenpeace.ru/")

@bot.command()
async def variant(ctx):
    v = ("не сливать сточные воды без очистки.", "ограничить вырубку лесов.", "борьба с пожарами", "меньше использовать ядохимикаты на полях.", "Регулировать охоту, рыболовство.", "Регулировать охоту, рыболовство.", "перерабатывать металлолом, макулатуру и др. отходы.", "использовать меньше топлива и больше другие источники энергии.", "внедрять новую технику и технологии, менее опасные для природы.")
    await ctx.send(random.choice(v))

bot.run("")
