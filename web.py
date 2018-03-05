# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 20:52:54 2018

@author: Anne
"""
from selenium import webdriver
class Item(object):
    IP=None
    port=None
    anonymous=None
    typeip=None
    local=None
    speed=None
class getProxy(object):
    def __init__(self):
        self.startUrls='https://www.kuaidaili.com/free/inha/'
        self.Urls=self.getUrls()
        self.items=self.spider(self.Urls)
        self.pipelines(self.items)
        
    def getUrls(self):
        urls=[]
        for i in range(1,2):
            urlc=self.startUrls+str(i)+'/'
            urls.append(urlc)
        return urls
    def spider(self,urls):
        items=[]
        browser=webdriver.Chrome("E:\pyhthon34\chromedriver.exe")
        for url in urls:
            browser.get(url)
            elements=browser.find_elements_by_xpath('//tbody/tr')
            for element in elements:
                item=Item()
                item.ip=element.find_element_by_xpath('./td[1]').text
                item.port=element.find_element_by_xpath('./td[2]').text
                item.anonymous=element.find_element_by_xpath('./td[3]').text
                item.typeip=element.find_element_by_xpath('./td[4]').text
                item.local=element.find_element_by_xpath('./td[5]').text
                item.speed=element.find_element_by_xpath('./td[6]').text
                items.append(item)
        return items
    def pipelines(self,items):
        filename='D:/web.txt'
        with open(filename,'w',encoding='utf-8') as fp:
            for item in items:
                fp.write(item.ip+'\t'+item.port+'\t'+item.anonymous+'\t'+item.typeip+'\t'+item.local+'\t'+item.speed+'\n')
        fp.close()
        
if __name__=='__main__':
    GD=getProxy()
    
            
            
        

