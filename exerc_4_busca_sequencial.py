# -*- coding: utf-8 -*-
"""
Este script implementa uma função de busca sequencial em uma lista.

A função `busca(lista, elemento)` percorre a `lista` e retorna o índice da primeira
ocorrência do `elemento`. Se o elemento não for encontrado, a função retorna `False`.

O bloco de exemplo abaixo demonstra o uso da função com uma lista de números.
"""

def busca(lista, elemento):
  """
  Realiza uma busca sequencial por um elemento em uma lista.
  Retorna o índice do elemento se encontrado, caso contrário, retorna False.
  """
  for i in range(len(lista)):
    if lista[i] == elemento:
      return i
  return False

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    lista_exemplo = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]

    print(f"Buscando na lista: {lista_exemplo}")

    elemento_encontrado = 30
    posicao = busca(lista_exemplo, elemento_encontrado)
    if posicao is not False:
        print(f"O elemento {elemento_encontrado} foi encontrado na posição {posicao}.")
    else:
        print(f"O elemento {elemento_encontrado} não foi encontrado na lista.")

    elemento_nao_encontrado = 99
    posicao = busca(lista_exemplo, elemento_nao_encontrado)
    if posicao is not False:
        print(f"O elemento {elemento_nao_encontrado} foi encontrado na posição {posicao}.")
    else:
        print(f"O elemento {elemento_nao_encontrado} não foi encontrado na lista.")