import requests
import pandas as pd


class ConsultorDeFilmes:
    def __init__(self, chave_api, base_url='https://api.themoviedb.org/3'):
        self.chave_api = chave_api
        self.base_url = base_url

    def buscar_filmes(self, consulta):
        """
        Busca filmes na API do The Movie Database com base na consulta fornecida.
        """
        url = f'{self.base_url}/search/movie'
        parametros = {
            'api_key': self.chave_api,
            'query': consulta,
            'language': 'pt-BR'
        }
        resposta = requests.get(url, params=parametros)
        dados = resposta.json()
        return dados.get('results', [])

    def salvar_em_excel(self, filmes, arquivo_excel='filmes.xlsx', path_destino='coloque_aqui_o_diretorio_de_destino'): # Exemplo: 'C:\\arquivos\\'
        """
        Salva os dados dos filmes em uma planilha Excel.
        """
        dados = [{
            'Título': filme.get('title'),
            'Descrição': filme.get('overview'),
            'Data de Lançamento': filme.get('release_date'),
            'Avaliação': filme.get('vote_average')
        } for filme in filmes]

        df = pd.DataFrame(dados)
        print(path_destino+arquivo_excel)
        #pd.ExcelFile(path_destino+arquivo_excel).parse(sheet_name='Filmes', header=1)
        df.to_excel(path_destino+arquivo_excel, sheet_name='Filmes', index=False)
        print(f'Dados salvos no arquivo Excel: {arquivo_excel}')


def main():
    chave_api = 'coloque_sua_chave_aqui'
    consulta = input('Digite o título do filme a ser pesquisado: ')

    consultor = ConsultorDeFilmes(chave_api)
    filmes = consultor.buscar_filmes(consulta)

    if filmes:
        consultor.salvar_em_excel(filmes)
        print('Consulta concluída. Dados dos filmes salvos com sucesso.')
    else:
        print('Nenhum filme encontrado para a consulta.')


if __name__ == '__main__':
    main()
