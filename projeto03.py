from cryptography.fernet import Fernet
import os

class CriptografiaArquivos:
    def __init__(self, chave_arquivo='chave.key'):
        self.chave_arquivo = chave_arquivo
        self.fernet = self.carregar_ou_gerar_chave()

    def gerar_chave(self):
        """
        Gera uma nova chave e a salva em um arquivo.
        """
        chave = Fernet.generate_key()
        with open(self.chave_arquivo, 'wb') as arquivo_chave:
            arquivo_chave.write(chave)
        return Fernet(chave)

    def carregar_ou_gerar_chave(self):
        """
        Carrega uma chave existente do arquivo ou gera uma nova se o arquivo não existir.
        """
        if os.path.exists(self.chave_arquivo):
            with open(self.chave_arquivo, 'rb') as arquivo_chave:
                chave = arquivo_chave.read()
            return Fernet(chave)
        else:
            return self.gerar_chave()

    def criptografar_arquivo(self, caminho_arquivo):
        """
        Criptografa um arquivo e salva o resultado em um novo arquivo com o sufixo '.enc'.
        """
        with open(caminho_arquivo, 'rb') as arquivo:
            dados = arquivo.read()
        
        dados_criptografados = self.fernet.encrypt(dados)
        caminho_arquivo_criptografado = f'{caminho_arquivo}.enc'
        
        with open(caminho_arquivo_criptografado, 'wb') as arquivo:
            arquivo.write(dados_criptografados)
        
        print(f'Arquivo criptografado salvo como: {caminho_arquivo_criptografado}')

    def descriptografar_arquivo(self, caminho_arquivo_criptografado):
        """
        Descriptografa um arquivo e salva o resultado em um novo arquivo sem o sufixo '.enc'.
        """
        with open(caminho_arquivo_criptografado, 'rb') as arquivo:
            dados_criptografados = arquivo.read()
        
        dados = self.fernet.decrypt(dados_criptografados)
        caminho_arquivo_descriptografado = caminho_arquivo_criptografado.replace('.enc', '')
        
        with open(caminho_arquivo_descriptografado, 'wb') as arquivo:
            arquivo.write(dados)
        
        print(f'Arquivo descriptografado salvo como: {caminho_arquivo_descriptografado}')

def main():
    print('Criptografia de Arquivos')
    acao = input('Digite "criptografar" para criptografar um arquivo ou "descriptografar" para descriptografar um arquivo: ').strip().lower()
    
    if acao not in ['criptografar', 'descriptografar']:
        print('Ação inválida.')
        return
    
    caminho_arquivo = input('Digite o caminho do arquivo: ')
    
    criptografia = CriptografiaArquivos()
    
    if acao == 'criptografar':
        criptografia.criptografar_arquivo(caminho_arquivo)
    elif acao == 'descriptografar':
        criptografia.descriptografar_arquivo(caminho_arquivo)

if __name__ == '__main__':
    main()
