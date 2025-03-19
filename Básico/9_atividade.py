# Verifique se um ano é bissexto

year = int(input('Informe um ano: \n'))

# Pega os dois últimos dígitos do ano
last_two_digits = year % 100

if last_two_digits % 4 == 0:
    print(f'O ano {year} é bissexto.')
else:
    print(f'O ano {year} não é bissexto.')
