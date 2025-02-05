# POO em Python

'''
    Atributos especiais em python
    __name__
    __class__
Especificar o tipo de atributo
(self.__atributo :int)
'''

class Animal:
    def __init__(self, age: int, height: int, weigth: int, position: tuple):
        self.age = age
        self.height = height
        self.weigth = weigth
        self.position: tuple = position

    def move_x(self):
        self.position[0] += 1

    def move_y(self):
        self.position[1] += 1
    
    def move_z(self):
        self.position[2] += 1

class Dog(Animal):# para herdar os atributos e métodos da classe PAI em python ela é informada na classe filha entre ()
    family = 'Canidae'# Definição de um atributo da classe.

    # Objeto pertencente a classe DOG
    ''' O __ refere-se a métodos especiais que são invocados automaticamente em situações especificas, 
tambem é possivel definir a tipagem do parametro. Setar o atributo no init permite que ele seja passado quando o objeto foi instanciado.'''
    def __init__(self, age: int, height: int, weigth: int, position: tuple):
        Animal.__init__(self, age, height, weigth, position)

        def move_z(self):
            self.position[2] += 2

        # Chama a classe Pai usando super e seu construtor __init__, é possivel tambem chamar usando o nome da propria classe PAI ao invés de SUPER
        # self.age: int = age       # Este age se refere ao parametro passado acima, e o age branco é o atribuido ao objeto.
        # self.__peso = peso # Incluindo mais um atributo ao objeto DOG, quando o atributo tem 2 underscore antes do nome, significa que ele não deve ser mexido
        #                    # já que o python não trabalha com atributos privados, essa é uma forma de impedir alterações.

# -- Main
# rex = Dog(10) #Passando o parametro ao instanciar o objeto DOG.
# print(f'A idade do rex é {rex.age}')
# caramelo = Dog(5)
# print(f'A idade do caramelo é {caramelo.age}')
# print(f'A classe DOG pertence a familia dos {Dog.family}')
# print(f'Rex é um objeto de qual classe? R: {rex.__class__.__name__}')

# Herança em Python.

caramelo = Dog(age=10, height=50, weigth=30, position=(0, 0, 0))
print(caramelo.age)