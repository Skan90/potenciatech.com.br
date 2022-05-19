# Curso LET'S CODE ao POTÊNCIA TECH: Pythons Basics
# https://potenciatech.com.br/ from iFood


# Aula 1: Introdução

# Noções de programação com a idéia de automação, bem como a explicação
# da popularização de Python estar ligada a sua facilidade de escrita e
# ter adentrado outros ramos divergentes ao da TI e se assemelhar muito
# a língua inglesa.


# Aula 2: Instalação do Python Windows Full

# Estou utilizando no lugar do Jupyter a IDE PyCharm


print("\nAula 2: Instalação do Python Windows Full\n")
print("Hello, world!")

print("\nFIM AULA 2\n")

# Aula 3: Tipos de variáveis
# Abordagem dos principais tipos de variáveis com 'int' (conj. inteiros),
# 'float' (ponto flutuante), 'str' (string) e 'bool' (boolean) (True ou False).

print("\nAula 3: Tipos de variáveis\n")

x = 5
print(x, type(x))
preco = 19.99
print(preco, type(preco))
cidade = "Rio Grande - RS"
print(cidade, type(cidade))
disponivel= True
print(disponivel, type(disponivel))
disponivel= False
print(disponivel, type(disponivel))


print("\nFIM AULA 3\n")

#Aula 4: Operadores Full
# São comentadas as operações aritméticas soma, subtração, multiplicação e divisão.
# Também são exemplificados expoentes, divisão inteira e resto de divisão.
# Logo depois a abordagem a operadores lógicos, como booleanos.
# Onde 'not' altera o valor de um boolean no print,
# bem como 'or', que retorna True se uma das opções for True,
# e 'and' onde só há retorno True se todas as váriáveis forem True.
# Por ultimo os operadores > (maior que), < (menor que), == (igual a),
# >= (maior ou igual a), <= (menor ou igual a) e o != (diferente de)

print("\nAula 4: Operadores Full\n")
x = 50
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)

print(x ** y)
print(x // y)
print(x % y)

print(3 //4)

tem_cafe = True
tem_pao = False

print(not tem_cafe)
print(tem_cafe or tem_pao)
print(tem_cafe and tem_pao)

dolar = 5.3
real = 1

print(dolar > real)
print(dolar < real)
print(dolar == real)
print(dolar >= real)
print(dolar <= real)
print(dolar != real)

print("\nFIM AULA 4\n\n")