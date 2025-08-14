# -*- coding: utf-8 -*-
"""
Este script define uma função `n_primos` que conta quantos números primos existem
entre 2 e um número 'n' (inclusive).

Como usar:
A função `n_primos(n)` recebe um número inteiro `n` como argumento e retorna
a contagem de números primos nesse intervalo. O bloco de exemplo demonstra seu
uso e imprime o resultado.
"""

def n_primos(n):
    """
    Conta a quantidade de números primos existentes até o número n.
    """
    if n < 2:
        return 0

    primo = 0
    # Itera de n descendo até 2
    for i in range(n, 1, -1):
        # Assume que o número é primo até que se prove o contrário
        is_primo = True
        # Verifica divisores de 2 até a raiz quadrada do número
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_primo = False
                break
        if is_primo:
            primo += 1

    return primo

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    numero_limite = 121

    print(f"Calculando a quantidade de números primos até {numero_limite}...")

    quantidade = n_primos(numero_limite)

    print(f"Existem {quantidade} números primos até {numero_limite}.")
