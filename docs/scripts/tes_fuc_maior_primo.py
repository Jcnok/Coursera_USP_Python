"""
[DESCRIÇÃO DO SCRIPT]

Como usar:
[INSTRUÇÕES DE USO]
"""
def maior_primo(n):
 e_primo=primo(n)
 while e_primo!=0:
    n-=1
    e_primo=primo(n)


 return n

def primo(n):
 e_primo = 0
 div = 2

 while (div < n and e_primo==0):
        if n % div == 0 and n!=div:
            e_primo = 1

        div = div + 1

 return e_primo


print(maior_primo(961))


# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    # TODO: Adicionar exemplo de execução com dados e prints.
    pass
