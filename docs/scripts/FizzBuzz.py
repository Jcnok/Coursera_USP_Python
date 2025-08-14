# -*- coding: utf-8 -*-
"""
Este script verifica se uma sequência de três números inteiros,
fornecida pelo usuário, está em ordem crescente.

Como usar:
O script solicita que o usuário digite três números inteiros, um de cada vez.
Ao final, ele imprime "crescente" se o segundo número for maior que o primeiro
e o terceiro for maior que o segundo. Caso contrário, imprime "não está em
ordem crescente".
"""

def verifica_ordem_crescente(n1, n2, n3):
    """Verifica se três números estão em ordem estritamente crescente."""
    if n1 < n2 and n2 < n3:
        return "crescente"
    else:
        return "não está em ordem crescente"

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    try:
        num1_str = input("Digite o primeiro número: ")
        num1 = int(num1_str)

        num2_str = input("Digite o segundo número: ")
        num2 = int(num2_str)

        num3_str = input("Digite o terceiro número: ")
        num3 = int(num3_str)

        resultado = verifica_ordem_crescente(num1, num2, num3)
        print(resultado)

    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números inteiros.")