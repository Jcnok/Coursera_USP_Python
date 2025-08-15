# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 08:22:28 2020

@author: jcnok
"""


def fatorial(n):
  if n < 1:  # base da recursao
    return 1
  else:
    return n * fatorial(n-1) # chamada recursiva

import pytest

@pytest.mark.parametrize("entrada, esperado",[
     (0,1),
     (1,1),
     (2,2),
     (3,6),
     (4,24),
     (5,120)
])
def testa_fatorial(entrada, esperado):
  assert fatorial(entrada) == esperado

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    # TODO: Adicionar exemplo de execução com dados e prints.
    pass
