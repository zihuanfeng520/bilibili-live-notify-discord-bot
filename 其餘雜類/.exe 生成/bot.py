import discord
import aiohttp
import asyncio
from discord.ext import tasks
from datetime import datetime

# Discord bot token 和頻道 ID
TOKEN = ''
CHANNEL_ID =   # 確保這是一个整數
ROOM_ID = ''

# 創建 Discord 客戶端實例
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # 確保啟用了消息內容權限
client = discord.Client(intents=intents)

current_status = 'OFFLINE'

@client.event
async def on_ready():
    print('Discord bot is online!')
    await check_live_status()
    check_live_status.start()  # 啟動定時任務

    # 啟動任務調度
    schedule_messages.start()

@client.event
async def on_message(message):
    # 確保不回應自己的消息
    if message.author == client.user:
        return
    
    # 打印所有收到的消息
    print(f"Received message: {message.content}")

    # 檢查消息內容是否包含關鍵字
    if 'bilibili bot' in message.content.lower():
        await message.channel.send('我還在喔!')

@tasks.loop(minutes=1)
async def check_live_status():
    global current_status
    try:
        async with aiohttp.ClientSession() as session:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            room_live_info_url = f'https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id={ROOM_ID}'
            async with session.get(room_live_info_url, headers=headers) as response:
                if response.content_type == 'application/json':
                    json_data = await response.json()
                else:
                    raise Exception(f'Unexpected content type: {response.content_type}')
        
        data = json_data.get('data')
        if json_data.get('code') != 0 or not data:
            raise Exception(f'Bili API response error for room {ROOM_ID}.')

        room_info = data['room_info']
        anchor_info = data['anchor_info']

        status = 'OFFLINE'
        live_status = room_info.get('live_status')
        if live_status == 1:
            status = 'ONLINE'
        elif live_status == 2:
            status = 'OFFLINE'  # 或者根據實際需要調整為其他狀態

        if status != current_status:
            current_status = status
            channel = client.get_channel(CHANNEL_ID)
            if status == 'ONLINE':
                message = (f'---------------------------------------------------\n'
                           f'({anchor_info["base_info"]["uname"]})的直播已開始！\n\n'
                           f'房間標題：{room_info["title"]}\n\n'
                           f'房間連結：https://live.bilibili.com/{room_info["room_id"]}\n\n'
                           f'[封面連結]({room_info["cover"]})\n'
                           f'---------------------------------------------------')
            else:
                message = (f'---------------------------------------------------\n'
                           f'({anchor_info["base_info"]["uname"]})的直播已結束！\n\n'
                           f'房間標題：{room_info["title"]}\n\n'
                           f'房間連結：https://live.bilibili.com/{room_info["room_id"]}\n\n'
                           f'[封面連結]({room_info["cover"]})\n'
                           f'---------------------------------------------------')
            await channel.send(message)
    except Exception as e:
        error_message = f'{get_current_timestamp()} 錯誤：獲取直播房間信息時出現錯誤。'
        print(error_message, e)
        await send_error_log(error_message, e)

@tasks.loop(seconds=30)  # 每 30 秒檢查一次調度消息
async def schedule_messages():
    now = datetime.now()
    if now.weekday() in [0, 2, 4] and now.hour == 20 and now.minute == 0:  # 周一、三、五的晚上8點
        await send_to_channel('hanser直播前測試!')
    if now.hour == 10 and now.minute == 0:  # 每天早上10點
        await send_to_channel('每天早上十點自檢！')
    if now.hour == 22 and now.minute == 0:  # 每天晚上10點
        await send_to_channel('每天晚上十點自檢！')

async def send_to_channel(message):
    try:
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(message)
    except Exception as e:
        error_message = f'{get_current_timestamp()} 錯誤：向頻道 {CHANNEL_ID} 發送消息時出現錯誤。'
        print(error_message, e)
        await send_error_log(error_message, e)

async def send_error_log(message, error):
    try:
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(f'{message}\n```{error}```')
    except Exception as send_error:
        print('錯誤：向頻道發送錯誤日誌時出現錯誤。', send_error)

def get_current_timestamp():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

client.run(TOKEN)

