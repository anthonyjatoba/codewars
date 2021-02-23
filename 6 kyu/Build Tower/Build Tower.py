def tower_builder(n_floors):
    fmt = "{esp}{ast}{esp}"
    return [fmt.format(ast='*' * ((n * 2) - 1), esp=' ' * (n_floors - n)) for n in range(1, n_floors + 1)]