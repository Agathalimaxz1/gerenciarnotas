from funcoes import *
import tabulate
lista_alunos = []
while True:
    print ('''Menu:
    1. Cadastrar alunos e notas
    2. Exibir relatório
    0. Sair
    ''')
    opcao = input("Escolha sua opçao: ")
    if opcao == "1":
        notas = []
        aluno = input("Digite o nome do aluno: ")
        for n in range(3):
            nota = int(input("Digite as notas: "))
            notas.append(nota)
        media = calcular_media(notas)
        situacao = verificar_situacao(media)
        aluno = {"aluno" : aluno, "notas" : notas, "situacao": situacao}
        lista_alunos.append(aluno)
    elif opcao == "2":
        print(lista_alunos)
    elif opcao == "0":
        print("programa finalizado!")
        break
   