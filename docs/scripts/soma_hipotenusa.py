"""
[DESCRIÇÃO DO SCRIPT]

Como usar:
[INSTRUÇÕES DE USO]
"""
# Para n = 25, as hipotenusas são:
# 5, 10, 13, 15, 17, 20, 25
# note que cada número deve ser somado apenas uma vez. Assim:
#soma_hipotenusas(25)
# deve devolver 105

#laço de 1 até n para verificar se é hipotenusa ou não
def soma_hipotenusas(n):

    soma = 1

    soma_hip = 0

    while soma <= n:

        if é_hipotenusa(soma):

            #print(soma)

            soma_hip = soma_hip + soma

        soma = soma + 1

    return soma_hip



def é_hipotenusa(x):

    cat1=1
    cat2=1
    hipotenusa=False
    import math

    while cat1 <= x and not hipotenusa:

        cat2 = 1

        while cat2 <= x and not hipotenusa:

            h = (math.sqrt(cat1**2 + cat2**2))

            if x == h:

                hipotenusa = True

            cat2 = cat2 + 1
        cat1 = cat1 +1

    return hipotenusa

print(soma_hipotenusas(5))


# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    # TODO: Adicionar exemplo de execução com dados e prints.
    pass
