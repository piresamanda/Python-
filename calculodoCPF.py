import re
import sys

#solicita o CPF do usuário
entrada = input('Digite seu CPF: ')

#remove os caracteres especiais
cpf_enviado_usuario = re.sub(r'[^0-9]','', entrada)


#Verifica a quantidade de caracteres do CPF
if len(cpf_enviado_usuario) != 11 :
    print('CPF inválido com', (len(cpf_enviado_usuario)), 'digitos.')
    sys.exit()

#verifica se o CPF é sequencial
entrada_e_sequencial = cpf_enviado_usuario == cpf_enviado_usuario[0] * len(cpf_enviado_usuario)

if entrada_e_sequencial:
  print('Dados sequenciais são inválidos')
  sys.exit()
  
#Calculo do primeiro digito
nove_digitos = cpf_enviado_usuario[:9]
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

#Verificação de CPF

if cpf_gerado_calculo == cpf_enviado_usuario:
  print(entrada, ', CPF válido ')
else:
 print(entrada, 'CPF inválido')
