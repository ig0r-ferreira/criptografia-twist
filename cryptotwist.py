def __char_para_int(c):
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


def __int_para_char(d):
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


def __validar_texto(textoplano):
    """
    :param textoplano: String
    :return: None

    Verifica se o texto contém apenas *letras minúsculas*, *pontos(.)* e *undescores(_)*.
    Levanta uma exceção caso contenha qualquer outro caracter não especificado.
    """

    if type(textoplano) is not str:
        raise TypeError('\'textoplano\' não é uma string!')

    if ' ' in textoplano:
        raise ValueError('O texto não deve conter espaços. Se necessário, utilize \'_\'.')

    if len(textoplano) > 70:
        raise ValueError('O tamanho máximo do texto deve ser de 70 caracteres.')

    elif len(textoplano) < 1:
        raise ValueError('O tamanho mínimo do texto deve ser de 1 caracter.')

    # Remove os caracteres '.' e '_' da string
    somente_palavras = textoplano.replace('.', '').replace('_', '')

    # Cria uma lista com os códigos de cada caracter
    msg_ascii = list(map(lambda l: ord(l), somente_palavras))

    # Verifica se há qualquer outro caracter fora do intervalo [a-z] em minúsculo
    if min(msg_ascii) < 97 or max(msg_ascii) > 122:
        raise ValueError(f'\'{textoplano}\' não é um texto válido! É permitido apenas '
                         f'letras minúsculas e sem acentos, pontos(.) e underscore(_).')


def __validar_chave(k, textoplano):
    """
    :param k: Número inteiro
    :param textoplano: String
    :return: None

    Verifica se a chave: \n
    - É um número inteiro
    - Está no intervalo de 1 a 300
    - Chave e a quantidade de caracteres de *textoplano* são primos entre si

    Caso contrário levanta uma exceção.
    """

    if type(k) is not int:
        raise TypeError('\'k\' não é um número inteiro!')

    if k < 1 or k > 300:
        raise ValueError('Chave inválida! A chave deve ser um número entre 1 e 300.')

    from math import gcd

    # Verifica se a chave e o tamanho da mensagem não são primos entre si
    if gcd(k, len(textoplano)) != 1:
        raise ValueError('Tente com outra chave! A chave e a quantidade de caracteres '
                         'devem ser primos entre si.')


def codificar(textoplano, k):
    """
    :param textoplano: String que será codificada
    :param k: Chave que será utilizada na codificação, deve ser um número inteiro
    :return: String codificada

    Retorna uma string codificada a partir da utilização do método Twist.
    """

    # Valida o texto informado
    __validar_texto(textoplano)
    # Valida a chave informada
    __validar_chave(k, textoplano)

    # 'n' recebe a quantidade de caracteres do texto que será codificado
    n = len(textoplano)

    # Gera uma nova lista onde os elementos são os números obtidos
    # para cada caracter de 'textoplano'
    codigoplano = list(map(__char_para_int, textoplano))

    cifradocodigo = []
    # Para cada elemento de 'codigoplano' é calculado um novo número utilizando a chave k,
    # em seguida, armazena-o em 'cifradocodigo'
    for i in range(0, len(codigoplano)):
        novo_cod = (codigoplano[(k * i) % n] - i) % 28
        cifradocodigo.insert(i, novo_cod)

    # Gera uma nova lista a partir de 'cifradocodigo' onde cada elemento é convertido
    # para caracter novamente
    textocifrado = list(map(__int_para_char, cifradocodigo))
    textocifrado = ''.join(textocifrado)

    return textocifrado


def decodificar(textocifrado, k):
    """
    :param textocifrado: String codificada
    :param k: Chave que será utilizada na decodificação, deve ser um número inteiro
    :return: String decodificada

    Retorna uma string decodificada a partir da utilização do método Twist.
    """

    # Valida o texto informado
    __validar_texto(textocifrado)
    # Valida a chave informada
    __validar_chave(k, textocifrado)

    # 'n' recebe a quantidade de caracteres do texto codificado
    n = len(textocifrado)

    # Gera uma nova lista onde os elementos são os números obtidos
    # para cada caracter de 'textocifrado'
    cifradocodigo = list(map(__char_para_int, textocifrado))

    # Inicializa 'codigoplano' com valores nulos e com o mesmo tamanho de 'texto cifrado'
    codigoplano = list([None] * n)

    # Cada elemento de 'cifradocodigo' é revertido para o número que corresponde
    # ao caracter original.
    # Em seguida, utilizando a chave 'k', o número é armazenado na sua posição original
    for i in range(0, len(cifradocodigo)):
        cod_ant = (cifradocodigo[i] + i) % 28
        pos = (k * i) % n
        codigoplano[pos] = cod_ant

    # Gera uma nova lista a partir de 'codigoplano' onde cada elemento é convertido
    # para caracter novamente
    textoplano = list(map(__int_para_char, codigoplano))
    textoplano = ''.join(textoplano)

    return textoplano


if __name__ == '__main__':
    exemplos = [
        {'texto': 'ola', 'chave': 5},
        {'texto': 'wxyz', 'chave': 5},
        {'texto': 'cachorro.', 'chave': 11},
        {'texto': 'espero_que_funcione.', 'chave': 29}
    ]

    print(f'\n\033[1m{" Codificação ":-^50}\033[m')
    for index, ex in enumerate(exemplos):
        texto = ex.get('texto')
        chave = ex.get('chave')
        texto_codificado = codificar(texto, chave)
        ex['texto_codificado'] = texto_codificado

        print(f'\033[1mTeste {index + 1}:\033[m\n'
              f'- Texto: {texto}\n'
              f'- Chave: {chave}\n'
              f'- Texto codificado: {texto_codificado}')

    print(f'\n\033[1m{" Decodificação ":-^50}\033[m')
    for index, ex in enumerate(exemplos):

        texto_codificado = ex.get('texto_codificado')
        chave = ex.get('chave')

        texto_original = decodificar(texto_codificado, chave)

        print(f'\033[1mTeste {index + 1}:\033[m\n'
              f'- Texto codificado: {texto_codificado}\n'
              f'- Chave: {chave}\n'
              f'- Texto original: {texto_original}')
