
import random
import sys

nove_digitos = '' #armazena os nove digitos

#gera os nove digitos inteiros 
for i in range(9): 
 nove_digitos += str(random.randint(0,9))

#calculo primeiro digito
contador_regressivo1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
 resultado_digito_1 += int(digito) * contador_regressivo1
 contador_regressivo1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 < 10 else 0

# Aqui é calculado o segundo digito
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
 resultado_digito_2 += int(digito)*contador_regressivo2
 contador_regressivo2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 < 10 else 0  # Corrigindo para que, se for maior ou igual a 10, o dígito seja 0

cpf_gerado_calculo = nove_digitos + str(digito_1) + str(digito_2)

#Mostra o CPF gerado
print(cpf_gerado_calculo, ', CPF válido ')
