#make new function from other one
def fun1(name):
    return "hello "+name

print(fun1('ghobad'))

fun2=fun1
print(fun2('ahmad'))

del fun1
print(fun2('arash'))
print(fun1('ehsan'))



#nesrted functions
def fun(name):
    print('inside in fun '+name)
    def fun1():
        return 'inside in fun1'
    def fun2():
        return 'inside in fun2'
    print('inside in fun1()')
    print('inside in fun2()')
    
fun('ghobad')
fun1()



# function by input functions
#1) 
def fun1(text):
    return "* "+ text + " #"


def fun2(text):
    str1=''
    for i in range(5):
        str1+=text
    return str1

def mainFun(func):
    print(func('ali raza '))
    print(10*"--")
    
mainFun(fun1)
mainFun(fun2)




#2)
def fun1(text):
    return "* "+ text + " #"


def fun2(text):
    str1=''
    for i in range(5):
        str1+=text
    return str1

def mainFun(funA,funB,name):
    print(funA(name))
    print(10*"--")
    print(funB(name))
    
mainFun(fun1,fun2,"ghobad ")




#3)
def calcFun(n):
    def sum(x,y):
        return x+y
    def sub(x,y):
        return x-y
    def mul(x,y):
        return x*y
    def div(x,y):
        return x/y
    if n==1:
        return sum
    if n==2:
        return sub
    if n==3:
        return mul
    if n==4:
        return div
    
# k=calcFun(1)
# print(k(20,10))

# k=calcFun(2)
# print(k(20,10))

# k=calcFun(3)
# print(k(20,10))

# k=calcFun(4)
# print(k(20,10))

for i in range(1,5):
    k=calcFun(i)
    print(k(5,2))







def mainFunc(func):                #act like a decorator
    def fun1():
        print(10*'--')
        print(func)
        print(10*'**')
    return fun1
    
def printName():
    return 'ghobad soltani'
    
k=mainFunc(printName())
k()



#make docorator
#1)function without inputs

def mainFun(func):
    def fun1():
        for i in range(5):
            func()
        print("#### ")
    return fun1

@mainFun
def printStar():
    print('***** ')
    
    
printStar()
    
    
    
    
    
#2)    function with inputs

def mainfun(func):
    def fun1(*args,**kwargs):
        print("$$$$$$$")
        print(func(*args,**kwargs))
        print('$$$$$$')
    return(fun1)


@mainfun
def sum(x,y):
    return(x+y)

sum(23,85)




#3)   more decorators for one function

def mainfun1(func):
    def fun1(*args,**kwargs):
        print("%%%%%%")
        print(func(*args,**kwargs))
        print("%%%%%%")
    return fun1


def mainfun2(func):
    def fun2(*args,**kwargs):
        print("$$$$$$$")
        print(func(*args,**kwargs))
        print("$$$$$$$")
    return fun2

@mainfun1
@mainfun2
def sum(x,y):
    return(x+y)

sum(23,85)

print(100*'-')

@mainfun2
@mainfun1
def sum(x,y):
    return(x+y)

sum(23,85)

