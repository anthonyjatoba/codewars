def count_smileys(arr):
    smiles = [':)', ':D', ':-)', ':-D',':~)', ':~D',
              ';)', ';D', ';-)', ';-D',';~)', ';~D']
    return sum(arr.count(smile) for smile in smiles)