# TURING - Linguagem Recursiva (R)

BRANCO = "_"

def recursivaMF(entrada, mostrar_passos=False):

    fita = list(entrada) + [BRANCO]

    cabeca = 0
    estado = "q0"

    passos = 0
    historico = []

    simbolo_memoria = None

    while True:

        simbolo = fita[cabeca]

        historico.append(
            f"Passo {passos + 1}: "
            f"estado={estado} "
            f"cabeca={cabeca} "
            f"simbolo={simbolo} "
            f"fita={''.join(fita)}"
        )

        passos += 1

        if estado == "q0":
            if simbolo == "X":
                cabeca += 1

            elif simbolo in ("0", "1"):
                simbolo_memoria = simbolo
                fita[cabeca] = "X"
                estado = "buscar_hash"
                cabeca += 1

            elif simbolo == "#":
                estado = "verificar_final"
                cabeca += 1

            else:
                estado = "q_reject"

        elif estado == "buscar_hash":

            if simbolo == "#":
                estado = "comparar"
                cabeca += 1
            else:
                cabeca += 1

        elif estado == "comparar":

            if simbolo == "X":
                cabeca += 1

            elif simbolo == simbolo_memoria:
                fita[cabeca] = "X"
                estado = "voltar"
                cabeca = 0

            else:
                estado = "q_reject"

        elif estado == "voltar":
            estado = "q0"

        elif estado == "verificar_final":

            if simbolo == "X":
                cabeca += 1

            elif simbolo == BRANCO:
                estado = "q_accept"

            else:
                estado = "q_reject"

        if estado in ("q_accept", "q_reject"):

            aceito = estado == "q_accept"

            if mostrar_passos:

                print("\n=== EXECUÇÃO PASSO A PASSO ===")

                for passo in historico:
                    print(passo)

                print("\nFita final:", "".join(fita))
                print("Passos:", passos)

            return {
                "aceito": aceito,
                "passos": passos,
                "historico": historico
            }