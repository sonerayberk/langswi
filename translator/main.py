import sys
import subprocess


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
    ord('?'): ord(','),
    ord('&'): ord('?'),
}


CYRILLIC_SYMBOLS = {
    chr(symbol) for symbol in cyrillic_latin_mapping.values() if chr(symbol).isalpha()
}


def get_mapping(input: str) -> dict:
    input = ''.join(
        symbol for symbol in input.strip().replace(' ', '') if symbol.isalpha()
    )

    if set(input.lower()) <= CYRILLIC_SYMBOLS:
        mapping = {v: k for k, v in cyrillic_latin_mapping.items()}
    else:
        mapping = cyrillic_latin_mapping

    return mapping


def translate(input: str) -> str:
    mapping = get_mapping(input)

    result = ''
    for symbol in input:
        if ord(symbol.lower()) in mapping.keys():
            result += chr(mapping[ord(symbol.lower())])
        else:
            result += symbol

    return result


def get_stdout() -> str:
    args = ('pbpaste', 'r',)
    process = subprocess.Popen(args, stdout=subprocess.PIPE, close_fds=True)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8')


def main() -> None:
    input = get_stdout()
    result = translate(input)
    sys.stdout.write(result + '\n')
