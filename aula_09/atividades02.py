#Programa para calcular IMC

def calcule_imc(a, p):
    imc = p / (a * a)
    return imc


altura = float(input('Informe a altura:  '))
peso = float(input('Informe o peso:  '))

imc = calcule_imc(p / (a * a))

if imc < 16.9:
    print('Muito abaixo do peso')
elif imc < 18.4:
    print('Abaixo do peso')
elif imc < 24.9:
    print('Peso normal')
elif imc < 29.9:
    print('Acima do peso')
elif imc < 34.9:
    print('Obesidade grau I')
elif imc < 35:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')
