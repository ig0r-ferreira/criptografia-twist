def char_para_int(c):
    """
    :param c: Um caracter
    :return: Um número inteiro, ou None se <b>c</b> diferente de
        <b>'_'</b>, <b>'.'</b> ou <b>[a-z]</b>

    Retorna um inteiro correspondente ao caracter informado, seguindo o padrão:
    ‘_’ = 0, ‘a’ = 1, ‘b’ = 2, ..., ‘z’ = 26 e ‘.’ = 27.
    """
    if c == '_':
        return 0
    elif c == '.':
        return 27
    elif ord('a') <= ord(c) <= ord('z'):
        return ord(c) - 96
    else:
        return None


def int_para_char(d):
    """
    :param d: Um número inteiro
    :return: Um caracter, ou None se <b>d &lt; 0</b> ou <b>d &gt; 27</b>

    Retorna um caracter correspondente ao inteiro informado seguindo o padrão:
    ‘_’ = 0, ‘a’ = 1, ‘b’ = 2, ..., ‘z’ = 26 e ‘.’ = 27.
    """
    if d == 0:
        return '_'
    elif d == 27:
        return '.'
    elif 1 <= d <= 26:
        return chr(d + 96)
    else:
        return None


def codificar(textoplano, k):
    """
    :param textoplano: String que será codificada
    :param k: Chave que será utilizada na codificação, deve ser um número inteiro
    :return: String codificada

    Retorna uma string codificada a partir da utilização do método Twist.
    """

    # 'n' recebe a quantidade de caracteres do texto que será codificado
    n = len(textoplano)

    # Gera uma nova lista onde os elementos são os números obtidos
    # para cada caracter de 'textoplano'
    codigoplano = list(map(char_para_int, textoplano))

    cifradocodigo = []
    # Para cada elemento de 'codigoplano' é calculado um novo número utilizando a chave k,
    # em seguida, armazena-o em 'cifradocodigo'
    for i in range(0, len(codigoplano)):
        novo_cod = (codigoplano[(k * i) % n] - i) % 28
        cifradocodigo.insert(i, novo_cod)

    # Gera uma nova lista a partir de 'cifradocodigo' onde cada elemento é convertido
    # para caracter novamente
    textocifrado = list(map(int_para_char, cifradocodigo))
    textocifrado = ''.join(textocifrado)

    return textocifrado


if __name__ == '__main__':
    exemplos = [
        {'texto': 'wxyz', 'chave': 5},
        {'texto': 'cachorro.', 'chave': 11},
        {'texto': 'espero_que_funcione.', 'chave': 29}
    ]

    print(f'\n\033[1m{" Codificação ":-^50}\033[m')
    for i, ex in enumerate(exemplos):
        print(f'\033[1mTeste {i + 1}:\033[m\n'
              f'- Texto: {ex.get("texto")}\n'
              f'- Chave: {ex.get("chave")}\n'
              f'- Texto codificado: {codificar(ex.get("texto"), ex.get("chave"))}')
