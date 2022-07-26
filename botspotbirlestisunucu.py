# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 10:36:26 2022

@author: okmen
"""


##############################################################################
import talib as ta
import pandas as pd
import pickle
import time
from binance.client import Client
import numpy as np
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import pyperclip 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import threading
import sys
from binance_f import RequestClient
from binance_f.model import *
from binance_f.constant.test import *
from binance_f.base.printobject import *
global client
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import glob
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pickle
import glob
import os





def spotthread():
        global client
        apiid=""

        namebot="Flavves- spot bot"
        username="flavvesspotbot"
        link="t.me/flavvesspotbot"     
        api_key="sz5J1OLyEnF2HQ2fpXnijHh0Sz8huYFPty4pv1REl4pyolJmSm8n96KQD5yrsl4t"
        api_secret="VmfhyTYIlsREYNiXhuYgOlqIlx0a3K5NNPGvOo0hWD2ZotOagS7QsKfkQmrAkNUr"
        client = Client(api_key, api_secret)
        ardardagondermeengelleyicisi=False
        with open("koinler.txt", "r") as dosya:    
                coinler=dosya.readline()

        coinlers=coinler.split(";")
        coinlers.pop(-1)
        ardardaengelleyici=[]
        for koin in coinlers:
                sembol=koin.split(",")[0]
                ardardaengelleyici.append(sembol+",False")
        while 1:
            
            with open("koinler.txt", "r") as dosya:    
                coinler=dosya.readline()

            coinler=coinler.split(";")
            coinler.pop(-1)
            time.sleep(1)
            
            for koin in coinler:
                    if coinler !=coinlers:
                        with open("koinler.txt", "r") as dosya:    
                                coinler=dosya.readline()
                
                        coinlers=coinler.split(";")
                        coinlers.pop(-1)
                        ardardaengelleyici=[]
                        coinler=coinlers
                        for koin in coinlers:
                                sembol=koin.split(",")[0]
                                ardardaengelleyici.append(sembol+",flavves")
            
          
            for koin in coinler:
            
                    time.sleep(0.01)
                    sembol=koin.split(",")[0]
                    interval=koin.split(",")[1]
                    print(sembol)
                    
                    ########################

                    try:    
                        #TALİBE BAŞLA   
                        
                        klines = client.get_klines(symbol=sembol, interval=interval,limit = 500)
                        
                        opens = [float(entry[1]) for entry in klines]
                        high = [float(entry[2]) for entry in klines]
                        low = [float(entry[3]) for entry in klines]
                                     
                        close = [float(entry[4]) for entry in klines]
                        last_closing_price = close[-1]
                        previous_closing_price = close[-2]
                        close_array = np.asarray(close)
                        close_finished = close_array[:-1]
                        
                        macd = ta.MACD(close_array,16,24,2)      
                        #########################    
                        ilkkırmızı=macd[2][-1]
                        mavi=macd[0][-1] 
                        premavi=macd[0][-2] 
                        pre2mavi=macd[0][-3] 
                        kırmızı=macd[1][-1]   
                        prekırmızı=macd[1][-2]  
                        pre2kırmızı=macd[1][-3] 
                        #########################
                    except:pass
                    
                    # olmadı 
                    #print("chatid"+str(chatid))
                    Close = close[-1]
                    High=high[-1]
                    Low=low[-1]
                    
                    PP = (High + Low + Close) / 3
                    R1 = 2 * PP - Low
                    S1 = 2 * PP - High
                    R2 = PP + (High - Low)
                    S2 = PP - (High - Low)
                    R3 = PP + 2 * (High - Low)
                    S3 = PP - 2 * (High - Low)
                    
                    
                    veriler={"pivot":{"R1":R1,"R2":R2,"R3":R3,"S1":S1,"S2":S2,"S3":S3},
                             "macd":{"ilkkirmizi":ilkkırmızı,"mavi":mavi,"kırmızı":kırmızı}}
                    #self.sonuclar.emit(veriler)
                    sinyal="-"
                    
                    print("R1:%s \nR2:%s \nR3:%s \n------------"%(R1,R2,R3))
                    print("S1:%s \nS2:%s \nS3:%s \n"%(S1,S2,S3))
                    print("kırmızı: %s | mavi: %s"%(kırmızı,mavi))
                    
                    def num_sim(n1, n2):
                    
                      return 1 - abs(n1 - n2) / (n1 + n2)

                    kesisme=num_sim(mavi,kırmızı)
                    A=mavi
                    B=kırmızı
                    yuzde=((B - A)/A ) * 100
                    yuzde=abs(yuzde)
                    sayac=0
                    for engel in ardardaengelleyici:
                        sembol_engelle=engel.split(",")[0]
                        boolean_engelle=engel.split(",")[1]
                        if sembol_engelle==sembol:
                            ardardagondermeengelleyicisi=boolean_engelle
                            break
                        sayac=sayac+1
                    
                    if ardardagondermeengelleyicisi==("False"):
                        
                        if (mavi>kırmızı and prekırmızı>premavi and pre2kırmızı>pre2mavi) == True:
                            
                            ardardaengelleyici[sayac]=sembol+",True"
                            
                          
                            
                            
                            
                            tickers = client.get_ticker()
                            currentprices=client.get_symbol_ticker(symbol=sembol)["price"]
                            currentprices=float(currentprices)
                            
                            print("R1:%s \nR2:%s \nR3:%s \n------------"%(R1,R2,R3))
                            print("S1:%s \nS2:%s \nS3:%s \n"%(S1,S2,S3))
                            print("kırmızı: %s | mavi: %s"%(kırmızı,mavi))
                            
                            
                            sinyal="AL"
                            
                            gonder="""
                            #%s\n\n➥ %s\n---------------------\n\n%s -\n\n%s -\n\n%s -\n\n---------------------
                            """%(sembol[:-4]+" / "+sembol[-4:],round(currentprices,4),round(R1,3),round(R2,3),round(R3,3))
                            gonder=gonder+"/"+str(mavi>kırmızı)+"/"+str(prekırmızı>premavi)+"/"+str(pre2kırmızı>pre2mavi)+"/"
                        
                            ######################
                            bot = telegram.Bot(apiid)
                            
                            bot.send_photo("-612215140",
                                           "https://drive.google.com/file/d/1kxagFfI00CzwXstesP1-H5fJnFFp1byY/view?usp=sharing",
                                           caption=gonder)
                            
                            """
                            document = open('resimler/Buy.gif', 'rb')
                            bot.sendDocument("-612215140",
                                             document = document,
                                             caption=gonder)
                            
                            """
                            
                    elif ardardagondermeengelleyicisi=="True":
                        if kırmızı>mavi == True:
                            ardardaengelleyici[sayac]=sembol+",False"
                    time.sleep(1)    
                        
       
def admin():
        global client
        apiid=""

        namebot="flavvesadmin"
        username="flavvesadminbot"
        link="t.me/flavvesadminbot"       
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

        logger = logging.getLogger(__name__)
                
                
        def admin(update, context):
            try:
                gelen_mesaj=update["message"]["text"]
            except Exception as e:
                gelen_mesaj="yokflavves"
                print("hata mesajı",e)
            
            
            if gelen_mesaj =="yokflavves":
                print("mesaj okunamadı")
            else:
                
                ######################## ÖRNEK
                # veri="BTCUSDT,15m;ETHUSDT,30m;SOLUSDT,1h;AAVEUSDT,4h;TRXUSDT,2h;"
                gelen_mesaj=gelen_mesaj.split("/admin ")[1]
                
                with open("koinler.txt", "w") as dosya:    
                    dosya.write(gelen_mesaj)
                    
        def adminfuture(update, context):
            try:
                gelen_mesaj=update["message"]["text"]
            except Exception as e:
                gelen_mesaj="yokflavves"
                print("hata mesajı",e)
            
            
            if gelen_mesaj =="yokflavves":
                print("mesaj okunamadı")
            else:
                
                ######################## ÖRNEK
                # veri="BTCUSDT,15m;ETHUSDT,30m;SOLUSDT,1h;AAVEUSDT,4h;TRXUSDT,2h;"
                gelen_mesaj=gelen_mesaj.split("/adminfuture ")[1]
                
                with open("koinlerfuture.txt", "w") as dosya:    
                    dosya.write(gelen_mesaj)

        
        def help(update, context):
            """Send a message when the command /help is issued."""
            update.message.reply_text('Yardım geliyor')
        
        
       
        
        
        def error(update, context):
            """Log Errors caused by Updates."""
            logger.warning('Update "%s" caused error "%s"', update, context.error)
        
        
        def main():
            try:
                    
                token = apiid
                updater = Updater(token, use_context=True)
                dp = updater.dispatcher
                #komutlar burada
                dp.add_handler(CommandHandler("admin", admin))
                dp.add_handler(CommandHandler("adminfuture", adminfuture))
                dp.add_handler(CommandHandler("help", help))
                
    
                dp.add_error_handler(error)
                
                
                
                
                
                
                updater.start_polling()
                updater.idle()
            except:pass
        
        
        if __name__ == '__main__':
            main()  
  

def futurebinance():
        global client
        apiid=""

        namebot="Flavves- future bot"
        username="flavvesfuturebot"
        link="t.me/flavvesfuturebot"   
        ardardagondermeengelleyicisifuture=False
        with open("koinlerfuture.txt", "r") as dosya:    
                coinler=dosya.readline()

        coinlers=coinler.split(";")
        coinlers.pop(-1)
        ardardaengelleyicifuture=[]
        for koin in coinlers:
                sembol=koin.split(",")[0]
                ardardaengelleyicifuture.append(sembol+",flavves")
                
        while 1:
            
            with open("koinlerfuture.txt", "r") as dosya:    
                coinler=dosya.readline()
            
                
            coinler=coinler.split(";")
            coinler.pop(-1)
            time.sleep(1)
            for koin in coinler:
                    if coinler !=coinlers:
                        with open("koinlerfuture.txt", "r") as dosya:    
                                coinler=dosya.readline()
                
                        coinlers=coinler.split(";")
                        coinlers.pop(-1)
                        ardardaengelleyicifuture=[]
                        for koin in coinlers:
                                sembol=koin.split(",")[0]
                                ardardaengelleyicifuture.append(sembol+",flavves")
                        
                        
                    time.sleep(0.01)
                    sembol=koin.split(",")[0]
                    interval=koin.split(",")[1]
                    
                    ########################
      
                    request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
                
                    try:    

                        result = request_client.get_candlestick_data(symbol=sembol, interval=interval, 
    												startTime=None, endTime=None)
 
                        df = pd.DataFrame([t.__dict__ for t in result])
                        klines=df.values.tolist()
                        opens = [float(entry[1]) for entry in klines]
                        high = [float(entry[2]) for entry in klines]
                        low = [float(entry[3]) for entry in klines]                               
                        close = [float(entry[4]) for entry in klines]
                        close_array = np.asarray(close)
                        close_finished = close_array[:-1]
                        macd = ta.MACD(close_array,16,24,2)
                        ilkkırmızı=macd[2][-1]
                        mavi=macd[0][-1] 
                        premavi=macd[0][-2] 
                        pre2mavi=macd[0][-3] 
                        kırmızı=macd[1][-1]   
                        prekırmızı=macd[1][-2]  
                        pre2kırmızı=macd[1][-3]   
                    except Exception as e:
                        print(e)
                    
                    try:
                        Close = close[-1]
                        High=high[-1]
                        Low=low[-1]
                        
                        PP = (High + Low + Close) / 3
                        R1 = 2 * PP - Low
                        S1 = 2 * PP - High
                        R2 = PP + (High - Low)
                        S2 = PP - (High - Low)
                        R3 = PP + 2 * (High - Low)
                        S3 = PP - 2 * (High - Low)
                        
                        
                        veriler={"pivot":{"R1":R1,"R2":R2,"R3":R3,"S1":S1,"S2":S2,"S3":S3},
                                 "macd":{"ilkkirmizi":ilkkırmızı,"mavi":mavi,"kırmızı":kırmızı}}
                        #self.sonuclar.emit(veriler)
                        sinyal="-"
                        if mavi>kırmızı:
                            sinyal="AL"
                        else:
                            sinyal="SAT"
        
                    except Exception as e:
                        print(e)
                    
                    
                    def num_sim(n1, n2):
                        
                          return 1 - abs(n1 - n2) / (n1 + n2)
    
                    kesisme=num_sim(mavi,kırmızı)
                    try:
                            
                        sayac=0
                        for engel in ardardaengelleyicifuture:
                            sembol_engelle=engel.split(",")[0]
                            boolean_engelle=engel.split(",")[1]
                            if sembol_engelle==sembol:
                                ardardagondermeengelleyicisi=boolean_engelle
                                break
                            sayac=sayac+1
                        if sayac > len(ardardaengelleyicifuture-1):
                            sayac=sayac-1
                    except:pass
                    
                    
                        
                    if ((mavi>=kırmızı) and (1.010>=kesisme>=0.990) and pre2kırmızı > pre2mavi and (ardardagondermeengelleyicisi==("False") or ardardagondermeengelleyicisi==("flavves"))) == True:
                        ardardaengelleyicifuture[sayac]=sembol+",True"
                        pricefuture = request_client.get_mark_price(symbol=sembol)
                        pricefuture=pricefuture.markPrice
                        pricefuture=float(pricefuture)
                        print("R1:%s \nR2:%s \nR3:%s \n------------"%(R1,R2,R3))
                        print("S1:%s \nS2:%s \nS3:%s \n"%(S1,S2,S3))
                        print("kırmızı: %s | mavi: %s"%(kırmızı,mavi))
                        
                        
                        gonder="""
                            #%s\n\n➥ %s\n---------------------\n\n%s -\n\n%s -\n\n%s -\n\n---------------------
                            """%(sembol[:-4]+" / "+sembol[-4:],round(pricefuture,6),round(R1,6),round(R2,6),round(R3,6))
                            
                        bot = telegram.Bot(apiid)
                        
                        
                        bot.send_photo("-729778822",
                                       "https://drive.google.com/file/d/1qmE5Rq86pD-zszKxotZk8RAfUk6o9byn/view?usp=sharing",
                                       caption=gonder)
                        
                        """
                        document = open('resimler/Long.gif', 'rb')
                        bot.sendDocument("-729778822",
                                         document = document,
                                         caption=gonder)
                        
                        """
                        
                        
                        
                    
                    elif (kırmızı>=mavi and 1.010>=kesisme>=0.990 and pre2mavi > pre2kırmızı and (ardardagondermeengelleyicisi==("True") or ardardagondermeengelleyicisi==("flavves"))) == True:
                        ardardaengelleyicifuture[sayac]=sembol+",False"
                        
                        pricefuture = request_client.get_mark_price(symbol=sembol)
                        pricefuture=pricefuture.markPrice
                        pricefuture=float(pricefuture)
                        print("R1:%s \nR2:%s \nR3:%s \n------------"%(R1,R2,R3))
                        print("S1:%s \nS2:%s \nS3:%s \n"%(S1,S2,S3))
                        print("kırmızı: %s | mavi: %s"%(kırmızı,mavi))
                        
                        
                        gonder="""
                            #%s\n\n➥ %s\n---------------------\n\n%s -\n\n%s -\n\n%s -\n\n---------------------
                            """%(sembol[:-4]+" / "+sembol[-4:],round(pricefuture,6),round(S1,6),round(S2,6),round(S3,6))
                            
                        bot = telegram.Bot(apiid)
                        
                        bot.send_photo("-729778822",
                                       "https://drive.google.com/file/d/109aj1SLdYWukqtpZ0bEVFBrWwfw_5z4-/view?usp=sharing",
                                       caption=gonder)
                        
                        
                        """
                        document = open('resimler/Short.gif', 'rb')
                        bot.sendDocument("-729778822",
                                         document = document,
                                         caption=gonder)
                        
                        """
                        
#########################################################




global graphapiid
graphapiid="5452698189:AAF86SIaZ4-LB5Dp_rojzwE1qOwayRR_1cU"

def grafiktelegram():
        global client
        global graphapiid
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome('/root/flavves/chromedriver',chrome_options=chrome_options)
        #driver = webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)
        driver.get("https://tr.tradingview.com/chart/?symbol=BINANCE%3ABTCBUSD")
    
    
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        print("cockie yuklendi")
        driver.refresh()

        menuxpath="/html/body/div[2]/div[3]/div/div/div/div"
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

        logger = logging.getLogger(__name__)
        
        def f(update, context):
            
                    try:
                        gelen_mesaj=update["message"]["text"]
                        chatid=update["message"]["chat"]["id"]
                    except Exception as e:
                        gelen_mesaj="yokflavves"
                        print("hata mesajı",e)
                    
                    
                    if gelen_mesaj =="yokflavves":
                        print("mesaj okunamadı")
                    else:
                        sembolual=gelen_mesaj.split("/f ")[1].upper()
                        
                    api_key=""
                    api_secret=""
                    client = Client(api_key, api_secret)
                    tickers = client.get_ticker()
                    currentprices=client.get_symbol_ticker(symbol=sembolual)["price"]
                    currentprices=float(currentprices)
                    #sembolual="BTCUSDT"
                    degisim="%"
                    for qeq in range(0,len(tickers)):
                        if tickers[qeq]["symbol"]==sembolual:
                            degisim=tickers[qeq]["priceChangePercent"]
                    #degisim="(% "+degisim+")"
                    
                    if "-" in degisim :
                        degisim="📉"+"(% "+degisim+")"
                    else:
                        degisim="📈 "+"(% "+degisim+")"
                       
                        
                    gonder="""
                        #%s %s\n\nPrice = $%s
                        """%(sembolual[:-4]+"/"+sembolual[-4:],degisim,round(currentprices,6))
                        
        
                    update.message.reply_text(gonder)
        def g(update, context):
            
            try:
                gelen_mesaj=update["message"]["text"]
                chatid=update["message"]["chat"]["id"]
            except Exception as e:
                gelen_mesaj="yokflavves"
                print("hata mesajı",e)
            
            
            if gelen_mesaj =="yokflavves":
                print("mesaj okunamadı")
            else:
                sembolual=gelen_mesaj.split("/g ")[1].upper()+"USDT"
                url="https://tr.tradingview.com/chart/2aQLONo5/?symbol=BINANCE%3A"+sembolual
            driver.get(url)
            time.sleep(4)
            #ss aldırıyom
            combine_keys = ActionChains(driver)
            combine_keys.key_down(Keys.CONTROL).key_down(Keys.ALT).key_down('s').perform()
            time.sleep(4)
            #linke git
            
            resim= glob.glob("/root/flavves/*.png")
            resminadi=resim[0].split("/")[-1]
            #gönderme
            
            bot = telegram.Bot(graphapiid)
            bot.send_photo(chatid, photo=open("/root/flavves/"+resminadi, 'rb'))
            time.sleep(1)
            os.remove(resminadi)   
            print("dosya kaldırıldı")
                    
            
            
            """
            gorseladi="deneme.png"
            while 1:     
                yapistir=pyperclip.paste()
                time.sleep(0.5)
                if yapistir[0:27]=="https://www.tradingview.com":  
                    a="guncel fiyat 123"

                    bot = telegram.Bot(graphapiid)
                    bot.send_photo(str(chatid), yapistir)
                    
                    
                    pyperclip.copy("deneme")
                    break
            """
                
        def gb(update, context):
            
            try:
                gelen_mesaj=update["message"]["text"]
                chatid=update["message"]["chat"]["id"]
            except Exception as e:
                gelen_mesaj="yokflavves"
                print("hata mesajı",e)
            
            
            if gelen_mesaj =="yokflavves":
                print("mesaj okunamadı")
            else:
                sembolual=gelen_mesaj.split("/gb ")[1].upper()+"_USDT"
                url="https://www.binance.com/tr/trade/"+sembolual+"?theme=dark&type=spot"
            driver.get(url)
            time.sleep(4)
            #ss aldırıyom
            combine_keys = ActionChains(driver)
            combine_keys.key_down(Keys.ALT).key_down('s').perform()
            #linke git
            gorseladi="deneme.png"
            while 1:     
                yapistir=pyperclip.paste()
                time.sleep(0.5)
                if yapistir[0:27]=="https://www.tradingview.com":  
                    a="guncel fiyat 123"

                    bot = telegram.Bot(graphapiid)
                    bot.send_photo(str(chatid), yapistir)
                    
                    
                    pyperclip.copy("deneme")
                    break    
        
        
        def help(update, context):
            """Send a message when the command /help is issued."""
            update.message.reply_text('Yardım geliyor')
            
        
       
        
        def error(update, context):
            """Log Errors caused by Updates."""
            logger.warning('Update "%s" caused error "%s"', update, context.error)
        
        
        def main():
            try:
                token = graphapiid
                updater = Updater(token, use_context=True)
                dp = updater.dispatcher
                #komutlar burada
                dp.add_handler(CommandHandler("g", g))
                #dp.add_handler(CommandHandler("gb", gb))
                dp.add_handler(CommandHandler("f", f))
                dp.add_handler(CommandHandler("help", help))
                
              
                dp.add_error_handler(error)
                
                
                
                
                
                
                
                updater.start_polling()
                updater.idle()
        
            except:pass
        if __name__ == '__main__':
            main()









#########################################################
  
y = threading.Thread(target=spotthread)
y.start()     
  
x = threading.Thread(target=admin)
x.start()    

z = threading.Thread(target=futurebinance)
z.start()  

w = threading.Thread(target=grafiktelegram)
w.start()  


































