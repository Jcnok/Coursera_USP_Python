# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:04:05 2020

@author: jcnok
"""


def busca(lista, elemento):
  for i in range(len(lista)):
    if lista[i]==elemento:
      return i
    else:
      i+=1
  return False