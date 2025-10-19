import requests
import re
import time
import subprocess
import json
import stalcraft
import interception
import keyboard
import pyautogui
from stalcraft import AppAuth
from bs4 import BeautifulSoup

interception.inputs.keyboard = 1
interception.inputs.mouse = 10

items = [['Вещество', 'gn976',16001],['Армейский аккумулятор','55621',28001],
          ['Цветущий рыжий папоротник','z30my',8001],
          ['Цветущий северный мох','z301y',28001],['Аммиак','40vn',10001],
          ['Продвинутые инструменты','4q7pl',35000],['Горьколистник','z3ogm',120001],
          ['Пси-мая','9dk7y',9001],['Темный Лимб','gnpr5',220001],
          ['Жмых','gn956',61001],['Остатки приборов','55olq',83001],
          ['Полыхающий срачник','009n9',16001],
          ['Крупный рассольник','y40kk',25001],['Чернобыльская ромашка','34z1l',14001],['Набор специй','1dk6',5001]]

CLIENT_ID = ""
CLIENT_SECRET = ""
time.sleep(2)
app_auth = AppAuth(CLIENT_ID, CLIENT_SECRET)
headers = {'Client-Id':CLIENT_ID,'Client-Secret':CLIENT_SECRET}
session = requests.Session()
def catal(g):
    if (g == 1) & (pages<2.0):
        interception.click(1146,776,button='left',delay=1)
    elif (g==1) & (pages <3.0):
        interception.click(1135,776,button='left',delay=1)
    elif (g==2) & (pages <3.0):
        interception.click(1158,776,button='left',delay=1)
    elif (g == 1) & (pages < 4.0):
        interception.click(1121,777,button='left',delay=1)
    elif (g == 2) & (pages < 4.0):
        interception.click(1146,777,button='left',delay=1)
    elif (g == 3) & (pages <4.0):
        interception.click(1169,777,button='left',delay=1)
def buy(t,i,data):
    api = f'https://eapi.stalcraft.net/RU/auction/{items[i][1]}/lots?limit=200&sort=buyout_price'
    response = session.get(api,headers=headers)
    dato = json.loads(response.text)
    lots = dato['lots']
    lots.reverse()
    if lots.count(data):
        interception.move_to(1050,450)
        if(t==0):
            interception.click(1325,409,button='left')
            interception.click(1325,448,button='left')
            interception.press('esc')
            return
        elif(t==1):
            interception.click(1325,448,button='left')
            interception.click(1325,482,button='left')
            interception.press('esc')
            return
        elif(t==2):
            interception.click(1325,485,button='left')
            interception.click(1325,522,button='left')
            interception.press('esc')
            return
        elif(t==3):
            interception.click(1325,519,button='left')
            interception.click(1325,556,button='left')
            interception.press('esc')
            return
        elif(t==4):
            interception.click(1325,557,button='left')
            interception.click(1325,594,button='left')
            interception.press('esc')
            return
        elif(t==5):
            interception.click(1325,594,button='left')
            interception.click(1325,632,button='left')
            interception.press('esc')
            return
        elif(t==6):
            interception.click(1325,632,button='left')
            interception.click(1325,668,button='left')
            interception.press('esc')
            return
        elif(t==7):
            interception.click(1325,668,button='left')
            interception.click(1325,708,button='left')
            interception.press('esc')
            return
        elif(t==8):
            interception.click(1325,710,button='left')
            interception.click(1325,741,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==9):
            interception.click(1325,700,button='left')
            interception.click(1325,741,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==10):
            interception.click(1325,701,button='left')
            interception.click(1325,731,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==11):
            interception.click(1325,701,button='left')
            interception.click(1325,728,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==12):
            interception.click(1325,696,button='left')
            interception.click(1325,724,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==13):
            interception.click(1325,691,button='left')
            interception.click(1325,720,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==14):
            interception.click(1325,691,button='left')
            interception.click(1335,720,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==15):
            interception.click(1325,695,button='left')
            interception.click(1325,715,button='left')
            interception.press('esc')
            return
        elif(t==16):
            interception.click(1325,726,button='left')
            interception.click(1325,749,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==17):
            interception.click(1325,719,button='left')
            interception.click(1325,744,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==18):
            interception.click(1325,726,button='left')
            interception.click(1325,742,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==19):
            interception.click(1325,729,button='left')
            interception.click(1325,746,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==20):
            interception.click(1325,723,button='left')
            interception.click(1325,743,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==21):
            interception.click(1325,720,button='left')
            interception.click(1325,739,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==22):
            interception.click(1325,714,button='left')
            interception.click(1325,739,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==23):
            interception.click(1325,714,button='left')
            interception.click(1325,732,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==24):
            interception.click(1325,710,button='left')
            interception.click(1325,725,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==25):
            interception.click(1325,709,button='left')
            interception.click(1325,723,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==26):
            interception.click(1325,705,button='left')
            interception.click(1325,717,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==27):
            interception.click(1325,700,button='left')
            interception.click(1325,715,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==28):
            interception.click(1325,700,button='left')
            interception.click(1325,712,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==29):
            interception.click(1325,693,button='left')
            interception.click(1325,709,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==30):
            interception.click(1325,700,button='left')
            interception.click(1325,709,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==31):
            interception.click(1325,703,button='left')
            interception.click(1325,708,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==32):
            interception.click(1325,699,button='left')
            interception.click(1325,710,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==33):
            interception.click(1325,674,button='left')
            interception.click(1325,681,button='left')
            interception.press('esc')
            return
        elif(t==34):
            interception.click(1325,708,button='left')
            interception.click(1325,717,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==35):
            interception.click(1325,707,button='left')
            interception.click(1325,709,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==36):
            interception.click(1325,703,button='left')
            interception.click(1325,703,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==37):
            interception.click(1325,700,button='left')
            interception.click(1325,709,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==38):
            interception.click(1325,701,button='left')
            interception.click(1325,701,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==39):
            interception.click(1325,700,button='left')
            interception.click(1325,700,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==40):
            interception.click(1325,704,button='left')
            interception.click(1325,704,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==41):
            interception.click(1325,697,button='left')
            interception.click(1325,697,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==42):
            interception.click(1325,696,button='left')
            interception.click(1325,696,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==43):
            interception.click(1325,693,button='left')
            interception.click(1325,693,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==44):
            interception.click(1325,691,button='left')
            interception.click(1325,691,button='left')
            interception.press('esc')
            return
        elif(t==45):
            interception.click(1325,729,button='left')
            interception.click(1325,729,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==46):
            interception.click(1325,723,button='left')
            interception.click(1325,723,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==47):
            interception.click(1325,714,button='left')
            interception.click(1325,714,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==48):
            interception.click(1325,719,button='left')
            interception.click(1325,719,button='left')
            interception.press('esc')
            return
        interception.click(1396,775,button='left',clicks=2)
        if(t==49):
            interception.click(1325,747,button='left')
            interception.click(1325,747,button='left')
            interception.press('esc')
            return
    
