# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:13:50 2018

@author: Anne
"""

import pymysql
class saveBooksData(object):
    def __init__(self,items):
        self.host='localhost'
        self.port=3306
        self.user='crawlUSER'
        self.password='crawl123'
        self.database='scrapyDB'
        self.run(items)
        
        
    def run(self,items):
        conn=pymysql.connect(host=self.host,
                             port=self.port,
                             password=self.password,
                             database=self.database,
                             user=self.user,
                             charset='utf8')
        cur=conn.cursor()
        for it in items:
            cur.execute("INSERT INTO qidianbooks(categoryName,bookName,wordNum,updateTime,authorName) values(%s,%s,%s,%s,%s);",(it.bookType,it.bookName,it.bookNumber,it.bookUpdate,it.bookAuthor))
            print(it.bookType)
        cur.close()
        conn.commit()
        conn.close()
        print('ok')
if __name__=='__main__':
    pass
        
        
        