import argparse
import sys

# Rule #2: Explicit is better than implicit.

cyrillic_latin_mapping = {
    ord('q'): ord('й'),
    ord('w'): ord('ц'),
    ord('e'): ord('у'),
    ord('r'): ord('к'),
    ord('t'): ord('е'),
    ord('y'): ord('н'),
    ord('u'): ord('г'),
    ord('i'): ord('ш'),
    ord('o'): ord('щ'),
    ord('p'): ord('з'),
    ord('['): ord('х'),
    ord(']'): ord('ъ'),
    ord('a'): ord('ф'),
    ord('s'): ord('ы'),
    ord('d'): ord('в'),
    ord('f'): ord('а'),
    ord('g'): ord('п'),
    ord('h'): ord('р'),
    ord('j'): ord('о'),
    ord('k'): ord('л'),
    ord('l'): ord('д'),
    ord(';'): ord('ж'),
    ord("'"): ord('э'),
    ord('z'): ord('я'),
    ord('x'): ord('ч'),
    ord('c'): ord('с'),
    ord('v'): ord('м'),
    ord('b'): ord('и'),
    ord('n'): ord('т'),
    ord('m'): ord('ь'),
    ord(','): ord('б'),
    ord('.'): ord('ю'),
    ord('§'): ord('ё'),
}


def translate(
    input: str,
    mapping: dict = None,
    reverse: bool = False
) -> str:

    if mapping is None:
        mapping = cyrillic_latin_mapping

    if reverse:
        mapping = {v: k for k, v in cyrillic_latin_mapping.items()}

    result = ''
    for symbol in input:
        if ord(symbol) in mapping.keys():
            result += chr(mapping[ord(symbol)])
        else:
            result += symbol

    return result


def test_translate_in_modern_way():
    input = 'njkmrj bp ,jkmijq k.,db r nt,t'
    result = translate(input)
    assert result == u'только из большой любви к тебе'
    input = 'ерфтл нщг мукн ьгср'
    result = translate(input, reverse=True)
    assert result == 'thank you very much'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Translate cyrillic-latin texts.')
    parser.add_argument('text', help='Text that need to be converted.')
    parser.add_argument('--reverse', help='Use to translate from cyrillic to latin.')
    args = parser.parse_args()

    result = translate(args.text, reverse=args.reverse)
    sys.stdout.write(result + '\n')
