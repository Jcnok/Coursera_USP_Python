# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 08:39:48 2020

@author: jcnok
"""


def bubble_sort(lista):
      fim = len(lista)
      for i in range(fim - 1, 0, -1):
        for j in range(i):
          if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j] 
            print(lista)
      return lista
            