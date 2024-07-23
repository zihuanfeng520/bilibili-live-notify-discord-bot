# Bilibili開播/下播通知Discord機器人
目前使用 [https://portal.daki.cc/](https://portal.daki.cc/) 免費託管。該程式目前僅支持單一discord頻道通知 與 單一直播間進行監測(test.js可以多頻道通知及多直播間同時偵測，但我用不到所以沒測試，說不定有bug，如果遇到可以反饋在Issues)

## 使用教學事項

## 1.註冊Discord機器人
◉請先用[https://discord.com/developers/applications](https://discord.com/developers/applications)  註冊一個Discord機器人，在左側的OAuth2中勾選下面兩個選項（我沒研究哪些權限用的到所以我全開），最下方的連結可以邀請機器人到你想要通知的伺服器
![image](https://github.com/user-attachments/assets/265e74af-725f-46db-bf90-a1cb2342bb79)



## 2.下載並修改index檔案
◉請把index檔案裡9~11行const程式後的''裡面依序改成自己需要的內容

const token = 'Discord機器人token';

const channelId = '想通知的Discord頻道id';

const roomId = '想監測的bilibili直播間id'; 


◉1.Discord機器人token獲取需要按下reset token後顯示(請保存好，離開頁面後就不可再讀取，除非再次reset過)
![image](https://github.com/user-attachments/assets/33c92d70-7d41-43a1-a609-eddc676a5538)

◉2.Discord頻道id 可在Discord設定裡的進階選項開啟開發者模式後
![image](https://github.com/user-attachments/assets/a79ee7e9-13ce-413b-bb6e-d8ea88b43703)

◉右鍵想讓機器人通知的頻道，最下面就是複製id的選項如下圖

![image](https://github.com/user-attachments/assets/10347246-6098-418b-a7b5-652d06993a78)

◉3.的直播間id為https://live.bilibili.com/XXXXXXX中的XXXXXXX

◉修改完後保存index.js檔案

## 3.邀請機器人到伺服器
請在剛剛創建機器人的網址中，於左側找到OAuth2選項，照圖中勾選bot 以及下方的Administrator，複製下方產生的連結，用瀏覽器打開
![image](https://github.com/user-attachments/assets/b999dd5d-1705-4c88-b8f1-cca3c6e9b176)

瀏覽器打開後應該如下圖，可以選擇想要機器人通知的伺服器
![image](https://github.com/user-attachments/assets/e54a1f00-fef9-43f4-b338-46750992e58a)

## 4.註冊 https://portal.daki.cc/ 帳號並託管機器人

◉如果是第一次註冊直接按下面的forgot password，因為這個網站沒有註冊按鈕
(註冊時會要求Discord登入，綁定後完成下面設定就可以退出該Discord群組)

◉註冊完後會分一組隨機不可改的密碼給你，我是都直接forgot password啦，因為他每次都會隨機分配
![image](https://github.com/user-attachments/assets/8d2337a8-878f-48fb-be06-9d1b9f4eb8db)

◉註冊完後打開Dashboard，點擊中間的黑色撥放鍵
![image](https://github.com/user-attachments/assets/3cbfe0e5-90d6-4d64-aa6a-0257648daff0)

◉取好名字後按下底部的Deploy
![image](https://github.com/user-attachments/assets/7153236c-0d96-420e-8517-8363ad3bf277)

◉點擊Portal Servers下方剛取好的名字(這步會要你再登入一次，直接按下方的forgot password，會引導到密碼的地方，按下show後複製)

![image](https://github.com/user-attachments/assets/62d7f314-200d-4eff-a7af-ea9076efad0a)

◉按下Control
![image](https://github.com/user-attachments/assets/da0dc96d-2306-4ada-9ae5-7800f45a26ed)

◉點擊上方的Files
![image](https://github.com/user-attachments/assets/6e8485b8-ce7e-455a-ae97-841d8125b16d)

◉選擇Upload
![image](https://github.com/user-attachments/assets/900cc8e9-5516-4b10-9fec-18176c2f0e57)

◉選擇剛剛的index.js 跟 package.json上傳

◉然後按下Console後，在按下Start
![image](https://github.com/user-attachments/assets/326c84ee-8439-4dca-8f91-36589b98cae6)

◉初次運行會跑一些代碼是正常的
![image](https://github.com/user-attachments/assets/0e81296b-eb98-4392-819e-83a78ee4e875)

◉然後專屬於你的discord機器人就上線啦!!!

◉效果圖

![image](https://github.com/user-attachments/assets/8c3a4521-ff0f-4b04-b294-731d5305cd3d)

## 5.使用安卓手機運行機器人

◉1.安装 Termux [Google Play 連結](https://play.google.com/store/apps/details?id=com.termux&hl=zh_TW)

◉2.運行以下程式碼
1. 更新並升級 Termux 套件：
 ```sh
 pkg update
 pkg upgrade
 ```

2. 安裝 Node.js：
 ```sh
 pkg install nodejs
 ```

3. 建立專案目錄並進入：
 ```sh
 mkdir my-bot
 cd my-bot
 ```

4. 建立 `package.json` 檔案：
 ```sh
 nano package.json
 ```
 然後貼上以下內容並儲存：

 ```json
 {
 "name": "nodejs",
 "version": "1.0.0",
 "description": "",
 "main": "index.js",
 "scripts": {
 "test": "echo \"Error: no test specified\" && exit 1"
 },
 "keywords": [],
 "author": "",
 "license": "ISC",
 "dependencies": {
 "@types/node": "^18.0.6",
 "discord.js": "^14.15.3",
 "node-fetch": "^3.3.2",
 "node-cron": "^3.0.0"
 }
 }
 ```

 儲存並退出 nano：按 `Ctrl + X`，然後按 `Ctrl + Y`，再按 `Enter`。
 
![image](https://github.com/user-attachments/assets/c38bec4a-0c31-45ba-8063-18d1e531b08c)

5. 安裝專案依賴：
 ```sh
 npm install
 ```

6. 建立 `bot.js` 檔案：
 ```sh
 nano bot.js
 ```
 在這裡貼上你修改好的 `index.js` 內容，並儲存：
 儲存並退出 nano：按 `Ctrl + X`，然後按 `Ctrl + Y`，再按 `Enter`。

7. 運行你的 bot：
 ```sh
 node bot.js
 ```

### 設定自啟動

1. 編輯 `~/.bashrc` 檔案：
 ```sh
 nano ~/.bashrc
 ```
 然後在文件末尾添加以下內容：

 ```sh
 cd ~/my-bot
 node bot.js &
 ```

 儲存並退出 `nano`：按 `Ctrl + X`，然後按 `Ctrl + Y`，再按 `Enter`。

2. 使更改生效：
 ```sh
 source ~/.bashrc
 ```
這樣下次重開機後開啟termux就會自動運行機器人啦!
