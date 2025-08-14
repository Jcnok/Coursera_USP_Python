n=int(input("Digite um número inteiro:"))
var_ant=0
var_atual=0
adj=True
while n>0 and adj:
    var_ant=n%10
    n=n//10
    var_atual=n%10
    if var_ant==var_atual:
        print("sim")
        break
else:
    print("não")