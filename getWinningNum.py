# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:57:16 2018

@author: Anne
"""


from bs4 import BeautifulSoup
import urllib
from mylog import MyLog as mylog
from sava2excel import SaveBallDate
class DoubleColorBallNum(object):
    date=None
    order=None
    red1=None
    red2=None
    red3=None
    red4=None
    red5=None
    red6=None
    blue=None
    money=None
    firstPrize=None
    secondPrize=None
    
    
class GetDoubleColorBallNumber(object):
    def __init__(self):
        self.urls=[]
        self.log=mylog()
        self.getUrls()
        self.items=self.spider(self.urls)
        self.pipelines(self.items)
        SaveBallDate(self.items)
    
    def getUrls(self):
        URL=r'http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'
        htmlContent=self.getResponseContent(URL)
        soup=BeautifulSoup(htmlContent,'lxml')
        tag=soup.find_all('p')[-1]
        num=tag.strong.get_text()
        
        for i in range(1,3):
            url=r'http://kaijiang.zhcw.com/zhcw/html/ssq/list_'+str(i)+'.html'
            self.urls.append(url)
            self.log.info(u'append url success')
        
            
            
            
        
    def getResponseContent(self,url):
        try:
            response=urllib.request.urlopen(url)
            
        except:
            self.log.error(u'urlopen:%s failed\r\n'%url)
        else:
            self.log.info(u'urlopen success')
            return response.read()
        
        
    def spider(self,urls):
        items=[]
        for url in urls:
            htmlContent=self.getResponseContent(url)
            soup=BeautifulSoup(htmlContent,'lxml')
            tags=soup.find_all('tr',attrs={})
            for tag in tags:
                if tag.find('em'):
                    item=DoubleColorBallNum()
                    tagTd=tag.find_all('td')                  
                    item.date=tagTd[0].get_text()
                    item.order=tagTd[1].get_text()
                    tagEm=tagTd[2].find_all('em')
                    item.red1=tagEm[0].get_text()
                    item.red2=tagEm[1].get_text()
                    item.red3=tagEm[2].get_text()
                    item.red4=tagEm[3].get_text()
                    item.red5=tagEm[4].get_text()
                    item.red6=tagEm[5].get_text()
                    item.blue=tagEm[6].get_text()
                    item.money=tagTd[3].find('strong').get_text()
                    item.firstPrize=tagTd[4].find('strong').get_text()
                    item.secondPrize=tagTd[5].find('strong').get_text()
                    items.append(item)
                    self.log.info(u'spider success')
                    
        return items
        
        
    def pipelines(self,items):
        filename='D:/shuangseqiu.txt'
        with open(filename,'w',encoding='utf-8') as fp:
            for it in items:
                print(it.date)
                fp.write('date:%s\t,order:%s\t,red1:%s\t,red2:%s\t,red3:%s\t,red4:%s\t,red5:%s\t,red6:%s\t,blue:%s\t,money:%s\t,firstPrize:%s\t,secondPrize:%s\n'%(it.date,it.order,it.red1,it.red2,it.red3,it.red4,it.red5,it.red6,it.blue,it.money,it.firstPrize,it.secondPrize))
                self.log.info(u'save success')                                                                                             
        fp.close()
        
if __name__=='__main__':

    GD=GetDoubleColorBallNumber()
    
            
        
        
        