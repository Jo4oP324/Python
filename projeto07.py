import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time


class MonitorNFe:
    def __init__(self, url, estados, arquivo_excel='disponibilidade_nfe.xlsx', path_destino='coloque aqui o diretorio de destino'): # Exemplo: 'C:\\arquivos\\'
        self.url = url
        self.estados = estados
        self.arquivo_excel = arquivo_excel
        self.path_destino = path_destino

    def capturar_disponibilidade(self):
        """
        Captura a disponibilidade do serviço de NFe para os estados fornecidos.
        """
        resultados = {}
        for estado in self.estados:
            resposta = requests.get(self.url)
            sopa = BeautifulSoup(resposta.text, 'html.parser')

            # Supondo que a página possui um elemento identificador para cada estado
            elemento_estado = sopa.find('td', string=estado)
            if elemento_estado:
                proximo_td = elemento_estado.find_next('td')
                if proximo_td:
                    # Verifica se dentro do próximo <td> existe uma imagem com o src desejado
                    img_tag = proximo_td.find('img')

                    if img_tag:
                        # Verifica o valor do atributo 'src' da imagem
                        src_value = img_tag['src']
                        if 'bola_verde_P.png' in src_value:
                            print(f'{estado} - Disponível', end=' - ')
                            disponibilidade = 'Disponível'
                        elif 'bola_vermelho_P.png' in src_value:
                            print(f'{estado} - Indisponível', end=' - ')
                            disponibilidade = 'Indisponível'
                        else:
                            print(f'{estado} - Falha na resposta', end=' - ')
                            disponibilidade = 'Falha na resposta'
                    else:
                        print(f'Disponibilidade para SP: {proximo_td.get_text()}')
            else:
                disponibilidade = 'Não encontrado'

            resultados[estado] = disponibilidade

        return resultados

    def salvar_em_excel(self, dados):
        """
        Salva os dados de disponibilidade em uma planilha Excel.
        """
        df = pd.DataFrame(list(dados.items()), columns=['Estado', 'Disponibilidade'])
        df.to_excel(self.path_destino+self.arquivo_excel, index=False)
        print(f'Dados salvos no arquivo Excel: {self.arquivo_excel}')

    def executar_monitoramento(self):
        """
        Executa o monitoramento da disponibilidade e salva os resultados periodicamente.
        """
        resultados = self.capturar_disponibilidade()
        self.salvar_em_excel(resultados)


def main():
    url = 'https://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx'
    estados = input('Digite os códigos dos estados a serem monitorados (separados por espaço): ').split()

    monitor = MonitorNFe(url, estados)

    # Executa o monitoramento a cada 30 minutos
    schedule.every(10).seconds.do(monitor.executar_monitoramento)

    print('Iniciando monitoramento de disponibilidade de NFe...')
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
