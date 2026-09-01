#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 16:00:44 2026

@author: ozodbekamirullayev
"""
# ism = input("Ismingiz nima? ")
# yosh = int(input(f"Salom, {ism.title()} yoshingiz nechada?"))

# height = float(input("Bo'yingiz necha metr ? ")) 

# son = 1
# while  son<=5 :
#     print(son ,  end=" ")
#     son +=1
# print("Dastur tugadi  ")    
    

# print("Istalgan sonni kvadratini chiqaruvchi dastur ")
# savol="Istalgan sonni kiriting: "
# savol +="(dasturni toxtatish uchun exit deb yozing )" 
# qiymat= " "
# while qiymat !="exit":
#     qiymat= input(savol)
#     if qiymat!="exit":  #1 - usul 
#         print(float(qiymat)**2)
# print("Dastur tugadi !")        
        
# 2 - usul 

# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat!= "exit":
#         print(float(qiymat)**2)
#     else:
#         ishora= False
# print("Dastur tugadi")        

# 3 usl break bilan 

# while True:
#     qiymat= float(input(savol))
#     if qiymat=="exit":
#         break
#     else:
#         print(qiymat**2)
# print("datsur tugadi! ")

# sonlar = list(range(1,11))
 
# for son in sonlar:
#     if son ==5 :
#         break
#     else:
#         print(f"{son} ning kvadrati  {son**2} ga teng ")

# sonlar = list(range(1,11)) # contiu
 
# for son in sonlar:
#     if son ==5 :
#         continue
#     else:
#         print(f"{son} ning kvadrati  {son**2} ga teng ")


# son = 0 
# while son<10:
#   son+=1
#   if son%2!=0:        
#       continue
#   else:
#       print(son)
      
  # yoki aksincha toq sonlarni chiqaradi
  
# son = 0 
# while son<10:
#   son+=1
#   if son%2!=0:        
#       continue
#   else:
#       print(son)      
    
#Amaliyot 

# savol = "Yaxshi ko'rgan kitoblaringizni kiriting"
# savol +="(kiritib bo'lgach 'stop' deb yozing)"

# while True:
#     kitob = input(savol)
#     if kitob=="stop":
#         break
# print("Raxmat")
        
       
     
# savol = "yoshingizni kiting va bilet qancha ekanligi aniqlab oling"
# savol +="(kiritib bo'lgach 'exit' yoki 'quit'  deb yozing)"
 
# while True:
#     yosh = input(savol)
#     if yosh == 'exit' or yosh=='quit':
#         break
#     else:
#         yosh = int(yosh)
#         if yosh <7:
#             print("Sizlarga kirish 2000 ming so'm")
        
#         elif 7 <= yosh and yosh < 18:
#             print("Sizlarga kirish 3000 ming so'm")
#         elif 18 <= yosh and yosh < 65:
#             print("Sizlarga kirish 10000 ming so'm")   
#         else:
#             print("Sizga kirish bepul! ")
            
# print("dastur tugadi")          
    
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0  :
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")


# print("Yaqin do'stlaringiz ro'yxatini kiriting ")
# ismlar = []
# n = 1
# while True:
#     savol = f"{n} - do'stingizni ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ismlar qo'shasizmi ? (ha/yo'q)")
#     n+=1
#     if takrorlash != "ha":
#         break
    
# for ism in ismlar:
#     print(ism.title())
    
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingizni ismini kiriting ")
#     yosh = input(f"{ism.title()} do'stingizni yoshinini kiriting ")
#     dostlar[ism] = int(yosh)
    
#     javob = input("Yana do'stlarini qo'shasizmi ")
#     if javob != 'ha':
#         ishora = False
    
# for ism , yosh in dostlar.items() :
#     print(f"{ism.title()}  {yosh} yoshda ")

# cars = ["malibu", "porsh", "nexia" , "titan" , "lambo" , "nexia" , "trevers" ,"nexia" ]
# car = 'nexia'
# while car in cars :
#     cars.remove(car)
# print(cars)

# talabalar = ['hasan' , 'husan' ,  'olim' , 'nargiza' ]
# baxolangan_talabalar = {}

# while talabalar:
#     talaba = talabalar.pop()
#     baxo = input(f"{talaba}ning baxosini qo'ying ")
#     print(f"{talaba} baxolandi")
#     baxolangan_talabalar[talaba] = int(baxo)

# Amaliyot

# savat = []
# savol = "Nima buyurtma bermoqchisiz"
# while True:
#     buyurtma = input(savol)
#     savat.append(buyurtma)
#     javob = input("yana nimadur buyurtma qilasizmi (ha / yo'q')")
#     if javob != 'ha':
#         break
        
    
    
# savat = {}

# while True:
#     mahsulot = input("Kiritmoqchi bo'lgan mahsulotingiz nomini yozing (to'xtatish uchun 'exit'): ")
#     if mahsulot.lower() == 'exit':
#         break
        
#     narx = input(f"{mahsulot.title()}ning narxini kiriting: ")
    
#     # Lug'atga kalit (mahsulot) va qiymat (narx) juftligi saqlanadi
#     savat[mahsulot] = int(narx)

# print("\n--- Savatdagi mahsulotlar ro'yxati ---")
# for mahsulot, narx in savat.items():
#     print(f"{mahsulot.title()}: {narx} so'm")
    
    
    
    
    

 







