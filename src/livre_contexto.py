# PDA - Linguagem Livre de Contexto
# Parenteses

# marcador pilha
SIMBOLO_BASE = "$"

transicoes = {

    ("q0", "(", SIMBOLO_BASE): ("q0", "EMPILHAR"),
    ("q0", "(", "("): ("q0", "EMPILHAR"),

    ("q0", ")", "("): ("q0", "DESEMPILHAR"),

    ("q0", "EOF", SIMBOLO_BASE): ("qf", "ACEITAR")
}


def topo_pilha(pilha):

    if pilha:
        return pilha[-1]

    return None


def reconhecer_parenteses(entrada, mostrar_passos=False):

    pilha = [SIMBOLO_BASE]
    estado = "q0"
    passos = 0
    historico = []

    for simbolo in entrada:

        topo = topo_pilha(pilha)

        chave = (estado, simbolo, topo)

        historico.append(
            f"Passo {passos + 1}: "
            f"estado={estado}, "
            f"entrada='{simbolo}', "
            f"pilha={pilha.copy()}"
        )

        if chave not in transicoes:

            historico[-1] += " -> REJEITADO"

            return {
                "aceito": False,
                "passos": passos,
                "historico": historico
            }

        novo_estado, operacao = transicoes[chave]

        if operacao == "EMPILHAR":

            pilha.append("(")

        elif operacao == "DESEMPILHAR":

            if topo != "(":

                historico[-1] += " -> REJEITADO"

                return {
                    "aceito": False,
                    "passos": passos,
                    "historico": historico
                }

            pilha.pop()

        estado = novo_estado

        passos += 1

    chave_final = (
        estado,
        "EOF",
        topo_pilha(pilha)
    )

    if chave_final in transicoes:

        estado, _ = transicoes[chave_final]

        passos += 1

    aceito = estado == "qf"

    if mostrar_passos:

        print("\n=== EXECUÇÃO PASSO A PASSO ===")

        for passo in historico:
            print(passo)

        print("\nPilha final:", pilha)
        print("Estado final:", estado)
        print("Passos:", passos)

    return {
        "aceito": aceito,
        "passos": passos,
        "historico": historico
    }