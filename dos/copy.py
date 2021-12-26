import wget
from bs4 import BeautifulSoup
import urllib.request
import time

url = "https://aims.iith.ac.in/aims/"

for _ in range(50000):
    webUrl = urllib.request.urlopen(url)
    html_doc = str(webUrl.read())


    soup = BeautifulSoup(html_doc, 'html.parser')
    try:
        download = soup.find(id="appCaptchaLoginImg")['src']
    except:
        # print(soup.find(id="appCaptchaLoginImg"))
        # exit()
        continue

    file = wget.download("https://aims.iith.ac.in/"+download,out="images/")
    # time.sleep(1)

