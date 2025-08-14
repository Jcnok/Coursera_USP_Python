# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 09:14:55 2020

@author: jcnok
"""


def conta_letras(frase, contar="vogais"):
  conta_tudo = frase.replace(' ','') # tamanho total da frase sem os espaços
  dic_vogais = ['a','e','i','o','u']
  if contar == "vogais":
    conta_vogais = [vogal for vogal in conta_tudo if vogal in dic_vogais] # cria uma lista com todas as vogais da frase
    return len(conta_vogais)
  elif contar == "consoantes":
    conta_consoantes = [consoante for consoante in conta_tudo if consoante not in dic_vogais] #cria uma lista sem as vogais - neste caso não haverá números ou caracteres especiais!
    return len(conta_consoantes)
  else:
    print("valor inválido")