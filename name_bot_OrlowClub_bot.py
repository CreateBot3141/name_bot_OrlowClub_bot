
def test_id (user_id,namebot,message_in):
    import requests
    import fake_useragent
    from bs4 import BeautifulSoup
    otv = message_in #'5140293'
    password  = 'Podkjf3141'
    email = 'Kupinov82@gmail.com'
    url = 'https://partner.quotex.com/ru/sign-in'
    session = requests.Session()
    user = fake_useragent.UserAgent().random
    header = {'user-agent': user}
    data   = {'email': email,'password': password,'remember': 'on'}
    responce = session.post(url, data=data, headers=header)
    cookie_dict = [{'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value} for key in session.cookies]
    session2 = requests.Session()
    for cookies in cookie_dict:
        session2.cookies.set(**cookies)
    profile_info = 'https://partner.quotex.com/ru/statistics'
    res = session2.get(profile_info, headers=header)
    url1 = 'https://partner.quotex.com/ru/statistics?chart=day&order=traders-desc&dateFrom=&dateTo=&linkId=&search=' + str(otv)
    respo = session2.get(url1).text
    try:
        soup = BeautifulSoup(respo, 'lxml')    
        block = soup.find('div', id='kt_content')
        blockchecker = block.find('table', id='kt_advance_table_widget_2')
        check = blockchecker.find_all('span')[1].text
        ready = check.replace(' ', '')
        ready1 = ready.replace('#', '')
        ready2 = ready1.replace('\n', '')
        print ('ready2',ready2) 
    except Exception as e:
        ready2 = ''

    if ready2 == otv:
        return ready2
    else:    
        return 0

def test_depozit (user_id,namebot,message_in):
    
    import iz_func
    id     = 0
    wallet = ''
    db,cursor = iz_func.connect ()
    sql = "select id,wallet from bot_active_user where user_id = "+str(user_id)+" and namebot = '"+str(namebot)+"';"
    cursor.execute(sql)
    data = cursor.fetchall()
    for rec in data: 
        id     = rec['id']
        wallet = rec['wallet']
        print ('[id] wallet:',id,wallet)    
    import requests
    import fake_useragent
    from bs4 import BeautifulSoup
    otv = wallet #'5140293'
    password  = 'Podkjf3141'
    email = 'Kupinov82@gmail.com'
    url = 'https://partner.quotex.com/ru/sign-in'
    session = requests.Session()
    user = fake_useragent.UserAgent().random
    header = {'user-agent': user}
    data   = {'email': email,'password': password,'remember': 'on'}
    responce = session.post(url, data=data, headers=header)
    cookie_dict = [{'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value} for key in session.cookies]
    session2 = requests.Session()
    for cookies in cookie_dict:
        session2.cookies.set(**cookies)
    profile_info = 'https://partner.quotex.com/ru/statistics'
    res = session2.get(profile_info, headers=header)
    url1 = 'https://partner.quotex.com/ru/statistics?chart=day&order=traders-desc&dateFrom=&dateTo=&linkId=&search=' + str(otv)
    respo = session2.get(url1).text
    try:
        soup = BeautifulSoup(respo, 'lxml')    
        block = soup.find('div', id='kt_content')
        blockchecker = block.find('table', id='kt_advance_table_widget_2')
        check = blockchecker.find_all('td')[2].text
        #check = blockchecker.find_all('span')[1].text
        ready = check.replace(' ', '')
        ready1 = ready.replace('#', '')
        ready2 = ready1.replace('\n', '')
        ready2 = int(ready2)
        print ('ready2',ready2) 
    except Exception as e:
        ready2 = 0
    return ready2

def answer_message (user_id,namebot,message_in,answer):
    print ('[+] ???????????????? ???????????????????? ???????? ',answer)
    import iz_telegram
    if answer != 0:             
        #import telebot
        #token = iz_telegram.get_token (namebot)
        #bot   = telebot.TeleBot(token) 
        #photo = open('good.jpg', 'rb')
        #bot.send_photo(user_id, photo)
        iz_telegram.save_active_user (namebot,user_id,'','','','','',answer,'','','')
        #message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'???????????????? ????????','S',0)
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'???????????????? ??????????','S',0) 
    else:
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'?????? ???? ????????????','S',0)

def filtr_kod (message_in):
    toosm = message_in[0:2]
    filter_code = "???? ??????"
    if toosm == "ID":
        filter_code = "?????? ??????"
    if toosm == "id":
        filter_code = "?????? ??????"
    try:
        sm = int (toosm)
        filter_code = "?????? ??????"
    except Exception as e:
        pass
    return filter_code    

def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import time
    import iz_func
    import iz_telegram    
    import datetime
    label_send = 'send'


    if message_in == '????????????':
        label_send = 'no send'
        iz_telegram.save_variable (user_id,namebot,"status",'')
        status = ""
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'????????????2','S',0)


    if status == '???????? ??????????':
        iz_telegram.save_variable (user_id,namebot,"status",'???????? ??????????')
        db,cursor = iz_func.connect ('')
        sql = "select id,user_id,username,first_name,last_name from bot_user where namebot = '"+str(namebot)+"';"
        cursor.execute(sql)
        data_user = cursor.fetchall()  
        for rec_user in data_user: 
            id_user,user_id,username,firstname,lastname = rec_user.values()
            print ('[+]',id_user,user_id,username,firstname,lastname)



    if message_in == '/send':
        iz_telegram.save_variable (user_id,namebot,"status",'???????? ??????????')



    if message_in == '/start':
        label_send = 'no send'
        iz_telegram.send_photo (user_id,namebot,'my_photo.jpg')
        iz_telegram.save_variable (user_id,namebot,"????????????????????","start")
        message_out,menu,answer = iz_telegram.wait_send_message (user_id,namebot,'???????????????????? ?????? ????????????','S',0,10,"????????????????????") 
        iz_telegram.save_variable (user_id,namebot,"????????","start")
        message_out,menu,answer = iz_telegram.wait_send_message (user_id,namebot,'?????? ??????????','S',0,60*60,"????????") 

    if message_in == '?????? ??????????':
        label_send = 'no send'
        iz_telegram.save_variable (user_id,namebot,"????????","")

    if message_in == '???????? ????????': 
        label_send = 'no send'
        iz_telegram.save_variable (user_id,namebot,"????????","")

    if message_in == '??????????':
        label_send = 'no send'
        import telebot
        token = iz_telegram.get_token (namebot)
        bot   = telebot.TeleBot(token) 
        try:
            photo = open('get_kod.jpg', 'rb')
            bot.send_photo(user_id, photo)
        except:
            pass
        #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 
        #message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'????????????1','S',0) 
        message_out,menu = iz_telegram.get_message (user_id,'????????????1',namebot)        
        from telebot import types
        markup = types.InlineKeyboardMarkup()
        url_button1 = types.InlineKeyboardButton(text="???????????????????? ?????????????? ????????", url="https://quotex.com/sign-up/?lid=31231")
        url_button2 = types.InlineKeyboardButton(text="Android ????????????????????", url="quotex.onelink.me/Feal?pid=aff&c=31232")
        markup.add(url_button1)
        markup.add(url_button2)
        mn11 = types.InlineKeyboardButton(text="?? ?????? ?????????????",callback_data="?? ?????? ?????????????")
        markup.add(mn11)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 

    if message_in == '?? ?????? ?????????????':
        label_send = 'no send'
        iz_telegram.send_forward (user_id,namebot,4060,-509375701)
        message_out,menu = iz_telegram.get_message (user_id,'????????????2',namebot)        
        markup = iz_telegram.menu_url ("????????????","???????????? ??????????????????????","Android ????????????????????","t.me/orlow_otz","quotex.com/sign-up/?lid=31231","quotex.onelink.me/Feal?pid=aff&c=31232","???????????? ID","???????????? ID")
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 

    if message_in == '???????????? ID':
        label_send = 'no send'
        iz_telegram.save_variable (user_id,namebot,"status",'???????????? ID')

    if status == '???????????? ID':
        label_send = 'no send'
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'???????????????? ???????? ???? ??????????????','S',0)
        iz_telegram.save_variable (user_id,namebot,"status",'')
        answer = test_id (user_id,namebot,message_in)
        answer_message (user_id,namebot,message_in,answer)

    if message_in == '????' or  message_in == '????':
        label_send = 'no send'
        #iz_telegram.save_variable (user_id,namebot,"status",'???????????? ID')
        #import telebot
        #token = iz_telegram.get_token (namebot)
        #bot   = telebot.TeleBot(token) 
        #video = open('2.mp4', 'rb')
        #bot.send_video(user_id, video)
        import telebot
        token = iz_telegram.get_token (namebot)
        bot   = telebot.TeleBot(token) 
        bot.forward_message(user_id, message_id=4082, from_chat_id=-509375701) 
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'???????????????????? ??????????','S',0)         

    if message_in == '?????????????????? ????????????!':
        label_send = 'no send'
        #iz_telegram.save_variable (user_id,namebot,"status",'???????????? ID')
        #import telebot
        #token = iz_telegram.get_token (namebot)
        #bot   = telebot.TeleBot(token) 
        #video = open('2.mp4', 'rb')
        #bot.send_video(user_id, video)
        import telebot
        token = iz_telegram.get_token (namebot)
        bot   = telebot.TeleBot(token) 
        bot.forward_message(user_id, message_id=4082, from_chat_id=-509375701) 
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'???????????????????? ??????????','S',0)         

    if message_in == '??????????????????' or message_in == '??????????????????':
        label_send = 'no send'
        #iz_telegram.save_variable (user_id,namebot,"status",'???????????? ID')
        #import telebot
        #token = iz_telegram.get_token (namebot)
        #bot   = telebot.TeleBot(token) 
        #video = open('4.MP4', 'rb')
        #bot.send_video(user_id, video)
        import telebot
        token = iz_telegram.get_token (namebot)
        bot   = telebot.TeleBot(token) 
        bot.forward_message(user_id, message_id=4084, from_chat_id=-509375701) 
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'????????????????????????','S',0)         

    if message_in == '????????????????':
        label_send = 'no send'
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'???????????????? ???????????????????? ???? ??????????????','S',0)
        answer = test_depozit (user_id,namebot,message_in)
        if answer == 0:
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'???????????? ????????????????','S',0)
        else:    
            #iz_telegram.send_photo (user_id,namebot,'good.jpg')
            message_out,menu = iz_telegram.get_message (user_id,'???????????????? ??????????',namebot)        
            markup = ""
            answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)
            iz_telegram.send_audio (user_id,namebot,'audio.ogg')

    if label_send != 'no send':
        filter_code = filtr_kod (message_in)
        if filter_code == "?????? ??????":
            message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'???????????????? ???????? ???? ??????????????','S',0)
            answer = test_id (user_id,namebot,message_in)
            answer_message (user_id,namebot,message_in,answer) 
        else:
            pass  ### ???? ???????????? ???????????????? ???? ?????????? ????????
            
     
