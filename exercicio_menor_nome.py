# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 08:28:18 2020

@author: jcnok
"""
def menor_nome(nomes):
  lista_ok = [x.strip().lower().capitalize() for x in nomes] #removendo os espaços,normalizando todas com letra minúscular e depois somente a primeira letra maiúscula!
  menor = (min(list(map(len,lista_ok)))) #Encontrar o menor elemento da lista!
  lista_menor = [y for y in lista_ok if len(y)==menor] #Separando todos os nomes com menor valor em uma lista!
  return lista_menor[0] # retornando apenas o primeiro menor elemento da lista!

