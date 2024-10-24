name='Ghobad'
age=32
list1=[211,326,594,846,3432,315,6548,321]
iterName=iter(name)
# iterage=iter(age)          #false
iterList=iter(list1)


print(next(iterName))
print(next(iterName))
print(next(iterName))
print(next(iterName))
print(next(iterName))
print(next(iterName))
# print(next(iterage))       #false
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))
print(next(iterList))



while True:
    try:
        print(next(iterName))
    except:
        break
    
    
    
while True:
    try:
        print(next(iterList))
    except:
        break
    




def chekIterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False



print(chekIterable(name))
print(chekIterable(age))
print(chekIterable(list1))


iterList1=iter(list1)
for i in range(len(list1)):
    print(next(iterList1))







def chekIterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False




class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"{self.name}\t\t{self.age}"
    
p1=person('ghobad',32)
p2=person('ahmad',30)
p3=person('arash',29)
p4=person('ehsan',34)
list2=[p1,p2,p3,p4]

itpeaple=iter(list2)
for i in range(len(list2)):
    print(next(itpeaple))
    
print(chekIterable(list2))


# functions in iterables     sum, min,sorted,enumerate,any,all

list1=[321,64,987,534,6984,36,-698,657,54,6987,5546]
print(sum(list1))
print(min(list1))

list2=sorted(list1)
print(list1)
print(list2)



list3=('red','blue','yellow','brown')
for item in enumerate(list3):
    print(item)



list4=[False,True,False,True,False]
list5=[True,True,True,True,True]
list6=[False,False,False,False,False]

print(any(list4))
print(any(list5))
print(any(list6))

print(all(list4))
print(all(list5))
print(all(list6))




class Counter:
    def __init__(self,start,end):
        self.start=start
        self.end=end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        current=self.start
        if current>self.end:
            raise StopIteration
        self.start+=1
        return current
    
counter1=Counter(0,20)
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))


for i in counter1:
    print(i)


# fobonachi counter

class FIB:
    def __init__(self,end):
        self.a=0
        self.b=1
        self.end=end
    
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>self.end:
            raise StopIteration
        return self.a
    
fib1=FIB(5000)
for item in fib1:
    print(item, end="\t")




# unpacking lists or tuples

list1=[321,654,69874,68456]

x,y,z,a=list1
print(x)
print(y)
print(z)
print(a)





# iter with two input (function , end character or integeer or obj)
start=0
def getString(str):
    return str[start]

str1="ghobad soltani"
iterStr=iter(lambda: getString(str1),' ')
for item in iterStr:
    print(item)
    start+=1




count=1
def Counter():
    return count

counter=iter(lambda: Counter(),31)

for item in counter:
    print(item)





class TestIter:
    def __init__(self,list):
        self.list=list
        self.itList=iter(self.list)
        
    def __iter__(self):
        return self.itList
    
    def __call__(self):      #زمانی می آید که اولین ورودی کالیبل باشد و متد باشد 
        return next(self.itList)
    
t1=TestIter([321,654,87,65,487,97,654])
iter1=iter(t1,487)
for item in iter1:
    print(item)
    
        