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


# n = int(input())
# x_list = [input().split(';') for x in range(n)]
# teams = set()
# for i in range(len(x_list)):
#     teams.add(x_list[i][0])
#     teams.add(x_list[i][2])
# score_table = {}
# for team in teams:
#     score_table[team] = [0, 0, 0, 0, 0]
# for team1, goal1, team2, goal2 in x_list:
#     score_table[team1][0] += 1
#     score_table[team2][0] += 1
#     if int(goal1) > int(goal2):
#         score_table[team1][1] += 1
#         score_table[team1][4] += 3
#         score_table[team2][3] += 1
#     elif int(goal2) > int(goal1):
#         score_table[team2][1] += 1
#         score_table[team2][4] += 3
#         score_table[team1][3] += 1
#     elif int(goal1) == int(goal2):
#         score_table[team1][2] += 1
#         score_table[team1][4] += 1
#         score_table[team2][2] += 1
#         score_table[team2][4] += 1
# for key in score_table:
#     print(key + ':', end='')
#     print(*score_table[key])
#
# print(x_list)

b = ['a', 'b', 'c', 'd']
a = {'a': [5,5,6,7,7,8], 'b': [1,2,3,4,5,1,], 'c': [8,7,6,5,4,3], 'd': [1,1,1,1,1,1]}
for team in b:
    a[team][3] = 100

print(a)
