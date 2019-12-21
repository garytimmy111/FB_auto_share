FB文章自動分享社團
=========

`此專案目的只為了學術技術分享，請勿拿來從事不法行為，違者自行負起法律責任`

FB文章自動分享社團，但還是必須要使用一個帳號，來做為機器人使用，切記不要是重要帳號，否則被封鎖。

2019/12/20新增分享圖片、影片文章。

<img src="https://i.imgur.com/841nwcA.png"/>

目錄
=================
* [事前必要準備](#事前必要準備)
* [範例](#範例)
    * [Console介面直接執行](#Console介面直接執行)
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
1. 必須要下載Chrome，若是在DOS沒有圖形化介面，也必須要下載Chrome。
2. [ChromeDriver請依照自己Chrome的版本進行下載](https://chromedriver.chromium.org/downloads)，若不知道自己Chrome，可以[到這裡進行查看](https://chromedriver.storage.googleapis.com/LATEST_RELEASE)。
4. [phantomjs若版本不合，請自行下載。](https://phantomjs.org/download.html)
5. phantomjs下載完以後，請依照作業系統擺放，如下圖。
<img src="https://i.imgur.com/vxk2PXt.png"/>

範例
=================
以下範例程式碼可以在FB自動發文.py中找到。

### Console介面直接執行

1. cd到facebook_tool.py的目錄上，執行檔案。

```
python facebook_tool.py
```

2. 輸入您的FB帳號。

<img src="https://imgur.com/7Ms1rJL.png"/>

3. 輸入您的FB密碼。

<img src="https://imgur.com/JgQB7xW.png"/>

4. 輸入您想要的社團關鍵字，此功能能避開部分社團不發送。假設您想要發送金融相關社團，而社團名稱中都有出現「股票」、「期貨」，那您就可以輸入「股票 期貨」，中間以空白分隔。

<img src="https://imgur.com/LuEUhof.png"/>

5. 輸入您想要發送的文章，目前支援一般PO文、圖片、影片。

<img src="https://imgur.com/tqc1G0f.png"/>

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
<img src="https://imgur.com/ifF0o38.png"/>

### 影片分享

影片類型的文章通常下面還有有別的影片，但您要發送的影片都會在第一個。

```
import facebook_tool as fbtool
fbtool.share_video(driver, groups=group, postURL=postURL)
```
<img src="https://imgur.com/duyYYxr.png"/>


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
