class Rectangle:
    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

# расчет площади
    def getArea(self):
        return self.width * self.height


rect_1=Rectangle(5,10,50,100)

#print('rect_1.x =', rect_1.x)
#print('rect_1.y =', rect_1.y)
#print('rect_1.width =', rect_1.width)
#print('rect_1.height =', rect_1.height)

Rectangle=(rect_1.x, rect_1.y, rect_1.width, rect_1.height)
print('Rectangle',Rectangle)