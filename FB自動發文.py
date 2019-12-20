# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:03:08 2019

@author: Ivan
"""
import facebook_tool as fbtool
###############################################################################
#                             FB 自動發文機器                                  #
###############################################################################

####### 您的發文設定 ####### 
# 想發的文章
postURL = '您想發的文章'
# 登入帳號的Email
useEmail = '您的FB帳號'
# 登入帳號的Pass
usePass = '您的FB密碼'
# 登入帳號的ID
useId = '您的個人數字ID'


driver = fbtool.login(useEmail = useEmail, usePass = usePass)
group = fbtool.get_group(driver, useId=useId, catch='廣告|行銷')
fbtool.share_article(driver, groups=group, postURL=postURL)






    


