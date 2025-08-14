largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
h=altura
while h > 0:
       c = largura
       while c > 0:
                print('#',end='')
                c = c - 1
       h = h - 1
       print()
