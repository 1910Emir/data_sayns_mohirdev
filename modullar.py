#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 15:16:26 2026

@author: ozodbekamirullayev
"""

# import avto_info_mod as aim # avto_info_mod faylini (modulini) chaqiramiz
# from  avto_info_mod import avto_info , info_print

# from avto_info_mod import * # bu hammasini chaqiradi

# as bilan chaqirish

# from  avto_info_mod import avto_info as ainfo , info_print as iprint

# avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# iprint(avto1)


# import math
# x = 400
# print(math.sqrt(x)) 
# print(math.pow(6, 2))
# print(math.pi )

# import random as r

# son = r.randint(0,100)
# print(son )

# ismlar = ['anvar', 'olim','hasan', 'husan']
# ism = r.choice(ismlar)
# print(ism )

# shuffle

# x = list(range(20))
# print(x)
# r.shuffle(x)
# print(x )



 # #Nomsiz funksiyalar

# uzunlik = lambda pi,r: 2*pi*r
# print(uzunlik(math.pi,10))

# kvadrat = lambda x , y : x**y
# print(kvadrat(5,3)) 

# def daraja(n):
#     return lambda x:x**n  # funksiya ichida funksiya

# kvadrat = daraja(2) 
# kub = daraja(3)

# print(kvadrat(5))
# print(kub(9 ))

# from math import sqrt 

# sonlar = list(range(11))
# ildizlar= list((map(sqrt,sonlar)))
# print(ildizlar)

# print(list(map(daraja(2), sonlar )))
# kvadratlar = list(map(lambda x:x*x, sonlar))
# print(kvadratlar)


# a =[3,5,8]
# b = [5,10,9]
# a_plus_b=list(map(lambda x , y : x+y, a,b))
# print(a_plus_b )

# import random as r

# sonlar = r.sample(range(100),10)
# print(sonlar)
# def juftmi(x):
#     return x%2==0  

# # juft_son = list(filter(juftmi, sonlar))
# juft_son = list(filter(lambda son : son%2==0, sonlar ))
# print(juft_son)



# mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", "tarvuz", "qovun", "banan"]
# harf = 'b'
# # mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))
# # print(mevalar_b)
# mevalar2= list((filter(lambda uzun:len(uzun)> =5, mevalar)))
# print(mevalar2)

















