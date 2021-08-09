import discord
from discord import embeds
from discord.ext import commands
import random
import os
import datetime
time = datetime.datetime.now()

client = discord.Client
bot = commands.Bot(command_prefix = 'su!')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name =f"{bot.command_prefix}help"))
    print(discord.__version__)

class Sussy(commands.Cog):
    def __init__(self):
        self.bot = bot
class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        embed = discord.Embed(
        color=discord.Color.red(), 
        title="**Soviet Union Bot**",
        description="")
        embed.set_footer(
          text=f"gamer"
          )
        embed.set_thumbnail(
          url="https://cdn.discordapp.com/attachments/500716923319877632/872735468335267850/Prof.png"
          )
        for page in self.paginator.pages:
            embed.description += page
        await destination.send(embed=embed)
    no_category = 'Sussy'   

bot.help_command = MyHelpCommand()

#=========================================================
@bot.command()
async def salute(ctx):
    randomlist = []
    for i in range(0, 5):
        n = random.randint(1, 5)
    randomlist.append(n)
    if n == 1:
      await ctx.send('https://cdn.discordapp.com/attachments/500716923319877632/861033255273103390/777f5eb2d37bd010df66f4f49063d27a.png')
    if n == 2: 
      await ctx.send('https://cdn.discordapp.com/attachments/500716923319877632/861034376087601182/British_Army_Soldier_Saluting_MOD_45154893.png')
    if n == 3:
      await ctx.send('https://cdn.discordapp.com/attachments/500716923319877632/861037521882316800/saluting-army-soldier-silhouette-on-white-vector-1889128.png')
    if n == 4:
      await ctx.send('https://cdn.discordapp.com/attachments/500716923319877632/861037693285433354/67805306-saluting-army-soldier-s-silhouette-vector-isolated-on-white-background-memorial-day-veteran.png')
    if n == 5:
      await ctx.send('https://cdn.discordapp.com/attachments/500716923319877632/861038017224114176/soldier-saluting-figure-silhouette-icon-2BRBPB6.png')
      print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================
