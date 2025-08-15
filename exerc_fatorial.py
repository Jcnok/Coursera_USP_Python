# -*- coding: utf-8 -*-
"""
Este script calcula o fatorial de um número inteiro não negativo
fornecido pelo usuário.

Como usar:
O script solicita que o usuário digite um número. Ele então calcula e
imprime o fatorial desse número. O fatorial de 0 é 1.
"""

def calcular_fatorial(n):
    """Calcula o fatorial de um número n."""
    if n < 0:
        return "Fatorial não definido para números negativos"

    fatorial = 1
    # O loop vai de n até 2, multiplicando os valores
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    return fatorial

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    try:
        num_str = input("Digite o valor de n: ")
        numero = int(num_str)

        resultado = calcular_fatorial(numero)

        print(f"O fatorial de {numero} é {resultado}")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")