# -*- coding: utf-8 -*-
"""
Este script é um detector automático de plágio, especificamente do fenômeno COH-PIAH,
que ocorre quando um autor deliberadamente altera um texto para disfarçar a cópia.

O programa calcula 6 traços linguísticos de um texto (ou de vários) e os compara
com a assinatura de um autor sabidamente infectado por COH-PIAH. O texto com a
assinatura mais similar é considerado o plágio.

Como usar:
O script, quando executado, não pedirá por entradas. Em vez disso, ele usará
uma assinatura e uma coleção de textos de exemplo que já estão no código para
demonstrar seu funcionamento. Ele imprimirá a assinatura de cada texto e, ao final,
indicará qual texto tem a maior probabilidade de ser um plágio.
"""
import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.\n")

    tamMedPalavra = float(input("Entre o tamanho medio de palavra: "))
    typeToken = float(input("Entre a relação Type-Token: "))
    hapaxLegomana = float(input("Entre a Razão Hapax Legomana: "))
    tamMedSentenca = float(input("Entre o tamanho médio de sentença: "))
    comMedSentenca = float(input("Entre a complexidade média da sentença: "))
    tamMedFrase = float(input("Entre o tamanho medio de frase: "))

    print()

    return [tamMedPalavra, typeToken, hapaxLegomana, tamMedSentenca, comMedSentenca, tamMedFrase]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    print()
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        print()

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
    """IMPLEMENTADO PELO ALUNO"""
    somatorio = 0
    for i in range(len(as_a)):
        somatorio += abs(as_a[i] - as_b[i])

    return somatorio / 6

def calcula_assinatura(texto):
    """IMPLEMENTADO PELO ALUNO"""
    sentencas = separa_sentencas(texto)

    frases = []
    for s in sentencas:
        frases.extend(separa_frases(s))

    palavras = []
    for f in frases:
        palavras.extend(separa_palavras(f))

    num_palavras = len(palavras)
    soma_tam_palavras = sum(len(p) for p in palavras)
    tam_medio_palavra = soma_tam_palavras / num_palavras if num_palavras > 0 else 0

    type_token = n_palavras_diferentes(palavras) / num_palavras if num_palavras > 0 else 0

    hapax_legomana = n_palavras_unicas(palavras) / num_palavras if num_palavras > 0 else 0

    num_sentencas = len(sentencas)
    soma_car_sentencas = sum(len(s) for s in sentencas)
    tam_medio_sentenca = soma_car_sentencas / num_sentencas if num_sentencas > 0 else 0

    num_frases = len(frases)
    complexidade_sentenca = num_frases / num_sentencas if num_sentencas > 0 else 0

    soma_car_frases = sum(len(f) for f in frases)
    tam_medio_frase = soma_car_frases / num_frases if num_frases > 0 else 0

    return [tam_medio_palavra, type_token, hapax_legomana, tam_medio_sentenca, complexidade_sentenca, tam_medio_frase]

def avalia_textos(textos, ass_cp):
    """IMPLEMENTADO PELO ALUNO"""
    assinaturas_textos = [calcula_assinatura(texto) for texto in textos]

    similaridades = [compara_assinatura(ass_cp, ass_texto) for ass_texto in assinaturas_textos]

    # Encontra o texto com a menor similaridade (mais parecido)
    menor_similaridade = min(similaridades)
    indice_infectado = similaridades.index(menor_similaridade)

    # O enunciado pede para retornar o número do texto (1, 2, 3...), não o índice (0, 1, 2...)
    return indice_infectado + 1

# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    # Assinatura de um autor sabidamente infectado por COH-PIAH
    assinatura_base = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]

    # Textos de exemplo para avaliação
    texto1 = "Muito além, nos confins inexplorados da ponta mais cafona da extremidade oeste da Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distância de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão primitivas que ainda acham que relógios digitais são uma grande ideia."
    texto2 = "Apesar da simplicidade aparente, a jornada de Frodo em direção à Montanha da Perdição foi repleta de perigos e desafios. A cada passo, o poder do Anel o tentava, sussurrando promessas de poder e domínio. A amizade de Sam, no entanto, provou ser um escudo mais forte do que qualquer armadura, mantendo a esperança viva nos momentos mais sombrios."
    texto3 = "A teoria da relatividade geral, proposta por Albert Einstein no início do século XX, revolucionou nossa compreensão da gravidade. Ela descreve a gravidade não como uma força, mas como uma curvatura no tecido do espaço-tempo, causada pela massa e energia. Planetas, estrelas e até a luz seguem essas curvas, o que explica fenômenos como a órbita dos planetas e as lentes gravitacionais."

    textos_exemplo = [texto1, texto2, texto3]

    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Este script analisará 3 textos de exemplo para encontrar o mais provável de ter sido escrito por um autor infectado.\n")
    print("-" * 20)

    # Avalia os textos
    autor_infectado = avalia_textos(textos_exemplo, assinatura_base)

    print(f"\nO autor do texto {autor_infectado} está infectado com COH-PIAH.")
