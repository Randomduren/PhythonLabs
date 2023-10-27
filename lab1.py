def myfunc(list):
    if any(list[i] == 1 and ((list[i+1] == 2 and list[i+2] == 3) or (list[i+1] == 3 and list[i+2] == 2)) for i in range(len(list)-2)):
        return True
    elif any(list[i] == 2 and ((list[i+1] == 1 and list[i+2] == 3) or (list[i+1] == 3 and list[i+2] == 1)) for i in range(len(list)-2)):
        return True
    elif any(list[i] == 3 and ((list[i+1] == 2 and list[i+2] == 1) or (list[i+1] == 1 and list[i+2] == 2)) for i in range(len(list)-2)):
        return True
    else:
        return  False

n=int(input("Введите размер массива: "))
mylist=[]
for i in range(n):
    i = int(input())
    mylist.append(i)
print(myfunc(mylist))
