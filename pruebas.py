from collections import namedtuple

a = (34, 24, 12)
b = (1, 2, 7)

red = lambda tup: tup[0]
green = lambda tup: tup[1]
blue = lambda tup: tup[2]
marron = lambda tup, i: tup[i]

print(red(a))

print(marron(b, 2))
Point = namedtuple('Point', ['x', 'y'])

p = Point(11, y=22)
print(p, p.x, p.y)

x1, y1 = p
print(y1)
