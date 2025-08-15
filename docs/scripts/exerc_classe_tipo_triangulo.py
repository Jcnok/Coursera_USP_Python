# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 08:42:17 2020

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

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    # TODO: Adicionar exemplo de execução com dados e prints.
    pass
