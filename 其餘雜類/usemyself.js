const { Client, GatewayIntentBits } = require('discord.js');
const cron = require('node-cron');

const ROOM_STATUS = {
  ONLINE: 'ONLINE',
  OFFLINE: 'OFFLINE'
};

// Discord bot token and channel ID
const token = '';
const channelId = '';
const roomId = '';

const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent] });

let currentStatus = ROOM_STATUS.OFFLINE;

client.once('ready', () => {
  console.log('Discord 機器人已上線！');
  checkLiveStatus();
  setInterval(checkLiveStatus, 60000); // 每分鐘檢查一次

  // 安排在 GMT+8 時區的每周一、三、五晚上8點發送消息
  cron.schedule('0 20 * * 1,3,5', async () => {
    await sendToChannel('我還在喔');
  }, {
    timezone: 'Asia/Taipei'
  });

  // 安排在 GMT+8 時區的每天晚上10點發送消息
  cron.schedule('00 22 * * *', async () => {
    await sendToChannel('每天晚上十點自檢！');
  }, {
    timezone: 'Asia/Taipei'
  });
});

// 監聽消息事件
client.on('messageCreate', message => {
  if (message.content.toLowerCase().includes('bilibili bot')) {
    message.reply('我還在喔');
  }
});

async function checkLiveStatus() {
  try {
    const fetch = await import('node-fetch').then(mod => mod.default); // 動態加載 node-fetch 模塊
    const roomLiveInfoUrl = `https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id=${roomId}`;
    const response = await fetch(roomLiveInfoUrl);
    const json = await response.json();

    const { data, code } = json;
    if (code !== 0 || !data) {
      throw new Error('房間 ${roomId} 的 Bili API 回應錯誤狀態。');
    }

    const { room_info, anchor_info } = data;
    let status = ROOM_STATUS.OFFLINE;
    if (room_info.live_status === 1) {
      status = ROOM_STATUS.ONLINE;
    }

    if (status !== currentStatus) {
      currentStatus = status; // 更新當前狀態
      const channel = await client.channels.fetch(channelId);

      if (status === ROOM_STATUS.ONLINE) {
        const message = `---------------------------------------------------------\n(${anchor_info.base_info.uname})的直播已開始！\n\n房間標題：${room_info.title}\n\n房間鏈接：https://live.bilibili.com/${room_info.room_id}\n\n[封面連結](${room_info.cover})\n---------------------------------------------------------`;
        await channel.send(message);
      } else {
        const message = `---------------------------------------------------------\n(${anchor_info.base_info.uname})的直播已結束！\n\n房間標題：${room_info.title}\n\n房間鏈接：https://live.bilibili.com/${room_info.room_id}\n\n[封面連結](${room_info.cover})\n---------------------------------------------------------`;
        await channel.send(message);
      }
    }
  } catch (error) {
    console.error('錯誤：獲取直播房間信息時出現錯誤。', error);
  }
}

async function sendToChannel(message) {
  try {
    const channel = await client.channels.fetch(channelId);
    await channel.send(message);
  } catch (error) {
      console.error(`錯誤：向頻道 ${channelId} 發送消息時出現錯誤。`, error);
  }
}

client.login(token);
