# Códigos de cores ANSI
RESET = "\033[0m"
VERDE = "\033[32m"
VERMELHO = "\033[31m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
ROXO = "\033[35m"

import random
import os

opcoes = ["1", "2", "3"]

nomes = {"1": "Pedra", "2": "Papel", "3": "Tesoura"}

vitorias = 0
empates = 0
derrotas = 0

print ("======================================================")
print ("===============PEDRA, PAPEL E TESOURA=================\n")
total_rodadas = input("Quantas Rodadas você deseja? ")


while not total_rodadas.isdigit():
     total_rodadas = input("Digite um número válido de rodadas: ")

total_rodadas = int(total_rodadas)

for rodada in range(1, total_rodadas + 1):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"========= Rodada {rodada} de {total_rodadas} =========\n")
    print("=============================")
    print("Escolha sua jogada:\n")
    print("1 - Pedra\n2 - Papel\n3 - Tesoura\n")

    jogador= input().strip()

    maquina = random.choice(opcoes)

    if jogador not in opcoes:
        print("Jogada inválida! Tente novamente.\n")
        continue
    print (f"Você escolheu: {nomes[jogador]}")
    print (f"A maquina escolheu: {nomes[maquina]}")

    if jogador == maquina:
       # print(AMARELO + "Empate!!" + RESET)
        empates +=1


    elif (jogador == "1" and maquina == "3") or \
        (jogador == "3" and maquina == "2") or \
        ( jogador == "2" and maquina == "1"):
        # print(VERDE + "Você venceu!!" + RESET)
         vitorias +=1

    elif jogador in opcoes:
       # print(VERMELHO + "Você perdeu!" + RESET)
        derrotas +=1

    else: print("Opcao invalida")

   
    print("\n===== PLACAR FINAL =====")
    print(VERDE + f"Vitórias: {vitorias}" + RESET)
    print(VERMELHO + f"Derrotas: {derrotas}" + RESET)
    print(AMARELO + f"Empates: {empates}" + RESET)

if vitorias > derrotas:
    print(VERDE + "\nVocê foi o campeão!" + RESET)
elif derrotas > vitorias:
    print(VERMELHO + "\nA máquina venceu a disputa!" + RESET)
else:
    print(AMARELO + "\nA disputa terminou empatada!" + RESET)


input("\nPressione Enter para sair...")
 
        













