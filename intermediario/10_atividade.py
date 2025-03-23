# Concatenar duas listas sem usar o operador +
Filmes = ['Pacto Sinistro', 'Cidadão Kane', 'Rastros de ódio']
Diretor = ['Alfred Hitchcock', 'Orson Welles', 'John Ford']

for q, a in zip(Filmes, Diretor):
    print('{0}? É {1}.'.format(q, a))