# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 13:52:48 2015

@author: maluko

Skript that helps extracting links of RSS Feeds from Websites and stores them in rsslinks.txt

"""

import BeautifulSoup
import requests
import re
a=requests.get("http://www.rediff.com/push/rss.htm")
soup = BeautifulSoup.BeautifulSoup(a.content)
a1=soup.findAll("a")
a5=BeautifulSoup.BeautifulSoup(str(a1))
print a1
f=open("rsslinks.txt","w")
t=open("rss.other.txt","w")
a5=a5.text.split(',')
a4=[]
for i in a5:
    print i
    a3=str(i).split('"')
    for n in a3:
        rss=".xml"
        if (rss in n) or (".feed" in n):
           # print "n: ",n
            a4.append(n)
            a2=re.findall('.+rss$',str(n))
          
            
            for u in a2:
                s=re.findall('http://.*xml$',str(u))
                for o in s:
                    t.write(o+"\n")
            prefix=""
            f.write(prefix+str(n)+"\n")
            #print a2
f.close()
t.close()
