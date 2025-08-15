"""
[DESCRIÇÃO DO SCRIPT]

Como usar:
[INSTRUÇÕES DE USO]
"""
def fatorial(n):
    fat = 1
    while (n>1):
        fat=fat*n
        n=n-1
    return fat


def n_binomial(n,k):
    return fatorial(n)/fatorial(k)*fatorial(n-k)




# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    # TODO: Adicionar exemplo de execução com dados e prints.
    pass
