#Digite um número inteiro: 78615
#O dígito das dezenas é 1
num=int(input("Digite um número inteiro:"))
dez=(((num%10000)%1000)%100)//10
print("O dígito das dezenas é",dez)