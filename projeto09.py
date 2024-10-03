import requests


class ConsultorDeClima:
    def __init__(self, chave_api, base_url='https://api.openweathermap.org/data/2.5'):
        self.chave_api = chave_api
        self.base_url = base_url

    def consultar_clima(self, cidade):
        """
        Consulta o clima atual para a cidade fornecida na API OpenWeather.
        """
        url = f'{self.base_url}/weather'
        parametros = {
            'q': cidade,
            'appid': self.chave_api,
            'units': 'metric',  # Temperatura em graus Celsius
            'lang': 'pt'
        }
        resposta = requests.get(url, params=parametros)
        dados = resposta.json()

        if resposta.status_code == 200:
            return {
                'Cidade': dados['name'],
                'Temperatura': dados['main']['temp'],
                'Descrição': dados['weather'][0]['description'],
                'Umidade': dados['main']['humidity']
            }
        else:
            return {'Erro': dados.get('message', 'Erro desconhecido')}


def main():
    chave_api = 'coloque_sua_chave_aqui'
    cidade = input('Digite o nome da cidade para consulta do clima: ')

    consultor = ConsultorDeClima(chave_api)
    clima = consultor.consultar_clima(cidade)

    if 'Erro' in clima:
        print(f'Erro ao consultar clima: {clima["Erro"]}')
    else:
        print(f'Cidade: {clima["Cidade"]}')
        print(f'Temperatura: {clima["Temperatura"]}°C')
        print(f'Descrição: {clima["Descrição"]}')
        print(f'Umidade: {clima["Umidade"]}%')


if __name__ == '__main__':
    main()
