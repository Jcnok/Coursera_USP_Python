# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:42:51 2020

@author: jcnok
"""


def ordena(lista):
  tam = len(lista)
  for i in range(tam-1):
      minimo = i
      for j in range(i+1,tam):
        if lista[j] < lista[minimo]:
          minimo = j
      lista[i],lista[minimo] = lista[minimo],lista[i]  
  return lista