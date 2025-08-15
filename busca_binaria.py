# -*- coding: utf-8 -*-
"""
Este script implementa o algoritmo de busca binária.

Como usar:
A função `busca_binaria(lista, elemento)` recebe uma lista **ordenada** e um
elemento para buscar. Ela retorna o índice do elemento se encontrado, ou `False`
caso contrário. A função imprime o índice do meio (`meio`) a cada iteração para
demonstrar como o espaço de busca é reduzido.

**Pré-requisito:** A lista de entrada deve estar ordenada para que a busca
binária funcione corretamente.

O bloco de exemplo abaixo demonstra o uso com uma lista ordenada.
"""

def busca_binaria(lista, elemento):
    """
    Realiza uma busca binária por um elemento em uma lista ordenada.
    Retorna o índice do elemento se encontrado, caso contrário, retorna False.
    """
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        print(f"Testando o meio no índice: {meio}")

        if lista[meio] == elemento:
            return meio
        elif elemento < lista[meio]:
            ultimo = meio - 1
        else: # elemento > lista[meio]
            primeiro = meio + 1

    return False

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    lista_ordenada = [10, 20, 30, 50, 60, 80, 100, 110, 130, 170]

    print(f"Buscando na lista ordenada: {lista_ordenada}")

    elemento_encontrado = 130
    print(f"\nBuscando pelo elemento {elemento_encontrado}...")
    posicao = busca_binaria(lista_ordenada, elemento_encontrado)
    if posicao is not False:
        print(f"O elemento {elemento_encontrado} foi encontrado na posição {posicao}.")
    else:
        print(f"O elemento {elemento_encontrado} não foi encontrado na lista.")

    elemento_nao_encontrado = 99
    print(f"\nBuscando pelo elemento {elemento_nao_encontrado}...")
    posicao = busca_binaria(lista_ordenada, elemento_nao_encontrado)
    if posicao is not False:
        print(f"O elemento {elemento_nao_encontrado} foi encontrado na posição {posicao}.")
    else:
        print(f"O elemento {elemento_nao_encontrado} não foi encontrado na lista.")