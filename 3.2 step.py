dict={}
n=int(input())
for i in range(n):
    x=int(input())
    if x in dict:
        print(dc[x])
    else:
        dict[x]=f(x)
        print(dict[x])

        # тотальное говно со степика