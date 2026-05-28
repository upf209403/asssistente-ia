def detect_topic(prompt: str):
    prompt = prompt.lower()

    topics = []

    if any(word in prompt for word in ["condicional", "condicionais", " if", "elif", "else"]): topics.append("condicionais.md")

    if any(word in prompt for word in ["função", "funcao", "funções", "funcoes", "argumento", "argumentos"]): topics.append("funcoes.md")

    if any(word in prompt for word in ["variável", "variavel", "variáveis", "variaveis", "constante", "constantes"]): topics.append("variaveis.md")

    if any(word in prompt for word in ["repetição", "repetiçao", "repeticao", "laços de repetição", "laços de repetiçao", " for ", "while"]): topics.append("loops.md")

    if not topics:
        return """
            Não foi possível identificar o tópico da conversa.

            Esse assistente é restrito a:

            - Pensamento computacional
            - Variaveis
            - Tipos de dados
            - Operadores
            - Estruturas condicionais
            - Estruturas de repetição
            - Funções

            Reformule sua busca utilizando os conceitos acima.
        """

    return topics