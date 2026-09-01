#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 12:24:02 2026

@author: ozodbekamirullayev
"""

# Data Science va Sun'iy Intellekt Praktikum
# Python asoslari.
#
# Klass va Obyekt



matn = "Assalom alaykum"

class Kompyuter:
    def __init__(self, model, ram, hdd, gpu, cpu):
        self.model = model
        self.ram = ram
        self.hdd = hdd
        self.gpu = gpu
        self.cpu = cpu

    def info(self):
        inf = f"{self.model}, RAM:{self.ram}, SSD:{self.hdd}, CPU:{self.cpu}"
        return inf

macbook = Kompyuter("Apple Macbook", "8GB", "512GB", "M1", "M1")