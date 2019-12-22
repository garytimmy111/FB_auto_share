# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:11:50 2019

@author: Ivan
"""
# selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
import time
import re
import platform
import random

# exception
class Error(Exception):
    """Base class for all exceptions raised by this module"""
    pass

class UnknownUrlType(Error):
    """Unknow url's Type, except 'posts', 'photos' or 'videos'. """
    pass

class PageNotFound(Error):
    """Can not fetch page by given url"""
    pass

#開啟selenium的driver
def open_driver():
    # 判斷是甚麼作業系統，決定selenium使用的工具
    theOS = list(platform.uname())[0]
    if theOS == 'Windows':
        theOS = theOS + '\\'
    else:
        theOS = theOS + '/'
    
    # 設定基本參數
    desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
    #此處必須換成自己電腦的User-Agent
    desired_capabilities['phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    
    # PhantomJS driver 路徑 似乎只能絕對路徑
    driver = webdriver.PhantomJS(executable_path = theOS +'phantomjs', desired_capabilities=desired_capabilities)
    
    # 關閉通知提醒
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    
    # 開啟瀏覽器
    driver = webdriver.Chrome(theOS +'chromedriver',chrome_options=chrome_options)
    
    return driver

#登入  
def login(useEmail = '您的FB帳號', usePass = '您的FB密碼'):
    driver = open_driver()
    ####### 開始操作 輸入帳號密碼登入 到fb首頁 ####### 
    driver.get("http://www.facebook.com")
    time.sleep(1)
    assert "Facebook" in driver.title
    try:
        elem = driver.find_element_by_id("email")
        elem.send_keys(useEmail)
        elem = driver.find_element_by_id("pass")
        elem.send_keys(usePass)
        elem.send_keys(Keys.RETURN)
    except:
        driver.find_element_by_xpath('//*[@name="email"]')
        elem.send_keys(useEmail)
        elem = driver.find_element_by_xpath('//*[@name="pass"]')
        elem.send_keys(usePass)
        elem.send_keys(Keys.RETURN)
    time.sleep(5)
    
    #取得帳號絕對ID
    getID = driver.find_element_by_xpath('//*[@title="個人檔案"]').get_attribute('href')
    yourID = getID[getID.find('id=')+3:]
    return driver, yourID

#抓到所有社團
def get_group(driver, useId='使用者絕對ID', catch=''):
    ####### 先取得所有的社團 #######
    # 切換到自己的社團
    driver.get('https://www.facebook.com/profile.php?id=' + useId + '&sk=groups')
    
    # 滾動頁面
    c=0 
    while len(driver.find_elements_by_id("pagelet_timeline_medley_movies")) <1  :
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        c+=1
        print('scroll '+str(c))
        time.sleep(1)
        
    # 取得所有社團
    getallgroup = driver.find_elements_by_xpath('//*[@data-hovercard]')
    get_groups = [] 
    
    #檢查，若無要求就社團全部發
    if len(catch) == 0:
        for groups in getallgroup:
            get_groups.append(groups.text)
    else:
        for groups in getallgroup:
            if len("".join(re.findall(catch, groups.text))) >0:
                get_groups.append(groups.text)
            
    return get_groups

class startSelenium:

    def __init__(self, useEmail = '您的FB帳號', usePass = '您的FB密碼', catch = ''):
        self.useEmail = useEmail
        self.usePass = usePass
        self.catch = catch
        self.driver, self.useId = login(self.useEmail, self.usePass)
        self.getallgroup = get_group(self.driver, self.useId, self.catch)
        
    def checkShareGroup(self):
        print('======================== 即將發送的社團 ========================')
        for group in self.getallgroup:
            print(group)



class share(startSelenium):
    
    def __init__(self, useEmail, usePass, catch, postURL = '您想發的文章'):
        super().__init__(useEmail, usePass, catch)
        self.postURL = postURL

        
    def share_article(self):
        '''
        只能發送文字形文章，範例如下：
        https://www.facebook.com/MarketingDataScienceTMR/posts/221821808488524
        '''
        ####### 開始分享 #######  
        # 切換到行銷資料科學文章
        self.driver.get(self.postURL)
        self.checkShareGroup()
        for send in self.getallgroup:
            # 按下分享
            self.driver.find_element_by_xpath('//*[@title="寄送這個給朋友或張貼在你的動態時報中。"]').click()
            time.sleep(random.randint(3,5))
            # 按下分享到社團
            self.driver.find_element_by_xpath("//*[contains(text(), '分享到社團')]").click()
            time.sleep(random.randint(2,7))
            # 輸入社團名稱
            self.driver.find_element_by_xpath('//*[@data-testid="searchable-text-input"]').send_keys(send)
            time.sleep(random.randint(2,7))
            # 按下向下建選擇第一個最相似的社團
            self.driver.find_element_by_xpath('//*[@data-testid="searchable-text-input"]').send_keys('\ue015')
            # 按下enter迴車建
            self.driver.find_element_by_xpath('//*[@data-testid="searchable-text-input"]').send_keys('\ue007')
            # 包含原始貼文打勾
            self.driver.find_element_by_class_name('_55sg').click()
            time.sleep(random.randint(7,15))
            # 發布
            self.driver.find_element_by_xpath('//*[@data-testid="react_share_dialog_post_button"]').click()
            time.sleep(random.randint(60,120))
        self.driver.quit()
            
            
    def share_photo(self):
        '''
        只能發送圖片形文章，範例如下：
        https://www.facebook.com/MarketingDataScienceTMR/photos/a.212187719451933/263276287676409/
        '''
        ####### 開始分享 #######  
        # 切換到行銷資料科學文章
        self.driver.get(self.postURL)
        
        for send in self.getallgroup:
            # 按下分享
            self.driver.find_elements_by_xpath("//*[contains(text(), '分享')]")[4].click()
            time.sleep(random.randint(3,5))
            # 按下分享到社團
            self.driver.find_elements_by_xpath("//*[contains(text(), '分享到你的動態時報')]")[7].click()
            time.sleep(random.randint(3,5))
            self.driver.find_elements_by_xpath("//*[contains(text(), '分享到社團')]")[6].click()
            time.sleep(random.randint(2,7))
            # 輸入社團名稱
            self.driver.find_elements_by_xpath('//*[@data-testid="searchable-text-input"]')[2].send_keys(send)
            time.sleep(random.randint(2,7))
            # 按下向下建選擇第一個最相似的社團
            self.driver.find_elements_by_xpath('//*[@data-testid="searchable-text-input"]')[2].send_keys('\ue015')
            # 按下enter迴車建
            self.driver.find_elements_by_xpath('//*[@data-testid="searchable-text-input"]')[2].send_keys('\ue007')
            # 包含原始貼文打勾
            #driver.find_element_by_class_name('_55sg').click()
            time.sleep(random.randint(7,15))
            # 發布
            self.driver.find_elements_by_xpath('//*[@data-testid="react_share_dialog_post_button"]')[5].click()
            time.sleep(random.randint(60,120))
        self.driver.quit()
            
            
    def share_video(self):
        '''
        只能發送影片形文章，範例如下：
        https://www.facebook.com/MarketingDataScienceTMR/videos/431458434058905/
        '''
        # 切換到行銷資料科學文章
        self.driver.get(self.postURL)
        # 按下分享
        self.driver.find_element_by_xpath("//*[contains(text(), '分享')]").click()
        time.sleep(random.randint(3,5))
        # 按下分享到社團
        self.driver.find_element_by_xpath("//*[contains(text(), '分享到社團')]").click()
        time.sleep(random.randint(2,7))
        
        for send in self.getallgroup:
            # 輸入社團名稱
            self.driver.find_element_by_xpath('//*[@aria-label="搜尋社團"]').send_keys(send)
            time.sleep(random.randint(2,7))
            self.driver.find_elements_by_xpath('//div[@aria-labelledby]')[5].click()
            
            length = len(self.driver.find_element_by_xpath('//*[@aria-label="搜尋社團"]').get_attribute('value')) #抓到欲刪除的欄位數量
            self.driver.find_element_by_xpath('//*[@aria-label="搜尋社團"]').send_keys(length * Keys.BACKSPACE) #案幾次刪除
            time.sleep(random.randint(60,120))
        self.driver.quit()
    
    
    def share_article_on_your_page(self):
        ####### 按下分享到自己的專欄 ####### 
        self.driver.get(self.postURL)
        self.driver.find_element_by_xpath("//*[contains(text(), '立即分享 (公開)')]").click()
        self.driver.quit()
        
def main():
    print('\n請輸入您的FB帳號：')
    useEmail = input() 
    
    print('\n請輸入您的FB密碼：')
    usePass = input()
    
    print('\n請輸入社團關鍵字,請用空白分隔：')
    print('(若要全部發，則直接Enter跳過)')
    catch = input()
    catch = catch.replace(' ','|')
    
    print('\n請輸入想發的文章：')
    postURL = input()
    
    

    if '/posts/' in postURL:
        gg=share( useEmail=useEmail, usePass=usePass, catch =catch, postURL = postURL)
        gg.share_article()
    elif '/photos/' in postURL:
        gg=share( useEmail=useEmail, usePass=usePass, catch =catch, postURL = postURL)
        gg.share_photo()
    elif '/videos/' in postURL:
        gg=share( useEmail=useEmail, usePass=usePass, catch =catch, postURL = postURL)
        gg.share_video()
    else:
        raise UnknownUrlType
        
if __name__ == '__main__':
    main()
