import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
def url_links(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    url_lis=[]
    for i in soup.find_all('a',href=True):
        b=i['href']
        if re.search(rf"^\b(?=\w){url}\b(?!\w)",b):
            a=b.replace(url,"")
            a=a.split('/')
            c=url
            for j in range(len(a)):
                if c in url_lis:
                    url_lis.remove(c)
                    url_lis.append(b)
                    break
                elif j==len(a)-1:
                    url_lis.append(b)
                    break
                c=c+"/"+a[j]
    return url_lis
   
df=pd.DataFrame(url_links('https://www.sakshi.com'))
df.to_csv('sak_links.csv',index=False,header=False)
df
