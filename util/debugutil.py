__all__ = [
    'print_all'
]


def print_all(*data, sep='\n', fmt='', pre='', post=''):
    if pre:
        print(end=pre)
    print(*map(lambda x: format(x, fmt), data), sep=sep)
    if post:
        print(end=post)
