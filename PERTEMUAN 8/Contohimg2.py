import requests
from bs4 import BeautifulSoup

url = 'https://dongengceritarakyat.com'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
datax = soup.find_all('img')
    
images = []

for img in datax:
    img_url = img.get('data-lazy-src')
    if img_url is not None and img_url.endswith(('.jpg')):
        images.append(img_url)

print(images)