"""
[DESCRIÇÃO DO SCRIPT]

Como usar:
[INSTRUÇÕES DE USO]
"""
def maiusculas(frase):
    M=""
    for i in frase:
        if ord(i) < 90 and ord(i) > 64:
          M += i
        else:
          pass
    return M





# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    # TODO: Adicionar exemplo de execução com dados e prints.
    pass
