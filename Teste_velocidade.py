import speedtest
from tabulate import tabulate

velocidade = speedtest.Speedtest()


def teste_velocidade():
    print('\nRealizando teste de velocidade, porfavor aguarde... \n')

    servidores = []
    velocidade.get_servers(servidores)

    velocidades = [str(f"{round(velocidade.download() / 1_000_000, 2)} Mbps"),
                   str(f"{round(velocidade.upload() / 1_000_000, 2)} Mbps"),
                   str(f"{round(velocidade.results.ping, 2)} ms")]

    return velocidades


def main():

    input('''
    >>> Para obter um melhor resultado feche todos os programas do computador.
    >>> Se possível reinicie o PC para desativar todos os programas que ficam rodando em segundo plano.
    
    >>> Pressione ENTER para iniciar o teste de velocidade <<<
    ''')

    velocidade = teste_velocidade()

    tabela = [["Download", "Upload", "Ping"], [
        velocidade[0], velocidade[1], velocidade[2]]]

    tabela_velocidade = tabulate(
        tabela, headers="firstrow", tablefmt="fancy_grid")

    print(tabela_velocidade)


if __name__ == '__main__':
    main()
