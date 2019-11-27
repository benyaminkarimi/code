from bs4 import BeautifulSoup
import re
import requests
import codecs

dataa=codecs.open(r'C:\Users\ben\Desktop\python\1397.txt','w','utf-8')

monolink1=""
for x in range(1, 6500):
    x=str(x)
    r= requests.get("https://www.isna.ir/page/archive.xhtml?mn=4&wide=0&dy=13&ms=0&pi="+x+"&yr=1397")
    data = r.text
    soup = BeautifulSoup(data)
    soup = soup.find('div', attrs={'class':'col-xs-12 col-md-9'})

    try:
        links= soup.find_all('a')
    except :
        continue
    for link in links:
        monolink=link.get('href')
        monolink=str(monolink)
        if re.match("/news/",monolink):
            if monolink!=monolink1:
                monolink1=monolink
                try:
                    r= requests.get("https://www.isna.ir"+monolink)
                except requests.exceptions.SSLError:
                    print("sslError")
                    continue
                except requests.exceptions.ReadTimeout:
                    print("timeout")
                    continue
                else:
                    data = r.text
                    soup = BeautifulSoup(data)
                    soup = soup.find('div', attrs={'class':'item-text'})
                    try:
                        text = soup.get_text()
                    except :
                        continue
                    dataa.write(str(text))
                    dataa.write("\n")
dataa.close()      
print("done")
        
