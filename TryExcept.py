'''
Introdução ao try/except
try -> tentar executar um bloco de código
except -> ocorreu algum erro ao tentar executar
'''

numero = input ('Vou dobrar o número que você digitar: ')

try:
    # Conversão de tipo de uma variavel
    numeroFloat = float(numero) 
    print(f'O dobro de {numero} é {numeroFloat * 2:.2f}')
except:
    print('Isso não é um número.')