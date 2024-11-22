'''
Faça jogo para o usuário adivinhar qual a palavra secreta. Você vai propor uma palavra secreta qualquer e vai dar a
possibilidade para o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.

- Se a letra digitada estiver na palavra secreta; exiba a letra.
- Se a letra digitada não estiver na palavra secreta; exiba *.
- Fazer a contagem de tentativas.
'''

palavra = 'fernando'

while True:

    letra = input('Digite uma letra: ')

    for l in palavra:
        if l == letra:
            print(f'Você acertou uma letra. Palavra secreta: {len(palavra) * '*'}')
