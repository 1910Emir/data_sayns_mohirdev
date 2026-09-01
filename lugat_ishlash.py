#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:15:39 2026

@author: ozodbekamirullayev
"""

# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
# }

# for kalit,qiymat in talaba_0.items():
#     print(f"Kalit : {kalit}")
#     print((f"Qiymat : {qiymat} \n"))
    
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'anvar':'pixel 3xl'
# }

# for k ,v in telefonlar.items():
#     print(f"{k.title()} ning telefon rusumi {v.title()}" )

# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
# }
# print(mahsulotlar.keys())  

# print("Do'kondagi mahsulotlar")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title()) 


# telefonlar = {
#     'ali': 'iphone x',
#     'vali': 'galaxy s9',
#     'olim': 'iphone x',          # Ali bilan bir xil telefon
#     'orif': 'nokia 3310',
#     'anvar': 'pixel 3xl',
#     'jasur': 'redmi note 10',
#     'bobur': 'galaxy s9',        # Vali bilan bir xil telefon
#     'zuxra': 'iphone 13',
#     'malika': 'iphone x',        # Ali va Olim bilan bir xil telefon
#     'dilshod': 'poco x3',
#     'nodira': 'iphone 11',
#     'bekzod': 'redmi note 10',   # Jasur bilan bir xil telefon
#     'davron': 'nokia 3310',      # Orif bilan bir xil telefon
#     'zarina': 'galaxy s21',
#     'akmal': 'pixel 3xl'         # Anvar bilan bir xil telefon
# }

# print("Foydanauvchilar quyidagi  telefonlar rusumlarini ishlatishadi: ")

# for tel in telefonlar.values():
#     print(tel)
    
# for tel in set(telefonlar.values()): # set funksiyasi 1 xil llarni olib tashlaydi
#     print(tel) 
 
# toys = {"bear", "ball" "car", "dino", "phone"} # set 
# print(type(toys))

# python_lugati = {
#     'string': 'Matnli maʼlumot turi (qoʻshtirnoq ichiga yoziladi)',
#     'integer': 'Butun sonlar (masalan: 5, -10, 100)',
#     'float': 'Oʻnlik sonlar (masalan: 5.5, 3.14)',
#     'boolean': 'Mantiqiy qiymat (faqat ikkita qiymatni oladi: True yoki False)',
#     'list': 'Roʻyxat – tartiblangan va oʻzgartirilib boʻladigan elementlar toʻplami ([])',
#     'dictionary': 'Lugʻat – kalit va qiymat (key-value) juftligidan iborat maʼlumot tuzilmasi ({})',
#     'tuple': 'Kortej – oʻzgartirib boʻlmaydigan oʻzgarmas roʻyxat (())',
#     'if-else': 'Shart operatori – shartlarni tekshirish va tarmoqlanish uchun ishlatiladi',
#     'for': 'Sikl operatori – biror amalni maʼlum bir marta takrorlash uchun xizmat qiladi',
#     'function': 'Funksiya – muayyan vazifani bajaruvchi qayta ishlatiladigan kod boʻlagi (def)'
# }

# for k, v in  sorted(python_lugati.items()):
#     print(f"{k.title()} -- {v.title()}")

# davlatlar_poytaxti = {
#     'oʻzbekiston': 'Toshkent',
#     'aqsh': 'Vashington',
#     'rossiya': 'Moskva',
#     'fransiya': 'Parij',
#     'germaniya': 'Berlin',
#     'yaponiya': 'Tokio',
#     'turkiya': 'Anqara',
#     'qozogʻiston': 'Ostona',
#     'italiya': 'Rim',
#     'buyuk britaniya': 'London'
# }
# # for davlat in sorted( davlatlar_poytaxti):
# #     print(davlat.upper())

# # for poytaxt in sorted( davlatlar_poytaxti.values()):
# #     print(poytaxt.title())


# user = input("Davlat nomini kiriting: ").lower()
# lugat = davlatlar_poytaxti.get(user, "Bunday ma'lumot bizda yo'q")
# print(lugat)

# taomlar = {
#     'osh': 35000,
#     'manti': 6000,
#     'somsa': 8000,
#     'shashlik': 15000,
#     'lag\'mon': 30000,
#     'chuchvara': 25000,
#     'norin': 40000,
#     'shorva': 28000,
#     'mastava': 24000,
#     'kabob': 55000
# }

# buyurtmalar = []

# for n in range(3):
#    buyurtmalar.append(input(f"{n+1} - buyurtma qilmoqchi bo'lgan taomingiz: ").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in taomlar:
#          print(f"{buyurtma}.title() narxi --{taomlar[buyurtma]}")
#     else:
#         print(" {buyurtma} -- bizda yo'q")


# car1 = {
#     'model': 'Malibu',
#     'rang': 'oq',
#     'yil': 2024,
#     'karobka': 'avtomat'
# }

# car2 = {
#     'model': 'Tracker',
#     'rang': 'qora',
#     'yil': 2023,
#     'karobka': 'avtomat'
# }

# car3 = {
#     'model': 'Cobalt',
#     'rang': 'kumushrang',
#     'yil': 2022,
#     'karobka': 'mexanika'
# }

# car4 = {
#     'model': 'Gentra',
#     'rang': 'qizil',
#     'yil': 2021,
#     'karobka': 'avtomat'
# }

# car5 = {
#     'model': 'Onix',
#     'rang': 'ko\'k',
#     'yil': 2025,
#     'karobka': 'avtomat'
# }

# cars = [car1, car2 , car3 , car4, car5]
# for car in cars:
#     print(f"{car['model'].title()} ,"
#          f"{car['rang']} ,"
#          f"{car['yil']}- yil "
#          f"{car['karobka']}")
 
# malibus=[]
# for n in range(10):
#     new_car={'model':'malibu',
#             'rang': None,
#             'yil': 2026,
#             'narx':None,
#             'km':0,
#             'korobka':'avtomat'
#         }
#     malibus.append(new_car)

# for malibu in malibus[:3]:
#     malibu['rang'] = 'yashil'
    
# for malibu in malibus[:6]:
#     malibu['rang'] = 'qizl'

# for malibu in malibus[6:]:
#     malibu['rang'] = 'qora'
#     malibu['korobka']= 'mexanika'

# for malibu in malibus:
#     if malibu['korobka']=='mexanika':
#         malibu['narx'] = 35000
#     else:
#         malibu['narx'] = 40000

# for malibu in malibus:
#     print(malibu)        
        

# dasturchilar = {
#     'linus torvalds': ['c', 'c++'],
#     'guido van rossum': ['python', 'c'],
#     'james gosling': ['java', 'c'],
#     'mark zuckerberg': ['php', 'javascript', 'hack'],
#     'tim berners-lee': ['html', 'css', 'javascript']
# }
# for ism , tillar in dasturchilar.items():
#     print(f"\n {ism.title()}- dasturlash tillarini biladi ")
#     for til in tillar:
#         print(f"{til.upper()}  ", end=' ')


# mashhurlar = {
#     'alisher_navoiy': {
#         'soha': 'Adabiyot',
#         'kasbi': 'Shoir va mutafakkir',
#         'asari': 'Xamsa'
#     },
#     'albert_einstein': {
#         'soha': 'Ilm-fan',
#         'kasbi': 'Fizik nazariyotchi',
#         'asari': 'Nisbiylik nazariyasi'
#     },
#     'leonardo_da_vinci': {
#         'soha': 'San\'at',
#         'kasbi': 'Rassom va ixtirochi',
#         'asari': 'Mona Liza'
#     },
#     'tim_berners_lee': {
#         'soha': 'Internet',
#         'kasbi': 'Dasturchi',
#         'asari': 'World Wide Web (WWW)'
#     }
# }

# # Lug'atdan foydalanish namunasi:
# for shaxs, malumot in mashhurlar.items():
#     print(f"{shaxs.title()}: {malumot['soha']} sohasida - {malumot['kasbi']} ")
# for shaxs, malumot in mashhurlar.items():
#     ism = shaxs
#     asar = malumot['asari']
#     print(f"{ism.title()}ning mashhur ishi - {asar}")

# dostlar_kinolari = {
#     'anvar': {
#         'sevimli_kinolari': ['Inception', 'Interstellar', 'The Matrix']
#     },
#     'jasur': {
#         'sevimli_kinolari': ['Titanic', 'Avatar', 'Gladiator']
#     },
#     'dilshod': {
#         'sevimli_kinolari': ['The Dark Knight', 'Joker', 'Avengers']
#     }
# }


# for ism, malumot in dostlar_kinolari.items():

#     kinolar = malumot['sevimli_kinolari']
    

#     kinolar_str = ', '.join(kinolar)
#     print(f"{ism.title()}ning sevimli kinolari: {kinolar_str}")


davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul_birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul_birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul_birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul_birligi':"rinngit"}
    }

# for davlat, info in davlatlar.items():
#     poytaxt = info['poytaxt']
#     maydon= info['maydon']
#     aholi = info['aholi']
#     puli = info['pul_birligi']
#     print(f"{davlat.title()}ning poytaxi - {poytaxt.title()} . Maydoni - {maydon} kv km , pul birligi - {puli} ")
    
davlat_savol = input("Malumot so'rang: ").lower()

if davlat_savol in davlatlar:
       
        info = davlatlar[davlat_savol]
        poytaxt = info['poytaxt']
        maydon= info['maydon']
        aholi = info['aholi']
        puli = info['pul_birligi']
        print(f"{davlat_savol.title()}ning poytaxi - {poytaxt.title()} . Maydoni - {maydon} kv km , pul birligi - {puli} ")
else:
        print("Bizda bunday davlat yo'q")

