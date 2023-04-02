def can_eat(h, f, h2, f2):
 dx = abs(h - f)
 dy = abs(h2 - f2)
 if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
 
     return True
 else:
     return False

h = int(input('Координаты коня (x,y): '))
f = int(input('Координаты другой фигуры (x,y): '))
print(can_eat(h[0], h[1], f[0], f[1]))
