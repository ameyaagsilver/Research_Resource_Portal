from os import link
from time import sleep
import requests, bs4 , sys
from threading import Thread
# print('Googling...')
# keyword = 'Beaglebone circuit'
# res = requests.get('https://google.com/search?q=' + keyword)

# soup = bs4.BeautifulSoup(res.text, "html.parser")

# linkElems = soup.select('div#main > div > div > div > a')  
# numOpen = min(5, len(linkElems))
# for i in range(numOpen):
#     print("*********************************************************************")
#     if len(linkElems[i].select('h3'))!=0:
#         print("".join(linkElems[i].select('h3')[0].select('div')[0].strings)) 
#         print('http://google.com' + linkElems[i].get("href"))

# class a(Thread):
#     def run(self):
#         for i in range(5):
#             print(i)
#             sleep(1)
def webScrapperForAddNewResource(keyword):
    print('Googling...')
    res = requests.get('https://google.com/search?q=' + keyword)

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    linkElems = soup.select('div#main > div > div > div > a')  
    numOpen = min(25, len(linkElems))
    linkCount = 0
    for i in range(numOpen):

        if len(linkElems[i].select('h3'))!=0 and linkCount<3:
            print("*********************************************************************")
            heading = "".join(linkElems[i].select('h3')[0].select('div')[0].strings)
            url = 'http://google.com' + linkElems[i].get("href")
            print(heading)
            print(url)
            if url:
                linkCount+=1
def foo():
    threadAddResource = Thread(target=webScrapperForAddNewResource, args=('Arduino', ))
    threadAddResource.start()
    return
foo()

