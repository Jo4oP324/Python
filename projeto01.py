import socket
import threading

class ScannerDePortas:
    def __init__(self, endereco_ip, portas):
        self.endereco_ip = endereco_ip
        self.portas = portas
        self.resultados = {}

    def verificar_porta(self, porta):
        """
        Verifica se uma porta específica está aberta no endereço IP fornecido.
        """
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.settimeout(1)  # Tempo máximo para a tentativa de conexão

        try:
            cliente_socket.connect((self.endereco_ip, porta))
        except (socket.timeout, ConnectionRefusedError):
            self.resultados[porta] = 'Fechada'
        else:
            self.resultados[porta] = 'Aberta'
        finally:
            cliente_socket.close()

    def escanear_portas(self):
        """
        Inicia o escaneamento das portas utilizando múltiplas threads.
        """
        threads = []

        for porta in self.portas:
            thread = threading.Thread(target=self.verificar_porta, args=(porta,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def exibir_resultados(self):
        """
        Exibe os resultados do escaneamento de portas.
        """
        print(f'Escaneamento de portas para o IP: {self.endereco_ip}')
        for porta, status in sorted(self.resultados.items()):
            print(f'Porta {porta}: {status}')

def main():
    endereco_ip = input('Digite o endereço IP a ser escaneado: ')
    portas = list(map(int, input('Digite as portas a serem escaneadas (separadas por espaço): ').split()))
    
    scanner = ScannerDePortas(endereco_ip, portas)
    scanner.escanear_portas()
    scanner.exibir_resultados()

if __name__ == '__main__':
    main()
