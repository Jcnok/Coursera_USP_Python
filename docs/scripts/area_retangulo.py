# -*- coding: utf-8 -*-
"""
Este script desenha um retângulo preenchido com o caractere '#'
com base na largura e altura fornecidas pelo usuário.

Como usar:
O script solicita que o usuário digite a largura e a altura do retângulo.
Em seguida, ele imprime o retângulo no console.
"""

def desenha_retangulo(largura, altura):
    """Desenha um retângulo de # com as dimensões dadas."""
    h = altura
    while h > 0:
        c = largura
        while c > 0:
            print('#', end='')
            c = c - 1
        print()
        h = h - 1

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    try:
        largura_str = input("Digite a largura: ")
        largura_int = int(largura_str)

        altura_str = input("Digite a altura: ")
        altura_int = int(altura_str)

        if largura_int > 0 and altura_int > 0:
            desenha_retangulo(largura_int, altura_int)
        else:
            print("Por favor, insira valores positivos para largura e altura.")

    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros.")
