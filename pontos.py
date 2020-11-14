x1=(int(input("Digite o número Correspondente a x1:")))
y1=(int(input("Digite o número Correspondente a y1:")))
x2=(int(input("Digite o número Correspondente a x2:")))
y2=(int(input("Digite o número Correspondente a y2:")))
import math
d=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
if d>=10:
    print("longe")
else:
    print("perto")