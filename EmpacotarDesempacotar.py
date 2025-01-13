# Empacotamento e desempacotamento de dicionários

a, b = 1 ,2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

a, b = pessoa.values()
print(a, b)

a, b = pessoa.items()
print(a, b)