# coding=utf-8
import urllib2
from threading import Timer

from bs4 import BeautifulSoup
import os
import pymongo
#import re
import time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
#获取模块
def main(commonUrk,initUrl):
    request = urllib2.Request(initUrl)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError, e:
        print e.code
    except urllib2.URLError, e:
        print e.reason
    html_data=response.read().decode('UTF-8')
    soup = BeautifulSoup(html_data, 'html.parser')
    content_news = soup.find_all('ul',attrs={'class': 'submenu'})
    list_news = content_news[0].find_all('li')
    all_moudle=[]
    for item in list_news:
        one_moudle={}
        one_moudle_a = item.find_all('a')
        one_moudle['url']=one_moudle_a[0]['href']
        one_moudle['title']=one_moudle_a[0].string
        all_moudle.append(one_moudle)
    moudleContentGet(commonUrk,all_moudle)
#每个模块的新闻获取
def moudleContentGet(commonUrk,all_moudle):
    for one_moudle in all_moudle:
        request = urllib2.Request(commonUrk+one_moudle['url'])
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            print e.code
        except urllib2.URLError, e:
            print e.reason

        html_data=response.read().decode('UTF-8')
        soup = BeautifulSoup(html_data, 'html.parser')
        content_news = soup.find_all('ul',id='requestUl')
        #print content_news
        list_news = content_news[0].find_all('li')

        all_news=[]
        for item in list_news:
            one_news={}
            one_news_a = item.find_all('a')
            #print one_news_a
            one_news['url']=one_news_a[0]['href']
            one_news['title']=one_news_a[0].string.replace(' ','').replace('•','')
            all_news.append(one_news)

        #print all_news
        newsContentGet(commonUrk,all_news,one_moudle['title'])

#每个新闻内容获取
def newsContentGet(commonUrk,news,moudle):
       for result_item in news:
           url=commonUrk+result_item['url']
           request = urllib2.Request(url)
           try:
                 response = urllib2.urlopen(request)
           except urllib2.HTTPError, e:
                 print e.code
           except urllib2.URLError, e:
                 print e.reason
           html_data = response.read().decode('utf-8')
           soup = BeautifulSoup(html_data, 'html.parser')
           content_news = soup.find_all('div',attrs={'class': 'rightWid maxWid'})
           [script.extract() for script in soup.findAll('script')]
           [style.extract() for style in soup.findAll('style')]
           [close.extract() for close in soup.findAll('div',attrs={'class': 'clos'})]
           [sm.extract() for sm in soup.findAll('div', attrs={'style': 'box-shadow:0 0 5px red;padding:20px;padding-top:5px;color:grey;background: transparent;font-weight:bold;'})]
           [img.extract() for img in soup.findAll('img')]
           [a.extract() for a in soup.findAll('a')]
           content = content_news[0].prettify()
           # reg = re.compile("<[^>]*>")
           # content = reg.sub('', content)
           #写文件
           #wtiteToFile(moudle,result_item['title']+'.txt',content)
           #保存数据库
           saveToDb(result_item['title'],content,moudle,'ht',url)
#单个新闻内容落地
def wtiteToFile(moudle,filename,content):
    try:
        path='D:/test/'+moudle+'/'
        if not os.path.exists(path):
           os.mkdir(path)
        fp = open(path + filename,"w+")
        fp.write(content)
        fp.close()
    except IOError:
        print("fail to open file")
def saveToDb(title,content,moudle,org,url):
    client = pymongo.MongoClient("127.0.0.1", 27017)
    testDB = client.testDB
    news = testDB.news
    result_news=[]
    result_news =news.find({"url": url,"title": title,})
    result_list = list(result_news[:])
    if(len(result_list)==0):
        news.insert_one({'title': title, 'content': content, 'moudle': moudle, 'org': org,'url':url})

#定时循环执行
def startTimer():
  print 'start onece task '+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
  main("https://www.htsec.com", "https://www.htsec.com/ChannelHome/2016102402/index.shtml")
  roll_time = 5 * 60
  t = Timer(roll_time, startTimer)
  t.start()


startTimer()

#main("https://www.htsec.com", "https://www.htsec.com/ChannelHome/2016102402/index.shtml")