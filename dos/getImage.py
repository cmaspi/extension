import wget
from bs4 import BeautifulSoup
import urllib.request
from threading import Thread

url = "https://aims.iith.ac.in/aims/"
def images():
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

Thread(target = images).start()
Thread(target = images).start()
Thread(target = images).start()
Thread(target = images).start()
Thread(target = images).start()
Thread(target = images).start()
Thread(target = images).start()
Thread(target = images).start()
