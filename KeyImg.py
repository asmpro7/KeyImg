# Made by Ahmed ElSaeed
# 21/10/2023
# TG: @asmprotk


import concurrent.futures
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument('--headless')
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.minimize_window()
driver.implicitly_wait(20)
Search = input('Search for: ')
driver.get(f'https://www.wallpaperflare.com/search?wallpaper={Search}')
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 1500);")
time.sleep(2)

images = driver.find_elements(By.CSS_SELECTOR,'img[class="lazy loaded"]')
images = [img.get_attribute('src') for img in images]

def DnIMG(img:str):
    ImgData = requests.get(img).content
    imgName = img.split('/')[-1]
    with open(imgName,'wb') as mg:
        mg.write(ImgData)
    return f'processing {imgName}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(DnIMG,images)
    for res in results:
        print(res)
        
print('Done!')