# def multa(peso):
#     total = peso * 4
#     return total 



# peso_total = float(input('Informe o peso total de peixes:  '))
# if peso_total > 100:
#     multa(peso_total)

# else:
#     print('Não há multa')



# ------------- correção professor------------------

def calcula_multa(exc):    
    multa = exc * MULTA_KG
    return multa


MULTA_KG = 4.00
QUILOS_PERMITIDO = 100

peso_pescado = float(input('Informe o peso  '))

if peso_pescado > QUILOS_PERMITIDO:
    excedente = peso_pescado - QUILOS_PERMITIDO
    vl_multa = calcula_multa(excedente)
    print(f'O valor da multa é {vl_multa}')
else:
    print('Não há multa à pagar')


print('Programa encerrado!  ')