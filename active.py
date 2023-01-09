# Модуль обработки

import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,Update
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler,ContextTypes, ApplicationBuilder
import klava as kl

def is_Win(arr, who):
    if (((arr[0] == who) and (arr[4] == who) and (arr[8] == who)) or
            ((arr[2] == who) and (arr[4] == who) and (arr[6] == who)) or
            ((arr[0] == who) and (arr[1] == who) and (arr[2] == who)) or
            ((arr[3] == who) and (arr[4] == who) and (arr[5] == who)) or
            ((arr[6] == who) and (arr[7] == who) and (arr[8] == who)) or
            ((arr[0] == who) and (arr[3] == who) and (arr[6] == who)) or
            ((arr[1] == who) and (arr[4] == who) and (arr[7] == who)) or
            ((arr[2] == who) and (arr[5] == who) and (arr[8] == who))):
        return True
    return False


def countUndefinedCells(cellArray):
    counter = 0
    for i in cellArray:
        if i == kl.SYMBOL_UNDEF:
            counter += 1
    return counter

def game(callBackData):
    message = kl.ANSW_YOUR_TURN  
    alert = None

    buttonNumber = int(callBackData[0])  
    if not buttonNumber == 9: 
        charList = list(callBackData)  
        charList.pop(0)  
        if charList[buttonNumber] == kl.SYMBOL_UNDEF:  
            charList[buttonNumber] = kl.SYMBOL_X  
            if is_Win(charList, kl.SYMBOL_X):  
                message = kl.ANSW_YOU_WIN
            else:  
                if countUndefinedCells(charList) != 0: 
                    isCycleContinue = True
                while (isCycleContinue):
                        rand = random.randint(0, 8)  
                        if charList[rand] == kl.SYMBOL_UNDEF:  
                            charList[rand] = kl.SYMBOL_O
                            isCycleContinue = False  
                            if is_Win(charList,kl.SYMBOL_O):  
                                message = kl.ANSW_BOT_WIN
                    
        else:
            alert = kl.ALERT_CANNOT_MOVE_TO_THIS_CELL

        if countUndefinedCells(charList) == 0 and message == kl.ANSW_YOUR_TURN:
            message = kl.ANSW_DRAW

        callBackData = ''
        for c in charList:
            callBackData += c

    if message == kl.ANSW_YOU_WIN or message == kl.ANSW_BOT_WIN or message == kl.ANSW_DRAW:
        message += '\n'
        for i in range(0, 3):
            message += '\n | '
            for j in range(0, 3):
                message += callBackData[j + i * 3] + ' | '
        callBackData = None  

    return message, callBackData, alert

async def hello_comand (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет!! {update.effective_user.first_name} для игры нажми /start')


def getKeyboard(callBackData):
    keyboard = [[], [], []]  

    if callBackData != None:  
        for i in range(0, 3):
            for j in range(0, 3):
                keyboard[i].append(InlineKeyboardButton(callBackData[j + i * 3], callback_data=str(j + i * 3) + callBackData))
               
    return keyboard



async def newGame(update, _):
    data = ''
    for i in range(0, 9):
        data += kl.SYMBOL_UNDEF

    await update.message.reply_text(kl.ANSW_YOUR_TURN, reply_markup=InlineKeyboardMarkup(getKeyboard(data)))



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
   await update.message.reply_text(kl.ANSW_HELP)

