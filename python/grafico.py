print ('ola baitchola')

#altura = 1.71 

#print (altura)

import matplotlib
 
matplotlib.__all__

import matplotlib.pyplot as plt

estudantes = ['joao', 'maria', 'jose','Ana']
#notas = [8.5,9.1,4.5,1.0]

#plt.bar(x=estudantes,height=notas)

#plt.show()

from random import choice

estudante = choice(estudantes)
print (estudante) 


notas = {'1 trimestre': 8.5, '2 trimestre': 5.3,'3 trimestre': 10.0 }

soma = 0 
soma = sum(notas.values())
print (soma)

quantidadeNotas = len(notas)
print(quantidadeNotas)

media = soma / quantidadeNotas
print (media)

media = round(media,1)
print(media)

nota = float(input('digite a nota do estuande: '))

def qualitativo(x):
    return x + 0.5

print(qualitativo(nota))
