# -*- coding: utf-8 -*-
import telebot
import sqlite3
import random
import json
import time 

from telebot import types
from grab import Grab

def print_massage (message,status):
    ### настройка цвета для вывода на экран
    c0  =  "\033[0;37m"  ## Белый
    c1  =  "\033[1;30m"  ## Черный
    c2  =  "\033[0;31m"  ## Красный
    c3  =  "\033[0;32m"  ## Зеленый
    c4  =  "\033[1;35m"  ## Magenta like Mimosa\033[1;m
    c5  =  "\033[1;33m"  ## Yellow like Yolk\033[1;m'
    c7  =  "\033[1;37m"  ## White
    c8  =  "\033[1;33m"  ## Yellow
    c9  =  "\033[1;32m"  ## Green
    c10 =  "\033[1;34m"  ## Blue
    c11 =  "\033[1;36m"  ## Cyan
    c12 =  "\033[1;31m"  ## Red
    c13 =  "\033[1;35m"  ## Magenta
    c14 =  "\033[1;30m"  ## Black
    c15 =  "\033[0;37m"  ## Darkwhite
    c16 =  "\033[0;33m"  ## Darkyellow
    c17 =  "\033[0;32m"  ## Darkgreen
    c18 =  "\033[0;34m"  ## Darkblue
    c19 =  "\033[0;36m"  ## Darkcyan
    c20 =  "\033[0;31m"  ## Darkred
    c21 =  "\033[0;35m"  ## Darkmagenta
    c22 =  "\033[0;30m"  ## Darkblack
    c23 =  "\033[0;0m"   ## Off
    
    name_program = 'courier'
    if status == '[s]':
        print ( c0+'Старт программы: '+c8+message+c0)
    if status == '[+]':
        print ( c9+'[+] '+c0+message+c0)
    if status == '[!]':
        print (c12+'[!] '+c0+message+c0)

#### ОСНОВНОЙ БЛОК МЕНЮ ####
iz_srtok01_kl01 = 'О ценах'
iz_srtok01_kl02 = 'О книгах'
iz_srtok01_kl03 = 'О доставке'
iz_srtok02_kl01 = 'Информация об оформленных заказах'
iz_srtok02_kl02 = ''
iz_srtok02_kl03 = ''
iz_srtok03_kl01 = 'Мне нужна помощь'
iz_srtok03_kl02 = ''
iz_srtok03_kl03 = ''
def menu_main ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(iz_srtok01_kl01,iz_srtok01_kl02,iz_srtok01_kl03)
    markup.row(iz_srtok02_kl01) 
    markup.row(iz_srtok03_kl01)
    return markup

def load_staus (user_id):  #### Прочитать статус клиента. В разрезе каждого клиента.
    conn = sqlite3.connect("user.sqlite") 
    cursor = conn.cursor()
    sql = "select id,user_id,status from user where user_id = '"+str(user_id)+"'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id,user_id,status = row
    return status

def save_status (user_id,username,status):  #### Записать статус клиента. В разрезе каждого клиента
    label = 'no'
    conn = sqlite3.connect("user.sqlite") 
    cursor = conn.cursor()
    sql = "select id,user_id from user where user_id = '"+str(user_id)+"'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id,user_id = row
        label = 'yes'
    if label == 'no':
        cursor = conn.cursor()
        a = [str(user_id),str(username),'','','','','','','','','',status]    
        cursor.execute("INSERT INTO user (user_id,username,name,first_name,last_name,setting01,setting02,setting03,setting04,setting05,setting06,status)VALUES (?,?,?,?,?,?,?,?,?,?,?,?);",a)    
        conn.commit()
    else:
        sql = "UPDATE user SET status = '"+str(status)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
   
def save_param (user_id,nom,znak):
    conn = sqlite3.connect("user.sqlite") 
    cursor = conn.cursor()
    if nom == 1:
        sql = "UPDATE user SET setting01 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 2:
        sql = "UPDATE user SET setting02 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 3:        
        sql = "UPDATE user SET setting03 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 4:        
        sql = "UPDATE user SET setting04 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 5:        
        sql = "UPDATE user SET setting05 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 6:        
        sql = "UPDATE user SET setting06 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 7:        
        sql = "UPDATE user SET setting07 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 8:        
        sql = "UPDATE user SET setting08 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 9:        
        sql = "UPDATE user SET setting09 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 10:        
        sql = "UPDATE user SET setting10 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 11:        
        sql = "UPDATE user SET setting11 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 12:        
        sql = "UPDATE user SET setting12 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 13:        
        sql = "UPDATE user SET setting13 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 14:        
        sql = "UPDATE user SET setting14 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 15:        
        sql = "UPDATE user SET setting15 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 16:        
        sql = "UPDATE user SET setting16 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 17:        
        sql = "UPDATE user SET setting17 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 18:        
        sql = "UPDATE user SET setting18 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()

