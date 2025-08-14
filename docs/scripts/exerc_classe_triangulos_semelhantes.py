# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 09:22:46 2020

@author: jcnok
"""


class Triangulo:
  def __init__(self,a,b,c):
    self.a = a
    self.b = b
    self.c = c
  def perimetro(self):
    return self.a + self.b + self.c
  def tipo_lado(self):
    if self.a == self.b and self.a == self.c:
      return 'equilátero'
    elif self.a == self.b or self.a == self.c or self.b == self.c:
      return 'isósceles'
    else:
      return 'escaleno'
  def retangulo(self):
    if max(self.a,self.b,self.c) == self.a:
      return self.a ** 2 == self.b**2 + self.c**2
    elif max(self.a,self.b,self.c) == self.b:
      return self.b**2 == self.a**2 + self.c**2
    else:
      return self.c**2 == self.a**2 + self.b**2
  def semelhantes(self,triangulo):
    return triangulo.tipo_lado() == self.tipo_lado()