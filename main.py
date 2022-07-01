import asyncio
import json
import time
import requests
import threading
import websockets
import discord

rainAmount = 0
contestants = 0

client = discord.Client()

token = "OTkwMzQ3Njk3ODc5OTM3MTU2.GniuCy.rArPBAwUv-8t2VI3b1SuAWHFZtnJFf45sFqQ-o"
guildId = "990347569576181800"
channelId = "990347569576181803"

async def handle_msg(websocket):
    async for message in websocket:

        print(message)

        # Ping message #
        if message == "2":
            await websocket.send("3")

        elif type(msg) is list and msg[0] == "events:rain:updatePotVariables":
            rainAmount = msg[1]["newPrize"]
            contestants = msg[1]["newJoinedPlayersCount"]
        
        elif type(msg) is list and msg[0] == "events:rain:setState":
            if msg[1]["newState"] == "ENDING":
                #data = {"content" : f"Tip rain ending in 2 minutes with {rainAmount} R$ prize pool! \n @everyone","username" : "RblxWild Notifier / hopatio"} 
                data = {"content" : "@everyone","username" : "Rain Pinger RBLXWILD"}
                data["embeds"] = [{"description" : f"Tip rain ending in 2 minutes with {rainAmount} R$ prize pool! \n @everyone","title" : "New Rain !"}]

                result = requests.post("https://discord.com/api/webhooks/992523489116422144/P5LLRzsfoMF8ZQt2L7lAsFfvQLKD1l36TUc3vQMyQDHTBsRsTX_kP9ZCNW8AX4C_wuPO", json = data)
                rainAmount = 0
                contestants = 0

            elif msg[1]["newState"] == "ENDED":
                requests.post("https://discord.com/api/webhooks/992523489116422144/P5LLRzsfoMF8ZQt2L7lAsFfvQLKD1l36TUc3vQMyQDHTBsRsTX_kP9ZCNW8AX4C_wuPO", data={"content" : "","username" : "RblxWild Notifier / hopatio"})
                rainAmount = 0
                contestants = 0

async def async_main(uri):
    async for websocket in websockets.connect(uri):
        try:
            await websocket.send("40")
            time.sleep(3)
            await websocket.send("42"+json.dumps([
                "authentication",
                {
                    "authToken": None,
                    "clientTime": int(time.time())
                }
            ]))

            print("Running now")
            await handle_msg(websocket)
        except websockets.ConnectionClosed:
            continue

    
@client.event
async def on_ready():
    print("Discord bot logged in")

    await async_main("wss://rblxwild.com/socket.io/?EIO=4&transport=websocket")




# Start bot #
client.run(token)
