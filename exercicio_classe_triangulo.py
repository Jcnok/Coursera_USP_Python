# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 08:26:09 2020

@author: jcnok
"""


class Triangulo:
  def __init__(self,a,b,c):
    self.a = a
    self.b = b
    self.c = c
  def perimetro(self):
    return self.a + self.b + self.c