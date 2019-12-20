FB文章自動分享社團
=========

`此專案目的只為了學術技術分享，請勿拿來從事不法行為，違者自行負起法律責任`

FB文章自動分享社團，但還是必須要使用一個帳號，來做為機器人使用，切記不要是重要帳號，否則被封鎖。

此專案只能分享貼文型文章，圖片、影片等，還不支援。

<img src="https://i.imgur.com/841nwcA.png"/>

目錄
=================
* [事前必要準備](#事前必要準備)
* [How to Use](#HowtoUse)
   * [變數postURL](#變數postURL)
   * [變數the_finance](#變數the_finance)
   * [變數useEmail](#變數useEmail)
   * [變數usePass](#變數usePass)
   * [變數useId](#變數useId)
* [檔案說明](#檔案說明)
    * [Windows/chromedriver](#Windowschromedriver)
    * [Linux/chromedriver](#Linuxchromedriver)
    * [FB自動發文](#FB自動發文)
 
事前必要準備
=================
1. 必須要下載Chrome
2. 若是在DOS沒有圖形化介面，也必須要下載Chrome。
3. selenium工具的部分，還是要依照自己的OS做調整。
4. [phantomjs檔案過大放不上來，請自行下載。](https://phantomjs.org/download.html)
5. phantomjs下載完以後，請依照作業系統擺放，如下圖。
<img src="https://i.imgur.com/vxk2PXt.png"/>

6. 此檔案是在Windows上面建立的，因此連結的打在Linux等作業系統是需要做調整的，需要將反斜線改成正斜線（39、47行）。
<img src="https://imgur.com/yRRG4i4.png"/>

How to Use
=================

### 變數postURL

想要發的文章網址，為了防止網頁中有多餘的文章，導致分享錯文章，請依照以下方式找到文章絕對網址。

1. 點選文章右上角的選單，選擇`嵌入`，如果沒有就在更多選項裡面。

<img src="https://imgur.com/Ha9s5By.png"/>

2. 選擇進階設定。

<img src="https://imgur.com/tYohPum.png"/>

3. 紅框內即是該文章的完整網址。

<img src="https://imgur.com/HFiXy05.png"/>

### 變數the_finance

此變數用來控制你的社團分類，就以此專案的例子來說，有些文章會發到財金方面的社團，但如果與財金不相關的文章，發到該社團，可能管理員會將您踢出，因此做這樣的分類。

### 變數useEmail

使用者的Email，當然若您的FB有設定電話，也可以用電話登入。

### 變數usePass

使用者的密碼，因此這個檔案小心不要給別人，否則他就知道你的FB登入帳密了。

### 變數useId

在您FB的首頁，即可看到網址如下。該使用者的編號ID，其目的在於程式中，會先到使用者的所有社團，將所有社團的名稱爬下來，因此需要使用者編號ID。

若您找不到，發現您的首頁網址全是英文，代表您有另外申請英文ID，那本爬蟲便無法順利執行，因為社團部分會無法爬取。

<img src="https://imgur.com/GAW5GJi.png"/>

檔案說明
=================

### Windows/chromedriver
Windows系統的chrome模擬器，64位元，若無法執行請自行另外做調整

### Linux/chromedriver
Linux系統的chrome模擬器，64位元，若無法執行請自行另外做調整

### FB自動發文
主程式部分
