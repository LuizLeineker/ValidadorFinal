# todas as funções serão executadas aqui, lendo o arquivo txt correspondente a ela.

from pathlib import Path
from regular import reconhecer_cpf
from livre_contexto import reconhecer_parenteses
from recursiva import recursivaMF


PASTA_TESTES = Path("../testes")


def carregar_testes(arquivo):

    aceitos = []
    rejeitados = []

    destino = None

    with open(arquivo, "r", encoding="utf-8") as f:

        for linha in f:
            linha = linha.strip()

            if not linha:
                continue

            if linha.startswith("#"):
                texto = linha.upper()

                if "ACEIT" in texto:
                    destino = aceitos

                elif "REJEIT" in texto:
                    destino = rejeitados

                continue

            if destino != None:
                destino.append(linha)

    return aceitos, rejeitados


def executar_bateria(nome, arquivo, reconhecedor):

    print("\n" + "=" * 60)
    print(nome)
    print("=" * 60)

    aceitos, rejeitados = carregar_testes(arquivo)

    total = 0
    corretos = 0

    print(f"\n{'CADEIA':30}"f"{'ESPERADO':12}"f"{'OBTIDO':12}"f"{'PASSOS'}")

    print("-" * 60)

    for cadeia in aceitos:

        total += 1

        resultado = reconhecedor(cadeia)

        if resultado["aceito"]:
            obtido = "ACEITO"
            corretos += 1
        else:
            obtido = "REJEITADO"

        print(
            f"{cadeia:30}"
            f"{'ACEITO':12}"
            f"{obtido:12}"
            f"{resultado['passos']}"
        )

    for cadeia in rejeitados:

        total += 1

        resultado = reconhecedor(cadeia)

        if resultado["aceito"]:
            obtido = "ACEITO"
        else:
            obtido = "REJEITADO"
            corretos += 1

        print(
            f"{cadeia:30}"
            f"{'REJEITADO':12}"
            f"{obtido:12}"
            f"{resultado['passos']}"
        )

    print(f"\nTestes Feitos: {corretos}/{total}")

    return corretos, total


def executar_tudo():

    total_geral = 0
    corretos_geral = 0

    configuracoes = [

        ("DFA — CPF",
         PASTA_TESTES / "testes_regular.txt",
         reconhecer_cpf),

        ("PDA — PARÊNTESES",
         PASTA_TESTES / "testes_livre_contexto.txt",
         reconhecer_parenteses),

        ("MT — w#w",
         PASTA_TESTES / "testes_recursiva.txt",
         recursivaMF)
    ]

    for nome, arquivo, funcao in configuracoes:

        corretos, total = executar_bateria(
            nome,
            arquivo,
            funcao
        )

        corretos_geral += corretos
        total_geral += total

    print("\n" + "=" * 60)

    print(f"TOTAL GERAL: {corretos_geral}/{total_geral}")

    print("=" * 60)



# RUN
executar_tudo()

