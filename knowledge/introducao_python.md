# Introdução à linguagem Python

## O que é Python?
- Python é uma das linguagens de programação mais usadas na atualidade.
- Python foi lançada em 1991, por Guido van Rossum.
- Atualmente, Python está na versão 3, que pode ser baixada no site oficial (python.org).

## Principais características
- Python é uma linguagem de alto nível. Isso significa que ela é pensada para que seus programas sejam relativamente compreensíveis para humanos.
- Python é geralmente considerada uma linguagem interpretada, o que significa que seus programas são executados por um interpretador, sem a necessidade de uma etapa explícita de compilação por parte do usuário.

## Onde Python é usado
- Análise e ciência de dados (uma das principais linguagens da área).
- Inteligência artificial (considerada uma das linguagens "oficiais").
- Desenvolvimento web (com bibliotecas e frameworks específicos).
- Automação de tarefas.

### Vantagens
- Por ser uma linguagem de alto nível, possui uma curva de aprendizado amigável a iniciantes.
- Além disso, escrever um programa em Python costuma exigir menos código do que em linguagens como Java, C ou C++.

### Limitações
- Como linguagem interpretada, Python possui desempenho inferior a outras linguagens em questões de velocidade de execução, como Rust ou C++.
- Em aplicações que exigem extrema eficiência, outras linguagens podem ser mais adequadas.

## Sintaxe básica
### Indentação
- Em Python, a indentação é parte da sintaxe. Isso quer dizer que blocos de código (como if, for, while e funções) devem estar indentados no seu conteúdo.
- Código correto:
if idade >= 18:
    print("Você é maior de idade")

- Código incorreto:
if idade >= 18:
print("Você é maior de idade")

### Comentários
- Em Python comentários de uma linha são indicados por # (cerquilha ou jogo da velha).
- - Tecnicamente, Python não possui uma sintaxe específica para comentários multilinha.
- No entanto, eles podem ser escritos com strings multilinhas, usando três aspas, simples ou duplas, antes e depois do texto, como no exemplo abaixo:

'''
Esse é um exemplo de string multilinha em Python,
usada para comentários longos e com aspas simples.
'''

"""
Esse é um exemplo de string multilinha em Python,
usada para comentários longos e com aspas duplas.
"""
### Case-sensitive
- Python é case-sensitive, isto é, diferencia letras maiúsculas e minúsculas para a nomeação de objetos como variáveis, funções e classes.
- Então, as variáveis abaixo são valores diferentes:

idade = 23
Idade = 30

print(idade)
print(Idade)

- Os valores impressos na tela serão 23 e 30, respectivamente.

## Como executar um programa Python?
- Após a instalação do Python em uma máquina (o que pode ser feito consultando a documentação oficial), um programa pode ser rodado usando o comando "python nome_do_arquivo.py", desde que o usuário esteja na pasta do arquivo "nome_do_arquivo.py".
- Às vezes, pode se fazer necessário especificar a versão do Python usada, como "python3 nome_do_arquivo.py".

## Exemplo
- Suponha que exista um arquivo chamado "ola_mundo.py":

print("Olá, Mundo!")

- Executando o comando abaixo na pasta do arquivo:
python ola_mundo.py

- Será impresso no terminal:
Olá, Mundo!