def n_primos(n):
    fator = 2
    primo=0
    contador = n
    while contador >= fator:
        while contador%fator !=0 :
            fator=fator+1
        if contador % fator == 0 and contador != fator:
            #print('nao é primo')
            contador = contador - 1
        else:
            #print(contador,'é primo')
            primo = primo +1
            contador = contador - 1
            fator=2
    return(primo)


n_primos(10)
