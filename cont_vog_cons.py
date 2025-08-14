# -*- coding: utf-8 -*-
"""
Este script foi criado para contar o número de vogais ou consoantes em uma frase fornecida.

Como usar:
A função `conta_letras(frase, contar)` aceita dois argumentos:
1. `frase`: A string de texto que você deseja analisar.
2. `contar`: Uma string que pode ser "vogais" (padrão) ou "consoantes" para especificar o que contar.

O script de exemplo abaixo demonstra como usar a função e imprime a contagem para uma frase de exemplo.
"""

def conta_letras(frase, contar="vogais"):
  """
  Conta o número de vogais ou consoantes em uma frase.
  Letras maiúsculas são contadas da mesma forma que minúsculas.
  Caracteres acentuados não são contados como vogais/consoantes.
  """
  frase_lower = frase.lower()
  conta_tudo = frase_lower.replace(' ','') # tamanho total da frase sem os espaços
  dic_vogais = ['a','e','i','o','u']

  if contar == "vogais":
    conta_vogais = [vogal for vogal in conta_tudo if vogal in dic_vogais] # cria uma lista com todas as vogais da frase
    return len(conta_vogais)
  elif contar == "consoantes":
    # Filtra apenas por letras do alfabeto para evitar contar números e símbolos
    letras = [char for char in conta_tudo if 'a' <= char <= 'z']
    conta_consoantes = [consoante for consoante in letras if consoante not in dic_vogais]
    return len(conta_consoantes)
  else:
    return "Opção 'contar' inválida. Use 'vogais' ou 'consoantes'."

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    frase_exemplo = "programar em python é divertido"

    print(f"Analisando a frase: '{frase_exemplo}'")

    num_vogais = conta_letras(frase_exemplo, "vogais")
    print(f"Número de vogais: {num_vogais}")

    num_consoantes = conta_letras(frase_exemplo, "consoantes")
    print(f"Número de consoantes: {num_consoantes}")

    # Exemplo com a opção padrão (vogais)
    frase_exemplo_2 = "Testando a funcao"
    print(f"\nAnalisando a frase: '{frase_exemplo_2}'")
    num_vogais_2 = conta_letras(frase_exemplo_2)
    print(f"Número de vogais (padrão): {num_vogais_2}")