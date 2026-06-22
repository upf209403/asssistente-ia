# Tipos de dados
## Definição
- Tipos de dados representam diferentes categorias de valores que podem ser manipulados por um programa.
- Cada tipo possui características próprias e permite operações específicas.
- Por exemplo, o nome de um usuário e o preço de um item representam tipos de informação diferentes e participam de operações diferentes durante a execução de um programa.

## Por que existem diferentes tipos de dados? 
- Diferentes tipos de dados existem porque programas precisam representar números, textos, valores lógicos e outros tipos de informação.

## Tipos de dados em Python
### int
- Representam números inteiros, como 2 e 3.
- Exemplo:

idade = 20

- A variável "idade" possui tipo int.

### float
- Representam números decimais, como 5.0 e 6.12.
- Exemplo:

altura = 1.70

- A variável "altura" é do tipo float.

### str (strings)
- Representam texto.
- Em Python, são simbolizadas pela abreviação "str".
- Strings devem ser representadas entre aspas, sejam simples ('') ou duplas ("").
- Exemplo:

nome = "Gustavo"

- A variável "nome" é do tipo string.

### bool (booleanos)
- Representam os valores lógicos "verdadeiro" e "falso"
- Em Python, são escritos como True e False (a primeira letra deve ser maiúscula). 
- São representados em Python pela abreviação "bool".
- Exemplo:

usuario_logado = True

- A variável "usuario_logado" é do tipo booleano.

## Conversões
- É possível converter alguns tipos em outros.
- int() é usada para converter decimais e texto em inteiros.
- float() converte inteiros e texto em decimais.
- str() converte números em texto.
- bool() converte valores dos outros tipos em booleanos. Suas regras são um pouco mais complicadas, mas de forma geral, valores nulos (como 0 ou 0.0) e vazios (como "") são False, enquanto a maioria dos demais valores retornam True.

### Importante
- A função input(), usada para receber entradas do usuário retorna texto por padrão.
- Então, para receber valores números do usuário, é necessário usar as funções de conversão:

idade = int(input("Digite a idade do aluno: "))
nota = float(input("Digite a nota do aluno: "))

## Exemplos
- Para obter of tipo de um objeto, usa-se a função "type()"

- print(type(5)) retorna o tipo 'int'
- print(type(5.0)) retorna o tipo 'float'
- print(type("5")) retorna o tipo 'str'
- print(type(True)) retorna o tipo 'bool'

## Erros comuns
### Confundir a representação gráfica com o tipo
- 5 e "5", apesar de visualmente usarem o mesmo caractere, são de tipos diferentes, sendo o primeiro inteiro e o segundo uma string.
- Python não permite concatenar strings e números diretamente.
- Assim, o trecho de código abaixo está errado:

idade = 20
mensagem = "Idade: " + idade

- O código correto seria:

idade = 20
mensagem = "Idade: " + str(idade)

### Misturar ints e floats
- 5 e 5.0 são valores diferentes, pois o primeiro é int e o segundo é o float.
- Quando uma operação entre um valor inteiro e um float é feita, o resultado é sempre convertido para float
- Dessa forma, o "resultado" impresso abaixo é 10.0 (float), não 10 (int).

valor1 = 5
valor2 = 5.0

resultado = valor1 + valor2

print(resultado)

### Esquecer que True e False devem ser maiúsculas
- Em Python, os valores booleanos devem obrigatoriamente ser escritos como True e False
- Assim, "true" e "false" não existem na linguagem e gerarão erro de execução.