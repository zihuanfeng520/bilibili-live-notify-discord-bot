# Bilibili 開播/下播通知 Discord 機器人

目前使用 [Daki](https://portal.daki.cc/) 免費託管。該程式僅支持單一 Discord 頻道通知和單一直播間監測。`test.js` 支援多頻道通知和多直播間偵測，但未測試過，如有問題請在 Issues 反饋。

## 使用教學

### 1. 註冊 Discord 機器人

1. 前往 [Discord Developer Portal](https://discord.com/developers/applications) 註冊一個 Discord 機器人。
2. 在左側的 **OAuth2** 中勾選以下選項（建議全開），並使用最下方的連結邀請機器人到你的伺服器。
   ![OAuth2 設定](https://github.com/user-attachments/assets/265e74af-725f-46db-bf90-a1cb2342bb79)

### 2. 下載並修改 `index.js` 檔案

1. 修改 `index.js` 中以下代碼：

    ```js
    const token = 'Discord 機器人 token';
    const channelId = '想通知的 Discord 頻道 ID';
    const roomId = '想監測的 Bilibili 直播間 ID';
    ```

   - **Discord 機器人 token**：點擊「Reset Token」獲取，請妥善保存，因為離開頁面後無法再次讀取。 ![Token 獲取](https://github.com/user-attachments/assets/33c92d70-7d41-43a1-a609-eddc676a5538)
   - **Discord 頻道 ID**：啟用 Discord 的開發者模式後，右鍵點擊頻道並選擇「複製 ID」。 ![頻道 ID](https://github.com/user-attachments/assets/a79ee7e9-13ce-413b-bb6e-d8ea88b43703) 
   - **右鍵想讓機器人通知的頻道，最下面就是複製id的選項如下圖**
     
     ![複製 ID](https://github.com/user-attachments/assets/10347246-6098-418b-a7b5-652d06993a78)

- **直播間 ID**：從 `https://live.bilibili.com/XXXXXXX` 中取得 `XXXXXXX`。

2. 修改完成後保存 `index.js` 檔案。

### 3. 邀請機器人到伺服器

1. 在 Discord 開發者平台的 **OAuth2** 中勾選 **bot** 和 **Administrator** 權限，複製生成的連結並在瀏覽器中打開。 ![OAuth2 設定](https://github.com/user-attachments/assets/b999dd5d-1705-4c88-b8f1-cca3c6e9b176)
2. 在瀏覽器中，選擇要邀請機器人的伺服器。 ![選擇伺服器](https://github.com/user-attachments/assets/e54a1f00-fef9-43f4-b338-46750992e58a)

### 4. 註冊 [Daki](https://portal.daki.cc/) https://portal.daki.cc/帳號並託管機器人

1. 註冊時點擊「Forgot Password」，因為該網站沒有註冊按鈕。註冊時會要求用 Discord 登入，完成後可退出該 Discord 群組。
2. 註冊後會獲得一組隨機密碼，建議記下或使用「Forgot Password」來重新獲取。 ![註冊頁面](https://github.com/user-attachments/assets/8d2337a8-878f-48fb-be06-9d1b9f4eb8db)
3. 打開 Dashboard，點擊中間的黑色播放鍵。 ![Dashboard](https://github.com/user-attachments/assets/3cbfe0e5-90d6-4d64-aa6a-0257648daff0)
4. 命名專案後按下底部的 **Deploy**。 ![Deploy](https://github.com/user-attachments/assets/7153236c-0d96-420e-8517-8363ad3bf277)
5. 點擊 **Portal Servers** 下方剛取的名字，登入後選擇「Forgot Password」來顯示並複製密碼。
   
   ![Portal Servers](https://github.com/user-attachments/assets/62d7f314-200d-4eff-a7af-ea9076efad0a)
   
6. 點擊 **Control**，然後 **Files**。 ![Control](https://github.com/user-attachments/assets/da0dc96d-2306-4ada-9ae5-7800f45a26ed) ![Files](https://github.com/user-attachments/assets/6e8485b8-ce7e-455a-ae97-841d8125b16d)
7. 選擇 **Upload** 上傳 `index.js` 和 `package.json`。 ![Upload](https://github.com/user-attachments/assets/900cc8e9-5516-4b10-9fec-18176c2f0e57)
8. 點擊 **Console** 然後 **Start**。 ![Console](https://github.com/user-attachments/assets/326c84ee-8439-4dca-8f91-36589b98cae6)
9. 初次運行會顯示一些代碼，這是正常的。 ![運行](https://github.com/user-attachments/assets/0e81296b-eb98-4392-819e-83a78ee4e875)

   現在你的 Discord 機器人就上線了！ 

   
   效果圖
   
   ![Portal Servers](https://github.com/user-attachments/assets/8c3a4521-ff0f-4b04-b294-731d5305cd3d)

### 5. 使用安卓手機運行機器人

1. 安裝 [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=zh_TW)。
2. 運行以下程式碼：

    ```sh
    pkg update
    pkg upgrade
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

    在文件中貼上以下內容並儲存：

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

    儲存並退出 `nano`：按 `Ctrl + X`，然後 `Ctrl + Y`，再按 `Enter`。

5. 安裝專案依賴：

    ```sh
    npm install
    ```

6. 建立 `bot.js` 檔案：

    ```sh
    nano bot.js
    ```

    貼上你修改好的 `index.js` 內容，儲存並退出 `nano`：按 `Ctrl + X`，然後 `Ctrl + Y`，再按 `Enter`。

7. 運行你的 bot：

    ```sh
    node bot.js
    ```

### 設定自啟動

1. 編輯 `~/.bashrc` 檔案：

    ```sh
    nano ~/.bashrc
    ```

    添加以下內容：

    ```sh
    cd ~/my-bot
    node bot.js &
    ```

    儲存並退出 `nano`：按 `Ctrl + X`，然後 `Ctrl + Y`，再按 `Enter`。

2. 使更改生效：

    ```sh
    source ~/.bashrc
    ```

    下次重啟後，Termux 將會自動運行機器人！

