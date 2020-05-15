def likes(names):

    verb = 'like'
    if len(names) < 2:
        verb = 'likes'

    if len(names) == 0:
        people = 'no one'
    if len(names) == 1:
        people = names[0]
    if len(names) == 2:
        people = '{} and {}'.format(names[0], names[1])
    if len(names) == 3:
        people = '{}, {} and {}'.format(names[0], names[1], names[2])
    elif len(names) > 3:
        people = '{}, {} and {} others'.format(names[0], names[1], len(names) - 2)
    
    return '{} {} this'.format(people, verb)