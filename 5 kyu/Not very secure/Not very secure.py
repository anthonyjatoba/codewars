import re

def alphanumeric(password):
    return True if re.match('^[a-zA-Z0-9]+$', password) else False