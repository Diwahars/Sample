import random
import requests
import urllib2
import requests
from bs4 import BeautifulSoup

fw=open('sample2.txt','w')

def crwlr(max_items):
    item=1;
    url="https://www.quora.com/What-are-the-best-productivity-tools-for-entrepreneurs"
    src=requests.get(url)
    plain_txt=src.text
    soup=BeautifulSoup(plain_txt)
    while item<=max_items:

        ans_cnt=soup.findAll('div',{'class':'answer_count'})
        a=str(ans_cnt)
        a=a.split('Answer')
        a=a[0]
        a=a.split('>')
        a=a[1]
        a=a.split('+')
        a=a[0]
        b=int(a)
        print(b)
        if(item>b):
            break
        #print(a)
        #a= ans_cnt.string
        #fw.write(a)
        #fw.write("\n")
        for text in soup.findAll('div',{'class':'qtext_para'}):
            tst=text.string
            if(tst!=None):
                #print(tst)
                fw.write(tst)
                fw.write("\n")
        item+=1

crwlr(5)
fw.close()


