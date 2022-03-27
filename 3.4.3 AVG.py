# dataset_3363_4.txt
a, b, c, d = 0, 0, 0, 0
asum, bsum, csum = 0, 0, 0,

with open('D:\dataset_3363_4.txt') as file1, open('D:\ew_dataset_3363_4.txt', 'w') as file2:
    for line in file1:
        line = line.strip().split(';')
        a, b, c = int(line[1]), int(line[2]), int(line[3])
        d += 1
        # print((a + b + c) / 3)
        file2.write(str((a + b + c) / 3) + '\n')
        asum += a
        bsum += b
        csum += c
    list1 = [str(asum/d),' ', str(bsum/d), ' ', str(csum/d)]
    file2.writelines(list1)
    # print(list1)
    # print(asum/d, bsum/d, csum/d)
    # file2.write(str(asum/d), str(bsum/d), str(csum/d))
        # print(line)
        # print(a, b, c)
    # print(d)

    # print((a+b+c)/3)
    # file = file1.read()
    #     print(line)
    #     a = line[1]
    #     print(a)
