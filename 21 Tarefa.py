import os

# Caminho para a pasta onde está o arquivo de áudio
caminho_pasta_audio = 'Aud'

# Nome do arquivo de áudio
nome_arquivo_audio = 'KORDHELL x 2KE x 808IULI - K-SLIDE.mp3'

# Caminho completo para o arquivo de áudio
caminho_arquivo_audio = os.path.join(caminho_pasta_audio, nome_arquivo_audio)

# Verificar se o arquivo existe
if os.path.exists(caminho_arquivo_audio):
    print(f'O arquivo de áudio está localizado em: {caminho_arquivo_audio}')
else:
    print(f'O arquivo de áudio não foi encontrado.')
    print(f'Verifique o caminho e o nome do arquivo.')
    print(f'Caminho construído: {caminho_arquivo_audio}')
    print(f'Diretório de trabalho atual: {os.getcwd()}')
