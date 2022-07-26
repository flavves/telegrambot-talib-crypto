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
from tradingview_ta import TA_Handler




def spotthread():
        global client
        apiid="enter your id"

        namebot="Flavves- spot bot"
        username="flavvesspotbot"
        link="t.me/flavvesspotbot"     

        client = Client()
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
                        ilkkırmızı=macd[2][-2]
                        mavi=macd[0][-2] 
                        premavi=macd[0][-3] 
                        pre2mavi=macd[0][-4] 
                        kırmızı=macd[1][-2]   
                        prekırmızı=macd[1][-3]  
                        pre2kırmızı=macd[1][-4] 
                        #########################
                    except:pass

                  
                    #self.sonuclar.emit(veriler)
                    sinyal="-"
                    

                    print("kırmızı: %s | mavi: %s"%(kırmızı,mavi))
                    
                    def num_sim(n1, n2):
                    
                      return 1 - abs(n1 - n2) / (n1 + n2)

                    kesisme=num_sim(mavi,kırmızı)
                    A=mavi
                    B=kırmızı
                    yuzde=((B - A)/A ) * 100
                    yuzde=abs(yuzde)
                    
                    
                    for engel in ardardaengelleyici:
                        sembol_engelle=engel.split(",")[0]
                        boolean_engelle=engel.split(",")[1]
                        if sembol_engelle==sembol:
                            ardardagondermeengelleyicisi=boolean_engelle
                            break
                        
                        
                    try:
                        
                        sira=ardardaengelleyici.index(sembol+",False")
                    except:
                        try:
                            sira=ardardaengelleyici.index(sembol+",flavves")
                        except:
                            try:
                                sira=ardardaengelleyici.index(sembol+",True")
                            except:
                                pass
                    
                    
                  
                    
                    if ardardagondermeengelleyicisi==("False") or ardardagondermeengelleyicisi==("flavves"):
                    #if "0"=="0":
                        
                        #if (mavi>kırmızı and prekırmızı>premavi and pre2kırmızı>pre2mavi) == True:
                        if (mavi>=kırmızı and prekırmızı>premavi) == True:
                            
                           
                            
                            #ardardaengelleyici[sira]=sembol+",True"
                                                        
                                                        
                            try:
                                    curr = TA_Handler(
                                        symbol=sembol,
                                        screener="crypto",
                                        exchange="binance",
                                        interval=interval
                                    )
                            except Exception as e:       
                                print(e)
                            
                            indicators = curr.get_analysis().indicators
                            
                            R1 = indicators['Pivot.M.Fibonacci.R1']
                            S1 = indicators['Pivot.M.Fibonacci.S1']
                            R2 = indicators['Pivot.M.Fibonacci.R2']
                            S2 = indicators['Pivot.M.Fibonacci.S2']
                            R3 = indicators['Pivot.M.Fibonacci.R3']
                            S3 = indicators['Pivot.M.Fibonacci.S3']
 
                            
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
                            gonder=gonder
                        
                            ######################
                            
                            if (R1 > currentprices)==True:
                                
                                bot = telegram.Bot(apiid)  
                                bot.send_photo("-612215140",
                                               "https://drive.google.com/file/d/1kxagFfI00CzwXstesP1-H5fJnFFp1byY/view?usp=sharing",
                                               caption=gonder)
                            
                            
                            
                            try:
                        
                 
                                str1 = ""
                                # traverse in the string 
                                for i in ardardaengelleyici:
                                    str1 += i 
                                ardardaengelleyicistrolarakal=(str1)
                                
                                
                                gonder2="""
                                        #%s\n\n➥ kırmızı: %s\nmavi: %s\nmavi kırmzıdan büyük mü: %s\nardardagonderme: %s\nsıra: %s\nyüzde: %s\nkesisme: %s\nkoin: %s\n ardardagondermeengelleyicisi: %s\n
                                        """%(sembol[:-4]+" / "+sembol[-4:],kırmızı,mavi,str(mavi>kırmızı),
                                        ardardaengelleyicistrolarakal,str(sira),yuzde,kesisme,koin,ardardagondermeengelleyicisi)
                                        
                                gonder2=gonder2
                                
                                chatidsi="762580886"
                                butunverilerid="5439377005:AAGKKJRQNeuWz92_5JIPy55JgfyiPtDr9EA"
                                bot2 = telegram.Bot(butunverilerid)  
                                bot2.send_photo(chatidsi,
                                               "https://drive.google.com/file/d/1kxagFfI00CzwXstesP1-H5fJnFFp1byY/view?usp=sharing",
                                               caption=gonder2)
                            except Exception as e:
                                print(e)
                            
                            
                            
                            """
                            document = open('resimler/Buy.gif', 'rb')
                            bot.sendDocument("-612215140",
                                             document = document,
                                             caption=gonder)
                            
                            """
                            
                    elif ardardagondermeengelleyicisi=="True":
                        if kırmızı>mavi == True:
                            
                            ardardaengelleyici[sira]=sembol+",False"
                    time.sleep(0.01)
                    
                    
                    
                    
                    
                        
       
