#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal
numero = int(input('Digite um número inteiro: '))
print('Escolha uma base de conversão:\n[ 1 ] converter para Binário\n[ 2 ] converter para Octal\n[ 3 ] converter para Hexadecimal')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido em Binário é igual a {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('{} convertido em Binário é igual a {}'.format(numero, oct(numero)))
elif opcao == 3:
    print('{} convertido em Binário é igual a {}'.format(numero, hex(numero)))
else:
    print('Opção inválida. Digite novamente')