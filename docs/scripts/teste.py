numero=int(input("Digite um número inteiro:"))
resto = numero%10
inteiro = 0
soma = 0
i = 0
while numero > 0:
    if (resto != 0):
        resto=numero%10
        inteiro=numero//10
        soma=soma+resto
        numero=inteiro
    else:
        inteiro=numero//10
        resto=numero%10
        soma=resto
        numero=inteiro

print (soma)
