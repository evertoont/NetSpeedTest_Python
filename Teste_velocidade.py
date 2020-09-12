import speedtest
from tabulate import tabulate

velocidade = speedtest.Speedtest()


def teste_velocidade(opcao):
    print('\nRealizando teste de velocidade...')

    servidores = []
    velocidade.get_servers(servidores)
    velocidades = [str(f"{round(velocidade.download() / 1_000_000, 2)} Mbps"), str(f"{round(velocidade.upload() / 1_000_000, 2)} Mbps"),
                   str(f"{round(velocidade.results.ping, 2)} ms")]

    if opcao == 1:
        return (velocidades[0], 'Download')
    elif opcao == 2:
        return (velocidades[1], 'Upload')
    elif opcao == 3:
        return (velocidades[2], 'Ping')
    elif opcao == 4:
        return (velocidades, 'Todos')


def main():

    opcao = int(input('''\nQual teste de velocidade você gostaria de fazer:
    1) Download
    2) Upload
    3) Ping
    4) Todos

    Sua escolha: '''))

    velocidade, tipo = teste_velocidade(opcao)

    if opcao == 4:
        tabela = [["Download", "Upload", "Ping"], [ velocidade[0], velocidade[1], velocidade[2]]]
        tabela_velocidade = tabulate(tabela, headers="firstrow", tablefmt="fancy_grid")

        print(tabela_velocidade)

    else:
        print(f'\nSeu {tipo} é de {velocidade}\n')


if __name__ == '__main__':
    main()
