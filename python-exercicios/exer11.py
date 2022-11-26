#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
#calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso.
#Entre 18.5 e 25: Peso ideal.
#Entre 25 até 30: Sobrepeso.
#Entre 30 até 40: Obesidade.
#Acima de  40: Obesidade mórbida.
peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('Seu peso é normal')
elif 25 <= imc < 30:
    print('Você está com sobrepeso')
elif 30 <= imc < 40:
    print('Você está com obesidade')
elif imc >= 40:
    print('Você está com obesidade mórbida')
