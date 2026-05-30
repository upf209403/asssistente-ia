# Estruturas condicionais

## Definição
- Estruturas condicionais, também chamadas de estruturas de decisão, são elementos usados na programação para controlar ou alterar o fluxo de execução de um programa de acordo com uma ou mais condições. 

## Por que existem estruturas condicionais?
- Estruturas condicionais existem porque muitas vezes a resolução de problemas depende de decisões diferentes de acordo com os dados, entradas ou estados do programa.

## Sintaxe
- A sintaxe das estruturas condicionais varia de acordo com a linguagem de programação em questão.
- No entanto, a maioria das linguagens modernas ou amplemente usadas na indústria possuem estruturas semelhantes.
- Aqui, focaremos na sintaxe das estruturas condicionas na linguagem Python 3.
### If
- "If" significa literalmente "se" em inglês.
- É usada para estabelecer a condição principal do fluxo.
- Depende de uma condição booleana (que retorne verdadeiro ou falso)
- É a única que pode ser usada independemente das demais.
#### Ifs aninhados
- Os "ifs aninhados" são ifs dentro de outro if.
- Permitem a implementação de "subcondições".

### Elif
- Abreviação de "else if", usado em Python.
- Permite a introdução de condições alternativas ao if principal.
- Não são obrigatórios.

### Else
- "Else" significa literalmente "senão" ou "caso contrário" em inglês
- Representa o caso no qual o if (e os elifs) não são logicamente satisfeitos.

## Exemplos
### If
- Imagine um programa de um banco. O valor do saque não pode ser maior que o saldo. Essa restrição poderia ser implementada com um if:

if saque > saldo:
    print("Saldo insuficiente")

    return

### If aninhado
- Imagine que em uma escola, todos os alunos com média maior que 6 sejam aprovados.
- Além disso, aqueles obtiverem uma nota maior que 9 sejam aprovados com distinção
- Essa regra poderia ser representada com um if aninhado:

if nota > 6:
    print("Você foi aprovado!")

    if nota > 9:
        print("Parabéns, você foi aprovado com distinção!")

### Elif
- No exemplo anterior, a mensagem de aprovação seria mostrada duas vezes, pois uma nota maior que 9 (aluno aprovado com distinção), será sempre maior que 6 (aprovado).
- Para resolver esse problema, poderia ser usado elif:

if nota > 9:
    print("Parabéns, você foi aprovado com distinção!")
elif nota > 6:
    print("Você foi aprovado!")

### Else
- Abaixo, a implementação da lógica do exemplo da escola com a mensagem de reprovação:

if nota > 9:
    print("Parabéns, você foi aprovado com distinção!")
elif nota > 6:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado")

- Perceba como não é necessário explicitar que a nota dos alunos reprovados é menor que 6. 
- O fato de o if e o elif não serem satisfeitos cai nesse caso automaticamente.

## Erros comuns
### Erro no uso dos operadores
- É comum confundir o sinal de atribuição (=) com o de igualdade (==)
- Esse erro acontece muito em comparações.
- O código abaixo está incorreto:

if nome = "Pedro":
    (restante do código...)

- A versão correta seria:
if nome == "Pedro":
    (restante do código...)

### Erro de indentação:
- Na linguagem Python, indentação é sintática.
- Isso significa que o trecho de código dentro de um if, elif ou else *precisa* estar corretamente indentado
- Assim, o trecho abaixo é inválido em Python:

if nota > 9:
print("Parabéns, você foi aprovado com distinção")

- A versão correta seria:
if nota > 9:
    print("Parabéns, você foi aprovado com distinção")

### Usar ifs no lugar de elifs
- Um sequência de ifs poderia ser satisfeita logicamente várias vezes.
- Voltemos ao exemplo da escola. Imagine que o programa fosse implementado da seguinte forma:

if nota > 9:
    print("Parabéns, você foi aprovado com distinção!")
if nota > 6:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado")

- Isso reintroduziria o problema visto anteriormente: notas maiores que 9 seriam sempre maiores que 6, e, portanto, executariam esse bloco de código também.

### Usar else quando não é necessário
- Nem sempre se faz necessário usar else explicitamente.
- Às vezes, um if sozinho já é suficiente para redirecionar o fluxo do programa.
- Considere esse programa fictício, que verifica se a senha inserida pelo usuário está correta e se este pode se logar:

if senha_inserida == senha_usuário:
    print("Usuário logado")
    (restante do código...)

else:
    print("Erro ao logar")
    return

- Este trecho poderia ser reescrito, invertendo a comparação:

if senha_inserida != senha_usuário:
    print("Erro ao logar")

    return

print("Usuário logado")
(restante do código...)