

#generator function type
def fun1():
    return "Ghobad"
    return 'soltani'


print(fun1)


def fun2():
    yield 'ghobad'
    yield 'soltani'
    yield '32'
    yield 'ghobad'
    
print(fun2)

for obj in fun2():
    print(obj)
    
    
set1=set(fun2())
print(set1)


obj1=fun2()
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))

# generator expresion type (or generator comprehsension)


list1=[x for x in range(1,50)]     #list comprehentions ()
print(list1)
for item in list1:
    print(item)


list1=(x for x in range(1,50))      # generator expression []
print(list1)
for item in list1:
    print(item)
    
    
    
    
    
    
    
    
list2=[x for x in range(1,10000)]
print(list2[1:8])


obj1=(x for x in range(1,10000))        #faster and using less memory
for i in range(0,8):
    print(next(obj1),end=" , ")





# fibonachi by generators

def fib(n):
    a=0
    b=1
    yield b
    for i in range(1,n):
        a,b=b,a+b
        yield b
        
for item in fib(8):
    print(item, end="\t")






#in loops when return to the start point generators remember last poin and begins from there
def fun1():
    x=20
    yield x
    x+=6
    yield x 
    x*=10
    yield x
    x=659898625
    
obj1=fun1()
for item in obj1:
    print(item)