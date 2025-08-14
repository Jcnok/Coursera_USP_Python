largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
h=altura
while h > 0:
    if h == altura or h == 1:
        print('#' * largura)
        h = h - 1
    else :
        c = largura

        while c > 0:
            if c == largura or c == 1:
                print('#',end='')
                c = c - 1
            else :
                print(' ',end='')
                c = c - 1
        h = h - 1
        print()
