from time import sleep
from tkinter.tix import TEXT
from webbrowser import get
import requests
from bs4 import BeautifulSoup
import csv

header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

url = 'https://getlatka.com/saas-companies?page=1'


def getdata(url):
    t=requests.get(url, headers=header)
    soup=BeautifulSoup(t.text,"html.parser")
    g=soup.find_all(class_='data-table_cell__a_9gs')
    # print(g)
    r=[]
    for name in g:
        r.append(name.text)
    
    return r


def getnextpage(soup):
    #this will return the next page url
    pages=soup.find_all(class_="pagination_button__gUpxa pagination_special_button__XQ4Z3")
    a= pages[1]['href']
    url= 'https://getlatka.com/saas-companies' + str(a)
    return url

def write(r):
    with open('file.csv','w',newline='') as f:
        writer=csv.writer(f)
        for i in range(0,len(r),12):
            a=r[i:i+12]
            print(a)
            writer.writerow(a)

r=getdata(url)
print(r)
write(r)

# print(getnextpage(g))



