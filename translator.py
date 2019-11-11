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


def translator(input, mapping=None, reverse=False):
    if mapping is None:
        mapping = cyrillic_latin_mapping

    if reverse:
        mapping = {value: key for key, value in cyrillic_latin_mapping.items()}

    result = ''
    for symbol in input:
        if ord(symbol) in mapping.keys():
            result += chr(mapping[ord(symbol)])
        else:
            result += symbol

    return result


if __name__ == '__main__':
    # result = translator('njkmrj bp ,jkmijq k.,db r nt,t', reverse=False)
    result = translator('rfrjq-nj vtuf ;tcnrbq ntrcn?', reverse=False)
    print(result)
