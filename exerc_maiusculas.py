def maiusculas(frase):
    M=""
    for i in frase:
        if ord(i) < 90 and ord(i) > 64:
          M += i
        else:
          pass
    return M 