@bot.command()
async def anthem(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/500716923319877632/861040544100909056/National_Anthem_of_USSR.mp4')
    print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================
@bot.command()
async def worthy(ctx):
    randomlist = []
    for i in range(0, 5):
        n = random.randint(1, 2)
    randomlist.append(n)
    if n == 1:
      await ctx.send('you are worthy')
    if n == 2: 
      await ctx.send('you are not worthy')
    if n == 1:
      await ctx.send('https://cdn.discordapp.com/attachments/500716923319877632/861043631879749652/cool.png')
    if n == 2:
      await ctx.send('https://cdn.discordapp.com/attachments/842090260480655360/861044209514446848/angy.png')
      print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================
@bot.command()
async def manifesto(ctx):
    await ctx.send('https://youtu.be/PdYLRTGmQ3c')
    print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================
@bot.command(aliases=["sussy"])
async def ssy(ctx):
    link = {
                1:('https://cdn.discordapp.com/attachments/741050244116119693/861774982078398514/un_sus.png'),
                2:('https://cdn.discordapp.com/attachments/500741674884923395/861114519266000906/kinda_sus.png'),
            }
    color = {
                1: discord.Color.green(),
                2: discord.Color.red(),
    }
    message= {
                1:"you're not lookin sussy comrade, move along",
                2:"you lookin kinda sussy comrade.."
    }
    rand = random.randint(1, 2)
    embed = discord.Embed(
    title="Ngl...",
    description= message[rand],
    color= color[rand])
    embed.set_image(
      url= (f'{link[rand]}')
    )
    await ctx.send(embed=embed)
    print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================
@bot.command()
async def att(ctx):
    numbers = {
                1:"1",
                2:"2",
                3:"3",
                4:"4",
                5:"5",
                6:"6",
                7:"7",
                8:"8",
                9:"9",
                10:"10"
            }
    strength = random.randint(1, 10)
    endurance = random.randint(1, 10)
    accuracy = random.randint(1, 10)
    loyalty = random.randint(1, 10)
    embed = discord.Embed(
      title="**Attributes**", 
      description=
      f"""strength: {numbers[strength]}/10 
      endurance: {numbers[endurance]}/10
      accuracy: {numbers[accuracy]}/10 
      loyalty: {numbers[loyalty]}/10""", 
      color=discord.Colour.blue())
    embed.set_footer(
      text=f"Requested by {ctx.author}")
    embed.set_thumbnail(
      url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================
@bot.command()
async def rr(ctx):
    color = {
                1: discord.Color.red(),
                2: discord.Color.green(),
                3: discord.Color.green(),
                4: discord.Color.green(),
                5: discord.Color.green(),
                6: discord.Color.green()
    }
    title= {
                1:"Shot!",
                2:"Dud!",
                3:"Dud!",
                4:"Dud!",
                5:"Dud!",
                6:"Dud!"
    }
    description= {
                1:"You lose, pay up.",
                2:"Opponent's turn.",
                3:"Opponent's turn.",
                4:"Opponent's turn.",
                5:"Opponent's turn.",
                6:"Opponent's turn."
    }
    rand = random.randint(1, 6)
    embed = discord.Embed(
    title= title[rand],
    description= description[rand],
    color= color[rand]
    )
    embed.set_footer(
      text=f"Requested by {ctx.author}")
    await ctx.send(embed=embed)
    print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================
@bot.command()
async def invite(ctx):
    await ctx.send('https://discord.com/oauth2/authorize?client_id=861032962387607554&permissions=117760&scope=bot')
    print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================
@bot.command()
async def horny(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/768594140006580267/863983732137394216/video0.mov')
    print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================
@bot.command(aliases=["slots"])
async def slot(ctx):
    list = {
                1:":v:",
                2:":ok_hand:",
                3:":raised_hand:",
            }
    rand1 = random.randint(1, 3)
    rand2 = random.randint(1, 3)
    rand3 = random.randint(1, 3)
    embed = discord.Embed(
      title="Slot Machine", 
      description=f"""{list[rand1]}""" f"""{list[rand2]}""" f"""{list[rand3]}""", 
      color=discord.Colour.blue())
    embed.set_footer(
      text=f"Requested by {ctx.author}")
    await ctx.send(embed=embed)
    print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================
@bot.command(aliases=["sluts"])
async def slut(ctx):
    list = {
                1:":peach:",
                2:":eggplant:",
                3:":sweat_drops:",
            }
    rand1 = random.randint(1, 3)
    rand2 = random.randint(1, 3)
    rand3 = random.randint(1, 3)
    embed = discord.Embed(
      title="Slut Machine", 
      description=f"""{list[rand1]}""" f"""{list[rand2]}""" f"""{list[rand3]}""", 
      color=discord.Colour.purple())
    embed.set_footer(
      text=f"Requested by {ctx.author}")
    await ctx.send(embed=embed)
    print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================
@bot.command()
async def slotimp(ctx):
    list = {
                1:":palms_up_together:",
                2:":open_hands:",
                3:":raised_hands:",
                4:":clap:",
                5:":handshake:",
                6:":thumbsup:",
                7:":thumbsdown:",
                8:":punch:", 
                9:":fist:",
                10:":left_facing_fist:",
                11:":right_facing_fist:",
                12:":fingers_crossed:",
                13:":v:",
                14:":love_you_gesture:",
                15:":metal:",
                16:":ok_hand:",
                17:":pinching_hand:",
                18:":pinched_fingers:",
                19:":point_left:",
                20:":point_right:",
                21:":point_up_2:",
                22:":point_down:",
                23:":point_up:",
                24:":raised_hand:",
                25:":raised_back_of_hand:",
                26:":hand_splayed:",
                27:":vulcan:",
                28:":wave:",
                29:":call_me:",
                30:":middle_finger:",
                31:":pray:"

            }
    rand1 = random.randint(1, 31)
    rand2 = random.randint(1, 31)
    rand3 = random.randint(1, 31)
    embed = discord.Embed(
      title="The Impossible Slot Machine", 
      description=f"""{list[rand1]}""" f"""{list[rand2]}""" f"""{list[rand3]}""", 
      color=discord.Colour.dark_red())
    embed.set_footer(
      text=f"Requested by {ctx.author}")
    await ctx.send(embed=embed)
    print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================
@bot.command()
async def test(ctx):
  embed = discord.Embed(
    title="sussy",
    url="https://youtu.be/dQw4w9WgXcQ",
    description="description",
    color=discord.Colour.blue())
  embed.add_field(
    name="sus", value="the sus", inline=False
    )
  embed.add_field(
    name="sus 2 electric boogaloo", value="gamer", inline=True
    )
  embed.add_field(
    name="this is still kinda sussy", value="ye ig so", inline=True
    )
  embed.set_thumbnail(
    url="https://cdn.discordapp.com/attachments/843145012362608640/870432418769817620/app.png"
    )
  embed.set_footer(
    text=f"Requested by {ctx.author}"
    )
  embed.set_author(
    name=ctx.author.display_name, icon_url=ctx.author.avatar_url
    )
  await ctx.send(embed=embed)
  print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#========================================================= 
@bot.command()
async def ping(ctx):
    link = {
                1:(''),
                2:(''),
                3:(''),
                4:(''),
                5:(''),
                6:(''),
            }
    rand = random.randint(1, 6)
    embed = discord.Embed(
    title="",
    url="",
    description="",
    color=discord.Colour.blue())
    embed.set_thumbnail(
      url= (f'{link[rand]}')
    )
    await ctx.send(embed=embed)
    print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================
@bot.command(aliases=["av"])
async def avatar(ctx):
  embed=discord.Embed(
    title="**Avatar**",
    color=discord.Colour.blurple())
  embed.set_author(
    name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
  embed.set_footer(
    text=f"Requested by {ctx.author}")
  embed.set_image(
    url=ctx.author.avatar_url)
  await ctx.send(embed=embed)
  print(f'-command: "{bot.command_prefix}{ctx.command}" ran by {ctx.author} in the "{ctx.channel}" channel. ({time.strftime("%Y-%m-%d %H:%M")})')
#=========================================================


bot.run(os.environ['Token'])