def admin():
        global client
        apiid="enter your id"

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
        apiid="enter your id"

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
                    
                    
                        
                    #if ((mavi>=kırmızı) and (1.010>=kesisme>=0.990) and pre2kırmızı > pre2mavi and (ardardagondermeengelleyicisi==("False") or ardardagondermeengelleyicisi==("flavves"))) == True:
                        
                        
                    if ((mavi>=kırmızı) and  prekırmızı > premavi and (ardardagondermeengelleyicisi==("False") or ardardagondermeengelleyicisi==("flavves"))) == True:
                        ardardaengelleyicifuture[sayac]=sembol+",True"
                        pricefuture = request_client.get_mark_price(symbol=sembol)
                        pricefuture=pricefuture.markPrice
                        pricefuture=float(pricefuture)
                        
                        try:
                                    curr = TA_Handler(
                                        symbol=sembol,
                                        screener="crypto",
                                        exchange="binance",
                                        interval=interval
                                    )
                        except Exception as e:       
                                print(e)
                        try:   
                            indicators = curr.get_analysis().indicators
                            
                            R1 = indicators['Pivot.M.Fibonacci.R1']
                            S1 = indicators['Pivot.M.Fibonacci.S1']
                            R2 = indicators['Pivot.M.Fibonacci.R2']
                            S2 = indicators['Pivot.M.Fibonacci.S2']
                            R3 = indicators['Pivot.M.Fibonacci.R3']
                            S3 = indicators['Pivot.M.Fibonacci.S3']
                        
                        
                        except:pass
                        
                        print("R1:%s \nR2:%s \nR3:%s \n------------"%(R1,R2,R3))
                        print("S1:%s \nS2:%s \nS3:%s \n"%(S1,S2,S3))
                        print("kırmızı: %s | mavi: %s"%(kırmızı,mavi))
                        
                        
                        gonder="""
                            #%s\n\n➥ %s\n---------------------\n\n%s -\n\n%s -\n\n%s -\n\n---------------------
                            """%(sembol[:-4]+" / "+sembol[-4:],round(pricefuture,6),round(R1,6),round(R2,6),round(R3,6))
                
                            
                
                        if (R1 > pricefuture)==True:
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
                        
                        
                        
                    
                    #elif (kırmızı>=mavi and 1.010>=kesisme>=0.990 and pre2mavi > pre2kırmızı and (ardardagondermeengelleyicisi==("True") or ardardagondermeengelleyicisi==("flavves"))) == True:

                    elif (kırmızı>=mavi and  premavi > prekırmızı and (ardardagondermeengelleyicisi==("True") or ardardagondermeengelleyicisi==("flavves"))) == True:
                        
                        
                        ardardaengelleyicifuture[sayac]=sembol+",False"
                        
                        pricefuture = request_client.get_mark_price(symbol=sembol)
                        pricefuture=pricefuture.markPrice
                        pricefuture=float(pricefuture)
                        
                        
                        try:
                                    curr = TA_Handler(
                                        symbol=sembol,
                                        screener="crypto",
                                        exchange="binance",
                                        interval=interval
                                    )
                        except Exception as e:       
                                print(e)
                        try:   
                            indicators = curr.get_analysis().indicators
                            
                            R1 = indicators['Pivot.M.Fibonacci.R1']
                            S1 = indicators['Pivot.M.Fibonacci.S1']
                            R2 = indicators['Pivot.M.Fibonacci.R2']
                            S2 = indicators['Pivot.M.Fibonacci.S2']
                            R3 = indicators['Pivot.M.Fibonacci.R3']
                            S3 = indicators['Pivot.M.Fibonacci.S3']
                        
                        except:pass
                        
                        
                        print("R1:%s \nR2:%s \nR3:%s \n------------"%(R1,R2,R3))
                        print("S1:%s \nS2:%s \nS3:%s \n"%(S1,S2,S3))
                        print("kırmızı: %s | mavi: %s"%(kırmızı,mavi))
                        
                        
                        gonder="""
                            #%s\n\n➥ %s\n---------------------\n\n%s -\n\n%s -\n\n%s -\n\n---------------------
                            """%(sembol[:-4]+" / "+sembol[-4:],round(pricefuture,6),round(S1,6),round(S2,6),round(S3,6))
                        
                            
                        if (S1 < pricefuture)==True:
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
                        
                    api_key="api"
                    api_secret="api"
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






























