import numpy
import requests

res=requests.get("https://darsman.com/ai-master")
print(res.status_code)
# print(res.text)



from bs4 import BeautifulSoup
soup=BeautifulSoup(res.content,'html.parser')       #واکشی اطلاعات از یک وبسایت
# print(soup.head)  
# print(soup.body)  

with open("darsman.html") as file1:                #باز کردن و خواندن محتوای فایلهای مربوط به وبسایتهایی که درست کردیم
    soup2=BeautifulSoup(file1,"html.parser")    
    imglist=soup2.find_all('img')      #واکشی اطلاعات به صورت لیست مثل عکس توسط تگ هر کدام
    for img in imglist:
        print(img['src'])
        
    links=soup2.find_all('a')           #پیدا کردن لینکها(با تگ آ )  
    for link in links:
        print(link['href'])    
        
    


res=requests.get("https://portal.lanmis.com/aux/darsman/login")
soup=BeautifulSoup(res.content,'html.parser')
items=soup.select("a")
print(f'itemscount:{len(items)}')




#.......