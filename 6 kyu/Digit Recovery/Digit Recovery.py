from itertools import permutations
def recover(st):
    digito_lista = {digito: list(permutations(nome)) for nome, digito in alph.items()}
    digitos = []
    for i in range(len(st)):
        for j in range(i, len(st) + 1):
            subs = st[i:j]
            for digito, nomes in digito_lista.items():
                if tuple(subs) in nomes:
                    digitos.append(str(digito))
    if not digitos:
        return 'No digits found'
    return ''.join(digitos)