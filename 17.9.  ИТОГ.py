
# Что-то набредил, буду рад посрочной критике )))

def F(raw, element):

 #сортировка по возрастанию:
 count=0
 k = 0

 for i in range(len(raw)):  # проходим по всему массиву

    idx_min = i  # сохраняется индекс рандомного элемента из ряда
    for j in range(i, len(raw)):
        count += 1
        if raw[j] < raw[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        raw[i], raw[idx_min] = raw[idx_min], raw[i]

    if raw[i] < element:
         k += 1

 print(count, '- количество проходок при перестановке')
 print('---')
 print(raw, ' - перетасованный ряд')
 print(k, ' - индекс элемента рядом слева в ряду, меньшего чем введено пользователем')



raw = list(map(int, input('ввод ряда чисел через пробел: ').split()))
element = int(input('ввод числа пользователем: '))

F(raw, element)