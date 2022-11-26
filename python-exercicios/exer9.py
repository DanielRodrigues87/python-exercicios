#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
# se ele vai se alistar no serviço militar.
#Se é hora de alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
anoAtual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = anoAtual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento,idade,anoAtual))
if idade == 18:
    print('Você tem que se alistar nas forças armadas.')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = anoAtual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = anoAtual - saldo
    print('Seu alistamento foi em {}'.format(ano))