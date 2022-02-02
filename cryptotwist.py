def char_para_int(c):
    if c == '_':
        return 0
    elif c == '.':
        return 27
    elif ord('a') <= ord(c) <= ord('z'):
        return ord(c) - 96
    else:
        return None


def int_para_char(d):
    if d == 0:
        return '_'
    elif d == 27:
        return '.'
    elif 1 <= d <= 26:
        return chr(d + 96)
    else:
        return None


def codificar(textoplano, k):
    n = len(textoplano)

    codigoplano = list(map(char_para_int, textoplano))

    cifradocodigo = []
    for i in range(0, len(codigoplano)):
        novo_cod = (codigoplano[(k * i) % n] - i) % 28
        cifradocodigo.insert(i, novo_cod)

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
