per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
L=list(per_cent)
L2=per_cent.values()

print('list of banks', (L))
print('list of pr%', (L2), 'percent-year')

s=int(input('Enter money value'))

x=per_cent.get('ТКБ')
c1=float(x)
print('pr', (c1), '%', 'ТКБ')
p1=(s)*(c1)/100
print('profit for year', (p1))

x=per_cent.get('СКБ')
c1=float(x)
print('pr', (c1), '%', 'СКБ')
p2=(s)*(c1)/100
print('profit for year', (p2))

x=per_cent.get('ВТБ')
c1=float(x)
print('pr', (c1), '%', 'ВТБ')
p3=(s)*(c1)/100
print('profit for year', (p3))

x=per_cent.get('СБЕР')
c1=float(x)
print('pr', (c1), '%', 'СБЕР')
p4=(s)*(c1)/100
print('profit for year', (p4))

Mx=max(p1, p2, p3, p4)
print('Максимальная сумма, которую вы можете заработать —', Mx)


