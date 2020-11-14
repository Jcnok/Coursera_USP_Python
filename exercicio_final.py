import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    Tam_Med_palavra      = float(input("Entre o tamanho medio de palavra:"))
    Type_Token           = float(input("Entre a relação Type-Token:"))
    Hapax_Legomana       = float(input("Entre a Razão Hapax Legomana:"))
    Tam_Med_Sentença     = float(input("Entre o tamanho médio de sentença:"))
    Complex_Med_Sentença = float(input("Entre a complexidade média da sentença:"))
    Tam_Med_Frase        = float(input("Entre o tamanho medio de frase:"))

    return [Tam_Med_palavra, Type_Token, Hapax_Legomana, Tam_Med_Sentença, Complex_Med_Sentença, Tam_Med_Frase]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)
    

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    Somatorio = 0
    for i in range(len(as_a)):
        Somatorio = Somatorio + abs(as_a[i] - as_b[i])
    return Somatorio / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    Sentencas           = separa_sentencas(texto)
    Num_Sentencas       = 0
    Num_Palavras        = 0
    Soma_Char_Sentencas = 0
    Soma_Char_Frases    = 0
    Total_Char          = 0
    Frases              = []
    Palavras            = []

    for i in range(len(Sentencas)):
        Frase_aux = separa_frases(Sentencas[i])
        Frases.extend(Frase_aux)
        Num_Sentencas = Num_Sentencas + 1
        Soma_Char_Sentencas = Soma_Char_Sentencas + len(Sentencas[i])
        
    for i in range(len(Frases)):
        Num_Frases = len(Frases)
        Soma_Char_Frases = Soma_Char_Frases + len(Frases[i])
        Num_Palavras = Num_Palavras + len(separa_palavras(Frases[i]))
        Palavras_aux = separa_palavras(Frases[i])
        Palavras.extend(Palavras_aux)
        
    for i in range(len(Palavras)):
        Total_Char = Total_Char + len(Palavras[i])        
    

    Tam_Med_palavra      = Total_Char / Num_Palavras
    Type_Token           = n_palavras_diferentes(Palavras) / Num_Palavras
    Hapax_Legomana       = n_palavras_unicas(Palavras) / Num_Palavras
    Tam_Med_Sentença     = Soma_Char_Sentencas / Num_Sentencas
    Complex_Med_Sentença = Num_Frases / Num_Sentencas
    Tam_Med_Frase        = Soma_Char_Frases / Num_Frases
         
    return [Tam_Med_palavra,Type_Token,Hapax_Legomana,Tam_Med_Sentença,Complex_Med_Sentença,Tam_Med_Frase]
    #return (Num_Sentencas,Num_Frases,Num_Palavras,Soma_Char_Sentencas,Soma_Char_Frases,Total_Char)
           
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    Assinaturas = []

    for i in textos:
        Assinaturas.append(calcula_assinatura(i))
    Similaridade = []
    for i in Assinaturas:
        Similaridade.append(compara_assinatura(ass_cp, i))
    Maior = Similaridade[0]
    Posicao = 0
    for i in range(len(Similaridade)):
        if Similaridade[i] > Maior:
            Maior = Similaridade[i]
            Posicao = i
    return Posicao

def main():
    ass_cp = le_assinatura()
    textos = le_textos()

    return print("O autor do texto " , avalia_textos(textos, ass_cp), " está infectado com COH-PIAH")






























