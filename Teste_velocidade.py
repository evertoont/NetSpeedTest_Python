import speedtest

velocidade = speedtest.Speedtest()


def main():
    
    opcao = int(input('''\nQual teste de velocidade você gostaria de fazer:
    1) Download
    2) Upload
    3) Ping
    4) Todos

    Sua escolha: '''))


if __name__ == '__main__':
    main()
