import numpy as np

a = 'x'
b = ord(a)
#print(f'O código para {a} é {b}')

c = chr(b)
#print(f'A letra para {b} é {c}')

for codigo in range(256):
    caracter = chr(codigo)
    #print(f'{codigo} - {caracter}')

# Receba uma string e retorne um código equivalente à string
# Faça o inverso


def convert_string_in_code(word: str):
    code = np.array([])
    for letter in word:
        np.append(code, ord(letter))

    return code


code = convert_string_in_code('marcelle')
print(code)