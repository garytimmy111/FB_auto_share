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
# 判斷是甚麼作業系統，決定selenium使用的工具
theOS = list(platform.uname())[0]
if theOS == 'Windows':
    theOS = theOS + '\\'
else:
    theOS = theOS + '/'
    
def open_driver():
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
   
def login(useEmail = '帳號', usePass = '密碼'):
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
    return driver

def get_group(driver, useId='你的使用者ID', catch='金融|財務|股票|交易|利率|期貨|基金|投資|理財|外匯|'):
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

    
    # 分成兩種發文的社團群
    for groups in getallgroup:
        if len("".join(re.findall(catch, groups.text))) >0:
            get_groups.append(groups.text)
            
    return get_groups

    


def share_article(driver, groups=['想發文的社團名稱'], postURL='文章網址'):
    ####### 開始分享 #######  
    # 切換到行銷資料科學文章
    driver.get(postURL)
    
    for send in groups:
        # 按下分享
        driver.find_element_by_xpath('//*[@title="寄送這個給朋友或張貼在你的動態時報中。"]').click()
        time.sleep(random.randint(3,5))
        # 按下分享到社團
        driver.find_element_by_xpath("//*[contains(text(), '分享到社團')]").click()
        time.sleep(random.randint(2,7))
        # 輸入社團名稱
        driver.find_element_by_xpath('//*[@data-testid="searchable-text-input"]').send_keys(send)
        time.sleep(random.randint(2,7))
        # 按下向下建選擇第一個最相似的社團
        driver.find_element_by_xpath('//*[@data-testid="searchable-text-input"]').send_keys('\ue015')
        # 按下enter迴車建
        driver.find_element_by_xpath('//*[@data-testid="searchable-text-input"]').send_keys('\ue007')
        # 包含原始貼文打勾
        driver.find_element_by_class_name('_55sg').click()
        time.sleep(random.randint(7,15))
        # 發布
        driver.find_element_by_xpath('//*[@data-testid="react_share_dialog_post_button"]').click()
        time.sleep(random.randint(2,7))
        
        
def share_photo(driver, groups=['想發文的社團名稱'], postURL='圖片網址'):
    ####### 開始分享 #######  
    # 切換到行銷資料科學文章
    driver.get(postURL)
    
    for send in groups:
        # 按下分享
        driver.find_elements_by_xpath("//*[contains(text(), '分享')]")[4].click()
        time.sleep(random.randint(3,5))
        # 按下分享到社團
        driver.find_elements_by_xpath("//*[contains(text(), '分享到你的動態時報')]")[7].click()
        time.sleep(random.randint(3,5))
        driver.find_elements_by_xpath("//*[contains(text(), '分享到社團')]")[6].click()
        time.sleep(random.randint(2,7))
        # 輸入社團名稱
        driver.find_elements_by_xpath('//*[@data-testid="searchable-text-input"]')[2].send_keys(send)
        time.sleep(random.randint(2,7))
        # 按下向下建選擇第一個最相似的社團
        driver.find_elements_by_xpath('//*[@data-testid="searchable-text-input"]')[2].send_keys('\ue015')
        # 按下enter迴車建
        driver.find_elements_by_xpath('//*[@data-testid="searchable-text-input"]')[2].send_keys('\ue007')
        # 包含原始貼文打勾
        #driver.find_element_by_class_name('_55sg').click()
        time.sleep(random.randint(7,15))
        # 發布
        driver.find_elements_by_xpath('//*[@data-testid="react_share_dialog_post_button"]')[5].click()
        time.sleep(random.randint(3,10))
        
        
def share_video(driver, groups=['想發文的社團名稱'], postURL='圖片網址'):
    # 切換到行銷資料科學文章
    driver.get(postURL)
    # 按下分享
    driver.find_element_by_xpath("//*[contains(text(), '分享')]").click()
    time.sleep(random.randint(3,5))
    # 按下分享到社團
    driver.find_element_by_xpath("//*[contains(text(), '分享到社團')]").click()
    time.sleep(random.randint(2,7))
    
    for send in groups:
        # 輸入社團名稱
        driver.find_element_by_xpath('//*[@aria-label="搜尋社團"]').send_keys(send)
        time.sleep(random.randint(2,7))
        driver.find_elements_by_xpath('//div[@aria-labelledby]')[5].click()
        
        length = len(driver.find_element_by_xpath('//*[@aria-label="搜尋社團"]').get_attribute('value')) #抓到欲刪除的欄位數量
        driver.find_element_by_xpath('//*[@aria-label="搜尋社團"]').send_keys(length * Keys.BACKSPACE) #案幾次刪除
        time.sleep(random.randint(3,10))


def share_article_on_your_page(driver, postURL='文章網址'):
    ####### 按下分享到自己的專欄 ####### 
    driver.get(postURL)
    driver.find_element_by_xpath("//*[contains(text(), '立即分享 (公開)')]").click()
    driver.quit()