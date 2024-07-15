# Bilibili開播/下播通知Discord機器人
目前使用 [https://portal.daki.cc/](https://portal.daki.cc/) 免費託管。該程式目前僅支持單一discord頻道通知 與 單一直播間進行監測

## 使用教學事項

## 1.註冊Discord機器人
請先用[https://discord.com/developers/applications](https://discord.com/developers/applications)  註冊一個Discord機器人，並把權限全開（我沒研究哪些權限用的到所以我全開）  
![image](https://github.com/user-attachments/assets/e9c5eef4-8c95-497f-aa23-4fbb6570e825)

## 2.下載並修改index檔案
請在index檔案裡把9~11行const程式後的''裡面依序改成自己需要的內容

const token = 'discord機器人token';

const channelId = '想通知的discord頻道id';

const roomId = '想監測的bilibili直播間id'; 

◉1.discord機器人token按下reset後會顯示(請保存好，離開頁面後就不可再讀取，除非reset過)

![image](https://github.com/user-attachments/assets/33c92d70-7d41-43a1-a609-eddc676a5538)
  
◉2.discord頻道id 可在discord設定裡的進階選項開啟開發者模式後

![image](https://github.com/user-attachments/assets/a79ee7e9-13ce-413b-bb6e-d8ea88b43703)

◉右鍵想讓機器人通知的頻道，最下面就是複製id的選項如下圖

![image](https://github.com/user-attachments/assets/10347246-6098-418b-a7b5-652d06993a78)

◉3.的直播間id為https://live.bilibili.com/XXXXXXX中的XXXXXXX

◉修改完後保存index.js檔案

## 3.註冊 並託管https://portal.daki.cc/ 帳號
◉如果是第一次註冊直接按下面的forgot password，因為這個網站沒有註冊按鈕
(註冊時會要求discord登入，綁定後就可以退出該discord群組)

◉註冊完後會分一組隨機不可改的密碼給你，我是都直接forgot password啦，因為他每次都會隨機分配
![image](https://github.com/user-attachments/assets/8d2337a8-878f-48fb-be06-9d1b9f4eb8db)

註冊完後打開dashboard，點擊中間的黑色撥放鍵
![image](https://github.com/user-attachments/assets/3cbfe0e5-90d6-4d64-aa6a-0257648daff0)


◉取好名字後按下底部的Deploy
![image](https://github.com/user-attachments/assets/7153236c-0d96-420e-8517-8363ad3bf277)


然後我們就創好了!

![image](https://github.com/user-attachments/assets/62d7f314-200d-4eff-a7af-ea9076efad0a)


◉點擊Portal Servers下方的剛剛取好的名字(這步大概率會要你再登入一次，直接按下方的forgot password，會引導到密碼的地方，按下show後複製就好了)

◉按下Control
![image](https://github.com/user-attachments/assets/da0dc96d-2306-4ada-9ae5-7800f45a26ed)

◉點擊上方的Files
![image](https://github.com/user-attachments/assets/6e8485b8-ce7e-455a-ae97-841d8125b16d)

◉選擇upload
![image](https://github.com/user-attachments/assets/900cc8e9-5516-4b10-9fec-18176c2f0e57)

◉選擇剛剛的index.js 跟 package.json上傳

◉然後按下Console後，在按下Start
![image](https://github.com/user-attachments/assets/326c84ee-8439-4dca-8f91-36589b98cae6)

然後專屬於你的discord機器人就上線啦!!!
