from collections import namedtuple

Book = namedtuple('Book', ['fiksi', 'nonfiksi'])

judul = Book('Bumi', 'Madilog')

print("Judul Buku :")
print("Fiksi : ", judul[0])
print("Non-fiksi : ", judul.nonfiksi)