def load_param (user_id,nom):
    conn = sqlite3.connect("user.sqlite") 
    cursor = conn.cursor()
    sql = "select id,user_id,setting01,setting02,setting03,setting04,setting05,setting06,setting07,setting08,setting09,setting10,setting11,setting12,setting13,setting14,setting15,setting16,setting17,setting18 from user where user_id = '"+str(user_id)+"'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id,user_id,setting01,setting02,setting03,setting04,setting05,setting06,setting07,setting08,setting09,setting10,setting11,setting12,setting13,setting14,setting15,setting16,setting17,setting18 = row
        if nom == 1:
            print ('[+1]',user_id,setting01)
            return setting01
        if nom == 2:
            print ('[+2]',user_id,setting02)
            return setting02
        if nom == 3:
            print ('[+3]',user_id,setting03)
            return setting03
        if nom == 4:
            print ('[+4]',user_id,setting04)
            return setting04
        if nom == 5:
            print ('[+5]',user_id,setting05)
            return setting05
        if nom == 6:
            print ('[+6]',user_id,setting06)
            return setting06
        if nom == 7:
            print ('[+6]',user_id,setting07)
            return setting07
        if nom == 8:
            print ('[+6]',user_id,setting08)
            return setting08
        if nom == 9:
            print ('[+6]',user_id,setting09)
            return setting09
        if nom == 10:
            print ('[+6]',user_id,setting10)
            return setting10
        if nom == 11:
            print ('[+6]',user_id,setting11)
            return setting11
        if nom == 12:
            print ('[+6]',user_id,setting12)
            return setting12
        if nom == 13:
            print ('[+6]',user_id,setting13)
            return setting13
        if nom == 14:
            print ('[+6]',user_id,setting14)
            return setting14
        if nom == 15:
            print ('[+6]',user_id,setting15)
            return setting15
        if nom == 16:
            print ('[+6]',user_id,setting16)
            return setting16
        if nom == 17:
            print ('[+6]',user_id,setting17)
            return setting17
        if nom == 18:
            print ('[+6]',user_id,setting18)
            return setting18

