"""
Dunder Name e Dunder Main

Dunder = Double Dunder

Dunder Name -> __name__

Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos propiedades e etc
utilizando Double Dunder para não gerar conflito com os nomes desses elementos na programação


# Na linguagem C, temos um programa da seguinte foma:

int main() {
    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma

public static void main(String[] args) {

}

# Em Python, se executarmos um módulo Python diretamente na linha de comando internamente
o Python atribuira á variavel __name__ o valor __main__ indicando que este módulo é o 
módulo de execução principal


from modulos_customizados.funcoes_com_parametros import soma_impares


print(soma_impares([5, 3, 7, 9]))
"""

import primeiro
import segundo
