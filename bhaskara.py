# Equação do 2º Grau utilizando Python
import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
print('')

delta = (-b) ** 2 - 4 * a * c
print(f'O valor de Delta é: {delta}')
print('')

if delta <= 0:
    print('Não existe raízes reais para a solução.')
else:
    x1 = -b + math.sqrt(delta) / 2 * a
    x2 = -b - math.sqrt(delta) / 2 * a
    print(f'O valor de X1 e X2 é, respectivamente, {x1} e {x2}')
