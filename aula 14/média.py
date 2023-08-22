# Crie um programa que realiza o cadastro de alunos e suas notas. O programa deve:

# Permitir ao usuário cadastrar o nome de um aluno e sua nota.
# Utilizar uma lista para armazenar os nomes dos alunos e uma lista separada para armazenar as notas.
# Apresentar uma estrutura de repetição que permite ao usuário cadastrar mais alunos e notas até que deseje parar.
# Ao final, exibir a média das notas cadastradas.

alunos = []

while True:

    continuar = input("Deseja continuar? (S/N)")

    if continuar == "S":

        nome = input("Digite o nome do aluno:")
        nota = float(input("Digite a nota:"))

        aluno = {"nome": nome, "nota": nota}

        alunos.append(aluno)
    else:
        print("Saindo...")
        break

print("Exibindo notas...")

print("Aluno  |  Nota")

soma = 0
for aluno in alunos:

    print(f"{aluno['nome']} | {aluno['nota']}")
    soma += aluno["nota"]

media = soma/len(alunos)
print(f"A média da turma é {media:.2f}")