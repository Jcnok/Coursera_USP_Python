"""
[DESCRIÇÃO DO SCRIPT]

Como usar:
[INSTRUÇÕES DE USO]
"""
def soma_hipotenusas(n):
    soma = 1
    hipo = 0
    while soma <= n:
        if é_hipotenusa(soma):
            hipo += soma
        soma += 1
    return hipo

def é_hipotenusa(n):
    from math import sqrt
    ca = 1
    co = 1
    hipo = False
    while ca <= n and not hipo:#loop cateto adjacente
        while co <= n and not hipo: #loop cateto oposto
            hipotenusa = sqrt(ca ** 2 + co ** 2)
            if n == hipotenusa:
                #print('hipotenusa: {} cateto adjacente {} cateto oposto {}'.format(hipotenusa, ca ,co))
                hipo = True
            co += 1
        co = 1
        ca += 1
    return hipo
    
def main():
    n = int(input('eh hipotenusa: '))
    print(soma_hipotenusas(n))
    
main()


# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    # TODO: Adicionar exemplo de execução com dados e prints.
    pass
