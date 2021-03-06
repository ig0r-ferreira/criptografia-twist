from cryptotwist import codificar, decodificar
from colorama import init, Fore, Style

init(autoreset=True)


def exibir_erro(_erro):
    # Exibe uma mensagem de erro com a cor da fonte em vermelho
    print(f'{Fore.RED + Style.BRIGHT}Erro: {_erro}')


largura_separador = 100

print(f'\n{Style.BRIGHT}{" CRIPTOGRAFIA TWIST ":^100}')

while True:
    print(f'\n{"=" * largura_separador}')

    # Enquanto o usuário não escolher as operações informadas, solicita que ele tente novamente
    while True:
        try:
            operacao = int(input('- Digite 0 para codificar ou 1 para decodificar: ').strip())
        except ValueError:
            operacao = None

        if operacao == 1 or operacao == 0:
            break

        exibir_erro('Opção inválida! Tente novamente!')
    print()

    mensagem = input('- Digite a mensagem: ')
    print()

    # Enquanto o usuário não digitar uma chave válida, solicita que ele tente novamente
    while True:
        try:
            chave = int(input('- Digite a chave: ').strip())
        except ValueError:
            exibir_erro('A chave não é um número inteiro!')
        else:
            break
    print()

    resultado = None

    # Operação escolhida: codificar
    if operacao == 0:
        try:
            resultado = codificar(mensagem, chave)
        except Exception as erro:
            exibir_erro('Falha na codificação!\n' + str(erro))

    # Operação escolhida: decodificar
    else:
        try:
            resultado = decodificar(mensagem, chave)
        except Exception as erro:
            exibir_erro('Falha na decodificação!\n' + str(erro))

    if resultado is not None:
        print(f'- {Fore.GREEN + Style.BRIGHT}Resultado: {resultado}')

    print(f'{"=" * largura_separador}\n')

    continuar = None
    while continuar != 'N' and continuar != 'S':
        continuar = input('* Você deseja continuar [S/N]? ').strip().upper()

    if continuar == 'N':
        break
