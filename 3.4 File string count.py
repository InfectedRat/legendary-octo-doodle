with open('D:\dataset_3363_3.txt') as file, open('D:\ew_dataset_3363_3.txt', 'w') as new_file:
    s = file.read().lower().strip().split()  # тут все прочитали не по линиям, а по элементам всего файла разделенного пробелами, и сделали из них список
    # s1 = s.count('aaxba')
    s.sort()
    maxcount = 0
    for el in s:
        s1 = s.count(el)
        if s1 > maxcount:
            maxcount = s1
            need_word = el
        # print(el, s1)
        # print(need_word)
    new_file.write(need_word + ' ' + str(maxcount))

    print(need_word)
    print(maxcount)

# with open('D:\dataset_3363_3.txt') as file:
#     for el in file:
#         line = el.strip()
#         print(line)
