import sys
import requests
import webbrowser
import bs4
import re
print("!!!!!!!!!!!!!!!!!!!!!!!!!!")

res = requests.get('https://www.leetcode.com')
soup = bs4.BeautifulSoup(res.text)
# print(soup)
# linkElements = soup.select(r'href=[\'"]?([^\'" >]+)')
linkElements=[]
for i in soup.find_all('a'):
    linkElements.append(i.get('href'))
print(len(linkElements))
linkToOpen = min(5, len(linkElements))
for i in range(linkToOpen):
    print(linkElements[i])
