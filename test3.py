import urllib2
import sys
from bs4 import BeautifulSoup

proxy = urllib2.ProxyHandler({'http' : 'heed:ravi@172.31.102.14:3128'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

a = sys.argv[1]
b = sys.argv[2]

url = "http://api.openweathermap.org/data/2.5/weather?q="+a+","+b+"&APPID=dd5c7c67226692f4e69a7cb50c4afb89&mode=html"


#url = "http://api.openweathermap.org/data/2.5/weather?q="+Delhi+","+IN+"&APPID=dd5c7c67226692f4e69a7cb50c4afb89&mode=html"

x = urllib2.urlopen(url)
soup = BeautifulSoup(x, 'html.parser')
soup.prettify()

#print(soup.get_text())
#t = soup.div
#p = t.contents
#for child in t.descendants:
#    print child

for string in soup.stripped_strings:
    print repr(string)




