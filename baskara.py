# -*- coding: utf-8 -*-
"""
Este script calcula as raízes de uma equação de segundo grau (ax² + bx + c = 0)
utilizando a fórmula de Bhaskara.

Como usar:
O script solicitará que o usuário insira os valores para os coeficientes 'a', 'b' e 'c'.
Após a inserção, ele calculará o delta e, se houver raízes reais, as exibirá.
- Se delta < 0, informa que não há raízes reais.
- Se delta = 0, informa a raiz única.
- Se delta > 0, informa as duas raízes, ordenadas.
"""
import math

# Solicita os coeficientes da equação ao usuário
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

# Calcula o delta
delta = (b**2) - (4 * a * c)

# Verifica as condições do delta e calcula as raízes
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    if delta == 0:
        print("a raiz desta equação é", x1)
    else:
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        if x1 < x2:
            print("as raízes da equação são", x1, "e", x2)
        else:
            print("as raízes da equação são", x2, "e", x1)
        