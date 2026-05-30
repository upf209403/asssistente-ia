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
- Depende de um condição booleana (que retorne verdadeiro ou falso)
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

if(saque > saldo):
    print("Saldo insuficiente")

    return

### If aninhado
- Imagine que em uma escola
### Elif
- No Brasil, o voto é obrigatório para pessoas entre 18 e 69 anos, mas facultativo para quem tem entre 16 e 17 anos ou 70 ou mais. O seguinte programa implementa 

### Else
- Em uma casa noturna  

## Erros comuns
### Usar ifs no lugar de elifs
- Ifs, quando satisfeitos, *interrompem* a execução do programa. Assim, no 
### Usar else quando não é necessário