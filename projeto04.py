# file_hash_updated_v2.py

import hashlib
import sys
import os

def compute_hash(file_path, hash_algo='sha256'):
    hash_func = getattr(hashlib, hash_algo)()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"Arquivo '{file_path}' não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")
        sys.exit(1)

def save_hash_to_file(file_path, hash_value):
    # Gera o caminho para o arquivo .hash
    hash_file_path = f"{file_path}.hash"
    try:
        with open(hash_file_path, 'w') as hash_file:
            hash_file.write(hash_value)
        print(f"Hash salvo em '{hash_file_path}'.")
    except Exception as e:
        print(f"Erro ao salvar o hash no arquivo: {e}")

def load_hash_from_file(file_path):
    hash_file_path = f"{file_path}.hash"
    if os.path.isfile(hash_file_path):
        try:
            with open(hash_file_path, 'r') as hash_file:
                return hash_file.read().strip().lower()
        except Exception as e:
            print(f"Erro ao ler o arquivo de hash: {e}")
    else:
        print(f"Arquivo '{hash_file_path}' não encontrado.")
    return None

def main():
    while True:
        print("\n=== Verificação de Integridade de Arquivos ===")
        print("1. Gerar hash de um arquivo")
        print("2. Comparar hash de um arquivo com o hash existente")
        print("0. Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            file_path = input("Digite o caminho do arquivo: ").strip()
            if not os.path.isfile(file_path):
                print(f"O arquivo '{file_path}' não existe ou não é um arquivo válido.")
                continue

            hash_value = compute_hash(file_path)
            print(f"Hash (SHA-256) de '{file_path}': {hash_value}")
            save_hash_to_file(file_path, hash_value)

        elif escolha == '2':
            file_path = input("Digite o caminho do arquivo: ").strip()
            if not os.path.isfile(file_path):
                print(f"O arquivo '{file_path}' não existe ou não é um arquivo válido.")
                continue

            # Tentar carregar o hash do arquivo .hash
            existing_hash = load_hash_from_file(file_path)

            # Se o arquivo .hash não for encontrado, pedir o hash manualmente
            if existing_hash is None:
                existing_hash = input("Digite o hash existente para comparar: ").strip().lower()

            current_hash = compute_hash(file_path)
            print(f"Hash atual: {current_hash}")

            if current_hash == existing_hash:
                print("Os hashes coincidem. O arquivo não foi alterado.")
            else:
                print("Os hashes NÃO coincidem. O arquivo foi alterado.")

        elif escolha == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
