# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:55:07 2018

@author: Anne
"""

import urllib
from bs4 import BeautifulSoup
from mylog import MyLog as mylog
import os
import pathlib



class Item(object):
    title=None#帖子的题目
    firstAuthor=None#帖子创建者
    firstTime=None#帖子创建时间
    reNum=None#帖子回复数
    content=None#帖子的内容
    img=None#帖子内容里的图片

class GetTiebaInfo(object):
    def __init__(self,url):
        self.url=url
        self.log=mylog()
        self.pageSum=1
        self.urls=self.getUrls(self.pageSum)
        self.items=self.spider(self.urls)
        self.pipeline(self.items)
        
    def getUrls(self,pageSum):
        urls=[]
        pns=[str(i*50) for i in range(pageSum)]
        ul=self.url.split('=')
        for pn in pns:
            ul[-1]=pn
            url='='.join(ul)
            urls.append(url)
        self.log.info(u'添加url成功')
        return urls
    
    def spider(self,urls):
        items=[]
        for url in urls:
            htmlContent=self.getResponseContent(url)
            soup=BeautifulSoup(htmlContent,'lxml')
            tags=soup.find_all('li',attrs={'class':' j_thread_list clearfix' })
            for tag in tags:
                item=Item()
                item.title=tag.find('a',attrs={'rel':'noreferrer'}).get_text().strip()
                item.firstAuthor=tag.find('span',attrs={'class':'frs-author-name-wrap'}).get_text().strip()
                item.firstTime=tag.find('span',attrs={'class':'pull-right is_show_create_time'}).get_text().strip()
                item.reNum=tag.find('span',attrs={'class':'threadlist_rep_num center_text'}).get_text().strip()
                item.content=tag.find('div',attrs={'class':'threadlist_abs threadlist_abs_onlyline '}).get_text().strip()
                item.img1=tag.find('img')
              
                if item.img1!=None:
                    item.img=item.img1.get('data-original')
                    
                    #item.img=item.img.get('data-original')
                items.append(item)
                #print(type(item))
                self.log.info(u'获取%s成功'%item.title)
            return items
    def pipeline(self,item):
        filename='D:/baidutieba.txt'
        path=pathlib.Path('D:/baidutiebapic')
        if path.exists():
            pass
        else:
            os.mkdir(path='D:/baidutiebapic')
            
        with open(filename,'w',encoding='utf-8') as fp:
            for it in item:    
                fp.write('title:%s \tauthor:%s \tfirstTime:%s \treNum:%s \tcontent:%s \t\n'%(it.title,it.firstAuthor,it.firstTime,it.reNum,it.content))
                if it.img!=None:
                    imgname=os.path.basename(it.img)
                    picfilename='D:/baidutiebapic/'+imgname
                    response=urllib.request.urlopen(it.img)
                    with open(picfilename,'wb+') as fq:
                        fq.write(response.read())
                    fq.close()
        self.log.info(u'%s保存数据成功'%filename)
        fp.close()
    
    def getResponseContent(self,url):
        try:
            response=urllib.request.urlopen(url)
        except:
            self.log.error(u'url：%s连接错误'%url)
        else:
            self.log.info(u'url：%s连接成功'%url)
            result=response.read()           
            return result 
        
if __name__=='__main__':
    url=u'http://tieba.baidu.com/f?kw=%E6%9D%83%E5%88%A9%E7%9A%84%E6%B8%B8%E6%88%8F&ie=utf-8&pn=50'
    GTI=GetTiebaInfo(url)
        
        
            
        
        
