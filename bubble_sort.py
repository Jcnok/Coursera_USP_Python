# -*- coding: utf-8 -*-
"""
Este script implementa o algoritmo de ordenação Bubble Sort.

Como usar:
A função `bubble_sort(lista)` recebe uma lista de números e a ordena em ordem
crescente. Durante a execução, a função imprime o estado da lista a cada troca,
permitindo visualizar o processo de ordenação passo a passo.

O bloco de exemplo abaixo demonstra o uso com uma lista desordenada.
"""

def bubble_sort(lista):
    """
    Ordena uma lista de números usando o algoritmo Bubble Sort.
    Imprime a lista a cada troca de elementos.
    """
    fim = len(lista)
    # O loop externo controla o número de passagens
    for i in range(fim - 1, 0, -1):
        trocou = False
        # O loop interno compara e troca os elementos adjacentes
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)  # Mostra o estado da lista após a troca
                trocou = True
        # Se não houve trocas em uma passagem, a lista já está ordenada
        if not trocou:
            return lista
    return lista

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    lista_desordenada = [5, 1, 4, 2, 8]

    print(f"Lista original: {lista_desordenada}")
    print("Iniciando o processo de Bubble Sort (mostrando a lista a cada troca):")

    lista_ordenada = bubble_sort(lista_desordenada)

    print(f"\nLista final ordenada: {lista_ordenada}")
            