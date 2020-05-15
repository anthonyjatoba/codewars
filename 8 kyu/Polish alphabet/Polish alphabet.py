def correct_polish_letters(st): 
    table = str.maketrans('ąćęłńóśźż', 'acelnoszz')
    return st.translate(table)