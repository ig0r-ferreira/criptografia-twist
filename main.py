def exibir_erro(_erro):
    # Exibe uma mensagem de erro com a cor da fonte em vermelho
    print(f'\033[1;31mErro: {_erro}\033[m')


def solicitar_operacao():
    # Enquanto o usuário não escolher as operações informadas, será exibido uma mensagem
    # para ele tentar novamente
    while True:
        try:
            _operacao = int(input('Digite 0 para codificar ou 1 para decodificar: ').strip())
        except ValueError:
            _operacao = None

        if _operacao == 1 or _operacao == 0:
            break

        exibir_erro('Opção inválida! Tente novamente!')

    return _operacao


def solicitar_mensagem():
    # Função responsável pela validação da mensagem
    def mensagem_valida(_msg):
        # Se a mensagem tem espaços
        if ' ' in _msg:
            exibir_erro('A mensagem não deve conter espaços. Utilize \'_\' ao invés de espaço.')
            return False

        # Se o tamanho da mensagem for superior a 70
        if len(_msg) > 70:
            exibir_erro('O tamanho máximo da mensagem deve ser de 70 caracteres.')
            return False
        # Se o tamanho da mensagem for inferior a 1
        elif len(_msg) < 1:
            exibir_erro('O tamanho mínimo da mensagem deve ser de 1 caracter.')
            return False

        # Remove os caracteres '.' e '_' da string
        somente_palavras = _msg.replace('.', '').replace('_', '')

        # Cria uma lista com os códigos de cada caracter
        msg_ascii = list(map(lambda l: ord(l), somente_palavras))

        # Verifica se há qualquer outro caracter fora do intervalo [a-z] em minúsculo
        if min(msg_ascii) < 97 or max(msg_ascii) > 122:
            exibir_erro('A mensagem deve estar em minúsculo, sem acentos e '
                        'sendo permitido apenas os caracteres \'.\' e \'_\'.')
            return False

        return True

    # Enquanto o usuário não digitar uma mensagem válida, será exibido uma mensagem
    # para ele tentar novamente atendendo aos requisitos
    while True:
        msg = input('Digite a mensagem: ')

        if mensagem_valida(msg):
            break

    return msg


def solicitar_chave(_msg):
    from math import gcd

    # Enquanto o usuário não digitar uma chave válida, será exibido uma mensagem
    # para ele tentar novamente atendendo aos requisitos
    while True:
        try:
            _chave = int(input('Digite a chave: ').strip())
        except ValueError:
            _chave = None

        # Verifica se chave não é nula e se está no intervalo de 1 a 300
        if _chave is not None and 1 <= _chave <= 300:
            # Verifica se a chave e o tamanho da mensagem são primos
            if gcd(_chave, len(_msg)) == 1:
                break
            else:
                exibir_erro('Chave inválida! Informe outra chave entre 1 e 300.')
        else:
            exibir_erro('Chave inválida! A chave deve ser um número entre 1 e 300.')

    return _chave


print()
# Solicita que o usuário escolha entre codificar ou decodificar
operacao = solicitar_operacao()
print()
# Solicita que o usuário informe a mensagem que será utilizada para fazer a operação escolhida
mensagem = solicitar_mensagem()
print()
# Solicita a chave que será utilizada nas operações de codificação e decodificação
chave = solicitar_chave(mensagem)
