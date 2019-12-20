FB文章自動分享社團
=========

`此專案目的只為了學術技術分享，請勿拿來從事不法行為，違者自行負起法律責任`

FB文章自動分享社團，但還是必須要使用一個帳號，來做為機器人使用，切記不要是重要帳號，否則被封鎖。

此專案只能分享貼文型文章，圖片、影片等，還不支援。

<img src="https://i.imgur.com/841nwcA.png"/>

目錄
=================
* [事前必要準備](#事前必要準備)
* [變數說明](#變數說明)
   * [變數postURL](#變數postURL)
   * [變數useEmail](#變數useEmail)
   * [變數usePass](#變數usePass)
   * [變數useId](#變數useId)
* [Function說明](#Function說明)
* [範例](#範例)
    * [參數準備](#參數準備)
    * [chromedriver啟動](#chromedriver啟動)
    * [文章分享](#文章分享)
    * [圖片分享](#圖片分享)
    * [影片分享](#影片分享)
* [檔案說明](#檔案說明)
    * [Windows/chromedriver.exe](#Windowschromedriverexe)
    * [Windows/phantomjs.exe](#Windowsphantomjsexe)
    * [Linux/chromedriver](#Linuxchromedriver)
    * [Linux/phantomjs](#Linuxphantomjs)
    * [FB自動發文.py](#FB自動發文py)
    * [facebook_tool.py](#facebook_toolpy)
 
事前必要準備
=================
1. 必須要下載Chrome
2. 若是在DOS沒有圖形化介面，也必須要下載Chrome。
3. selenium工具的部分，還是要依照自己的OS做調整。
4. [phantomjs檔案過大放不上來，請自行下載。](https://phantomjs.org/download.html)
5. phantomjs下載完以後，請依照作業系統擺放，如下圖。
<img src="https://i.imgur.com/vxk2PXt.png"/>


變數說明
=================

### 變數postURL

想要發的文章網址，為了防止網頁中有多餘的文章，導致分享錯文章，請依照以下方式找到文章絕對網址。

1. 點選文章右上角的選單，選擇`嵌入`，如果沒有就在更多選項裡面。

<img src="https://imgur.com/Ha9s5By.png"/>

2. 選擇進階設定。

<img src="https://imgur.com/tYohPum.png"/>

3. 紅框內即是該文章的完整網址。

<img src="https://imgur.com/HFiXy05.png"/>

### 變數useEmail

使用者的Email，當然若您的FB有設定電話，也可以用電話登入。

### 變數usePass

使用者的密碼，因此這個檔案小心不要給別人，否則他就知道你的FB登入帳密了。

### 變數useId

在您FB的首頁，即可看到網址如下。該使用者的編號ID，其目的在於程式中，會先到使用者的所有社團，將所有社團的名稱爬下來，因此需要使用者編號ID。

若您找不到，發現您的首頁網址全是英文，代表您有另外申請英文ID，那本爬蟲便無法順利執行，因為社團部分會無法爬取。

<img src="https://imgur.com/GAW5GJi.png"/>

Function說明
=================

範例
=================
以下範例程式碼可以在FB自動發文.py中找到。

### 變數usePass

設定所有所需的參數，若不清楚如何取得這些參數內容，請參考[變數說明](#變數說明)。

```
# 想發的文章
postURL = '您想發的文章'
# 登入帳號的Email
useEmail = '您的FB帳號'
# 登入帳號的Pass
usePass = '您的FB密碼'
# 登入帳號的ID
useId = '您的個人數字ID'
```

### chromedriver啟動

啟動後便會自動登入FB，因此帳號密碼必須事先準備好。利用get_group()方法進到該帳號的社團中，爬取所有社團的名稱，其中catch的參數設定，將您想要發的社團名稱進行篩選，例如範例為「廣告|行銷」，代表社團名稱中有廣告、行銷等字眼，就會被抓取到。

```
import facebook_tool as fbtool
driver = fbtool.login(useEmail = useEmail, usePass = usePass)
group = fbtool.get_group(driver, useId=useId, catch='廣告|行銷')
```

### 文章分享

一般如下圖的文章，用此方式分享。

```
import facebook_tool as fbtool
fbtool.share_article(driver, groups=group, postURL=postURL)
```
<img src="https://imgur.com/mQvKTLo.png"/>

### 圖片分享

圖片類型的文章，會出現類似劇院模式，因此程式必須做調整。

```
import facebook_tool as fbtool
fbtool.share_photo(driver, groups=group, postURL=postURL)
```
<img src="https://imgur.com/mQvKTLo.png"/>

### 影片分享

影片類型的文章通常下面還有有別的影片，但您要發送的影片都會在第一個。

```
import facebook_tool as fbtool
fbtool.share_video(driver, groups=group, postURL=postURL)
```
<img src="https://imgur.com/mQvKTLo.png"/>


檔案說明
=================

### Windows/chromedriver.exe
Windows系統的chrome模擬器，64位元，若無法執行請自行另外做調整。

### Windows/phantomjs.exe
Windows系統的phantomjs，64位元，若無法執行請自行另外做調整。

### Linux/chromedriver
Linux系統的chrome模擬器，64位元，若無法執行請自行另外做調整。

### Linux/phantomjs
Linux系統的phantomjs，64位元，若無法執行請自行另外做調整。

### FB自動發文.py
主程式部分。

### facebook_tool.py
所有功能function。
