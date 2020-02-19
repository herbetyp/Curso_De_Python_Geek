def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'estou de dieta.'
    else:
        final = 'comida preferida.'
    return f'Estou comendo {comida}, {final}'


def dormir(num_horas):
    if num_horas < 8:
        final = 'pouco, vou para o trabalho cansado.'
    elif num_horas >= 8:
        final = 'muito, estou atrasado para o trabalho.'

    return f'Estou dormindo {final}'


def eh_engracada(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    else:
        return False
