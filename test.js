const { Client, GatewayIntentBits } = require('discord.js');

const ROOM_STATUS = {
  ONLINE: 'ONLINE',
  OFFLINE: 'OFFLINE'
};

// Discord bot token and channel IDs
const token = '';
const channelIds = ['', '']; // 假設這是兩個不同的頻道ID
const roomIds = ['', '', '']; // 假設這是三個不同的房間ID

const client = new Client({ intents: [GatewayIntentBits.Guilds] });

let currentStatuses = {};

// 初始化所有房間的狀態為 OFFLINE
roomIds.forEach(roomId => {
  currentStatuses[roomId] = ROOM_STATUS.OFFLINE;
});

client.once('ready', () => {
  console.log('Discord bot is online!');
  checkLiveStatuses();
  setInterval(checkLiveStatuses, 60000); // 每分鐘檢查一次
});

async function checkLiveStatuses() {
  try {
    const fetch = await import('node-fetch').then(mod => mod.default); // 動態加載 node-fetch 模塊

    const checkRoomStatus = async (roomId) => {
      const roomLiveInfoUrl = `https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id=${roomId}`;
      const response = await fetch(roomLiveInfoUrl);
      const json = await response.json();

      const { data, code } = json;
      if (code !== 0 || !data) {
        throw new Error(`Bili API responded with an error status for room ${roomId}.`);
      }

      const { room_info } = data;
      let status = ROOM_STATUS.OFFLINE;
      if (room_info.live_status === 1) {
        status = ROOM_STATUS.ONLINE;
      }

      if (status !== currentStatuses[roomId]) {
        currentStatuses[roomId] = status; // 更新當前狀態

        if (status === ROOM_STATUS.ONLINE) {
          const message = `直播已開始！房間標題：${room_info.title}\n\n房間鏈接：https://live.bilibili.com/${room_info.room_id}\n\n[封面連結](${room_info.cover})`;
          await sendToAllChannels(message);
        } else {
          const message = `直播已結束！房間標題：${room_info.title}\n\n房間鏈接：https://live.bilibili.com/${room_info.room_id}\n\n[封面連結](${room_info.cover})`;
          await sendToAllChannels(message);
        }
      }
    };

    await Promise.all(roomIds.map(checkRoomStatus));
  } catch (error) {
    console.error('Error fetching live room info:', error);
  }
}

async function sendToAllChannels(message) {
  for (const channelId of channelIds) {
    try {
      const channel = await client.channels.fetch(channelId);
      await channel.send(message);
    } catch (error) {
      console.error(`Error sending message to channel ${channelId}:`, error);
    }
  }
}

client.login(token);
