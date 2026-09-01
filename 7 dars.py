# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug 16 13:36:22 2026

# @author: ozodbekamirullayev
# """
# mevalar = ["Olma" , "anor " , "anjir"]
# narxlar = [20000, 12000, 43000, 120000 ,51000]
# sonlar = ["Bir", "IKKI", 32, 13]
# ismlar = ["sobirov " , "Firdavs", "Abush"]
# bozorlik = ["yog'", "un", "piyoz", "banan" , "go'sht"]
# mahsulot = bozorlik.pop(2)

# print("Men " + mahsulot +"sotib oldim ")
# print("sotib olinmagan  mahsulotlar" , bozorlik)

# ism1 =ismlar.pop(1)
# print("Salom " + "," + ism1 + "Kompuyuterxonaga boramizmi?")

# print(f"Qolganlarchi {ismlar} ham boradimi?")

# raqamlar = [1, 2, 100, 42, 33]

# raqamlar[1]= raqamlar[1] + raqamlar[0]
# raqamlar[0]= raqamlar[1]+ raqamlar[2]
# t_shaxslar = ["I.Karimov", "Amir Temur"]
# z_shaslar = ["Elon mask" ,"Bill gates"]
# t_shaxs= t_shaxslar.pop(1)
# z_shaxs= z_shaslar.pop(0)
# print(f"Men tarixiy shaxslar {t_shaxs} va zamanaviy shaxs {z_shaxs} bilan uchrashishni istardim")

# cars = ["Bmw" , "mercedes", "audi" , "tesla" , "volvo"]

# my_cars=cars[:]

# toys= ("dino", "bear", "lizard", "bird")
# pi=(3.14159)
# davlatlar = ["O'zbekiston", "Qozog'izton" , "Qirg'iziston"  , "Rossiya" , "AQSH"]
# sonlar= list(range(120,1200,2))

# taomlar= ["shashlik", "fri" , "tuxum", "osh", "sho'rva"]
# nonushta = taomlar[:]
# mehmonlar = ["Ali", "Vali" , "Sardor" , "sodiq" , "Amir", "Ozod"]

# for mehmon in mehmonlar:
#     print("Salom", mehmon) 

# for mehmon in mehmonlar:
#     print(f"Salom {mehmon} sizni ertaga nahorgi oshga taklif qilamiz")    
    

# sonlar = list(range(1,11))

# for son in sonlar:
#     print(f"{son} Sonning kvadrati {son**2} ga teng")


# dostlar =[]
# for n in range(5):
#     dostlar.append(input(f"{n+1} - chi do'stingizni ismini kiriting : "))
# print(dostlar)


# dostlar = ["ali", "vali", "abror", "sardor", "amir"]

# for n in dostlar:
#     print(f"Salom {n.title()} yaxshimisan")
# print(f"bu xabar  {len(n)+1} marta takrorlandi")  


# toq_sonlar = list(range(11, 100, 2))
# toq_son_kv = []


# for toq_son in toq_sonlar:
#     toq_son_kv.append(toq_son ** 2)

# print(toq_son_kv)

# sevimli_kinolar= []
# for n in range(5):
#   sevimli_kinolar.append(input(f"{n+1} chi yaxshi ko'rgan filmingizni kiriting: "))
# print(sevimli_kinolar)  

# uchrashgan_insonlar= []
# insonlar_soni = int(input("Bugun nechta inson bilan gaplashdiz: "))

# for inson in range(insonlar_soni):
#     uchrashgan_insonlar.append(input(f"{inson + 1} - chi gaplashgan insoningiz ismini kiriting: "))
# print(uchrashgan_insonlar)

# avtolar = ["Kia", "hyundai", "audi", "merc" ,"porsche" , "bmw"]
# for avto in avtolar:
#     if avto == "bmw":
#         print(avto.upper())
#     else :
#         print(avto.title())
# ism = "Ali"
# ism.lower()=="ali"

# javob = float(input("12x6 nechaga teng : >>>"))
# if javob !=72:
#     print("JAvob xato")

# login = input("5 harfdan ko'p login yozing! :")

# if len(login) <= 5 :
#     print("5 harfdan ko'p login kiriting!!!")

# tugilgan_yil = int(input("Tug'ilgan yilingizni kiritng: "))
# from datetime import date
# hozirgi_yil=date.today().year
# if hozirgi_yil-tugilgan_yil>=18:
#     print(f"Yoshingiz {hozirgi_yil-tugilgan_yil} da ekan kirishingiz mumkin")
#     print("Xush kelipsiz")
# else:
#     print("KEchirasiz sizga ruxsat yo'q!!!")

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != "gm":
#         print(car.title())
#         # print("GM")
#     else:
#         # print(car.title())
#         print("GM")
    
# login = input("Login ismingizni kiriting: ").lower()
# if login == "admin":
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi? ")
# else:
#    print(f"Xush kelibsiz, {login.title()}!")    

# narh = 15000
# choy= False
# salad = False

