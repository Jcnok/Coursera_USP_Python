"""
[DESCRIÇÃO DO SCRIPT]

Como usar:
[INSTRUÇÕES DE USO]
"""
def computador_escolhe_jogada(n, m):
    Comp_Remove = 1 #var recebe 1
    while Comp_Remove != m:#enquanto var for diferente da var m faça;
        if (n - Comp_Remove) % (m+1) == 0:#se ex: se o resto da divisão de n-computador remove por m+1 for zero;
            return Comp_Remove # retorna para partida
        else:#senão
            Comp_Remove += 1 # var adiciona 1
    return Comp_Remove #retora para partida;
def usuario_escolhe_jogada(n, m):
    Jogo_Valido = False #var booleana
    while not Jogo_Valido: #enquanto a var for falsa
        Jogador_Remove = int(input('Quantas peças você vai tirar? '))#var que recebe quantidade de peças que o usuário irá tirar;
        if Jogador_Remove > m or Jogador_Remove < 1:#se a var do jogador for maior que M ou menor que 1 faça: 
            print()#espaço;
            print('Oops! Jogada inválida! Tente de novo.')#imprime a mensagem
            print()#espaço;
        else:#senão;
            Jogo_Valido = True # var recebe valor verdadeiro;
    return Jogador_Remove # retorna para partida;
def campeonato(): #função campeonato;
    Num_Rodada = 1 # se var for igual a 1
    while Num_Rodada <= 3: # enquanto a var for menor ou igual a 3 faça;
        print()#espaço
        print('**** Rodada', Num_Rodada, '****')#imprime a mensagem e a var;
        print()#espaço;
        partida()# chama função partida;
        Num_Rodada += 1 # adiciona mais 1 à var;
    print()#espaço;
    print('Placar: Você 0 X 3 Computador')#imprime mensagem;
def partida():#chama função da partida;
    n = int(input('Quantas peças? '))#var tipo inteira que recebe a quantidade de peças do jogo;
    m = int(input('Limite de peças por jogada? '))#var tipo interio que recebe o limite de peças por jogada;
    Rodada_PC = False #var booleana
    if n % (m+1) == 0: #se o resto de n dividido por m+1 for 0 faça;
        print()#espaço
        print('Voce começa!')# imprime a mensagem;
    else:#senão
        print()#espaço
        print('Computador começa!')#imprime a mensagem;
        Rodada_PC = True #var booleana
    while n > 0:#enquanto n for maior que zero faça;
        if Rodada_PC: #se a var for True faça;
            Comp_Remove = computador_escolhe_jogada(n, m) #variável recebe valores da função;
            n = n - Comp_Remove # n subtrai o número de peças que a função computador removeu;
            if Comp_Remove == 1: # se variavel fo 1 então:
                print()#espaço
                print('O computador tirou uma peça')#imprime a mensagem
            else:#senão;
                print()#espaço
                print('O computador tirou', Comp_Remove, 'peças')#imprime a mensagem com o valor da variável;
            Rodada_PC = False #var booleana;
        else:#senão;
            Jogador_Remove = usuario_escolhe_jogada(n, m)#var recebe valor da funçao;
            n = n - Jogador_Remove # n subtrai o número de peças que o usuário removeu;
            if Jogador_Remove == 1:#se var for 1;
                print()#espaço
                print('Você tirou uma peça')#imprime a mensagem;
            else:#senão;
                print()#espaço
                print('Você tirou', Jogador_Remove, 'peças')#imprime a mens. com o valor da var em questão;
            Rodada_PC = True #var booleana;
        if n == 1:#se n for igual a 1;
            print('Agora resta apenas uma peça no tabuleiro.')#imprime mensagem;
            print()#imprime espaço;
        else:#senão;
            if n != 0:#se n for diferente de zero;
                print('Agora restam,', n, 'peças no tabuleiro.')#imprime mens como valor da var em questão;
                print()# espaço;
    print('Fim do jogo! O computador ganhou!')#fim do while então imprime a mensagem;
print('Bem-vindo ao jogo do NIM! Escolha:')#início do Jogo;
print()#espaço
print('1 - para jogar uma partida isolada')#imprime a mensagem;
tipoDePartida = int(input('2 - para jogar um campeonato ')) #Váriavel tipo inteiro que recebe o tipo de partida;
if tipoDePartida == 2: # se a variável for 2;
    print()#espaço;
    print('Voce escolheu um campeonato!')#imprime na tela a mensagem;
    print()#espaço;
    campeonato()#vai para a função campeonato;
else:#senão;
    if tipoDePartida == 1:#se a variável for 1;
        print()#espaço
        partida()#vai para função partida;


# --- Bloco de Execução de Exemplo ---
if __name__ == "__main__":
    # TODO: Adicionar exemplo de execução com dados e prints.
    pass
