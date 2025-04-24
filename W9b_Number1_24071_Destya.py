from collections import namedtuple

Koordinat = namedtuple('Koordinat', ['x', 'y'])

titik1 = Koordinat('2', '4')

print("x = ", titik1[0])
print("y = ", titik1[1])

print("x = ", titik1.x)
print("y = ", titik1.y)

print("x = ", getattr(titik1, 'x'))
print("y = ", getattr(titik1, 'y'))