# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 08:58:43 2015

@author: maluko
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 15:39:31 2015

@author: maluko
"""
import requests
import feedparser
import re
import requests
import BeautifulSoup
from geopy.geocoders import Nominatim
from pony.orm import *
import sqlite3
db = Database("sqlite", "./feed.db",create_db=True)
class Feed(db.Entity):
             timestamp = Required(str)
             title = Required(str)
             text = Required(str)
             links = Required(str)
             html = Required(str)
             location = Required(str)
class Reader(object):
    """Reader is a Class written to Parse Newsfeeds"""
    def __init__(self, url=["http://news.google.com/?output=rss"]):
        self.monthes = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "Jun": 5, \
            "Jul": 6, "Aug": 7, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
        self.url=url
        
    #@db_session
    def init_db(self):
         sql_debug(True)
         
         db.generate_mapping(create_tables=True)
         db.commit()
                
    @db_session        
    def save(self):
        try:
            t1 = Feed(timestamp = self.topic.published, title = self.topic.title, text = unicode(self.soup.text), links =self.topic.link, html = self.topic["summary"], location = "Default")
        except:
            print "Couldnt save"
        commit()
    @db_session
    def print_db(self):
        q=db.schema
        
    def readrss(self):
        """Reads and parses the RSS-Feed"""
        self.feednumber = 0
        self.title = []
        self.published = []
        self.links = []
        self.html = []
        self.text = []
        #f=open("/run/shm/h.dat","w")
        self.read_config()
        for newfeed in self.url:
            self.read = feedparser.parse(newfeed)
            for self.topic in self.read.entries:
                self.feednumber+=1
                self.title.append(self.topic.title)
                self.links.append(self.topic.link)
                #loc=re.findall("\w+",str(read.entries[0].summary))
                try:
                    self.html.append(self.topic["summary"])
                except:
                    print "keyerror: summary"
                try:
                    self.soup=BeautifulSoup.BeautifulSoup(self.topic["summary"])
                except:
                    print "key error"
                self.text.append(unicode(self.soup.text))
                self.published.append(self.topic.published)
                self.save()        
                
                print "Feednumber: "
                print
                print self.feednumber
                print
                print "Title:"
                print
                print self.title[-1:]
                print
                print "Links:"
                link=self.links[-1:]
                print link[0]
                print "_____________________"
                print self.published[-1:]
                print "_____________________"
                text=self.text[-1:]
                print text
                print "====================="
                print
    def read_config(self):
        con=open("./rss-over9000.txt","r")
        for i in con:
            self.url.append(i)
    def keywords(self,text,target):
        
        import string
        if type(text)==list:
            for textstr in text:
                tokens = textstr.split() # split on whitespace
                keyword = re.compile(target, re.IGNORECASE)
                window =3
                for index in range( len(tokens) ):
                    if keyword.match( tokens[index] ):
                        start = max(0, index-window)
                        finish = min(len(tokens), index+window+1)
                        lhs = string.join( tokens[start:index] )
                        rhs = string.join( tokens[index+1:finish] )
                        print "%s [%s] %s" % (lhs, tokens[index], rhs)
        else:
           for target in target:
                tokens = text.split() # split on whitespace
                keyword = re.compile(target, re.IGNORECASE)
                window =3
                for index in range( len(tokens) ):
                    if keyword.match( tokens[index] ):
                        start = max(0, index-window)
                        finish = min(len(tokens), index+window+1)
                        lhs = string.join( tokens[start:index] )
                        rhs = string.join( tokens[index+1:finish] )
                        
                        print "%s [%s] %s" % (lhs, tokens[index], rhs)
                        
           
    
        
