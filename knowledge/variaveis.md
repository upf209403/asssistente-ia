# Variáveis

## Definição

- Variáveis são espaços utilizados para armazenar valores durante a execução de um programa.
- Esses valores podem ser consultados, modificados e reutilizados ao longo da execução.
- Em termos práticos, uma variável funciona como um nome associado a uma informação.

## Por que existem variáveis?

- Variáveis permitem que programas trabalhem com informações que mudam ao longo do tempo.
- Sem variáveis, seria necessário escrever todos os valores diretamente no código, tornando os programas pouco flexíveis.
- Elas permitem que aplicações processem dados fornecidos por usuários, arquivos, bancos de dados e outras fontes de informação.

## Regras e convenções de nomenclatura

### Regras

- O nome de uma variável não pode começar com números.
- O nome de uma variável não pode conter espaços.
- O nome de uma variável não pode utilizar palavras reservadas da linguagem, como if, for, while e def.

### Convenções

- Utilize nomes que descrevam claramente o propósito da variável.
- Prefira nomes como nome_usuario, idade, salario ou data_nascimento.
- Evite nomes genéricos como x, y, z, a ou teste, exceto em exemplos simples ou cálculos matemáticos.
- Em Python, a convenção mais comum é utilizar letras minúsculas separadas por underline (_).

## Exemplos
### Armazenando números
- Exemplo:

idade = 20

- A variável idade armazena o valor 20.

### Armazenando texto
- Exemplo:

nome = "Gustavo"

- A variável nome armazena o texto "Gustavo".

### Alterando valores

- Exemplo:

saldo = 100
saldo = 150

- Após a segunda atribuição, o valor armazenado será 150.

## Erros comuns

### Utilizar nomes inválidos

- Exemplos inválidos:

2idade = 20
nome completo = "Maria"
for = 10

- Esses nomes violam regras da linguagem e geram erro.

### Utilizar nomes pouco descritivos

- Exemplo:

x = "João"

- Embora o código funcione, o nome da variável não deixa claro o que está sendo armazenado.
- Uma alternativa melhor seria:

nome_usuario = "João"

### Utilizar uma variável antes de criá-la

- O código abaixo gera erro:

print(cidade)
cidade = "São Paulo"

- A variável precisa ser criada antes de ser utilizada.

### Ignorar o escopo das variáveis

- Variáveis declaradas dentro de funções normalmente só existem dentro delas.
- Exemplo:

numero = 8

def alterar_numero():
    numero = 5

alterar_numero()

print(numero)

- O valor exibido será 8.
- A variável criada dentro da função é diferente da variável criada fora dela.

### Uso excessivo de variáveis globais
- Python permite modificar variáveis globais utilizando a palavra-chave global.
- Exemplo:

numero = 8
def alterar_numero():
    global numero
    numero = 5

alterar_numero()
print(numero)

- Nesse caso, o valor exibido será 5.
- Embora isso seja possível, o uso excessivo de variáveis globais pode dificultar a manutenção e o entendimento do código.