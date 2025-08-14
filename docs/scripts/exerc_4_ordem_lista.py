# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:47:50 2020

@author: jcnok
"""


def ordenada(lista):
   tam = (len(lista))-1

   for i in range(tam):
     if lista[i] > lista[i+1]:
       return False
     else:
       i+=1
   return True