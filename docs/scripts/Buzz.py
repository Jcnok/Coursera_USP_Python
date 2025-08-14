# -*- coding: utf-8 -*-
"""
Este script verifica se um número inteiro fornecido pelo usuário é divisível por 5.

Como usar:
O script solicita que o usuário digite um número inteiro.
- Se o número for divisível por 5, ele imprime a palavra "Buzz".
- Caso contrário, ele imprime o próprio número.
"""

def checa_buzz(numero):
    """Verifica se um número é divisível por 5."""
    if numero % 5 == 0:
        return "Buzz"
    else:
        return numero

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    try:
        num_str = input("Digite o número inteiro: ")
        num_int = int(num_str)
        resultado = checa_buzz(num_int)
        print(resultado)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")