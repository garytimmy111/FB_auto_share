# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:03:08 2019

@author: Ivan
"""
import facebook_tool as fbtool

'''
####### 您的發文設定 ####### 
請依照發文的文章性質，使用不同的方法

範例文章是一般的文字文章，因此使用 share_article()
若是圖片型文章，請使用 share_photo()
影片型文章，請使用 share_video()。
'''
gg=fbtool.share( 
        useEmail='您的FB帳號', 
        usePass='您的FB密碼', 
        catch ='廣告|行銷', 
        postURL = 'https://www.facebook.com/MarketingDataScienceTMR/posts/221821808488524'
        )

# 請依照發文的文章性質，使用不同的方法
gg.share_article()




    