a=0
i = 0
g = 0
while i<15:
    time.sleep(2)
    interception.press('esc')
    interception.click(220,1020,button='left')
    api = f'https://eapi.stalcraft.net/RU/auction/{items[i][1]}/lots?limit=200&sort=buyout_price'
    response = session.get(api,headers=headers)
    data = json.loads(response.text)
    lots = data['lots']
    total = data['total']
    print(total)
    pages = total/50
    lots.reverse()
    if total >= 200:
        i+=1
        continue
    for lot in lots:
        data_str = str(lot).replace("'", '"')
        data = json.loads(data_str)
        amount = int(data['amount'])
        buyout_price = int(data['buyoutPrice'])
        if buyout_price != 0:
            summ = buyout_price/amount
            if(summ < items[i][2]):
                print('Покупаю')
                if a < 10:
                    interception.press('p')
                    interception.click(1200, 340, button="left")
                    keyboard.write(f'{items[i][0]}')
                    interception.click(1340, 346, button="left")
                    interception.click(1310, 380, button="left")
                    interception.click(1310, 380, button="left")
                    time.sleep(0.5)
                    catal(g)
                    buy(a,i,data)
                elif (10<=a)& (a<20):
                    interception.press('p')
                    interception.click(1200, 340, button="left")
                    keyboard.write(f'{items[i][0]}')
                    interception.click(1340, 346, button="left")
                    interception.click(1310, 380, button="left")
                    interception.click(1310, 380, button="left")
                    time.sleep(0.5)
                    catal(g)
                    buy(a,i,data)
                elif (20 <= a) & (a < 30):
                    interception.press('p')
                    interception.click(1200, 340, button="left")
                    keyboard.write(f'{items[i][0]}')
                    interception.click(1340, 346, button="left")
                    interception.click(1310, 380, button="left")
                    interception.click(1310, 380, button="left")
                    time.sleep(0.5)
                    catal(g)
                    buy(a,i,data)
                elif (30 <= a) & (a< 40):
                    interception.press('p')
                    interception.click(1200, 340, button="left")
                    keyboard.write(f'{items[i][0]}')
                    interception.click(1340, 346, button="left")
                    interception.click(1310, 380, button="left")
                    interception.click(1310, 380, button="left")
                    time.sleep(0.5)
                    catal(g)
                    buy(a,i,data)
                elif 40 <= a:
                    interception.press('p')
                    interception.click(1200, 340, button="left")
                    keyboard.write(f'{items[i][0]}')
                    interception.click(1340, 346, button="left")
                    interception.click(1310, 380, button="left")
                    interception.click(1310, 380, button="left")
                    time.sleep(0.5)
                    catal(g)
                    buy(a,i,data)
                break
        a+=1
        if a == 50:
            g+=1
            a-=50
    if i==14:
        i=0
    g=0
    a=0
    i = i+1