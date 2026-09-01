# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sun Aug 30 18:15:24 2026

# @author: ozodbekamirullayev
# """


# def salom_ber(ism):
#     """Salom beruvchi funksiya"""
#     print(f"Assalomu alaykum {ism.title()}")
    
# salom_ber('ozodbekamirullayev')

# from datetime import datetime

# def yosh_hisobla(ism, tugilgan_yil):
#     hozirgi_yil = datetime.now().year
#     yosh = hozirgi_yil - tugilgan_yil
#     print(f"{ism.title()} {yosh} yoshda.")

# # Funksiyani chaqirib tekshirish:
# yosh_hisobla("Ozodbek", 2005) 

# #Amaliyot

# ism= input("Ismingiz nima? ")
# yosh= int(input("Yoshingiz nechada? "))

# def tugilgan_yil_hisobla(ism,yosh):
#     hozirgi_yil = datetime.now().year
#     print(f"{ism.title()} siz {hozirgi_yil - yosh} - yilda tug'ilgan ekansiz")
    
# tugilgan_yil_hisobla(ism, yosh)  

# def kv_kub_hisobla(son):
#     """Sonni kv va kubini hisoblab beradi"""
#     print(f"{son} ning kavdrati - {son**2} va kubi {son**3}")
    
# kv_kub_hisobla(4)


# def toliq_ism_yasa(ism,familiya):
    
#     toliq_ism= f"{ism}  {familiya}"
#     return toliq_ism
# talaba = toliq_ism_yasa('olim', 'olimov')
# print(talaba)

    
# def toliq_ism_yasa(ism,familiya,otasini_ismi=''):
#     if otasini_ismi:
#         toliq_ism= f"{ism}  {familiya} , {otasini_ismi}"
#     else:
#         toliq_ism= f"{ism}  {familiya}"
    
    
#     return toliq_ism
# talaba = toliq_ism_yasa('olim', 'olimov' )
# talaba2 = toliq_ism_yasa('olim', 'olimov' , 'amirullovich' )
# print(talaba)
# print(talaba2)

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {
#         'kompaniya': kompaniya,
#         'model': model,
#         'rang': rangi,
#         'korobka': korobka,
#         'yil': yili,
#         'narh': narhi
#     }
#     return avto

# avto1=avto_info('GM', 'malibu', 'qora', 'avtomat', 2026)
# avto2= avto_info('GM', 'cobalt', 'qora', 'mexanika', 2026,11000)
# mashinalar= [avto1,avto2]
# # print("Bozordagi mavjud mashinlar: ")

# # for mashina in mashinalar:
# #     if mashina['narh']:
# #         narh=mashina['narh']
# #     else:
# #         narh = "Nomalum"
# #     print(f"{mashina['model']} , {mashina[rang]})

# # def oraliq(min ,max,qadam = 1 ):
# #     sonlar=[]
    
# #     while min<max:
# #         sonlar.append(min)
# #         min+=qadam
# #     return sonlar
# # print(oraliq(1,11,1))

# avtolar = []  # Bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting:", end=' ' )
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rang = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yil = input("Ishlab chiqarilgan yili: ")
#     narh = input("Narhi: ")
#     avtolar.append(avto_info(kompaniya,model,rang,korobka,yil,narh))
#     javob= input("Yana avtolarni qo'shasizmi? (ha/yo'q)")
#     if javob!='ha':
#         break
    
# print("\nSAlonimizdagi avtolar: ")
# for avto in   avtolar:
#     if avto['narh']:
#         narh=avto['narh']
#     else:
#         narh = "Nomalum"
#     print(f"{avto['rang']} , {avto['model']} , {avto['yil']} , {avto['narh']}")
    


# # Amaliyot    


# def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {'ism':ism,
#              'familiya':familiya,
#              'tyil':tyil,
#              'yoshi':2020-tyil,
#              'tjoy':tjoy,
#              'email':email,
#              'telefon':tel}
#     return mijoz

# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar =[]
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob!='ha':
#         break

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
#           f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")

# def kattasini_aniqla(x,y,z):
#     max=x
#     if(y>=max):
#         max=y
#     elif(z>=max):
#         max=z
#     return(max)
# print(kattasini_aniqla(5, 3, 20))

# def tub_son(min,max):
#     tub_sonlar=[]
#     for n in range(min,max+1):
#         tub=True
#         if(n==1):
#             tub=False
#         elif(n==2):
#             tub=True
#         else:
#             for x in range(2,n):
#               if(n%x==0):
#                     tub=False
#         if tub:
#                 tub_sonlar.append(n)
#     return tub_sonlar
    
# print(tub_son(5, 10))

# def fibonachi(n):
#     sonlar=[]
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)
#         else :
#             sonlar.append((x-1)+(x-2))
#     return sonlar
# print(fibonachi(12))
            


# # funksiyaga ro'yxat uzatish


# def bahola(ismlar):
#      baholar = {}
#      while ismlar:
#          ism=ismlar.pop()
#          baho=input(f"Talaba {ism.title()}ning baxosoni qo'ying: ")
#          baholar[ism]=int(baho)
#      return baholar

            
# talabar= ['ozod', 'sarvar','rahim','odil']
# baholar=bahola(talabar[:])
# print(baholar)
# print(talabar)

#    #Amaliyot 

# def katta_harf(matn):
#     matn = matn[:]
#     for x in range(len(matn)):
#         matn[x] = matn[x].title()
#     return matn
# text = ["Salom","men" ,"ozodbekman"]
# # katta_harf(text[:])
# yangi_tekst = katta_harf(text)
# print(yangi_tekst)
# print(text)



# # Moslashuvchan funksiyalar


# def summa(*sonlar):
#     """NEchta son bolsa hammmasini qoshib beradi * bu args """
#     yigindi = 0
#     for son in  sonlar:
#         yigindi+=son
        
#     return yigindi
 
        
# # def summa(x,y ,*sonlar):
# #     """NEchta son bolsa hammmasini qoshib beradi * bu args """
   
# #     return x+y+sum(sonlar  )


# def avto_info(kompaniya, model, **malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar


# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000, yil=2020)

# def sonlar_kopaytmasi(*sonlar):
#     kopaytuvchilar = 1
#     for son in sonlar:
#         kopaytuvchilar*=son

# def talaba_info(ism, familiya, **kwargs):
#     kwargs['ism']=ism
#     kwargs['familiya']=familiya
#     return kwargs

# talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')

        

    


  
























