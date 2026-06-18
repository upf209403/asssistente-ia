# Estruturas de repetição

## Definição
- Estruturas ou laços de repetição, também chamados loops, são objetos da programação que permitem que a mesma operação lógica seja executada diversas vezes de forma automática.

## Por que existem estruturas de repetição?
- Estruturas de repetição servem para executar uma certa sequência de passos lógicos sobre um certos conjunto de entradas.

## Tipos
### For
- "For" significa literalmente a preposição "para" em inglês.
- Recebe um conjunto delimitado de entradas e aplica a estes certa operação.
- Em Python, o lastro de repetição "for" é frequentemente usado junto com o objeto "range", que representa a lista de valores para os quais 
- "Range" recebe um valor de início, fim e um passo (que é opcional e é definido como 1 se não for passado).
- Um detalhe importante é que o valor de fim passado ao objeto "range" é sempre um unidade maior que o último valor para o qual o "for" será executado.
- Assim, a lastro de repetição abaixo imprime os números de 1 a 10, não incluindo o 11:
for i in range(1, 11):
    print(i)

- Por outro lado, o "for" seguinte mostra na tela os números de 1 a 9:
for i in range(1, 10):
    print(i)

### While
- "While" significa "enquanto"
- Recebe uma condição booleana (verdadeira ou falsa) e só se encerra quando o teste lógico não for mais satisfeito.

## Exemplos
- 

## Erros comuns
### Confundir for e while
- Para iniciantes, a diferença 
- A regra principal é que "for" só pode ser usado quando o número de entradas for bem delimitado e conhecido de antemão.
- Considere um programa que deve somar os números naturais entre 1 e 100 (sem usar a fórmula das progressões aritméticas). Em Python, isso poderia ser implementado usando "for":

soma = 0

for i in range(1, 101):
    soma += i

print(soma)


- Considere agora um outro programa, que deve somar todos os valores informados pelo usuário até este digitar 0.
- Como é impossível saber de antemão quantos valores o usuário vai digitar, esse programa só pode ser implementado utilizando "while", como demonstrado abaixo:

soma = 0
num = int(input("Digite um número (0 para encerrar o programa)"))

while num !== 0:
    soma += num
    num = int(input("Digite um número (0 para encerrar o programa)"))

print(soma)


- Além disso, é possível recriar o lastro de repetição "for" usando "while" e uma variável contadora, como no exemplo abaixo:

cont = 0
### Criar whiles infinitos
- 
### Problema do n+1