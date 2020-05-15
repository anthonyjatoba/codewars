def DNA_strand(dna):
    pair = {'A':'T',
            'T':'A',
            'C':'G',
            'G':'C'}
    return ''.join(pair[k] for k in dna)