const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// 健康檢查路徑
app.get('/health', (req, res) => {
  res.status(200).send('OK');
});

// Discord bot 相關程式碼
const { Client, GatewayIntentBits } = require('discord.js');
const ROOM_STATUS = {
  ONLINE: 'ONLINE',
  OFFLINE: 'OFFLINE'
};

const token = process.env.TOKEN;
const channelId = process.env.CHANNEL_ID;
const roomId = process.env.ROOM_ID;

const client = new Client({ intents: [GatewayIntentBits.Guilds] });
let currentStatus = ROOM_STATUS.OFFLINE;

client.once('ready', () => {
  console.log('Discord bot is online!');
  checkLiveStatus();
  setInterval(checkLiveStatus, 60000); // 每分鐘檢查一次
});

async function checkLiveStatus() {
  try {
    const fetch = require('node-fetch');
    const roomLiveInfoUrl = `https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id=${roomId}`;
    const response = await fetch(roomLiveInfoUrl);
    const json = await response.json();

    const { data, code } = json;
    if (code !== 0 || !data) {
      throw new Error('Bili API responded with an error status.');
    }

    const { room_info } = data;
    let status = ROOM_STATUS.OFFLINE;
    if (room_info.live_status === 1) {
      status = ROOM_STATUS.ONLINE;
    }

    if (status !== currentStatus) {
      currentStatus = status; // 更新當前狀態
      const channel = await client.channels.fetch(channelId);

      if (status === ROOM_STATUS.ONLINE) {
        const message = `直播已開始！房間標題：${room_info.title}\n\n房間鏈接：https://live.bilibili.com/${room_info.room_id}\n\n[封面連結](${room_info.cover})`;
        await channel.send(message);
      } else {
        const message = `直播已結束！房間標題：${room_info.title}\n\n房間鏈接：https://live.bilibili.com/${room_info.room_id}\n\n[封面連結](${room_info.cover})`;
        await channel.send(message);
      }
    }
  } catch (error) {
    console.error('Error fetching live room info:', error);
  }
}

client.login(token);

// 啟動 Express 伺服器
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
