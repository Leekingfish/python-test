import requests
from bs4 import BeautifulSoup

url = "https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/"
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, "html.parser")
a = soup.find_all(class_="comments-area")
for b in a:
    talk = b.find(class_="comment-content")
    print(talk.text)
