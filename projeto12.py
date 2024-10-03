import random
import string
import argparse

def gerar_senha(tamanho, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    caracteres = ""
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    
    if not caracteres:
        raise ValueError("Nenhum tipo de caractere foi selecionado para a senha.")
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    parser = argparse.ArgumentParser(description="Gerador de Senhas Seguras")
    parser.add_argument("-t", "--tamanho", type=int, default=12, help="Tamanho da senha (padrão: 12)")
    parser.add_argument("-m", "--maiusculas", action="store_true", help="Incluir letras maiúsculas")
    parser.add_argument("-n", "--minusculas", action="store_true", help="Incluir letras minúsculas")
    parser.add_argument("-d", "--numeros", action="store_true", help="Incluir números")
    parser.add_argument("-s", "--simbolos", action="store_true", help="Incluir símbolos")
    
    args = parser.parse_args()

    try:
        senha_gerada = gerar_senha(
            tamanho=args.tamanho,
            incluir_maiusculas=args.maiusculas,
            incluir_minusculas=args.minusculas,
            incluir_numeros=args.numeros,
            incluir_simbolos=args.simbolos
        )
        print(f"Senha gerada: {senha_gerada}")
    except ValueError as ve:
        print(f"Erro: {ve}")

if __name__ == "__main__":
    main()
