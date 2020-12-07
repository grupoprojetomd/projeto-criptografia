from desencriptar import desencriptar
from encriptar import encriptar
from gerarChavePublica import gerarChavePublica

print("==== CRIPTÓGRAFO ====\n")

print("O que você deseja fazer?")
print("1 - Gerar chave pública")
print("2 - Encriptar")
print("3 - Desencriptar\n")

opcao = int(input("-> "))


if (opcao == 1):
    numeroPrimo1 = int(input("Digite um número primo: "))
    numeroPrimo2 = int(input("Digite outro número primo: "))
    expoente = int(input("Digite o expoente:"))
    chavePublica = gerarChavePublica(numeroPrimo1, numeroPrimo2, expoente)

    print(chavePublica)

elif (opcao == 2):

    encriptar()
elif (opcao == 3):
    desencriptar()
else:
    print("Opção Inválida")