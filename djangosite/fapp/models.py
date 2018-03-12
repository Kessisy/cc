#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

COUNTRY=(('中国','中国'),('英国','英国'),('美国','美国'))
class Area(models.Model):
    country=models.CharField(max_length=20,choices=COUNTRY,default=COUNTRY[0])
    
class User(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=15,default='')
    email=models.EmailField(max_length=15,default='')
    #area=models.ForeignKey(Area,on_delet=models.CASCADE)
    #friend=models.ManyToManyField("self",verbose_name='朋友')
    
    def __unicode__(self):
        return self.username
    def add_time(self):
        return self.addtime.strftime('%Y-%m-%d %H:%M:%S')
    def save(self):
        super(User,self).save()
        
    class Meta:
        verbose_name=u'用户'
        verbose_name_plural=u'用户'
        
    
        


    