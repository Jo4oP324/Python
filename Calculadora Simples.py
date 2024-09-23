operacao = input('Digite qual operador utilizar (+, -, *, /): ')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if operacao == '+':
    resultado = n1 + n2
    print('A soma é de: {}'.format(resultado))
elif operacao == '-':
    resultado = n1 - n2
    print('A subtração é de: {}'.format(resultado))
elif operacao == '/':
    if n2 != 0:
        resultado = n1 / n2
        print('A divisão é de: {}'.format(resultado))
    else:
        print('Erro: Divisão por zero!')
elif operacao == '*' or operacao == 'x':
    resultado = n1 * n2
    print('A multiplicação é de: {}'.format(resultado))
else:
    print('Operador inválido')
