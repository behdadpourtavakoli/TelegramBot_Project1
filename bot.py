#region Urheberrechte
'''
///*-=============================================================================================-*
/// Dateiname             : bot.py
/// Version               : 1.0.0.0
/// Beginn                : 2024-02-21 (1402/12/02)
/// Letzte Aktualisierung : 2024-02-21 (1402/12/02)
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
import telegram.ext
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
#endregion

#region Handschriftliche Funktionen und Prozeduren
'''
///*********************************************************************************************************
///* Handschriftliche Funktionen und Prozeduren
///*********************************************************************************************************
'''

'''
/// Start_Commmand() Funktion zum Anzeigen der Startmeldung
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/02
'''
async def Start_Commmand(update, context):
    await update.message.reply_text("Hallo! Willkommen beim Mein zweiter Telegram BOT.")

'''
/// Help_Commmand() Funktion zum Anzeigen der Telegram BOT-Hilfe
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/02
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
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/02
'''
async def Error_Log(update, context):
    await logger.warning("Update '%s' caused error '%s;", update, context.error)

'''
/// Hila1_Commmand() Funktion zum Anzeigen einer Nachricht
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/02
'''
async def Hila1_Commmand(update, context):
    await update.message.reply_text("Hallo! Ich heiße Hila Pourtavakoli.")

'''
/// Hila2_Commmand() Funktion zum Anzeigen einer Nachricht
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/02
'''
async def Hila2_Commmand(update, context):
    await update.message.reply_text("سلام. اسم من هیلا پورتوکلی است.")


'''
/// BOT_Get_ShortInfo() Funktion zum Abrufen von BOT-Kurzinformationen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/02
'''
async def BOT_Get_ShortInfo(strBOT_Token):
    response = requests.get("https://api.telegram.org/bot" + strBOT_Token + "/getMe")
    return(await response.content, '\n', response.content == response.text)

'''
/// BOT_Get_Updates() Funktion zum Abrufen der BOT-Updates
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/02
'''
async def BOT_Get_Updates(strBOT_Token):
    response = requests.get("https://api.telegram.org/bot" + strBOT_Token + "/getUpdates")
    return(await response.content, '\n', response.content == response.text)

'''
/// BOT_Send_Message() Funktion zum Abrufen von BOT-Kurzinformationen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/02
'''
async def BOT_Send_Message(strToken, strMethod, intChat_Id, strMessage):
    response = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(strToken, strMethod),
            data={'chat_id': intChat_Id, 'text': strMessage}
        ).json()


'''
/// Help2_Commmand() Funktion zum Anzeigen der Telegram BOT-Hilfe
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/02
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
#endregion

#region Standardfunktionen und -verfahren
'''
///*********************************************************************************************************
///* Standardfunktionen und -verfahren
///*********************************************************************************************************
'''

'''
/// WinMain() enthält Hauptanweisungen und aufrufende Funktionen
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/02
'''
def WinMain():
    intStartTime = time.time()

    load_dotenv()
    TOKEN = os.getenv("TOKEN1")
    print("Telegram BOT Token: ", TOKEN, end='\n\n', sep='')

    ## data = GetBOT_Updates(strBOT_Token)
    ## data = BOT_Get_ShortInfo(strBOT_Token)
    ## print("BOT Updates: ", data, '\n', sep='', end='')
    ## print(data['message_id.id'])
    ## strWEB_ADDRESS = "https://api.telegram.org/bot" + strBOT_Token + "/sendMessage?chat_id=" + strChatID + "&text=" + strMessage
    ## print("Web request: ", strWEB_ADDRESS, '\n', sep='', end='')
    ## print("Web request response: ", requests.get(strWEB_ADDRESS), '\n', sep='', end='')
    ## strChatID = "670023094"
    ## strBOT_Token = "7195803806:AAGSWNByd1IfHjdn7TnERS39vs3eCiOGFr8" # @Mein_zweite_Telegram_Bot
    ## print("BOT Updates: ", BOT_Get_Updates(strBOT_Token), '\n', sep='', end='')
    ## strWEB_ADDRESS = "https://api.telegram.org/bot" + strBOT_Token + "/sendMessage?chat_id=" + strChatID + "&text=" + strMessage
    ## print("Web request: ", strWEB_ADDRESS, '\n', sep='', end='')
    ## print("Web request response: ", requests.get(strWEB_ADDRESS), '\n', sep='', end='')

    print("Einen Bot starten...")
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', Start_Commmand))
    application.add_handler(CommandHandler('help', Help_Commmand))
    application.add_handler(CommandHandler('help2', Help2_Commmand))
    application.add_handler(CommandHandler('hila1', Hila1_Commmand))
    application.add_handler(CommandHandler('hila2', Hila2_Commmand))

    application.add_handler(CommandHandler('youtube', YouTube_URL_Commmand))
    application.add_handler(CommandHandler('help', Help2_Commmand))
    application.add_handler(CommandHandler('linkedin', LinkedIn_URL_Commmand))
    application.add_handler(CommandHandler('gmail', Gmail_URL_Commmand))
    application.add_handler(CommandHandler('geeks', Geeks_URL_Commmand))
    
    #application.add_handler(MessageHandler(telegram.ext.filters.TEXT, Unknown_Log))
    #application.add_handler(MessageHandler(telegram.ext.filters.COMMAND, Unknown_Log))
    #application.add_handler(MessageHandler(telegram.ext.filters.TEXT, Unknown_Text))

    application.add_handler(MessageHandler(telegram.ext.filters.COMMAND, Unknown_TC))
    application.add_handler(MessageHandler(telegram.ext.filters.TEXT, Unknown_TC))
    application.add_error_handler(Error_Log)
    
    application.run_polling()
    application.idle()
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
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/02
'''
if (__name__ == "__main__"):
    WinMain()
#endregion
