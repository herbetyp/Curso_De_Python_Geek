"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

O que são testes unitários?

Testes unitários é a forma de se testar unidades undividuais de código fonte

Unidades individuais poder ser: funções, métodos, classes, módulos etc...

# OBS: Teste unitários não é especifico da Linguagem Python.

Para criar nossos testes criamos classes que herdam de unittest.TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo

Para rodar os testes, utilizamos unittest.main()

TesteCase -> Casos de testes para sua unidade

# Conhecendo os assertions
https://docs.python.org/3/library/unittest.html

Método                            Checa se
--------------------------------------------------
assetEqual(a, b)                  a == b
assertNotEqual(a, b)              a != b
assertTrue(x)                     x é verdadeiro
assertFalse(x)                    x é falso
assertIs(a, b)                    a é b
assertIsNot(a, b)                 a não é b
assertIfNone(x)                   x é None
assertIsNotNone(x)                x não é None
assertIn(a, b)                    a está em b
assertNotIn(a, b)                 a não está em b
assertIsInstance(a, b)            a é instância de b
assertNotIsInstance(a, b)         a não é instância de b

Por convenção todos os testes em uma test case, devem ter seu nome
iniciado com test_

Para executar os testes com unittest

python nome_do_modulo.py

# Para executar os testes com unittest com verbose (detalhes)

python nome_do_modulo.py -v

# Docstrings dos testes

Podemos acrescentar (e é recomendado) docstrings em nossos testes

"""
# Prática - Utilizando a abordagem TDD
