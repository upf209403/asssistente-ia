from utils.normalize_text import normalize_text
from utils.tokenize import tokenize

TOPICS = {
    "condicionais.md": [
        "condicional",
        "condicionais",
        "if",
        "elif",
        "else"
    ],

    "funcoes.md": [
        "funcao",
        "funcoes",
        "argumento",
        "argumentos",
        "parametro",
        "parametros"
    ],

    "introducao_python.md": [
        "python"
    ],

    "loops.md": [
        "repeticao",
        "loop",
        "loops",
        "for",
        "while"
    ],

    "operadores.md": [
        "atribuicao",
        "comparacao",
        "maior que",
        "menor que",
        "instancia de"
    ],

    "pensamento_computacional.md": [
        "pensamento computacional",
        "algoritmo",
        "algoritmos",
        "decomposicao",
        "abstracao",
        "reconhecimento de padroes"
    ],

    "tipos_dados.md": [
        "string",
        "str",
        "int",
        "float"
    ],

    "variaveis.md": [
        "variavel",
        "variaveis",
        "constante",
        "constantes"
    ]
}

def detect_topic(prompt: str):
    normalized_prompt = normalize_text(prompt)

    tokens = set(tokenize(normalized_prompt))

    topics = []

    for file, keywords in TOPICS.items():
        for keyword in keywords:
            keyword = normalize_text(keyword)
            
            keyword_tokens = keyword.split() #Detecta se a keyword é simples ou composta

            #Keyword simples (ex: "while")
            if len(keyword_tokens) == 1:
                if keyword in tokens:

                    topics.append(file)
                    break

            #Keyword composta (ex: "estruturas de repetição")
            else:
                if keyword in normalized_prompt:

                    topics.append(file)
                    break

    if not topics:
        return """
            Não foi possível identificar o tópico da conversa.

            Esse assistente é restrito a:

            - Pensamento computacional:

            - Variáveis:

            - Tipos de dados:

            - Operadores:

            - Estruturas condicionais:

            - Estruturas de repetição:
            
            - Funções: 

            Reformule sua busca utilizando os conceitos acima.
        """

    return topics