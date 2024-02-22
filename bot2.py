#region Urheberrechte
'''
///*-=============================================================================================-*
/// Dateiname             : bot2.py
/// Version               : 1.0.0.0
/// Beginn                : 2024-02-22 (1402/12/03)
/// Letzte Aktualisierung : 2024-02-22 (1402/12/03)
/// Autor                 : Ingenieur Behdad Pourtavakoli
/// Warenzeichen          : Behdad Software Developers Group™
/// ----------------------------------------------------------------------------------------------
/// Copyright© 1380-1402,2001-2024 von B.S.D Group™
/// Alle Rechte vorbehalten.
/// ----------------------------------------------------------------------------------------------
///
/// Beschreibung: Lernen Sie von YouTube PW Skills Tech. Wie erstelle ich einen Telegram-Bot mit 
///               Python? von der Website (https://www.youtube.com/watch?v=Agkf4hEprwE)
///
///-=============================================================================================-*///
'''
#endregion

#region Wichtige Module und Header-Dateien
'''
///*********************************************************************************************************
///* Wichtige Module und Header-Dateien
///*********************************************************************************************************
'''
import time, os, requests, urllib.parse, logging
from dotenv import load_dotenv
import telebot, yfinance as yf
from telegram.ext import *
#endregion

#region Konstanten, Variablen und Deklarationen
'''
///*********************************************************************************************************
///* Konstanten, Variablen und Deklarationen
///*********************************************************************************************************
'''
strMessage = "Hello User! Behdad Pourtavakoli is here.\n\n"
strMessage += "Hallo Benutzer! Behdad Pourtavakoli ist hier.\n\n"
strMessage += "Mein_Telegram_Bot"
strMessage = urllib.parse.quote(strMessage)

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
TOKEN = os.getenv("TOKEN1")
bot = telebot.TeleBot(TOKEN)
#endregion

#region Handschriftliche Funktionen und Prozeduren
'''
///*********************************************************************************************************
///* Handschriftliche Funktionen und Prozeduren
///*********************************************************************************************************
'''

'''
/// Start_Commmand() Funktion zum Anzeigen der Startmeldung
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/03
'''
async def Start_Commmand(update, context):
    await update.message.reply_text("Hallo! Willkommen beim Mein zweiter Telegram BOT.")

'''
/// Help_Commmand() Funktion zum Anzeigen der Telegram BOT-Hilfe
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/03
'''
async def Help_Commmand(update, context):
    await update.message.reply_text(
        """
        Hi there! I'm Telegram BOT created by Behdad Pourtavakoli. Please follow these commands: -
        
        /start - start message
        /help - Show the commands Help
        /hila1 - Show Hila Message 1
        /hila2 - Show Hila Message 2
        /help2 - Show the another commands list Help
        """
    )

'''
/// Error_Log() Funktion zum Anzeigen einer Nachricht
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/03
'''
async def Error_Log(update, context):
    await logger.warning("Update '%s' caused error '%s;", update, context.error)

'''
/// Hila1_Commmand() Funktion zum Anzeigen einer Nachricht
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/03
'''
async def Hila1_Commmand(update, context):
    await update.message.reply_text("Hallo! Ich heiße Hila Pourtavakoli.")

'''
/// Hila2_Commmand() Funktion zum Anzeigen einer Nachricht
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/03
'''
async def Hila2_Commmand(update, context):
    await update.message.reply_text("سلام. اسم من هیلا پورتوکلی است.")


'''
/// BOT_Get_ShortInfo() Funktion zum Abrufen von BOT-Kurzinformationen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/03
'''
async def BOT_Get_ShortInfo(strBOT_Token):
    response = requests.get("https://api.telegram.org/bot" + strBOT_Token + "/getMe")
    return(await response.content, '\n', response.content == response.text)

'''
/// BOT_Get_Updates() Funktion zum Abrufen der BOT-Updates
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/03
'''
async def BOT_Get_Updates(strBOT_Token):
    response = requests.get("https://api.telegram.org/bot" + strBOT_Token + "/getUpdates")
    return(await response.content, '\n', response.content == response.text)

'''
/// BOT_Send_Message() Funktion zum Abrufen von BOT-Kurzinformationen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/03
'''
async def BOT_Send_Message(strToken, strMethod, intChat_Id, strMessage):
    response = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(strToken, strMethod),
            data={'chat_id': intChat_Id, 'text': strMessage}
        ).json()