if __name__ == "__main__":
    print_massage ('@to_ask_bot','[s]')
    print_massage ('Ver 3.2.0, Аvtor: @Pi_3dot141 (https://t.me/Pi_3dot141)','[s]')
    token = '475069061:AAE4R_aua774MYTXop0bpNZN8ZACwUzprc8'
    bot    = telebot.TeleBot(token)
    
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    username   = message.from_user.username
    first_name = message.from_user.first_name
    last_name  = message.from_user.last_name
    user_id    = message.from_user.id
    date       = message.date
    message_in = message.text
    save_status (user_id,username,'start')
    save_param (user_id,1,'')
    save_param (user_id,2,'')
    save_param (user_id,3,'')
    save_param (user_id,4,'')
    save_param (user_id,5,'')
    save_param (user_id,6,'')
    save_param (user_id,7,'')
    save_param (user_id,8,'')
    save_param (user_id,9,'')
    save_param (user_id,10,'')
    save_param (user_id,11,'')
    save_param (user_id,12,'')
    save_param (user_id,13,'')
    save_param (user_id,14,'')
    save_param (user_id,15,'')
    save_param (user_id,16,'')
    save_param (user_id,17,'')
    save_param (user_id,18,'')
    markup = menu_main ()
    message_out = 'Бот компании myinstabook помогает отследить статус заказа, а также узнать полезную информацию'
    bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
    markup = menu_main ()  
    message_out = 'Введите номер заказа:'
    bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
    save_status (user_id,username,'F001')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    user_id    = message.from_user.id 
    message_in = message.text
    username   = message.from_user.username
    first_name = message.from_user.first_name
    last_name  = message.from_user.last_name
    date       = message.date
    status     = load_staus (user_id)
    print_massage ('Новое сообщение: '+str(message_in)+'','[+]')
    
    
    ##iz_srtok01_kl01 = 'О ценах'
    
    ##iz_srtok01_kl03 = 'О доставке'
    ##iz_srtok02_kl01 = 'Информация об оформленных заказах'
    ##iz_srtok02_kl02 = ''
    ##iz_srtok02_kl03 = ''
    ##iz_srtok03_kl01 = 'Мне нужна помощь'
    ##iz_srtok03_kl02 = ''
    ##iz_srtok03_kl03 = ''    
    
    Labeladmin = 'good'
    if 1==1:
        if iz_srtok01_kl01 == message_in:
            Labeladmin = 'bad'
            message_out = '' 
            message_out = message_out + 'Сколько стоит Инстабук?'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer01")
            keyboard.add(callback_button)
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)
            #'Инстабук формата 15х15 см стоит от 1390 рублей; книга формата 20х20 см - от 2690 рублей. Книги формата 20х20 мы доставляем бесплатно в руки!'
            Labeladmin = 'no'                   
                                    
        if iz_srtok01_kl02 == message_in:   ##iz_srtok01_kl02 = 'О книгах'
            Labeladmin = 'bad'
            message_out = ''
            message_out = 'Сколько фотографий в книге?'
            ###'От 20 до 500. Вы сами выбираете схему расположения снимков в книге-на каждой странице умещается 1, 4, 5 или 9 фотографий. Страниц может быть от 20 до 70.\n'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer020")
            keyboard.add(callback_button)
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)
            
            message_out = 'Какой размер у книги?'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer021")
            keyboard.add(callback_button)
            ###15х15 см или 20х20см-на ваш выбор\n'
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)
            
            message_out = 'Как заказать книгу?'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer022")
            keyboard.add(callback_button)
            ###Необходимо перейти на сайт www.myinstabook.ru, войти в конструктор, выбрать тип оформления и заполнить страницы книги любимыми фотографиями\n'
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)

            #markup = types.InlineKeyboardMarkup()
            #btn_my_site= types.InlineKeyboardButton(text='Наш сайт', url='myinstabook.ru')
            #markup.add(btn_my_site)
            ###bot.send_message(user_id, "Нажми на кнопку и перейди на наш сайт.", reply_markup = markup)
            
            message_out = 'Каков срок изготовления книги?'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer023")
            keyboard.add(callback_button)
            ##"3-4 рабочих дня с момента оплаты заказа'
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)


            message_out = 'Технические особенности книги'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer024")
            keyboard.add(callback_button)
            ###Химическая печать, толстые листы с пластиковой прослойкой, фотобумага\n'            
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)
            Labeladmin = 'no'
            
                   
                                     
        if iz_srtok01_kl03 == message_in:
            Labeladmin = 'bad'
            message_out = ''
            message_out = 'Как оплатить доставку книги?'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer030")
            keyboard.add(callback_button)            
            ## Доставка оплачивается при получении заказа за исключением тех случаев, когда она осуществляется за пределы РФ\n'
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)            
            
            message_out = 'Как осуществляется доставка?'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer031")
            keyboard.add(callback_button)            
            ##Мы доставляем книг транспортной компанией dpd до пункта выдачи в вашем городе или лично в руки, а также Почтой России. Обращаем ваше внимание на то, что книги формата 20х20 мы доставляем бесплатно в руки в том случае, если в вашем городе есть пункт выдачи транспортной компании dpd.\n'
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)            
                        
            message_out = 'Стоимость доставки почтой РФ'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer032")
            keyboard.add(callback_button)            
            ##Стоимость доставки Почтой России зависит от веса посылки и региона, в который она направлена. Как правило, она составляет 250-350 рублей. Более точный расчёт вам помогут сделать наши специалисты\n'
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)            
            
            message_out = 'Стоимость доставки транспортной компании'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer033")
            keyboard.add(callback_button)            
            ##Тут мы с тобой хотели брать данные с сайта dpd\n'
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)
                        
            Labeladmin = 'no'       
                                     
        if iz_srtok02_kl01 == message_in:
            Labeladmin = 'bad'
            message_out = ''            
            message_out = 'Как узнать номер моего заказа?'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer040")
            keyboard.add(callback_button)
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)            
            ##После того, как вы завершили процесс оформления книги, на вашу почту придёт информационное письмо, в котором будет указан номер вашей книги, а также информация о способах оплаты заказа\n'
            
            message_out = 'Со мной не связался специалист'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer041")
            keyboard.add(callback_button)
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)            
            ## Введите номер заказа'
            ### (Человек вводит номер заказа, в вк идёт сообщение «клиент с номером таким-то заказа ожидает связи)
            ### И клиенту в телеграмме выходит сообщение
            ### Ваша информация обрабатывается, в ближайшее время с Вами свяжется специалист.
            
            message_out = 'Каков статус моего заказа?\n'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer042")
            keyboard.add(callback_button)
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)            
            Labeladmin = 'no'       
                        
        if iz_srtok03_kl01 == message_in:
            Labeladmin = 'bad' 
            message_out = ''
            message_out = 'Мне нужна техническая помощь в работе с конструктором'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer050")
            keyboard.add(callback_button)
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)                        
            
            ##Также как и в прошлом пункте, сообщение идёт с проблемой в вк, клиенту сообщение
            ##Ваша информация обрабатывается, в ближайшее время с Вами свяжется специалист.
            
            message_out = 'Со мной не связался специалист'
            keyboard = types.InlineKeyboardMarkup()
            callback_button = types.InlineKeyboardButton(text="Ответ", callback_data="Answer051")
            keyboard.add(callback_button)            
            bot.send_message(user_id,message_out,parse_mode='HTML', reply_markup=keyboard)            
            
            ##(Человек вводит номер заказа, в вк идёт сообщение «клиент с номером таким-то заказа ожидает связи)
            ##И клиенту в телеграмме выходит сообщение
            ##Ваша информация обрабатывается, в ближайшее время с Вами свяжется специалист.            
            Labeladmin = 'no'  
            
            
    if Labeladmin == 'good':
        ### МОДУЛЬ ЕСЛИ НЕ НАЖАТЫ ОСНОВНЫЕ КНОПКИ ###
        message_out = 'Поиск заказа по номеру: <b>'+str(message_in+'</b>')
        bot.send_message(user_id,message_out,parse_mode='HTML')       
        ### МОДУЛЬ АВТОРИЗАЦИИ НА СЕРВИСЕ ###
        g  = Grab()
        url = 'https://fotoport67.amocrm.ru/private/api/auth.php'
        g.setup(post={'USER_LOGIN': 'foto-port@mail.ru','USER_HASH': 'c221c7318ee7c9a1c17f122ee32dafe3'})
        try:
            g.setup(post={'USER_LOGIN': 'foto-port@mail.ru','USER_HASH': 'c221c7318ee7c9a1c17f122ee32dafe3'})
            g.go(url)
        except:
            print ('[+] Повторное запрос на авторизацию')
            time.sleep(4)
            g.setup(post={'USER_LOGIN': 'foto-port@mail.ru','USER_HASH': 'c221c7318ee7c9a1c17f122ee32dafe3'})
            g.go(url)  
        body = g.doc.body.decode('utf-8')
        nomer = 0  # Колличество заказов вытащино из базы 
        sm    = 0  # Смещение при запросе
        label = '' # Метка поиска данных
        while sm < 2:
            sm = sm +1
            url = 'https://fotoport67.amocrm.ru/api/v2/leads?limit_rows=500&limit_offset='+str(sm*500)+''
            g.go(url)
            body = g.doc.body
            bodynew = body.decode('utf-8')
            parsed_string = json.loads(bodynew)
            embedded = parsed_string['_embedded']
            items = embedded['items']
            for n in items:
                imya  = nomer,n['name']
                nomer = nomer + 1
                ID_zakaza = n['custom_fields']
                for h in ID_zakaza:
                    if str(h).find ('ID заказа') != -1:
                        s = h['values']
                        for f in s:
                            poisk = f['value'] 
                            if poisk == message_in:
                                label = 'mes'
                                message_out = 'Название заказа: <b>'+str(imya)+'</b>\n'
                                status_zakaz = str(n['status_id'])
                            
                                if status_zakaz == '16955785':
                                    status_zakaz = 'Заказ принят и ожидает оплаты'                            
                                if status_zakaz == '16955788':
                                    status_zakaz = 'Заказ оплачен и отправлен в печать'                            
                                if status_zakaz == '16955791':
                                    status_zakaz = 'Заказ оплачен и отправлен в печать'                            
                                if status_zakaz == '16955794':
                                    status_zakaz = 'Заказ в производстве'                            
                                if status_zakaz == '17742886':
                                    status_zakaz = 'Заказ передан в службу доставки'                            
                                if status_zakaz == '142':
                                    status_zakaz = 'Заказ передан в службу доставки'                            
                                                        
                                message_out = message_out +'Статус заказа: '+status_zakaz
                                bot.send_message(user_id,message_out,parse_mode='HTML')

        if label == '':
            message_out = 'Заказ не найден'
            bot.send_message(user_id,message_out,parse_mode='HTML')
        else:           
            message_out = 'Поиск закончен '
            bot.send_message(user_id,message_out,parse_mode='HTML')       
                                 
        message_out = 'Введите еще один номер заказа: '
        bot.send_message(user_id,message_out,parse_mode='HTML')       


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    user_id = call.message.chat.id
    if call.data == "Answer01":
        message_out = '<b>Сколько стоит Инстабук?</b>\nИнстабук формата 15х15 см стоит от 1390 рублей; книга формата 20х20 см - от 2690 рублей. Книги формата 20х20 мы доставляем бесплатно в руки!'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')
        
        
    if call.data == "Answer020":
        message_out = '<b>Сколько фотографий в книге?</b>\nОт 20 до 500. Вы сами выбираете схему расположения снимков в книге-на каждой странице умещается 1, 4, 5 или 9 фотографий. Страниц может быть от 20 до 70.\n\n'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')        
    if call.data == "Answer021":
        message_out = '<b>Какой размер у книги?</b>\n15х15 см или 20х20см-на ваш выбор'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')        
    if call.data == "Answer022":
        message_out = '<b>Как заказать книгу?</b>Необходимо перейти на сайт www.myinstabook.ru, войти в конструктор, выбрать тип оформления и заполнить страницы книги любимыми фотографиями\n'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')        
    if call.data == "Answer023":
        message_out = '<b>Каков срок изготовления книги?</b>\n3-4 рабочих дня с момента оплаты заказа'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')        
    if call.data == "Answer024":
        message_out = '<b>Технические особенности книги</b>\nХимическая печать, толстые листы с пластиковой прослойкой, фотобумага'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')
                
    if call.data == "Answer030":
        message_out = '<b>Как оплатить доставку книги?</b>\nДоставка оплачивается при получении заказа за исключением тех случаев, когда она осуществляется за пределы РФ\n'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')        
    if call.data == "Answer031":
        message_out = '<b>Как осуществляется доставка?</b>\nМы доставляем книг транспортной компанией dpd до пункта выдачи в вашем городе или лично в руки, а также Почтой России. Обращаем ваше внимание на то, что книги формата 20х20 мы доставляем бесплатно в руки в том случае, если в вашем городе есть пункт выдачи транспортной компании dpd.'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')        
    if call.data == "Answer032":
        message_out = '<b>Стоимость доставки почтой РФ</b>\nСтоимость доставки Почтой России зависит от веса посылки и региона, в который она направлена. Как правило, она составляет 250-350 рублей. Более точный расчёт вам помогут сделать наши специалисты'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')        
    if call.data == "Answer033":
        message_out = '<b>Стоимость доставки транспортной компании</b>\nСтоимость доставки транспортной компании'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')        
                
    if call.data == "Answer040":
        message_out = '<b>Как узнать номер моего заказа?</b>\nПосле того, как вы завершили процесс оформления книги, на вашу почту придёт информационное письмо, в котором будет указан номер вашей книги, а также информация о способах оплаты заказа'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')        
    if call.data == "Answer041":
        message_out = '<b>Со мной не связался специалист</b>\nВведите номер заказа'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')        
    if call.data == "Answer042":
        message_out = '<b>Каков статус моего заказа?\n</b>\n'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')        
        
    if call.data == "Answer050":
        message_out = '<b>Мне нужна техническая помощь в работе с конструктором</b>\nОпишите, пожалуйста, вашу проблему'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')
                
    if call.data == "Answer051":
        message_out = '<b>Со мной не связался специалист</b>\nВведите номер заказа'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out,parse_mode='HTML')        
        

bot.polling()
  
