import urllib2
import webbrowser
import ctypes
import time
#the web address from where Price is to be taken
addr = 'http://www.flipkart.com/nikon-d5100-slr/p/itmczcqzxuws7bgn?pid=CAMCXH4FFUDGAMHS&'
#reference price
ref_price = 25999 
#proxy make the proxy variable 1
#and set the proxy_addr to the proxy address:port
proxy = 0
if proxy:
    proxy_addr="10.1.5.89:80"
def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxA(0,text,title,style)
def retreiveprice():
    try:
        if proxy:
            proxy_support=urllib2.ProxyHandler({"http":proxy_addr})       
            open = urllib2.build_opener(proxy_support)
        else:
            open = urllib2.build_opener()
        open.addheaders = [('User-agent', 'Mozilla/5.0')]
        infile=open.open(addr)
        page = infile.read()
        a=page.find('fk-font-verybig pprice fk-bold')
        #print a
        b=page[a:].find("Rs. ")
        start=a+b+4
        end=page[start:].find('<')+start
        price=int(page[start:end])
        print price
        if price<ref_price:
            Mbox('Price is less than '+str(ref_price), 'The current price is '+str(price),0)
            
    except:
        print 'error'
while(1):
    retreiveprice()
    time.sleep(50) #To save bandwidth
