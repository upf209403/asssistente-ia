# Funções

## Definição
- Funções são sequências de código definidas para executar algum procedimento que é usado diversas vezes ao longo do programa.
- Funcionam como "fábricas", que recebem determinado valor (ou valores), executam um certa operação sobre estes e retornam um resultado específico.

## Por que existem funções?
- A principal razão da existência das funções é evitar a repetição de código.
- Podemos dizer que funções são uma aplicação do princípio da abstração, discutido na seção sobre pensamento computacional.

## Elementos
- Funções seguem as mesmas regras e convenções usadas na criação de variáveis.
- No entanto, em Python, elas são declaradas com a palavra reservada "def" antes do nome e o uso de parênteses e dois pontos após.
- O conteúdo da função em si é indentado.
- Exemplo:
def hello_world():
    (corpo da função...)

### Parâmetros
- Parâmetros são os dados que uma função espera receber para executar sua tarefa.
- Uma função pode receber de zero a um número indeterminado de parâmetros.
- No exemplo abaixo, "a" e "b" são parâmetros:

def soma(a, b):
    return a+b

### Argumentos
- Argumentos são os valores passados para que a função seja de fato executada.
- O número de argumentos de uma função é dado pelo número de parâmetros na hora de sua definição.
- Usando o exemplo da seção anterior:

soma(2, 5)

- Nesse caso, os valores 2 e 5 são argumentos da função soma.

### Valores de retorno
- Esses são os valores os quais a função em questão
- Assim como parâmetros, nem toda função possui valores de retorno.
- Quando eles existem, geralmente usa-se a palavra reservada "return" para indicá-los.

### Escopo
- Variáveis declaradas dentro de uma função normalmente só existem dentro dela.
- Elas não podem ser acessadas diretamente fora da função.
- Além disso, uma variável interna pode ter o mesmo nome de uma variável externa sem representar o mesmo valor.

### Chamada da função
- Para chamar uma função em Python, é usada a seguinte sintaxe: funcao().
- Assim como no caso das variáveis, deve-se prestar atenção a ordem de execução; em Python, funções só podem ser chamadas após terem sido definidas.

## Exemplos
- A função a seguir não possui parâmetros ou valores de retorno (note como a palavra "return" não é usada):

def ola_mundo():
    print("Olá, Mundo")

- No caso abaixo, há um parâmetro , mas nenhum valor de retorno:

def ola_usuario(nome):
    print("Hello ", nome)

- Já no exemplo seguinte, não há parâmetro, mas há um valor de retorno (a palavra "return" é usada pela primeira vez aqui):

def retorna_soma_um_a_dez():
    soma = 0

    for i in range(1,11):
        soma += i
    
    return soma

- Por fim, o próximo exemplo trata de uma função com um parâmetro e um valor de retorno:

def soma_range_personalizado(num):
    soma = 0

    for i in range(1, num+1):
        soma += i

    return soma

## Erros comuns
### Ignorar escopo
- Muitos iniciantes tendem a não considerar o escopo de variáveis.
- No exemplo a seguir, "nome" representam valores diferentes:

nome = "Gustavo"

def define_nome():
    nome = "João"
    return nome

define_nome()

print(nome)

- O valor exibido na tela será "Gustavo", não "João", pois a variável "nome" criada dentro da função é diferente daquela criada fora dela

### Criar funções "faz-tudo"
- Como mencionado anteriormente, funções são o exemplo mais direto da aplicação do princípio da abstração.
- Dessa forma, o ideal é que cada função realize uma operação específica.
- Assim, ao invés de escrever uma função que, por exemplo, recebe o nome do aluno, da matéria, do semestre, suas notas, calcula a média e exibe uma mensagem como "O aluno Fulano tirou tal nota na tal matéria no enésimo semestre", seria recomendado nesse caso criar, no mínimo duas funções: uma para calcular a média do aluno no semestre e outra que formatasse a mensagem a ser exibida.

### Nomes pouco descritivos
- Assim como no caso das variáveis, é uma boa prática que os nomes das funções evidenciem o que elas fazem.
- Isso melhora a leitura do código por outros desenvolvedores e a manutenabilidade do código no longo prazo.
- Dessa forma, os exemplos abaixo ilustram funções ruins desse ponto de vista (o que representa o "valor" calculado?):

def calcula_valor(valor1, valor2...):
    (corpo da função...)

- Um exemplo corrigido (dependeria do contexto do programa):

def calcula_faturamento_liquido_trimestre(faturamento_bruto, total_deducoes):
    (corpo da função...)