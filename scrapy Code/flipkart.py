import requests
from bs4 import BeautifulSoup
product_name = raw_input("Enter Product Name to Search in Flipkart: ")
product_name = product_name.replace(" ", "+")
data = requests.get("http://www.flipkart.com/search?q="+str(product_name))
soup = BeautifulSoup(data.content)
title_list =  soup.findAll("div", {"class":"pu-details lastUnit"}, True, None, None)
print "###############Products List####################" #product-unit unit-4 browse-product new-design pu-details lastUnit
for title in title_list:
    product_title = title.find("div", {"class":"pu-title fk-font-13"},True,None).text
    product_price = title.find("div", {"class":"pu-final"},True,None).text
#    product_offer = title.find("div", {"class":"pu-discount"}),True,None).text
    print str(product_title) + "  ===  " +str(product_price)#+ "  ===  " +str(product_offer)
print "###############################################"
