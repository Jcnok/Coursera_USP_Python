impar=int(input("Digite o valor de n:"))
impar=impar*2
contador=1
while(impar>=0):
    if((impar%2)!=0):
        print(contador)
        contador=contador+2
        impar=impar-1
    else:
        impar=impar-1