import math




  # print("Периметр равно: ", figure.perimetr())

# elif v == 12:
#   print("Конус: ")
#   figure = Сube(
#     x = int(input('Вводите a = : '))
# )
#   print("Площадь равно: ", figure.area())
#   print("Периметр равно: ", figure.perimetr())

# площадь и переметр – общий метод для всех  фигур
class Shape:

  title = "Фигура"

  def area(self):
    pass

  def perimetr(self):
    pass
# V - объем фигур – спец. метод для объемных фигур
  def volume(self):
    pass


class Square(Shape):

  title = "Кватрат"

  def __init__(self, x):
    self.x = x

  def area(self):
    return self.x ** 2

  def perimetr(self):
    return self.x * 4

class Rectangle(Square):

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def area (self):
    return self.x * self.y

  def perimetr(self):
    return 2 * (self.x + self.y)


class Circle(Shape):

  def __init__(self, r):
    self.r = r

  def area(self):
    return math.pi * self.r **2

  def perimetr(self):
    return 2 * math.pi * self.r

class Romb(Square):

  def __init__(self, x, h):
    self.x = x
    self.h = h

  def area(self):
    return self.x * self.h

  def perimetr(self):
    return self.x * 4


class Triangle(Romb):

  def __init__(self, a, b, c, h):
    self.a = a
    self.b = b
    self.c = c
    self.h = h

  def area(self):
    return (self.a * self.h)/2

  def perimetr(self):
    return self.a + self.b + self.c


class Trapez(Triangle):

  def __init__(self, a, b, c, d, h):
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.h = h

  def area (self):
    return ((self.a * self.b) * self.h)/2

  def perimetr(self):
    return  (self.a + self.b + self.c + self.d)


class Sfera(Shape):

  def __init__(self, r):
    self.r = r

  def area(self):
    return math.pi * 4 * self.r **2

  def volume(self):
    return  4/3 * math.pi * r**3

class Сube():

  def __init__(self,x):
    self.x = x

  def area(self):
    return 6 * self.x ** 2

  def perimetr(self):
    return 12 * self.x


class Parallelep():

  def __init__(self,a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def area(self):
    return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)

  def perimetr(self):
    return 4 * (self.a + self.b + self.c)

class Piramida(Shape):

  def __init__(self,a,h):
    self.a = a
    self.h = h

  def area(self):
    return self.a * (self.a + 2 * self.h)


class Сylin(Shape):

  def __init__(self,r,h):
    self.r = r
    self.h = h

  def area(self):
    return 2 * math.pi * self.r * (self.r + self.h)


print("Выберите фигуру: ")
# круг, квадрат, прямоугольник, треугольник, трапеция, ромб.
print("Квадрат - '1' | Прямоугольник - '2' ")
print("Круг - '3' | Ромб - '4' ")
print("Треугольник - '5' | Трапеция - '6'")


f = int(input("\n Выберите вид фигуры: Плоский - 1, Объемные - 2 (1/2) "))

if f == 1:
  print("Квадрат - '1' | Прямоугольник - '2' ")
  print("Круг - '3' | Ромб - '4' ")
  print("Треугольник - '5' | Трапеция - '6'")
  v = int(input("\n Наберите номер фигуры: "))
  if v == 1:
    print("Квадрат: ")
    figure = Square(
    x = int(input('Вводите a = : '))
)
    print("Площадь равно: ", figure.area())
    print("Периметр равно: ", figure.perimetr())
  elif v == 2:
     print("Прямоугольник: ")
     figure = Rectangle(
    x = int(input('Вводите a = : ')),
    y = int(input('Вводите b = : '))
)
     print("Площадь равно: ", figure.area())
     print("Периметр равно: ", figure.perimetr())

  elif v == 3:
     print("Круг: ")
     figure = Circle(
    r = int(input('Вводите r = : '))
)
     print("Площадь равно: ", figure.area())
     print("Периметр равно: ", figure.perimetr())

  elif v == 4:
     print("Ромб: ")
     figure = Romb(
      x = int(input('Вводите a = : ')),
      h = int(input('Вводите h = : '))
)
     print("Площадь равно: ", figure.area())
     print("Периметр равно: ", figure.perimetr())

  elif v == 5:
     print("Треугольник: ")
     figure = Triangle(
       a = int(input('Вводите a = : ')),
       b = int(input('Вводите b = : ')),
       c = int(input('Вводите c = : ')),
       h = int(input('Вводите h = : '))
)
     print("Площадь равно: ", figure.area())
     print("Периметр равно: ", figure.perimetr())

  elif v == 6:
     print("Трапеция: ")
     figure = Trapez(
       a = int(input('Вводите a = : ')),
       b = int(input('Вводите b = : ')),
       c = int(input('Вводите c = : ')),
       d = int(input('Вводите d = : ')),
       h = int(input('Вводите h = : '))
)
     print("Площадь равно: ", figure.area())
     print("Периметр равно: ", figure.perimetr())


elif f==2:
  # сфера, куб, параллелепипед, пирамида, цилиндр, конус.
  print("Сфера: '7' | Куб: '8'")
  print("Параллелепипед: '9' | Пирамида: '10'")
  print("Цилиндр: '11' | Конус: '12'")
  v = int(input("\n Наберите номер фигуры: "))
  if v == 7:
    print("Сфера: ")
    figure = Sfera(
    r = int(input('Вводите r = : '))
)
    print("Площадь равно: ", figure.area())
    print("Объем: ", figure.volume())

  elif v == 8:
    print("Куб: ")
    figure = Сube(
    x = int(input('Вводите x = : '))
)
    print("Площадь равно: ", figure.area())
    print("Периметр равно: ", figure.perimetr())

  elif v == 9:
    print("Параллелепипед: ")
    figure = Parallelep(
      a = int(input('Вводите a = : ')),
      b = int(input('Вводите b = : ')),
      c = int(input('Вводите c = : '))
)
    print("Площадь равно: ", figure.area())
    print("Периметр равно: ", figure.perimetr())

  elif v == 10:
    print("Пирамида: ")
    figure = Piramida(
    a = int(input('Вводите a = : ')),
    h = int(input('Вводите h = : '))
)
    print("Площадь равно: ", figure.area())


  elif v == 11:
    print("Цилиндр: ")
    figure = Сylin(
    r = int(input('Вводите r = : ')),
    h = int(input('Вводите h = : '))
)
    print("Площадь равно: ", figure.area())
else:
  print("Неверная цифра")
