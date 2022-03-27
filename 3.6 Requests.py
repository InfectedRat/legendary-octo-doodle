import requests

# r = requests.get('https://example.com/')
# print(r.text)

# url = 'https://example.com/'
# par = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get(url, params=par)
# print(r.url)
j = 0
i = 0
# url = 'https://stepic.org/media/attachments/course67/3.6.2/790.txt'
# r = requests.get(url).text.splitlines()
# for el in r:
#     j += 1


with open('D:\dataset_3378_2.txt') as file, open('D:\ew_dataset_new_new.txt', 'w') as file2:
    url = file.readline().strip()
    r = requests.get(url).text.splitlines()
    file2.write(str(len(r)))
print(int(len(r)))

# while i < len(r):
#     i += 1

# print(r)
# print(i)
# print(int(len(r))+1)