'''
/// Help2_Commmand() Funktion zum Anzeigen der Telegram BOT-Hilfe
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/03
'''
async def Help2_Commmand(update, context):
    await update.message.reply_text(
        """
        Available Commands :-
        /youtube - To get the youtube URL
        /linkedin - To get the LinkedIn profile URL
        /gmail - To get gmail URL
        /geeks - To get the GeeksforGeeks URL
        """
    )

async def Gmail_URL_Commmand(update, context):
    await update.message.reply_text("Your gmail link here mailto:bpourtavakoli@gmail.com")

async def YouTube_URL_Commmand(update, context):
    await update.message.reply_text("Youtube Link => https://www.youtube.com/channel/UCJ0ASROLBIFjjw_hRWOi3CQ")

async def LinkedIn_URL_Commmand(update, context):
    await update.message.reply_text("LinkedIn URL => https://www.linkedin.com/in/behdad-pourtavakoli-69b03b4b/")

async def Geeks_URL_Commmand(update, context):
    await update.message.reply_text("GeeksforGeeks URL => https://auth.geeksforgeeks.org/user/bpourtavakoli/")


#async def Unknown_Log(update, context):
#    await update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)

#async def Unknown_Text(update, context):
#    await update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)

async def Unknown_TC(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


@bot.message_handler(commands=["start"])
def start(strMessage):
    bot.reply_to(strMessage, "Hey! Wie geht's?")

@bot.message_handler(commands=["hello"])
def hello(message):
    bot.send_message(message.chat.id, "Hallo! Wie geht's?")

@bot.message_handler(commands=["wsb"])
def get_stocks(message):
    response = ""
    stocks = ['gme', 'amc', 'nok']
    stock_data = []
    for stock in stocks:
        data = yf.download(tickers=stock, period='2d', interval='1d')
        data = data.reset_index()
        response += f"-----{stock}-----\n"
        stock_data.append([stock])
        columns = ["stock"]
        for index, row in data.iterrows():
            stock_position = len(stock_data) - 1
            price = round(row["Close"], 2)
            format_date = row["Date"].strftime("%m/%d")
            response += f"{format_date}: {price}\n"
            stock_data[stock_position].append(price)
            columns.append(format_date)
        print()
    response = f"{columns[0] : <10}{columns[1] : ^10}{columns[2] : >10}\n"
    for row in stock_data:
        response += f"{row[0] : <10}{row[1] : ^10}{row[2] : >10}\n"
    response += "\nStock Data"
    print(response)
    bot.send_message(message.chat.id, response)

def stock_request(message):
    request = message.text.split()
    if (len(request) < 2 or request[0].lower() not in "price"):
        return(False)
    else:
        return(True)

@bot.message_handler(func=stock_request)
def get_stocks(message):
    request = message.text.split()[1]
    data = yf.download(tickers=request, period='5m', interval='1m')
    if (data.size > 0):
        data = data.reset_index()
        data["format_date"] = data["Datetime"].dt.strftime("%m/%d %I:%M %p")
        data.set_index("format_date", inplace=True)
        print(data.to_string())
        bot.send_message(message.chat.id, data["Close"].to_string(header=False))
    else:
        bot.send_message(message.chat.id, "No data!?")

@bot.message_handler(func=stock_request)
def send_price(message):
    pass

#endregion

#region Standardfunktionen und -verfahren
'''
///*********************************************************************************************************
///* Standardfunktionen und -verfahren
///*********************************************************************************************************
'''

'''
/// WinMain() enthält Hauptanweisungen und aufrufende Funktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/03
'''
def WinMain():
    intStartTime = time.time()

    print("Telegram BOT Token: ", TOKEN, end='\n\n', sep='')


    print("Einen Bot starten...")
    bot.polling()
    print("Einen Bot beenden...")
    
    intEndTime = time.time()
    intElapsedTime = intEndTime - intStartTime
    print("Elapsed Time: %s ms" % round(intElapsedTime, 3))
#endregion
 
#region Hauptprogramm
'''
///*********************************************************************************************************
///* Hauptprogramm
///*********************************************************************************************************
'''

'''
/// Hauptprogramm, enthält Hauptanweisungen und Aufruffunktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/03
'''
if (__name__ == "__main__"):
    WinMain()
#endregion
