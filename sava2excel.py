# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:00:05 2018

@author: Anne
"""

import xlwt
class SaveBallDate(object):
    def __init__(self,items):
        self.items=items
        self.run(self.items)
        
    def run(self,items):
        filename='D:/shuangseqiu.xls'
        book=xlwt.Workbook(encoding='utf8')
        sheet=book.add_sheet('ball',cell_overwrite_ok=True)
        sheet.write(0,0,u'开奖日期')
        sheet.write(0,1,u'期号')
        sheet.write(0,2,u'红1')
        sheet.write(0,3,u'红2')
        sheet.write(0,4,u'红3')
        sheet.write(0,5,u'红4')
        sheet.write(0,6,u'红5')
        sheet.write(0,7,u'红6')
        sheet.write(0,8,u'蓝')
        sheet.write(0,9,u'销售金额')
        sheet.write(0,10,u'一等奖')
        sheet.write(0,11,u'二等奖')
        i=1
        while i <=len(items):
            item=items[i-1]
            sheet.write(i,0,item.date)
            sheet.write(i,1,item.order)
            sheet.write(i,2,item.red1)
            sheet.write(i,3,item.red2)
            sheet.write(i,4,item.red3)
            sheet.write(i,5,item.red4)
            sheet.write(i,6,item.red5)
            sheet.write(i,7,item.red6)
            sheet.write(i,8,item.blue)
            sheet.write(i,9,item.money)
            sheet.write(i,10,item.firstPrize)
            sheet.write(i,11,item.secondPrize)
            i+=1
            
        book.save(filename)
        
if __name__=='__main__':
    pass