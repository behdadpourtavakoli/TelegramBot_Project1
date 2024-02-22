#region Urheberrechte
'''
///*-=============================================================================================-*
/// Dateiname             : bot3.py
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
import time, os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler
#endregion

#region Konstanten, Variablen und Deklarationen
'''
///*********************************************************************************************************
///* Konstanten, Variablen und Deklarationen
///*********************************************************************************************************
'''
load_dotenv()
TOKEN = os.getenv("TOKEN1")
#endregion

#region Handschriftliche Funktionen und Prozeduren
'''
///*********************************************************************************************************
///* Handschriftliche Funktionen und Prozeduren
///*********************************************************************************************************
'''

'''
/// start() Funktion zum Anzeigen der Startmeldung
/// HINZUFÜGEN durch Ingenieur B.Pourtavakoli im 1402/12/03
'''
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Your bot is up and running.")

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

    updater = Updater(TOKEN, update_queue="use_context")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

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
