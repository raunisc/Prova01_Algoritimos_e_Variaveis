#exemplos de tipos de variaveis
#inteiro
inteiro = int(input("Digite um numero inteiro: "))
#real
real = float(input("Digite um numero real: "))
#texto
texto = input("Digite um texto: ")
#logico
logico = bool(input("Digite um valor logico: "))

#crie uma solicitaçao de dados ao usuario
nome = input("Digite seu nome: ")
bairro = input("Digite seu bairro: ")
habitantes = int(input("Digite a quantidade de habitantes: "))

#imprima a solicitação anterior na tela com uma mensagem personalizada
print(f"Olá {nome} seu bairro é: {bairro} e tem {habitantes} habitantes, que legal!")