# if choy and salad :
#     narh= narh+10000
# elif choy or salad :
#     narh = narh +5000
# print(f"Narh = {narh}")

# menu = ["osh", "qozonkabob" , "shashlik" , "norin" , "somsa"]
# buyurtmalar = ["osh" , "somsa" , "manti" , "shashlik" ]
# # "somsa" in menu
# ovqat = input("Nima ovqat yeysiz? ")
# if ovqat in menu:
#     print("Buyurtma qabul qilindi! ")
# else:
#     print("Bizda bunday ovqat yo'q! ")

# "Gumma" not in menu
# for taom in menu: 
#     if taom in buyurtmalar:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Menuda {taom}  yo'q")

# juft_son = int(input("Juft son kiriting!: "))

# if juft_son%2 :
#     print("Bu juft son emas")
# else:
#     print("judt son")
   
# yosh = int(input("Yoshingizni kiriting: "))

# if yosh<=4 or yosh>=60:
#     narx = 0
# elif yosh<18:
#     narx= 10000
# else:
#     narx = 20000
# print(f"Sizga kirish {narx} so'm")

# son_1 = float(input("1-chi sonni kirting: "))
# son_2 = float(input("2-chi sonni kirting: "))

# if son_1>son_2:
#     print(f"{son_1} > {son_2}")
# elif son_1<son_2:
#     print(f"{son_1} < {son_2}")
# else:
#     print(f"{son_1} = {son_2}")

# mahsulotlar = ["olcha", "sut", "suv", "cola", "non", "semechka", "yog'", "kartoshka", "un", "shakar", "tuz"]
# savat = []


# for n in range(5):

#     mahsulot = input(f"5 tadan {n+1} - mahsulotni kiriting: ").lower()
#     savat.append(mahsulot)


# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"'{mahsulot}' mahsulotlar orasida bor ")
#     else:
#         print(f"'{mahsulot}' — yo'q ")
  

# mahsulotlar = ["olcha", "sut", "suv", "cola", "non", "semechka", "yog'", "kartoshka", "un", "shakar", "tuz"]
# savat = []
# bor_mahsulotlar=[]
# mavjud_emas = []

# for n in range(5):

#     mahsulot = input(f"5 tadan {n+1} - mahsulotni kiriting: ").lower()
#     savat.append(mahsulot)


# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
        
# if len(mavjud_emas)==0:
#     print("Siz so'ragan barcha mahsulotlar bor ")
# else:
#     print(f"Quyidagi mahsulotlar yo'q\n {mavjud_emas}")    
    
# foydalanuvchilar = ["amir", "temur", "odil", "vali", 'ali']
# login = input("Ro'yxatdan o'tish uchun login kiriting: ").lower()

# if login in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
   

# else:
#     print(f"Xush kelibsiz, {login} !")
   
# son = int(input("Butun son kiriting! "))  
# for n in range(2,11):
#     if son%(n) ==0:
#         print(f"Bu {son} soni {n} ga qoldiqsiz bo'linadi") 

# talaba_0= {"ism" : "Murod Olimov" , "yosh" : 21, "t_yil":2005 }
# print(f"{talaba_0['ism'].title()},\
# {talaba_0['t_yil']}-yilda tu'gilgan,\
# {talaba_0['yosh']} yoshda")

# talaba_0["kurs"]=4
# talaba_0["fakultet"]="Informatika"


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'anvar':'pixel 3xl'
# }

# phone = telefonlar["ali"]
# print(f"Alining telefoni {'ali'}")

# phone = telefonlar.get('hasan' , "Bunday ism mavjud emas")
# print(phone)

# dada = {"ism": "Otabek" , "familya":"Sharipov", "shahar":"Qarshi"}
# print(f"Dadamning ismi {dada["ism"]} ,\
#       familyasi {dada["familya"]},\
#      tugilgan shahri {dada["shahar"]} ")

# sevimli_taomlar = {"Ali":"osh", "vali":"Shashlik" , "sardor":"Qozonkabob", "ozod":"fri","ilhom": "somsa" }
# taom = sevimli_taomlar["Ali"]
# print(f"Alining sevimli taomi {taom}")

# python = {"int":"integer raqam",
#           "float":"o'nlik son",
#           "fstring":"o'zharuvchi bilan keladi"}

# eng_lugati = {
#     'apple': 'Olma (meva) yoki Apple kompaniyasi',
#     'string': 'Matnli maʼlumot turi',
#     'integer': 'Butun son',
#     'float': 'Oʻnlik (kasr) son',
#     'boolean': 'Mantiqiy qiymat (True yoki False)',
#     'list': 'Roʻyxat',
#     'dictionary': 'Lugʻat (kalit va qiymat)',
#     'function': 'Funksiya',
#     'tuple': 'Oʻzgarmas roʻyxat',
#     'module': 'Modul (fayl)'
# }
# soroq_soz = input("Biror narsa so'rang: ")

# lugat = eng_lugati.get(soroq_soz, "Bunda so'z mavjud emas")
# print(lugat)



