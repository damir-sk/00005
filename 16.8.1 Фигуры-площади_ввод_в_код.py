from Полиморфизм_пример_1_к_16_8_КОД import Rectangle, Square, Circle

#иже описываются прямоугольники для расчета

rect_1=Rectangle(3,4)
rect_2=Rectangle(12,5)

#и ниже вывод данных после вычисления
print('площадь прямоугольника=',rect_1.get_area())
print('площадь прямоугольника=',rect_2.get_area())

# или
print('площадь прямоугольника=',rect_1.get_area(),','
      'площадь прямоугольника=',rect_2.get_area())


square_1=Square(3)
print('площадь равностороннего прямоугольника=',square_1.get_area_square())


circle_1=Circle(5)
print('площадь круга=', circle_1.get_area_circle())


figs=[rect_1, rect_2, square_1, circle_1]

for i in figs:
    if isinstance(i,Square):
        print('площадь равностороннего прямоугольника (вывод через цикл)=', i.get_area_square())
    elif isinstance(i,Circle):
        print('площадь круга (вывод через цикл)=', i.get_area_circle())
    else:
        print('площадь прямоугольника (вывод через цикл)=',i.get_area())