# test.js使用細項

## 各程式解釋

## 1.下載test.js
請編輯圖中這個地方，依序在''中放入 discord機器人token/想要通知的頻道(請先確保機器人有在該伺服器中)/想要偵測的bilibili直播間 
![image](https://github.com/user-attachments/assets/69b2bfec-c92a-44b4-bf0a-0e89580e03a0)

## 2.設定XX標準時間機器人會自動通知(我還在喔)確保託管並未斷線
![image](https://github.com/user-attachments/assets/b450c31a-c58e-4140-a06b-1748ff104e84)

想改時區則把 timezone: 'Asia/Taipei' 後的 'Asia/Taipei'改為你想要的時區
想改每天通知自檢時間則是把 cron.schedule('0 22 * * *', async () => { 改成 ('分鐘 小時 * * *', async () => {
(如果不需要可以刪掉這兩段)

## 3.手動確認機器人是否正常運作
我用的判斷句是在頻道內輸入bilibili bot，如果機器人正常運作則會回覆(我還在喔)，可以自己修改判斷句以及回覆句
![image](https://github.com/user-attachments/assets/840d3ce9-c3de-4980-b1e7-cddac80b192e)

## 4.效果圖
![image](https://github.com/user-attachments/assets/85152dcc-e167-4628-aa19-4144984e7d80)
