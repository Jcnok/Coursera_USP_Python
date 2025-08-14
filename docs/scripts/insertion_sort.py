# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 07:44:52 2020

@author: jcnok
"""


def insertion_sort(lista):
  i = 1 # inicia na segunda posição
  while i < len(lista):
    var_temp = lista[i]
    trocou = False
    j = i - 1
    while j >= 0 and lista[j] > var_temp:
      lista[j+1] = lista[j]
      trocou = True
      j -= 1
    if trocou:
      lista[j+1] = var_temp
    i += 1
  return lista