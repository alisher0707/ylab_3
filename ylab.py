import math



print("Выберите фигуру: ")
# круг, квадрат, прямоугольник, треугольник, трапеция, ромб.
print("Круг: '1' | Квадрат: '2' ")
print("Прямоугольник: '3' | Треугольник: '4' ")
print("Трапеция: '5' | Ромб: '6'")

# сфера, куб, параллелепипед, пирамида, цилиндр, конус.
print("Сфера: '7' | Куб: '8'")
print("Параллелепипед: '9' | Пирамида: '10'")
print("Цилиндр: '11' | Конус: '12'")

# v = int(input("\n Наберите номер фигуры: "))

# if v == 1:
#   print("Квадрат: ")
#   figure = Square(
#     x = int(input('Вводите a = : '))
# )
#   print("Площадь равно: ", figure.area())
#   print("Периметр равно: ", figure.perimetr())

# elif v == 2:
#  print("Прямоугольник: ")
#  figure = Rectangle(
#     x = int(input('Вводите a = : ')),
#     y = int(input('Вводите b = : '))
# )
#  print("Площадь равно: ", figure.area())
#  print("Периметр равно: ", figure.perimetr())

# elif v == 3:
#   print("Круг: ")
#   figure = Circle(
#     r = int(input('Вводите r = : '))
# )
#   print("Площадь равно: ", figure.area())
#   print("Периметр равно: ", figure.perimetr())

# elif v == 4:
#   print("Прямоугольник: ")
#   figure = Сube(
#     x = int(input('Вводите a = : '))
# )
#   print("Площадь равно: ", figure.area())
#   print("Периметр равно: ", figure.perimetr())

# elif v == 5:
#   print("Прямоугольник: ")
#   figure = Сube(
#     x = int(input('Вводите a = : '))
# )
#   print("Площадь равно: ", figure.area())
#   print("Периметр равно: ", figure.perimetr())

# elif v == 6:
#   print("Прямоугольник: ")
#   figure = Сube(
#     x = int(input('Вводите a = : '))
# )
#   print("Площадь равно: ", figure.area())
#   print("Периметр равно: ", figure.perimetr())

# elif v == 7:
#   print("Прямоугольник: ")
#   figure = Сube(
#     x = int(input('Вводите a = : '))
# )
#   print("Площадь равно: ", figure.area())
#   print("Периметр равно: ", figure.perimetr())

# elif v == 8:
#   print("Прямоугольник: ")
#   figure = Сube(
#     x = int(input('Вводите a = : '))
# )
#   print("Площадь равно: ", figure.area())
#   print("Периметр равно: ", figure.perimetr())

# elif v == 9:
#   print("Прямоугольник: ")
#   figure = Сube(
#     x = int(input('Вводите a = : '))
# )
#   print("Площадь равно: ", figure.area())
#   print("Периметр равно: ", figure.perimetr())

# elif v == 10:
#   print("Прямоугольник: ")
#   figure = Сube(
#     x = int(input('Вводите a = : '))
# )
#   print("Площадь равно: ", figure.area())
#   print("Периметр равно: ", figure.perimetr())

# elif v == 11:
#   print("Прямоугольник: ")
#   figure = Сube(
#     x = int(input('Вводите a = : '))
# )
#   print("Площадь равно: ", figure.area())
#   print("Периметр равно: ", figure.perimetr())

# elif v == 12:
#   print("Прямоугольник: ")
#   figure = Сube(
#     x = int(input('Вводите a = : '))
# )
#   print("Площадь равно: ", figure.area())
#   print("Периметр равно: ", figure.perimetr())


class Shape:

  title = "Фигура"
  
  def area(self):
    pass

  def perimetr(self):
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
    return 2 * (self.a + self.b + self.c + self.d)


class Sfera(Shape):

  def __init__(self, r):
    self.r = r

  def area(self):
    return math.pi * 4 * self.r **2

class Сube():

  title = "Куб"

  def __init__(self,x):
    self.x = x
     
  def area(self):
    return 6 * self.x ** 2

circle = Circle(8)
print(circle.perimetr())
print(circle.area())

