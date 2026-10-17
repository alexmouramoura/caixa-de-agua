from colorama import Fore, Style, init

init(autoreset=True)

NIVEL_MIN = 5.00
NIVEL_MAX = 100.00

# Cada item da lista: (limite superior da faixa, situação, cor)
FAIXAS = [
    (24.00,  "Nível 1 - Muito baixo (CRÍTICO)", Fore.RED),
    (43.00,  "Nível 2 - Baixo",                 Fore.YELLOW),
    (62.00,  "Nível 3 - Médio",                 Fore.GREEN),
    (81.00,  "Nível 4 - Alto",                  Fore.CYAN),
    (100.00, "Nível 5 - Muito alto (ALERTA)",   Fore.BLUE),
]


def classificar(nivel):
    for limite, mensagem, cor in FAIXAS:
        if nivel <= limite:
            return mensagem, cor


def ler_nivel():
    texto = input("\nDigite o nível do reservatório em metros (ou 'sair'): ").strip()
    if texto.lower() == "sair":
        return None
    try:
        nivel = float(texto.replace(",", "."))
    except ValueError:
        print(Fore.MAGENTA + "Valor inválido. Digite um número, ex.: 37,5")
        return -1
    if nivel < NIVEL_MIN or nivel > NIVEL_MAX:
        print(Fore.MAGENTA + f"Fora da faixa! Use valores entre {NIVEL_MIN:.2f} e {NIVEL_MAX:.2f} m.")
        return -1
    return nivel


def main():
    print(Style.BRIGHT + "=== MONITOR DO RESERVATÓRIO ===")
    print(f"Faixa de medição: {NIVEL_MIN:.2f} m a {NIVEL_MAX:.2f} m")

    while True:
        nivel = ler_nivel()
        if nivel is None:
            print("Encerrando o programa. Até logo!")
            break
        if nivel == -1:
            continue
        mensagem, cor = classificar(nivel)
        print(cor + Style.BRIGHT + f"Nível atual: {nivel:.2f} m -> {mensagem}")


main()