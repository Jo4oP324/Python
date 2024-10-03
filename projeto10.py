import time
import os

def monitorar_log(caminho_arquivo):
    """
    Monitora um arquivo de log, exibindo novas entradas à medida que aparecem.
    """
    print(f'Monitorando {caminho_arquivo}...')
    with open(caminho_arquivo, 'r') as arquivo:
        # Move para o final do arquivo
        arquivo.seek(0, os.SEEK_END)
        try:
            while True:
                # Lê uma nova linha
                linha = arquivo.readline()
                if not linha:
                    time.sleep(1)  # Espera um segundo se não houver nova linha
                    continue
                print(linha.strip())
        except KeyboardInterrupt:
            print("\nMonitoramento encerrado.")
            return

def menu():
    """
    Exibe o menu de opções para o usuário.
    """
    while True:
        print("\nEscolha um arquivo de log para monitorar:")
        print("1. /var/log/syslog - Logs do sistema")
        print("2. /var/log/auth.log - Logs de autenticação")
        print("3. /var/log/dpkg.log - Logs de instalação de pacotes")
        print("0. Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            monitorar_log('/var/log/syslog')
        elif opcao == '2':
            monitorar_log('/var/log/auth.log')
        elif opcao == '3':
            monitorar_log('/var/log/dpkg.log')
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == '__main__':
    menu()
