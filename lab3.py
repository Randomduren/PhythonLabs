def myfunc(funclist, c, d):
    if c>n or d>n:
        return ("a или b больше границ списка")

    generated_arr = [i for i in funclist if (funclist.index(i) >= (c - 1) and funclist.index(i) <= (d - 1))]
    return generated_arr

n=int(input("Введите размер массива: "))
mylist=[]
for i in range(n):
    i = int(input())
    mylist.append(i)
a= int(input())
b= int(input())
print(myfunc(mylist, a, b))

