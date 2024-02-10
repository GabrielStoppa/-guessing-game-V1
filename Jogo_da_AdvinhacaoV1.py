import random

def iniciar_jogo_adivinhacao():
    n_random = random.randint(0, 10)
    regra = """ 
    AS REGRAS SÃO SIMPLES SÃO ELAS:
    1- VOCÊ TERÁ 3 TENTATIVAS PARA ACERTAR, SE NÃO GAME OVER
    2- TENTE ACERTAR O NÚMERO ENTRE 0 E 10
    """

    print("\n   SEJA BEM-VINDO AO JOGO DA ADIVINHAÇÃO!   ")
    print(regra)

    # Repetir a pergunta até que o jogador esteja preparado
    while True:
        start = input("\nVocê está preparado? (sim/não): ").upper()
        if start == "SIM":
            break
        else:
            print("Por favor, responda com 'sim' para iniciar o jogo.")

    acerto = False
    total_tentativa = 3

    for x in range(1, total_tentativa + 1):
        print(f'Tentativa {x} de {total_tentativa}')
        numero = int(input("O número foi sorteado! Qual foi ele? "))
        assert 0 <= numero <= 10, "O número deve estar entre 0 e 10"

        if numero == n_random:
            acerto = True
            break
        else:
            if numero > n_random:
                print("Eita! Calma lá amigão, talvez o buraco seja mais lá embaixo...")
            elif numero < n_random:
                print("Eita! Que tal subir uns degraus?")

    if not acerto:
        print(f'\nVocê Perdeu! o número sorteado era {n_random}')
    else:
        print(f'\nVocê Acertou! O número sorteado foi {n_random}')
    print("\n#################### FIM DE JOGO ####################")

iniciar_jogo_adivinhacao()
