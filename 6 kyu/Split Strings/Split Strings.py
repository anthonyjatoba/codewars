from textwrap import wrap
def solution(s):
    return [i if len(i) == 2 else i[0] + '_' for i in wrap(s, 2)]