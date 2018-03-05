import mechanize
from bs4 import BeautifulSoup
import codecs
class Item(object):
    singer=None
    song=None

class getMyfavorite(object):
    def __init__(self):
        self.url='http://www.xiami.com/u/351710382?spm=a1z1s.6843761.1478643737.1.dOhu5r'
        self.headFile='F:/python27/HeadersRaw.txt'
        self.outFile='F:/python27/my.txt'
        self.spider()
    def getHeaders(self,fileName):
        headers=[]
        HeaderList=['User-Agent','Cookie']
        with open(fileName,'r') as fp:
            for line in fp.readlines():
                name,value=line.split(':',1)
            if name in HeaderList:
                headers.append((name.strip(),value.strip()))
        print headers
        return headers
    def getResponse(self,url):
        print 1
        br=mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.set_handle_gzip(False)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor,max_time=1)
        headers=self.getHeaders(self.headFile)
        br.addheaders=headers
        br.open(url)
        print br.response().read()
        return br.response().read()
    def spider(self):
        print 2
        items=[]
        responseContent=self.getResponse(self.url)
        soup=BeautifulSoup(responseContent,'lxml')
        tags=soup.find_all('td',attrs={'class','song_name'})
        for tag in tags:
            item=Item()
            info=tag.find_all('a')
            item.song=info[0].get_text()
            item.singer=info[1].get_text()
            print item
            items.append(item)
        self.pipelines(items)


    def pipelines(self,items):
        with codecs.open(self.outFile,'w','utf8') as fp:
            for item in items:
                fp.write(item.song+'\t')
                fp.write(item.singer+'\r\n')
        fp.close()

if __name__=='__main__':
    GB=getMyfavorite()
    
            
    
    

