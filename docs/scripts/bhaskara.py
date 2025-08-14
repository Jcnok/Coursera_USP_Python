# criando uma formula que calcula a formula de Baskara
# Delta = (b**2)- 4*a*c
# -b + ou - a raiz de delta /2.a
a=float(input("Informe o valor de a:"))
b=float(input("Informe o valor de b:"))
c=float(input("Informe o valor de c:"))
Delta=b**2-4*a*c
if Delta<0:
    print("esta equação não possui raízes reais")
else:
    import math
    x=((-b+math.sqrt(Delta))/(2*a))
    y=((-b-math.sqrt(Delta))/(2*a))
    if Delta==0:
        print("a raiz desta equação é",x)
    else:
        if x<y:
            print("as raízes da equação são",x,"e",y)
        else:
            print("as raízes da equação são",y,"e",x)
