def main():
    escolha = 0
    while escolha != 1 and escolha != 2:
        print("Bem-vindo ao jogo Nim! Escolha:")
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato")
        escolha = int(input("Sua escolha: "))
        if escolha == 1:
            print("\nVocê escolheu uma partida isolada\n")
            print("****Partida****\n")
        elif escolha == 2:
            print("\nVocê escolheu um campeonato\n")
        else:
            print("\nOpção inválida! Você deve escolher 1 ou 2\n")
    return escolha


def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        q = n % (m+1)
        if q > 0:
            return q
    return m
        
def usuario_escolhe_jogada(n, m):
    j = 0
    while j == 0:
        j = int(input("\nQuantas peças você vai tirar? "))
        if j > n or j < 1 or j > m:
            print("Oops! Jogada inválida! Tente de novo.\n")
            j = 0
    return j

                
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    vez_do_computador = True

    if n%(m+1) == 0:
        vez_do_computador = False

    while n > 0:
        if vez_do_computador:
            j = computador_escolhe_jogada(n, m)
            vez_do_computador = False
            print("\nO computador tirou",j,"peça(s).")
        else:
            j = usuario_escolhe_jogada(n, m)
            vez_do_computador = True
            print("\nVocê tirou",j,"peça(s).")
        n = n - j
        print("Agora restam",n,"peça(s) no tabuleiro.")

    if vez_do_computador == True:
        print("Você ganhou!")
        return 1
    else:
        print("\nFim do jogo! O computador ganhou!")
        return 0


def campeonato():
    usuario = 0
    computador = 0

    print("\n****Rodada 1****\n")
    vencedor = partida()
    if vencedor == 1:
        usuario = usuario + 1
    else:
        computador = computador + 1

    print("\n****Rodada 2****\n")
    vencedor = partida()
    if vencedor == 1:
        usuario = usuario + 1
    else:
        computador = computador + 1

    print("\n****Rodada 2****\n")
    vencedor = partida()
    if vencedor == 1:
        usuario = usuario + 1
    else:
        computador = computador + 1

    print("\nPlacar: Você",usuario,"X",computador,"Computador")


if __name__ == "__main__":
    
    escolha = main()

    if escolha == 1:
        partida()
    else:
        campeonato()


