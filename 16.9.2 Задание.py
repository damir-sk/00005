class Rectangle:
    def __init__(self,a, b):
        self.a = a
        self.b = b


    def getx(self):
        return self.a

    def gety(self):
        return self.b


# расчет площади
    def getArea(self):
        return self.a * self.b


rect_1=Rectangle(5,10)

print('Ширина =', rect_1.a)
print('Длина =', rect_1.b)


Rectangle=(rect_1.a, rect_1.b)
print('Прямоугольник со сторонами',Rectangle)