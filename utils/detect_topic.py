from normalize_text import normalize_text
from tokenize import tokenize

TOPICS = {
    "condicionais.md": [
        "condicional",
        "condicionais"
        "for",
        "while",
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

    ],

    "loops.md": [
        "repeticao",
        "laco de repeticao",
        "lacos de repeticao",
        "for",
        "while"
    ],

    "operadores.md": [

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

    ],

    "variaveis.md": [

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

            #Keyword simples
            if len(keyword_tokens) == 1:
                if keyword in tokens:

                    topics.append(file)
                    break
            #Keyword composta
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