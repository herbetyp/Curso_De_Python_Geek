"""
POO - Métodos Mágicos

Métodos mágicos são todos os métodos que utilizam dunder __.


Dunder > Double Underscore __

# dunder init -> __init__()
def __init__(self, titulo, autor, paginas):
    self.__titulo = titulo
    self.__autor = autor
    self.__paginas = paginas


# dunder repr -> Representação do objeto
def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor}'

"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __str__(self):
        return self.__titulo

    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor}'

    def __len__(self):
        return self.__paginas

    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memoria')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python Rocks', 'Geek', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)


print(livro1)
print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)

print(livro1 * 3)
