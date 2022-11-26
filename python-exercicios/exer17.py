#Crie um programa que simule o funcionamento de um caixa eletrônico.No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#Obs: Considere que o caixa possui cédulas de R$50,R$20,R$10 e R$1.
print('=' * 30)
print('{:^30}'.format('BANCO MST'))
print('=' * 30)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor 
totalCedula = 0
cedula = 50
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print('Total de {} cédulas de R${}'.format(totalCedula,cedula))
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO MST!')

