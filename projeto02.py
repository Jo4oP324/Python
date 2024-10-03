import socket
import threading
from queue import Queue
import ipaddress


class ScannerPortasAvancado:
    def __init__(self, ip_inicial: str, ip_final: str, porta_inicial: int, porta_final: int):
        """
        Inicializa o scanner com o intervalo de IPs e portas.
        """
        self.ip_inicial = ipaddress.IPv4Address(ip_inicial)
        self.ip_final = ipaddress.IPv4Address(ip_final)
        self.porta_inicial = porta_inicial
        self.porta_final = porta_final
        self.fila = Queue()
        self.lock = threading.Lock()  # Lock para controlar o acesso ao console

    def verificar_porta(self, ip: str, porta: int):
        """
        Tenta conectar à porta no IP especificado.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            resultado = s.connect_ex((ip, porta))
            with self.lock:  # Usa o lock para controlar a saída no console
                if resultado == 0:
                    print(f"[+] Porta {porta} aberta no IP {ip}")
                else:
                    print(f"[-] Porta {porta} fechada no IP {ip}")

    def scanner(self):
        """
        Função executada por threads para processar as portas da fila.
        """
        while not self.fila.empty():
            ip, porta = self.fila.get()
            self.verificar_porta(ip, porta)
            self.fila.task_done()

    def preparar_fila(self):
        """
        Prepara a fila com combinações de IPs e portas para serem verificadas.
        """
        for ip_int in range(int(self.ip_inicial), int(self.ip_final) + 1):
            ip = str(ipaddress.IPv4Address(ip_int))
            for porta in range(self.porta_inicial, self.porta_final + 1):
                self.fila.put((ip, porta))

    def iniciar(self, num_threads=10):
        """
        Inicia o processo de verificação com múltiplas threads.
        """
        self.preparar_fila()

        print(
            f"Iniciando verificação de IPs {self.ip_inicial} a {self.ip_final}, portas {self.porta_inicial} a {self.porta_final}...")

        threads = []
        for _ in range(num_threads):
            t = threading.Thread(target=self.scanner)
            t.daemon = True
            t.start()
            threads.append(t)

        self.fila.join()

        for t in threads:
            t.join()


def main():
    ip_inicial = input("Digite o IP inicial (ex: 192.168.0.1): ")
    ip_final = input("Digite o IP final (ex: 192.168.0.254): ")
    porta_inicial = int(input("Digite a porta inicial (ex: 20): "))
    porta_final = int(input("Digite a porta final (ex: 1024): "))

    scanner = ScannerPortasAvancado(ip_inicial, ip_final, porta_inicial, porta_final)
    scanner.iniciar(num_threads=20)


if __name__ == '__main__':
    main()
