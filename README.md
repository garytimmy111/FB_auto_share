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
    * [程式碼執行](#程式碼執行)
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

4. 輸入您想要的社團關鍵字，此功能能避開部分社團不發送。假設您想要發送金融相關社團，而社團名稱中都有出現「股票」、「期貨」，那您就可以輸入「股票 期貨」，中間以空白分隔。若全部社團都想要發，則直接Enter就好了。

<img src="https://imgur.com/LuEUhof.png"/>

5. 輸入您想要發送的文章，目前支援一般PO文、圖片、影片。

<img src="https://imgur.com/tqc1G0f.png"/>

### 程式碼執行

1. 此處的範例可以參考FB自動發文.py檔案，裡面有完整程式碼。首先引入facebook_tool.py檔案，而後執行share物件，並傳送參數帳號、密碼、關鍵字、文章連結。

```
gg=fbtool.share( 
        useEmail='您的FB帳號', 
        usePass='您的FB密碼', 
        catch ='廣告|行銷', 
        postURL = 'https://www.facebook.com/MarketingDataScienceTMR/posts/221821808488524'
        )
```

 

2. 文章分享,一般如下圖的文章，用此方式分享。

```
gg.share_article()
```
<img src="https://imgur.com/mQvKTLo.png"/>

圖片類型的文章，會出現類似劇院模式，因此程式必須做調整。

```
gg.share_photo()
```
<img src="https://imgur.com/ifF0o38.png"/>

影片類型的文章通常下面還有有別的影片，但您要發送的影片都會在第一個。

```
gg.share_video()
```

<img src="https://imgur.com/duyYYxr.png"/>


檔案說明
=================

### Windows/chromedriver.exe
Windows系統的chrome模擬器，64位元，若無法執行請自行另外做調整[下載](https://chromedriver.chromium.org/downloads)。

### Windows/phantomjs.exe
Windows系統的phantomjs，64位元，若無法執行請自行另外做調整[下載](https://phantomjs.org/download.html)。

### Linux/chromedriver
Linux系統的chrome模擬器，64位元，若無法執行請自行另外做調整[下載](https://chromedriver.chromium.org/downloads)。

### Linux/phantomjs
Linux系統的phantomjs，64位元，若無法執行請自行另外做調整[下載](https://phantomjs.org/download.html)。

### FB自動發文.py
利用facebook_tool.py檔案內的物件達到自動發文功能，比較有活性，若要定期且長期使用，建議可以使用此方式，並將帳號密碼寫入，減少重複性工作。

### facebook_tool.py
所有功能function，也可以使用console介面執行，若是使用[Anaconda](https://www.anaconda.com/distribution/)執行Python者，請使用[Anaconda prompt](https://www.anaconda.com/distribution/)，MAC電腦直接使用終端機（terminal）即可。若Windows有安裝Python者，也可以直接在cmd執行，若沒有，建議[下載Anaconda](https://www.anaconda.com/distribution/)來執行。
