# n = int(input('kolichestvo igr: '))
# x_list = [input('kom1;gol1;kom2;gol2: ').split(';') for x in range(n)]
#
# vs = [(x[0], x[2]) for x in x_list]
#
# print(x_list)
# print(vs)


# n = int(input())
# team_lst = [input().split(';') for el in range(n)]
# print(team_lst)


n = int(input('Количесвтво игр: '))
x_list = [input('Ком1;Гол1;Ком2;Гол2: ').split(';') for x in range(n)]

print(x_list)