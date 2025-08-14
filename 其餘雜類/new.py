import discord
import aiohttp
import asyncio
from discord.ext import tasks
from datetime import datetime
import json

TOKEN = ''
CHANNEL_ID = 
USER_ID = ''
ROOM_ID = '255'

# Create Discord client instance - 兼容 discord.py 1.7.3 並嘗試新版本功能
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.guild_messages = True

# 嘗試啟用 message_content intent（僅在新版本中可用）
try:
    intents.message_content = True  # Enable the message_content intent
    print("Message content intent enabled")
except AttributeError:
    print("Message content intent not available in this Discord.py version")

client = discord.Client(intents=intents)

current_status = 'OFFLINE'

@client.event
async def on_ready():
    print('Discord bot is online!')
    print(f'Bot user: {client.user}')
    print(f'Monitoring channel: {CHANNEL_ID}')
    check_live_status.start()
    schedule_messages.start()

@client.event
async def on_message(message):
    # 確保不回應自己的消息
    if message.author == client.user:
        return
    
    # 打印更詳細的消息信息用於除錯
    print(f"Received message: '{message.content}' from {message.author} in channel {message.channel.id}")
    print(f"Message length: {len(message.content)}")
    print(f"Message type: {type(message.content)}")
    
    # 檢查消息是否為空
    if not message.content:
        print("Warning: Empty message received")
        return
    
    # 整合兩種關鍵字檢測方式
    message_lower = message.content.lower()
    
    # 第一份代碼的簡潔檢測
    if 'bilibili bot' in message_lower:
        await message.channel.send(f'<@{USER_ID}> 我還在喔!')
        print("Reply sent via simple detection!")
    # 添加更多關鍵字作為備選
    elif any(keyword in message_lower for keyword in ['bot', 'ping', '測試', '機器人']):
        await message.channel.send(f'<@{USER_ID}> I am still here! 我還在這裡！')
        print("Reply sent via backup detection!")
    

@tasks.loop(minutes=1)
async def check_live_status():
    global current_status
    try:
        async with aiohttp.ClientSession() as session:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            room_live_info_url = f'https://api.live.bilibili.com/xlive/web-room/v1/index/getRoomBaseInfo?room_ids={ROOM_ID}&req_biz=video'
            
            async with session.get(room_live_info_url, headers=headers) as response:
                if response.content_type == 'application/json':
                    json_data = await response.json()
                else:
                    raise Exception(f'Unexpected content type: {response.content_type}')
        
        data = json_data.get('data')
        if json_data.get('code') != 0 or not data:
            raise Exception(f'Bili API response error for room {ROOM_ID}.')

        by_room_ids = data.get('by_room_ids', {})
        if not by_room_ids:
            raise Exception('No room data found')
        
        room_info = list(by_room_ids.values())[0]
        
        status = 'OFFLINE'
        live_status = room_info.get('live_status')
        if live_status == 1:
            status = 'ONLINE'
        elif live_status == 2:
            status = 'OFFLINE'

        if status != current_status:
            current_status = status
            channel = client.get_channel(CHANNEL_ID)
            if channel is None:
                print(f'Error: Cannot find channel with ID {CHANNEL_ID}')
                return
                
            username = room_info.get("uname", "Unknown")
            room_title = room_info.get("title", "Unknown")
            room_link = room_info.get("live_url", f'https://live.bilibili.com/{ROOM_ID}')
            cover_link = room_info.get("cover", "")
            
            if status == 'ONLINE':
                message = (f'---------------------------------------------------\n'
                           f'<@{USER_ID}>\n\n'
                           f'({username})的直播已開始！\n\n'
                           f'房間標題：{room_title}\n\n'
                           f'房間連結：{room_link}\n\n'
                           f'[封面連結]({cover_link})\n'
                           f'---------------------------------------------------')
            else:
                message = (f'---------------------------------------------------\n'
                           f'<@{USER_ID}>\n\n'
                           f'({username})的直播已結束！\n\n'
                           f'房間標題：{room_title}\n\n'
                           f'房間連結：{room_link}\n\n'
                           f'[封面連結]({cover_link})\n'
                           f'---------------------------------------------------')
            await channel.send(message)
            
    except Exception as e:
        error_message = f'{get_current_timestamp()} 錯誤：獲取直播房間信息時出現錯誤。'
        print(error_message, e)
        # 添加從第一份代碼的錯誤處理
        await send_error_log(error_message, e)

@tasks.loop(minutes=1)
async def schedule_messages():
    now = datetime.now()
    if now.weekday() in [0, 2, 4] and now.hour == 20 and now.minute == 0:
        await send_to_channel(f'hanser直播前測試!')
    if now.hour == 10 and now.minute == 0:
        await send_to_channel(f'每天早上十點自檢！')
    if now.hour == 22 and now.minute == 0:
        await send_to_channel(f'每天晚上十點自檢！')

async def send_to_channel(message):
    try:
        channel = client.get_channel(CHANNEL_ID)
        if channel is None:
            print(f'Error: Cannot find channel with ID {CHANNEL_ID}')
            return
        await channel.send(message)
    except Exception as e:
        print(f'Error sending to channel: {e}')
        # 添加從第一份代碼的錯誤處理
        error_message = f'{get_current_timestamp()} 錯誤：向頻道 {CHANNEL_ID} 發送消息時出現錯誤。'
        await send_error_log(error_message, e)

# 添加從第一份代碼的錯誤日誌功能
async def send_error_log(message, error):
    try:
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(f'{message}\n```{error}```')
    except Exception as send_error:
        print('錯誤：向頻道發送錯誤日誌時出現錯誤。', send_error)

def get_current_timestamp():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    try:
        client.run(TOKEN)
    except Exception as e:
        print(f'Bot startup error: {e}')