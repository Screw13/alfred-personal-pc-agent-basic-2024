import discord
from discord.ext import commands
import subprocess
from dotenv import load_dotenv
import os
import webbrowser
import psutil
import pyautogui as pp
import time

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

PREFIX = '.'

intents = discord.Intents.default()


bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready(ctx):
    print(f'We have logged in as {bot.user}')

@bot.command(name='valo')
async def open_program(ctx):
    try:
        pp.hotkey('super',"d")
        time.sleep(2)
        valo = pp.locateOnScreen("valo.png")
        if valo == None:
            await ctx.send("couldnt run")
            time.sleep(1)
        else:
            pp.click(valo)
            pp.click(valo)

        await ctx.send('Program opened successfully!')
    except Exception as e:
        await ctx.send(f'Error opening program: {e}')

@bot.command(name='mc')
async def open_program(ctx):
    try:
        pp.hotkey('super',"d")
        time.sleep(2)
        mc = pp.locateOnScreen("mc.png")
        if mc == None:
            await ctx.send("couldnt run")
            time.sleep(1)
        else:
            pp.click(mc)
            pp.click(mc)
            time.sleep(20)
            pp.click(pp.locateOnScreen("mc2.png"))

        await ctx.send('Program opened successfully!')
    except Exception as e:
        await ctx.send(f'Error opening program: {e}')


@bot.command(name='search')
async def search(ctx, *, query):
    try:
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open_new_tab(search_url)
        await ctx.send(f'Searching for "{query}"...')
    except Exception as e:
        await ctx.send(f'Error performing search: {e}')


@bot.command(name='shutdown', hidden=True)
async def shutdown(ctx):
    # Check if the command issuer is the bot owner (you)
        await ctx.send('Shutting down...')
        os.system('shutdown /s /t 1')  # Shutdown the computer

@bot.command(name='restart', hidden=True)
async def restart(ctx):
        await ctx.send('Restarting...')
        os.system('shutdown /r /t 1')  # Restart the computer

@bot.command(name='sleep', hidden=True)
async def lock(ctx):
        await ctx.send('Locking your PC...')
        os.system('rundll32.exe user32.dll,LockWorkStation')


@bot.command(name='close')
async def close_program(ctx, *, program_name):
    try:
        # Convert program name to lowercase for case-insensitive comparison
        program_name = program_name.lower()
        
        # Check if the program is running
        program_found = False
        for proc in psutil.process_iter(['pid', 'name']):
            if program_name in proc.info['name'].lower():
                program_found = True
                proc.terminate()
                await ctx.send(f'{proc.info["name"]} closed successfully!')
        
        if not program_found:
            await ctx.send(f'No running program found with name "{program_name}"')
            
    except Exception as e:
        await ctx.send(f'Error closing program: {e}')

@bot.command(name='tm')
async def open_program(ctx):
    subprocess.call("C:\\WINDOWS\\system32\\Taskmgr.exe")
    await ctx.send('Program opened successfully!')
bot.run(TOKEN)
