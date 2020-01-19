"""
Decoradores (Decoretors)

O que sõa decorators?

- Decorators são funções
- Decorators envolvem outras funções e aprimoram seu comportamento
- Decorators também são exemplos de Higher Order Functions
- Decorator tem uma sintaxe própia, usando "@" (Syntact Sugar / Açucar Sintático)

-----------------------------------------------------------------
|           Function Decorator                                  |
-----------------------------------------------------------------

-----------------------------------------------------------------
|                   Decorator                                   |
| ------------------------------------------------------------- |
| |                    Função Decorada                        | |
| ------------------------------------------------------------- |
| ------------------------------------------------------------- |

# Decorators como Funções (Sintaxe não recomendada)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer te conhecer!')
        funcao()
        print('Tenha um bom dia!')
    return sendo


def saudacao():
    print('Seja bem vindo!')


# Teste 1

teste = seja_educado(saudacao)

teste()

# Teste 2

def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)

raiva_educada()

# Decorators com sintax recomendada (Syntax Sugar)


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um praze te conhecer!')
        funcao()
        print('Tenha um bom dia!')
    return sendo_mesmo


@seja_educado_mesmo   # Decorator
def apresentando():
    print('Meu nome é Herbety')


# Teste 1

apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero domir!')


dormir()

-----------------------------------------------------------
|   Home | Serviços | Produtos | Administrativo |
----------------------------------------------------------
http: // www.suaempresa.com.br/home
http: // www.suaempresa.com.br/servicos
http: // www.suaempresa.com.br/produtos
http: // www.suaempresa.com.br/admi

OBS: Apenas um exemplo abaixo


def checa_login(): -> Decorator Function
    if not request.user:
        redirect('http://suaempresa.com.br')


def home(request):
    return 'Pode acessar home'


@checa_login -> Decorator
def servicos(request):
    return 'Pode acessar seviços'


def produtos(request):
    return 'Pode acessar produtos'


@checa_login -> Decorator
def admin(request):
    return 'Pode acessar admin


# Função Decorador


def desc_cartao(funcao):
    def calc(valor):
        return valor - (valor * 5 / 100)
    return calc

# Função Decoradora


def desc_boleto(funcao):
    def calc(valor):
        return valor - (valor * 7 / 100)
    return calc

# Função Decoradora


def desc_avista(funcao):
    def calc(valor):
        return valor - (valor * 10 / 100)
    return calc


@desc_cartao  # Decorator
def produto(valor):
    return valor


@desc_boleto  # Decorator
def produto2(valor):
    return valor


@desc_avista  # Decorator
def produto3(valor):
    return valor


print(produto(50))

print(produto2(50))

print(produto3(50))


# OBS: Não confunda Decorator com Decorator Function

"""
