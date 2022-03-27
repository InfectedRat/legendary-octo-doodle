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

#
# n = int(input('Количесвтво игр: '))
# x_list = [input('Ком1;Гол1;Ком2;Гол2: ').split(';') for x in range(n)]
#
# print(x_list)

# n = int(input())
# # x_list = [input().split(';') for x in range(n)]
# ls = [['ffff', '44', 'ggggg', '666'], ['jjjj', '1212', 'kjkj', '999']]
# print(ls)


n = int(input())
x_list = [input().split(';') for x in range(n)]
teams = set()
for i in range(len(x_list)):
    teams.add(x_list[i][0])
    teams.add(x_list[i][2])
score_table = {}
for team in teams:
    score_table[team] = [0, 0, 0, 0, 0]

print(score_table)