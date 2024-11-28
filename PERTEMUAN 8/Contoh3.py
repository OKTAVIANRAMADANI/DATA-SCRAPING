from bs4 import BeautifulSoup
import requests
import os
import MainFungsi
from urllib.parse import urljoin

url = 'https://dongengceritarakyat.com'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
datax = soup.find_all('img')

images = [urljoin(url, img['src']) for img in datax if 'src' in img.attrs]

direktori = "PERTEMUAN 8/Hasil Gambar"

# Debugging untuk verifikasi
print(f"Attempting to create directory: {direktori}")
MainFungsi.CreateDirectory(direktori)
print("Directory created successfully")

for gmb in images:
    response = requests.get(gmb)
    if response.status_code == 200:
        fileName = os.path.basename(gmb)
        MainFungsi.WriteToFile2(direktori, fileName, response)
        print(f"Downloaded: {fileName}")
    else:
        print(f"Failed to download {gmb}: {response.status_code}")