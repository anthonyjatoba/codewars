def namelist(names):
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    elif len(names) == 2:
        return '{} & {}'.format(names[0]['name'], names[1]['name'])
    else:
        string = ', '.join(name['name'] for name in names[:-1])
        string += ' & ' + names[-1]['name']
        return string
        