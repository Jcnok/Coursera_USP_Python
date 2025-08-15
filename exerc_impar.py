# -*- coding: utf-8 -*-
"""
Este script imprime os 'n' primeiros números ímpares naturais,
com base em um número 'n' fornecido pelo usuário.

Como usar:
O script solicita que o usuário digite um número 'n'. Em seguida, ele
imprime os 'n' primeiros números ímpares, começando de 1.
"""

def imprime_impares(n):
    """Imprime os n primeiros números ímpares."""
    if n <= 0:
        print("Por favor, insira um número positivo.")
        return

    impar_atual = 1
    for _ in range(n):
        print(impar_atual)
        impar_atual += 2

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    try:
        n_str = input("Digite o valor de n: ")
        n_int = int(n_str)

        print(f"Os {n_int} primeiros números ímpares são:")
        imprime_impares(n_int)

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")