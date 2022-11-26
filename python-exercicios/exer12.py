#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#-À vista dinheiro/pix: 10% de desconto
#-À vista cartão: 5% de desconto
#-Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
print('{:=^40}'.format('LOJAS DANIEL'))
preco = float(input('Preço das compras: R$'))
print(' Formas de pagamento\n[1] à vista dinheiro ou pix\n[2] à vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco 
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalParcelas = int(input('Quantas parcelas? '))
    parcela = total / totalParcelas
    print('Sua compra será parcelada em {} de R${:.2f}'.format(totalParcelas,parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco,total))