#packing and unpacking     محتوای چندین متغیر در قالب یک متغیر بیان می شود
list1=[1,2,3,4,5]
print(list1)
print(*list1)


list2=['a','b','c','d']
def fun1(a,b,c,d):
    print(a,b,c,d)
fun1(*list2)


def fun2(**kwargs):
    for key in kwargs:
        print(key,kwargs[key])
        
fun2(X=10, Y=20 , Z=45)


def fun3(a,b,c):
    print(a,b,c)
def fun4(*args):
    list1=list(args)       #در اینجا list عمل unpacking را انجام می دهد.
    list1[0]='ghobad'
    list1[1]='ahmad'
    fun3(*list1)
fun4('ali','jasem','arash')


dic1={'ali':100,'jasem':200,'ghobad':400,'ahmad':300}
def fun1(**dic):
    print(dic)
    
fun1(**dic1)
    

#recursive functions (فراخوانی تابع درون خودش)
def fun1(n):
    if n==0:
        return 1
    else:
        return fun1(n-1)+3
    
print(fun1(4))



def mul(n,m):
    if n==0:
        return 0
    else:
        return m+mul(n-1,m)

print(mul(4,6))


def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
print(fib(6))




#توابع بازگشتی در لیستها
def printList(list):
    if len(list)==0:
        print(end=' ')
    else:
        print(list[0],end='\t')
        printList(list[1:])
list1=[1,2,3,4,5,6,7]
printList(list1)



# #توابع بازگشتی در لیستها(معکوس)
def printList(list):
    if len(list)==0:
        print(end=' ')
    else:
        printList(list[1:])
        print(list[0],end='\t')
list1=[1,2,3,4,5,6,7]
printList(list1)


#generator.next()   vs   generator.send()
def fun1():
    x=100
    x=yield x
    x=yield x+100
    yield x*5

g=fun1()                 #اگر خواستیم با send مقدار دهی کنیم می آییم و yieldها را درون ظرف می ریزیم 
print(next(g))
print(g.send(25))        #  هر موقع خواستیم که علاوه بر صدا زدن تابع به آن مقدار دهی هم بکنیم از send استفاده می کنیم.
print(g.send(35))        



def fun1():
    while True:
        x=yield 500
        yield x*100
g=fun1()
print(next(g))
print(g.send(15))
print(g.send(3))               #برگشت به خط اول به خاطر تمام شدن yield ها



import random
def fun1():
    while True:
        x=yield
        print(x,end='\t')

def fun2(func):
    while True:
        r=random.randint(1,100)
        func.send(r)
        yield
g1=fun1()
g1.send(None)

g2=fun2(g1)
next(g2)
next(g2)
next(g2)

