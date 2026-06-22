# Estruturas de repetição

## Definição
- Estruturas ou laços de repetição, também chamados loops, são estruturas de programação que permitem que a mesma operação lógica seja executada diversas vezes de forma automática.

## Por que existem estruturas de repetição?
- Estruturas de repetição servem para executar uma certa sequência de passos lógicos sobre um determinado conjunto de valores ou enquanto uma certa condição for satisfeita.

## Tipos
### For
- "For" pode ser entendido como "para cada".
- Recebe um conjunto delimitado de entradas e executa um certa operação para cada valor.
- Em Python, o laço de repetição "for" é frequentemente usado junto com o objeto "range", que representa uma sequência de valores inteiros.
- "Range" recebe um valor de início, fim e um passo (que é opcional e é definido como 1 se não for passado).
- Um detalhe importante é que o valor de fim passado ao objeto "range" é sempre uma unidade maior que o último valor para o qual o "for" será executado.
- Assim, o laço de repetição abaixo imprime os números de 1 a 10, não incluindo o 11:
for i in range(1, 11):
    print(i)

- Por outro lado, o "for" seguinte mostra na tela os números de 1 a 9:
for i in range(1, 10):
    print(i)

### While
- "While" significa "enquanto"
- Recebe uma condição booleana (verdadeira ou falsa) e só se encerra quando o teste lógico não for mais satisfeito.

## Exemplos
- O código abaixo vai imprimir o dobro dos valores entre 1 e 20 na tela:

for i in range(1,21):
    print(i*2)

- Já esse exemplo com "while", o usuário digita nomes até um deles começar pela letra Z (note que o programa também trata do caso de o usuário digitar uma string vazia):

rodando = True

while rodando:
    nome = input("Digite um nome: ")

    if(nome):
        print(nome)

        if(nome.lower()[0] == "z"):
            rodando = False
            print("Programa finalizado")
    else:
        print("String vazia")

## Erros comuns
### Confundir for e while
- Para iniciantes, a diferença entre "for" e "while" nem sempre é clara.
- A regra principal é que "for" só deve ser usado quando se quer percorrer uma sequência de valores.
- Considere um programa que deve somar os números naturais entre 1 e 100 (sem usar a fórmula das progressões aritméticas). Em Python, isso poderia ser implementado usando "for":

soma = 0

for i in range(1, 101):
    soma += i

print(soma)

- Considere agora um outro programa, que deve somar todos os valores informados pelo usuário até este digitar 0.
- Como é impossível saber de antemão quais valores o usuário vai digitar, esse programa só pode ser implementado utilizando "while", como demonstrado abaixo:

soma = 0
num = int(input("Digite um número (0 para encerrar o programa)"))

while num != 0:
    soma += num
    num = int(input("Digite um número (0 para encerrar o programa)"))

print(soma)

- Além disso, é possível recriar o laço de repetição "for" usando "while" e uma variável contadora, como no exemplo abaixo:

cont = 1
soma = 0

while cont < 101:
    soma += cont
    cont += 1

### Criar whiles infinitos
- "While" depende de uma condição lógica e só para e executar a sequência de comandos especificada quando esta não for mais satisfeita.
- É possível, assim acabar criando laços "while" que não param de ser executados, pois sua condição é sempre satisfeita.
- Um caso clássico desse erro é quando se esquece de incrementar a variável contadora ao final do while, e, assim, o valor de cont nunca muda.
- No exemplo abaixo, cont é sempre 1 e nunca satisfaz a condição de parada e esse valor é impresso infinitamente:

cont = 1

while cont <=5:
    print(cont)

### Confundir o fim do range ou usar <= no lugar de < no while
- Como discutido acima, o fim do range é sempre uma unidade maior que o último valor da série.
- Assim, o código abaixo não imprimiria o valor 10, mesmo que esse tenha sido usado como limite superior do range.

for i in range(1, 10):
    print(i)

- O equivalente usando while seria reescrever o laço de repetição usando a variável contadora da seguinte forma:

cont = 1

while cont < 10:
    print(cont)
    cont += 1

- Usando while, há duas formas de corrigir o problema: usando o operador <= e o último valor como condição de parada, como no exemplo abaixo:

cont = 1

while cont <= 10:
    print(cont)
    cont += 1

- Ou usando uma unidade a mais (na mesma lógica do range) e o operador < :

cont = 1

while cont < 11:
    print(cont)
    cont += 1

- Note que esses exemplos assumem variáveis que são incrementadas, isto é, seu valor cresce. Seria perfeitamente possível ter contadores descrescentes. Nesse caso, o sentido das desigualdades se inverteriam (>= e > seriam usados no lugar).