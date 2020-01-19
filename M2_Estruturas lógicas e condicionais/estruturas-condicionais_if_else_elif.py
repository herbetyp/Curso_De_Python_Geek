"""
Estruturas condicionais
if, else, elif (else if)

idade = 25
 Estrutura condicional if, else em C
if(idade < 18){
    printf("Menor de idade");
}else{
     printf("Maior de idade");
}

Estrutura condicional if, else em Java
if(idade < 18){
    System.out.println("Menor de idade");
}else{
     System.out.println("Maior de idade");
}
"""
idade = 18
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
elif idade == 26:
    print('Tem 26 anos')
else:
    print('Maior de idade')



