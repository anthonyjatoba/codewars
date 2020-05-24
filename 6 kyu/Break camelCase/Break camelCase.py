import re

def solution(s):
    transitions = re.findall('[a-z][A-Z]', s)
    for t in transitions:
        s = s.replace(t, t[0] + ' ' + t[1])
    return s