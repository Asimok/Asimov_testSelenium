import random
import time

import numpy as np
import matplotlib.pyplot as plt
import psutil as psutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# times="12:34"
# thistime = int(times[0:times.index(':')])*60+int(times[times.index(':')+1:])
# print(thistime)

# js1="var scrollt = document.documentElement.scrollTop+document.body.scrollTop"
# js2="document.body.scrollTop"
#
# option = webdriver.ChromeOptions()
# option.add_argument('disable-infobars')
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# myChrome = webdriver.Chrome()
# myChrome.get('https://pc.xuexi.cn/points/login.html')
# time.sleep(5)
# a=myChrome.execute_script(js1)
# b= myChrome.execute_script(js2)
# print(a)
# print(b)


from PIL import Image

img = Image.open('图片路径')
img.show()

time.sleep(2)

for proc in psutil.process_iter():  # 遍历当前process
    if proc.name() == "display":  # 如果process的name是display
        proc.kill()  # 关闭该process

