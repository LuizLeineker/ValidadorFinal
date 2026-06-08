# DFA - Linguagem Regular
# cpf


def tipo_simbolo(simbolo):

    if simbolo.isdigit():
        return "DIG"

    return simbolo


transicoes = {

    ("q0", "DIG"): "q1",
    ("q1", "DIG"): "q2",
    ("q2", "DIG"): "q3",

    ("q3", "."): "q4",

    ("q4", "DIG"): "q5",
    ("q5", "DIG"): "q6",
    ("q6", "DIG"): "q7",

    ("q7", "."): "q8",

    ("q8", "DIG"): "q9",
    ("q9", "DIG"): "q10",
    ("q10", "DIG"): "q11",

    ("q11", "-"): "q12",

    ("q12", "DIG"): "q13",
    ("q13", "DIG"): "q14",
}


def reconhecer_cpf(entrada, mostrar_passos=False):

    estado = "q0"
    passos = 0
    historico = []

    for simbolo in entrada:

        chave = (estado, tipo_simbolo(simbolo))

        historico.append(
            f"Passo {passos + 1}: "
            f"{estado} --[{simbolo}]--> "
        )

        if chave not in transicoes:

            historico[-1] += "ERRO"

            return {
                "aceito": False,
                "passos": passos,
                "historico": historico
            }

        proximo_estado = transicoes[chave]

        historico[-1] += proximo_estado

        estado = proximo_estado

        passos += 1

    aceito = estado == "q14"

    if mostrar_passos:

        print("\n=== EXECUÇÃO PASSO A PASSO ===")

        for passo in historico:
            print(passo)

        print(f"\nEstado final: {estado}")
        print(f"Passos: {passos}")

    return {
        "aceito": aceito,
        "passos": passos,
        "historico": historico
    }