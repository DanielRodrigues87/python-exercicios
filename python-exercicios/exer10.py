#A Confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: Mirim
#Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 25 anos: Sênior
#Acima: Master
from datetime import date
anoAtual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = anoAtual - nascimento
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 25:
    print('Classificação: Sénior')
else:
    print('Classificação: Master')

