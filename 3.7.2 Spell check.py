# пробуем через сравнение списков, что видимо не ожидается
really_words = []
check_words = []
n_check_words = []

cnt_rll_w = int(input())
for i in range(cnt_rll_w):
    really_words.append(input().lower())

cnt_chk_w = int(input())
for i in range(cnt_chk_w):
    check_words.append(input().lower())

for i, j in enumerate(check_words):
    n_check_words.append(j.split())  # пиздец пакуем

flat_1 = [x for l in n_check_words for x in l]  # пиздец распакуем

mn_rly = set(really_words)  # тут мы просто преобразуем в множество

dup_free = []
for x in flat_1:
    if x not in dup_free:
        dup_free.append(x)

mn_check = set(dup_free)

result = mn_check - mn_rly

result_1 = [*result]

# print(f"Список с проверочными словами {really_words}")
# print(f"Множество с проверочными словами {mn_rly}")
# print(f"Проверить эти слова {check_words}")
# print(f"Проверить эти слова {n_check_words}")
# print(f"Множество со словами на проверку {mn_check}")
# print(dup_free)
# print(flat_1)
# for i, j in enumerate(result_1):
#     print(result_1[j], end='\n')
print(*result_1, sep='\n')
