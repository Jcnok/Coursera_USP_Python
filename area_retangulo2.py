# -*- coding: utf-8 -*-
"""
Este script desenha a borda de um retângulo com o caractere '#'
com base na largura e altura fornecidas pelo usuário.

Como usar:
O script solicita que o usuário digite a largura e a altura do retângulo.
Em seguida, ele imprime a borda do retângulo no console.
"""

def desenha_retangulo_vazado(largura, altura):
    """Desenha um retângulo vazado de # com as dimensões dadas."""
    for i in range(altura):
        for j in range(largura):
            # Imprime '#' na primeira/última linha ou primeira/última coluna
            if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
                print('#', end='')
            else:
                print(' ', end='')
        print()

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    try:
        largura_str = input("Digite a largura: ")
        largura_int = int(largura_str)

        altura_str = input("Digite a altura: ")
        altura_int = int(altura_str)

        if largura_int > 0 and altura_int > 0:
            desenha_retangulo_vazado(largura_int, altura_int)
        else:
            print("Por favor, insira valores positivos para largura e altura.")

    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros.")
