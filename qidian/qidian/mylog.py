# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:54:13 2018

@author: Anne
"""

import sys
import getpass
import logging

class MyLog(object):
    def __init__(self):
        user=getpass.getuser()
        self.logger=logging.getLogger(user)
        self.logger.setLevel(logging.DEBUG)
        
        logfile=sys.argv[0][0:-3]+'.log'
        #print(sys.argv[0][0:-3])
        logFormatter='%(asctime)-12s%(name)-8s%(message)-8s'
        fileformatter=logging.Formatter(logFormatter)
        
        fileHandler=logging.FileHandler(logfile)
        fileHandler.setFormatter(fileformatter)
        fileHandler.setLevel(logging.DEBUG)
        
        fileHandler2=logging.StreamHandler(logfile)
        fileHandler2.setFormatter(fileformatter)
        fileHandler2.setLevel(logging.ERROR)
        
        self.logger.addHandler(fileHandler)
        self.logger.addHandler(fileHandler2)
        
    def debug(self,message):
        self.logger.debug(message)
        
    def info(self,message):
        self.logger.info(message)
        
    def warn(self,message):
        self.logger.debug(message)
        
    def error(self,message):
        self.logger.error(message)
        
    def critical(self,message):
        self.logger.critical(message)
    
        
if __name__=='__main__':
    MyLog()
    MyLog().debug("I'm debug")
    MyLog().info("I'm info")
    MyLog().warn("I'm warn")
    MyLog().error("I'm error")
    MyLog().critical("I'm critical")
    
    