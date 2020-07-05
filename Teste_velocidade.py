import speedtest

velocidade = speedtest.Speedtest()


def teste_velocidade(opcao):
    print('\nRealizando teste de velocidade...')

    servidores = []
    velocidade.get_servers(servidores)
    velocidades = [velocidade.download(), velocidade.upload(),
                   velocidade.results.ping]

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


if __name__ == '__main__':
    main()
