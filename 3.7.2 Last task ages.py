f = open('D:\dataset_3380_5.txt', 'r')
a = []
for i in f:
    a.append(i.split())
f.close()

res = [[] for i in range(11)]  # список из 11 пустых списков

for i in a:
    res[int(i[0]) - 1].append(int(i[2]))  #

# print(a)
# print(res)

res1 = []
for i in res:
    if len(i) == 0:
        res1.append(0)  # если данных о росте нет, но пишем 0
    else:
        res1.append(sum(i) / len(i))  # если данные есть, то высчитываем среднее

# print(res1)
for i in res1:
    if i == 0:
        print(res1.index(i) + 1, '-')  # если 0, то выводим прочерк
    else:
        print(res1.index(i) + 1, i)  # если не 0,то выводим номер класса и среднее
        # значение