# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:52:48 2018

@author: Anne
"""
from mylog import MyLog as mylog
from bs4 import BeautifulSoup
import urllib
import pathlib
import os
import random
import resource
import codecs
from save2mysql import saveBooksData
class bookItem(object):
    bookName=None
    bookType=None
    bookAuthor=None
    bookIntroduce=None
    bookNumber=None
    bookUpdate=None
    
class getBookInfo(object):
    def __init__(self):
        self.log=mylog()
        self.urls=self.getUrls()
        self.items=self.spider(self.urls)
        self.pipelines(self.items)
        saveBooksData(self.items)
        
        
    def getUrls(self):
        urls=[]
        url='https://www.qidian.com/all?action=1&orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1'
        html=self.getContent(url)
        soup=BeautifulSoup(html,'lxml')
        pageNum=soup.find('div',attrs={'class':'pagination fr'}).get('data-pagemax')
        print(pageNum)
        urlf=url.split('=')
        for i in range(1,2):
            urlf[-1]=str(i)
            urln='='.join(urlf)
            urls.append(urln)
        return urls
            
    def getRandomUserAgent(self):
        return random.choice(resource.UserAgent)
    def getRandomProxy(self):
        return random.choice(resource.PROXIES)
    def getContent(self,url): 
        fakeHeader={'User-Agent':self.getRandomUserAgent()}
        request=urllib.request.Request(url,headers=fakeHeader)
        proxy=urllib.request.ProxyHandler({'http':'http://'+self.getRandomProxy()})
        opener=urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)
        try:
            response=urllib.request.urlopen(request)
        except:
            self.log.error('urlopen failed')
        else:
            self.log.info('urlopen success')
            return response.read()
        
    def spider(self,urls):
        for urlw in urls:
            items=[]
            htmlContent=self.getContent(urlw)
            soup=BeautifulSoup(htmlContent,'lxml')
            tagBook=soup.find_all('div',attrs={'class':'book-mid-info'})
            for tag in tagBook:
                item=bookItem()
                item.bookName=tag.find('h4',attrs={}).a.get_text()
                #item.bookAuthor=tag.find('a',attrs={'class':"name" }).get_text()
                itema=tag.find('p',attrs={'class':'author'}).find_all('a')
                item.bookAuthor=itema[0].get_text()
                item.bookType=itema[1].get_text()+''+itema[2].get_text()
                item.bookUpdate=tag.find('p',attrs={'class':'author'}).span.get_text()
                item.bookIntroduce=tag.find('p',attrs={'class':'intro'}).get_text()
                item.bookNumber=tag.find('p',attrs={'class':'update'}).span.get_text()
                items.append(item)      
            return items
     
    def pipelines(self,items):
        filename='D:/qidian/qidian.txt'
        path=pathlib.Path('D:/qidian')
        if path.exists():
            pass
        else:
            os.mkdir(path)
        with codecs.open(filename,'w',encoding='utf-8') as fp:
            for it in items:
                fp.write('书名:%s \t作者:%s \t类型:%s \t进度:%s \t内容:%s \t字数：%s\r\n'%(it.bookName,it.bookAuthor,it.bookType,it.bookUpdate,it.bookIntroduce,it.bookNumber))
        fp.close()    
        
if __name__=='__main__':
    GBN=getBookInfo()
        