from PIL import Image,ImageDraw
import math
import time
import numpy as np
from selenium import webdriver
from collections import Counter
import os
import pandas as pd
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def getpic(fn,str):
    url = 'http://www.diyiziti.com/xingkai'
    yf = {'profile.default_content_settings.popups': 0,  # 防止保存弹窗
          'download.default_directory': '/Users/pptg/Documents/python/pigyyf',  # 设置默认下载路径
          "profile.default_content_setting_values.automatic_downloads": 1  # 允许多文件下载
          }
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('prefs', yf)
    opt.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    opt.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    opt.add_argument('--hide-scrollbars')  # 隐藏滚动条，应对一些特殊页面
    driver = webdriver.Chrome(options=opt)
    driver.get(url)
    driver.find_element_by_id("FontInfoId").send_keys("漂亮行楷字体")
    driver.find_element_by_id("Content").send_keys(str)
    driver.find_element_by_id("btnSelImageBgColor").click()
    driver.find_element_by_class_name('nocolor').click()
    driver.find_element_by_id("btnOnline").click()
    driver.find_element_by_id("btnDownload").click()
    time.sleep(2)
    driver.quit()

    files = '/Users/pptg/Documents/python/pigyyf/'
    for filename in os.listdir(files):
        if filename.endswith('.PNG') and filename != "db.png":
            os.rename(filename, fn)

getpic('id.png','2017211111')
getpic('name.png','pptg')
getpic('class.png','冷酸灵牙膏学院')
getpic('number.png','09-099')

# img0 = Image.open('db.png')
img0 = Image.open('db2.png')    # 新的橙色
img1 = Image.open('id.png')
img2 = Image.open('name.png')
img3 = Image.open('class.png')
img4 = Image.open('number.png')
img5 = Image.open('head.png')
w = 250
h = 340
img6 = img5.resize((w,h), Image.ANTIALIAS)


opacity = 1
sx = 205
sy = 390
for x in range(sx, sx+w):
  for y in range(sy, sy+h):
        p = img0.getpixel((x, y))
        b = img6.getpixel((x-sx,y-sy))
        p = [int(p[i]*(1-opacity) + b[i]*opacity) for i in range(3)]
        img0.putpixel((x, y), tuple(p))

opacity = [0,0,0,1]
sx = 760
sy = 330
for x in range(sx,sx+570):
    for y in range(sy,sy+120):
        p = img0.getpixel((x, y))
        b = img1.getpixel((x - sx, y - sy))
        p = [int(p[i] * (1 - opacity[i]) + (255-b[i]) * opacity[i]) for i in range(4)]
        img0.putpixel((x, y), tuple(p))

opacity = [0,0,0,1]
sx = 760
sy = 420
for x in range(sx,sx+570):
    for y in range(sy,sy+120):
        p = img0.getpixel((x, y))
        b = img2.getpixel((x - sx, y - sy))
        p = [int(p[i] * (1 - opacity[i]) + (255-b[i]) * opacity[i]) for i in range(4)]
        img0.putpixel((x, y), tuple(p))

opacity = [0,0,0,1]
sx = 760
sy = 530
for x in range(sx,sx+570):
    for y in range(sy,sy+120):
        p = img0.getpixel((x, y))
        b = img3.getpixel((x - sx, y - sy))
        p = [int(p[i] * (1 - opacity[i]) + (255-b[i]) * opacity[i]) for i in range(4)]
        img0.putpixel((x, y), tuple(p))

opacity = [0,0,0,1]
sx = 760
sy = 650
for x in range(sx,sx+570):
    for y in range(sy,sy+120):
        p = img0.getpixel((x, y))
        b = img4.getpixel((x - sx, y - sy))
        p = [int(p[i] * (1 - opacity[i]) + (255-b[i]) * opacity[i]) for i in range(4)]
        img0.putpixel((x, y), tuple(p))

img0.show()





