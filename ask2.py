# -*- coding: utf-8 -*-
import json
print ('Версия 3.1')
from grab import Grab
g  = Grab()
url = 'https://fotoport67.amocrm.ru/private/api/auth.php'
g.setup(post={'USER_LOGIN': 'foto-port@mail.ru','USER_HASH': 'c221c7318ee7c9a1c17f122ee32dafe3'})
g.go(url)
body = g.doc.body
print (body)
print ("------------------------------------------------------------------------")
nomer = 0 
sm = 0
while sm < 2:
    sm = sm +1
    url = 'https://fotoport67.amocrm.ru/api/v2/leads?limit_rows=500&limit_offset='+str(sm*500)+''
    g.go(url)
    body = g.doc.body
    ##print (body) 
    bodynew = body.decode('utf-8') 
    parsed_string = json.loads(bodynew)
    print ('------------------------------------------------------------------------')
    body3 = parsed_string['_embedded']
    ##print (body3)
    ##for n in body3:
        ##print (n)  
    body4 = body3['items']
    for n in body4:
        imya = nomer,n['name']
        nomer = nomer + 1
        ID_Zak = n['custom_fields']
        for h in ID_Zak:
            if str(h).find ('ID заказа') != -1:
                s = h['values']
                for f in s:
                    poisk = f['value'] 
                    if poisk == '1717':
                        print ('Имя заказа',imya)
                        print (ID_Zak)
                        print ('--------------------------------') 
                        print (n)
                        print (n['status_id'])

     






 
