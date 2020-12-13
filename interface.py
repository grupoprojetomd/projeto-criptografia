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
    expoente = int(input("Digite o expoente: "))
    
    resultado = gerarChavePublica(numeroPrimo1, numeroPrimo2, expoente)
    
    chavePublica = resultado['chavePublica']

    if (resultado['erro']):
        print(resultado['erro'])
    else:
        arquivo = open("chave-publica.txt", "w")
        arquivo.write("({}, {})".format(chavePublica[0], chavePublica[1]))
        print("Chave pública gerada com sucesso! Arquivo chave-publica.txt criado!")

elif (opcao == 2):
    texto = input('Digite a mensagem de texto que deseja encriptar: ')

    chavePublica = []
    chavePublica.append(int(input('Digite o primeiro valor da chave pública: ')))
    chavePublica.append(int(input('Digite o valor do expoente: ')))

    mensagemEncriptada = encriptar(texto, chavePublica)
    quantidadeCaracteresMensagem = len(mensagemEncriptada) # 6

    stringFinal = ""
    for inteiro in range(quantidadeCaracteresMensagem):

        numero = mensagemEncriptada[inteiro]
        if (inteiro == 0):
            stringFinal += str(numero)
        else:
            stringFinal += "," + str(numero)

    arquivo = open("mensagem-encriptada.txt", "w")
    arquivo.write(stringFinal)
    print("Mensagem encriptada com sucesso!\nArquivo mensagem-encriptada.txt criado!")
elif (opcao == 3):
    numeroPrimo1 = int(input("Digite um número primo: "))
    numeroPrimo2 = int(input("Digite outro número primo: "))
    expoente = int(input("Digite o expoente: "))

    mensagemEncriptada = open("mensagem-encriptada.txt", "r")

    mensagemEncriptadaArray = mensagemEncriptada.read().split(',')

    resultado = desencriptar(mensagemEncriptadaArray, expoente, numeroPrimo1, numeroPrimo2)
    mensagem = resultado['mensagemFinal']


    if (resultado['erro']):
        print(resultado['erro'])
    else:
        arquivo = open("mensagem-descriptografada.txt", "w")
        arquivo.write(mensagem)
        print("Mensagem descriptografada com sucesso!\nArquivo mensagem-descriptografada.txt criado!")
else:
    print("Opção Inválida")