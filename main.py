import argparse
import threading
import asyncio
import discord
from discord.ext import commands

Client = discord.Client()

parser = argparse.ArgumentParser(description="Disconnect anyone from a private call using a Discord invite Link.")
parser.add_argument('-userid', type=int, help='The Snowflake ID of the person who you would like to disconnect.')
parser.add_argument('-all', action='store_true', help="Do this to everyone, in where if anyone clicks the Invite link, they are disconnected from active call.")
parser.add_argument('-token', type=str, help='Token of bot as found in the Discord Developer Portal')

args = parser.parse_args()

@Client.event
async def on_connect():
    await Client.wait_until_ready()
    print("Connected with")

@Client.event
async def on_message(message):
    if args.all is not None:
        await message.author.kick()
        print("> Successfully kicked " + str(message.author))
    else:
        if message.author.id == args.userid:
            try:
                await message.author.kick()
                print("> Successfully kicked " + str(message.author))
            except:
                print("ERR> Most likely due to having insufficient permissions to kick, did you set your join link Permissions level to 8?")
        elif message.author.bot:
            return



if args.userid and args.token != "" or args.all is not None:
    if args.userid and args.all != "":
        print("ERR> You cannot provide two opposing arguments (-all & -userid)")
    else:
        try:
            Client.run(args.token)
        except:
            print("ERR> Invalid/Insufficient Token Supplied")
else:
    parser.print_help()

