import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    lista=[wal, ttr, hlr, sal, sac, pal]
    return lista

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
    Sab = 0
    for i in range(len(as_a)): #i vai de 0 a 5 = 6 traços linguísticos
        Sab = Sab + abs(as_a[i] - as_b[i])
        #print("Diferença: ",abs(as_a[i] - as_b[i]))
    Sab = Sab/6
    return Sab

def lista_palavra_texto(texto):
    ''' Função que lista todas as palavras do texto'''
    lista_sentenca=separa_sentencas(texto)
    lista_palavra=[]
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            for palavra in separa_palavras(frase):
                lista_palavra.append(palavra)
    return lista_palavra

def tamanho_medio_palavras(texto):
    ''' Função que calcula o tamanho médio de palavras do texto'''
    lista_palavra=lista_palavra_texto(texto)
    soma=0
    for palavra in lista_palavra:
        soma=soma+len(palavra)
    media=soma/len(lista_palavra)
    return media

def relacao_type_token(texto):
    ''' Função que calcula a relação Type-Token de palavras do texto'''
    lista_palavra=lista_palavra_texto(texto)
    relacao = n_palavras_diferentes(lista_palavra)/len(lista_palavra)
    return relacao

def razao_hapax_Legomana(texto):
    ''' Função que calcula razão de Hepax-Legomana do texto'''
    lista_palavra=[]
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            for palavra in separa_palavras(frase):
                lista_palavra.append(palavra)
    razao=n_palavras_unicas(lista_palavra)/len(lista_palavra)
    return razao

def tamanho_medio_sentenca(texto):
    ''' Função que calcula tamanho médio de sentenças do texto'''
    lista_sentenca=separa_sentencas(texto)
    n_sentenca=len(lista_sentenca)
    n_caracteres=0
    i=0
    while i<n_sentenca:
        n_caracteres=n_caracteres+len(lista_sentenca[i])
        i=i+1
    media=n_caracteres/n_sentenca
    return media

def complexidade_media_sentenca(texto):
    ''' Função que determina a complexidade média de sentencas do texto'''
    lista_sentenca=separa_sentencas(texto)
    lista_frase=[]
    for sentenca in lista_sentenca:
        lista_frase.extend(separa_frases(sentenca))
    complexidade=len(lista_frase)/len(lista_sentenca)
    return complexidade

def tamanho_medio_frase(texto):
    ''' Função que calcula o tamanho médio das frases do texto'''
    lista_frase=[]
    n_caracteres=0
    lista_frase=[]
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            lista_frase.append(frase)
    i=0
    while i<len(lista_frase):
        n_caracteres=n_caracteres+len(lista_frase[i])
        i=i+1
    media=n_caracteres/len(lista_frase)
    return media

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    # Chama as funções para determinar a assinatura do texto#
    t_wal = tamanho_medio_palavras(texto)
    t_ttr = relacao_type_token(texto)
    t_hlr = razao_hapax_Legomana(texto)
    t_sal = tamanho_medio_sentenca(texto)
    t_sac = complexidade_media_sentenca(texto)
    t_pal = tamanho_medio_frase(texto)
    return [t_wal, t_ttr, t_hlr, t_sal, t_sac, t_pal]

def avalia_textos(textos, assinatura):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    # Seleciona cada texto digitado e calcula assinatura#
    n_textos= len(textos)
    grau_similaridade=[]
    ass_texto=0
    i=0
    while i<n_textos:
        ass_texto=calcula_assinatura(textos[i]) #calcula a assinatura do texto#
        grau_similaridade.append(compara_assinatura(ass_texto, assinatura))
        i+=1
        print("Assinatura do texto %d: ",i,ass_texto)
    print("Grau de Similaridade: ",grau_similaridade)
    # Determina qual texto com menor probabilidade de estar infectado com COH-PIAH#
    Maior_Probabilidade = grau_similaridade[0]
    i=1
    texto_infectado=0
    while i<n_textos:
        if grau_similaridade[i]<Maior_Probabilidade:
            Maior_Probabilidade = grau_similaridade[i]
            texto_infectado=i
        i+=1
    print("Menor grau de similaridade:",texto_infectado+1)
    return texto_infectado

def main():
    '''FUNÇÃO PRINCIPAL. Inicia a execução do programa '''
    #print("")
    ass_cp=[]
    textos_lidos=[]
    ass_cp = le_assinatura()             #leitura dos traços linguísticos e devolve uma lista com a assinatura#
    print("")
    textos_lidos = le_textos()           #lê os textos digitados e devolve uma lista de textos#
    texto_infectado=avalia_textos(textos_lidos, ass_cp)  #todos os textos serão comparados com a assinatura do aluno infectado com COH-PIAH para ver qual é mais parecido
    print("")
    print ("O autor do texto %d está infectado com COH-PIAH" %(texto_infectado+1))

main()
