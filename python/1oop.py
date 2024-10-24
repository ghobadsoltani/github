# oop

class person:
    count=0
    def __init__(self,name,family):
        self.name=name
        self.family=family
        person.count+=1
        
    def __str__(self):
        return f'{self.name}\t{self.family}'
    
    def __del__(self):
        print(self.name,"\t",self.family)
        
person1=person("Ghobad","Soltani")
person2=person("Ahmad","Asgari")
print(person.count)



# capsulation and encapsulation

class Person:
    count=0
    def __init__(self,name,family):
        self.__name=name
        self._family=family
        Person.count+=1
        
    def __str__(self):
        return f'{self.__name}\t{self._family}'
    
    def __del__(self):
        print(self.__name,"\t",self._family)
        
    def getName(self):
        return self.__name

    def getFamily(self):
        return self._family
    
           
person1=Person("Ghobad","Soltani")
person2=Person("Ahmad","Asgari")
print(person1.getName())
print(person2.getFamily())
print(Person.count)



def __PascalCase(str):
    strList=list(str)
    strList[0]=chr(ord(strList[0])-32)
    return ''.join(strList)

print(__PascalCase('sdkfn oijol kkjn kjn lkj nijub lih bijl'))



# inheritance

#1) single inhertance

class person:
    count=0
    def __init__(self,name,family):
        self.__name=name
        self._family=family
        person.count+=1
        
    def __str__(self):
        return f'{self.__name}\t{self._family}'
    
class Employee(person):
    def __init__(self,name,family,id,income):
        super().__init__(name,family)
        self._id=id
        self.__income=income
        
    def getFamily(self):
        return self._family
    
person1=Employee("ahmad",'asgari',35486,14000000)
print(person1.getFamily())    


# 2) multiple inheritance

class teacher:
    def __init__(self,name,family):
        self.__name=name
        self._family=family
        
    def getFamily(self):
        return self._family
    
class Employee:
    def __init__(self,id,income):
        self._id=id
        self.__income=income
        
    def __str__(self):
        return f'{self._id}\t{self.__income}'
    
class Karmand(teacher,Employee):
    def __init__(self,name,family,id,income,address):
        teacher.__init__(self,name,family)
        Employee.__init__(self,id,income)
        self.address=address
    
    def printInfo(self):
        return f"{self.name} , {self.family}"
    
    
    person1=Karmand('ghobad', 'soltani',369,10000,'shahrekord')
    print(karmand.printInfo())
        



#3)multi level inheritance
class Employee:
    def __init__(self,name,family):
        self.name=name
        self.family=family
        print("run init of Employee")
        
    def showEmployee(self):
        print("employee")
        
        
    def __str__(self):
        return f'{self.id}\t{self.income}'
    
class teacher(Employee):
    def __init__(self,name,family,id,income):
        Employee.__init__(self,name,family)
        self.id=id
        self.income=income
        print("run init of teacher")
        
    def showteacher(self):
        print("teacher")
        
    def getId(self):
        return self.id
  
  
class moalem(teacher):
    def __init__(self,name,family,id,income,address):
        teacher.__init__(self,name,family,id,income)
        self.address=address  
        print("run init of moalem")

    def showmoalem(self):
        print("moalem")
  
    def printInfo(self):
        print( self.name , self.family)
    
    
p1=moalem('ghobad','soltani',32565,10000,'shahrekord')
p1.printInfo()
p1.showteacher()
p1.showEmployee()
p1.showmoalem()






#4)hierarchical inheritance
class Employee:
    def __init__(self,name,family):
        self.name=name
        self.family=family
        print("run init of Employee")
        
    def showEmployee(self):
        print("employee")
        
        
    def __str__(self):
        return f'{self.id}\t{self.income}'
    
class teacher(Employee):
    def __init__(self,name,family,id,income):
        Employee.__init__(self,name,family)
        self.id=id
        self.income=income
        print("run init of teacher")
        
    def showteacher(self):
        print("teacher")
        
    def getId(self):
        return self.id
  
  
class moalem(Employee):
    def __init__(self,name,family,address):
        Employee.__init__(self,name,family)
        self.address=address  
        print("run init of moalem")

    def showmoalem(self):
        print("moalem")
  
    def printInfo(self):
        print( self.name , self.family)
        
p1=moalem('ahmad',"asgari","ghalehDarvish")
p2=teacher("arash","heidari",25,1000)
p2.showEmployee()
p2.showteacher()
p1.showEmployee()
p1.showmoalem()

    




#5)hybrid inheritance

class Employee:
    def __init__(self,name,family):
        self.name=name
        self.family=family
        print("run init of Employee")
        
    def showEmployee(self):
        print("employee")
        
        
    def __str__(self):
        return f'{self.id}\t{self.income}'
    
    
class teacher(Employee):
    def __init__(self,name,family,id):
        Employee.__init__(self,name,family)
        self.id=id
        print("run init of teacher")
        
    def showteacher(self):
        print("teacher")
        
  
  
class moalem(Employee):
    def __init__(self,name,family,address):
        Employee.__init__(self,name,family)
        self.address=address  
        print("run init of moalem")

    def showmoalem(self):
        print("moalem")
  
    def printInfo(self):
        print( self.name , self.family)
        
        
        
class student(teacher,moalem):
    def __init__(self,name,family,id,address,avg):
        teacher.__init__(self,name,family,id)
        moalem.__init__(self,name,family,address)
        self.avg=avg
        print("run init of student")
        
    def showstudent(self):
        print("student")
  
    def printInfo(self):
        print( self.name , self.family)
        
    
p1=student("ghobad","soltani",58,"shahrekord",19.75)
p1.printInfo()
p1.showteacher()
p1.showmoalem()
p1.showstudent()





#poly morphism in python
#kind1
def sum(a,b):
    return a+b

def sum(a,b,C=0):
    return a+b+C


print(sum(10,20))
print(sum(10,20,30))


#kind2
from multipledispatch import dispatch

@dispatch(int,int)
def sum(a,b):
    return a+b

@dispatch(int,int,int)
def sum(a,b,C):
    return a+b+C


print(sum(10,20))
print(sum(10,20,30))



#overloading(in classes)
#search standard operators as function in python
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age 
        
    def __add__(self,obj2):
        return self.age+obj2.age 
    
    def __mul__(self,obj2):
        return self.age*obj2.name
    
    def __lt__(self,obj2):
        return self.age>obj2.age
        
person1=person("ghobad",32)
person2=person("ahmad ",30)
print(person1+person2)
print(person1*person2)
print(person1>person2)



#polymorphism by *args
def sum(*args):
    s=0
    for item in args:
        s+=item
    return s
print(sum(12,34,5))
print(sum(12,34,5,56,345))
print(sum(12,34))

#exercise2
def sum(datatype,*args):
    if datatype=='int':
        s=0
    elif datatype=="str":
        s=""
    for item in args:
        s+=item
    return s

print(sum("int",12,34,5))
print(sum("int",12,34,5,56,345))
print(sum("int",12,34))
print(sum("str","ghobad ","ahmad ","arash"))


#overriding
#use of fuctions 

class A:
    def fun1(self):
        print('A class run Fun1')
    
    def fun2(self):
        print('A class run Fun2')

    def fun3(self):
        print('A class run Fun3')
    
    def mul(self,a,b):
        print(a*b)
        
#-------------------------------------------
        
class B:
    def fun1(self):
        print('B class run Fun1')
    
    def fun2(self):
        print('B class run Fun2')
    
    def sum(self,a,b):
        return a+b   
    
     
    def mul(self,a,b):
        print((a+b)*1000)
    
#-------------------------------------------
def func(obj):
    obj.fun1()
    obj.fun2()
    obj.mul(30,4)
    
a=A()
b=B()

func(a)
func(b)

# ====================================================

#overriding
#use of class methods
 
class A:
    def show(self):
        print("AAAAAA")
        
#-------------------------------------------
        
class B(A):
    def show(self):
        print("BBBBB")
#-------------------------------------------

a=A()
a.show()
b=B()
b.show()
super(B,b).show()


#another example
class A:
    def show(self):
        print("AAAAAA")
        
#-------------------------------------------
        
class B:
    def show(self):
        print("BBBBB")
#-------------------------------------------
class C(A,B):      #C(B,A)
    def show(self):
        print("CCCCC")
        #return A.show(self)
#-------------------------------------------

c=C()
c.show()
super(C,c).show()

# ==================================================================
#another example
class Employee:
    def __init__(self,name,family):
        self.name=name
        self.family=family
        
    def show(self):
        print("employee")
        
        
    def __str__(self):
        return f'{self.id}\t{self.income}'
    
    
class teacher(Employee):
    def __init__(self,name,family,id):
        Employee.__init__(self,name,family)
        self.id=id
        
    def show(self):
        print("teacher")
        
  
  
class moalem(Employee):
    def __init__(self,name,family,address):
        Employee.__init__(self,name,family)
        self.address=address  

    def show(self):
        print("moalem")
  
    def printInfo(self):
        print( self.name , self.family)
        
        
        
class student(teacher,moalem):       #(moalem,teacher)
    def __init__(self,name,family,id,address,avg):
        teacher.__init__(self,name,family,id)
        moalem.__init__(self,name,family,address)
        self.avg=avg
        
    def show(self):
        print("student")
        # return Employee.show(self)
        # return teacher.show(self)
  
    def printInfo(self):
        print( self.name , self.family)
        
        
    
p1=student("ghobad","soltani",58,"shahrekord",19.75)
p1.show()
super(student,p1).show()


#instance method , staticmethod , classmethod

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def showinfo(self):
        print(self.name)
        print(self.age)
    
    @staticmethod       #work independantly
    def sum(x,y):
        return x+y
    
    @classmethod        #work with class data
    def fun1(cls,x,y):
        return cls.sum(x,y)+2000
    
person1=person('ghobad',32)
person1.showinfo()

print(person.sum(20,40))
print(person.fun1(20,40))


#setter and getter
#by methods
class person:
    def __init__(self,name,family):
        self.__name=name
        self._family=family
        
    def showInfo(self):
        return f"{self.__name} , {self._family}"
        
    def getName(self):
        return self.__name
    
    def setName(self,name):
        self.__name=name
        
        
person1=person('ghobad','soltani')
print(person1.getName())
person1.setName('Ghobad')
print(person1.showInfo())



#by decorators
class person:
    def __init__(self,name,family):
        self.__name=name
        self._family=family
        
    def showInfo(self):
        return f"{self.__name} , {self._family}"
    
    @property             #name =name
    def name(self):
        return self.__name
    
    @name.setter       #name=name
    def name(self,name):
        self.__name=name
    
    @property             #family =family
    def family(self):
        return self._family
    
    @family.setter       #family=family
    def family(self,family):
        self._family=family
    
person1=person('ghobad','soltani')
print(person1.name)
person1.name='Ghobad'
print(person1.showInfo())
print(100*"-")
print(person1.family)
person1.family='Soltani'
print(person1.showInfo())


# __eq__ METHOD
class Person:
    def __init__(self, name, family):
        self.__name=  name
        self._family = family
        
    def showInfo(self):
       print(self.__name)
       print(self._family)
    
    def __eq__(self,obj2):
        if not isinstance(obj2,Person):
            return False
        return self.__name==obj2.__name and self._family==obj2._family


    def __str__(self):
        return f"{self.__name}\t\t{self._family}"
    
    
class MyClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
person1=Person("ghobad",'soltani')
person2=Person("ahmad",'asgari')
person3=Person("ghobad",'soltani')
if person1==person3:
    print("yes")
else:
    print("no")

m1=MyClass('ahmad',30)

if person2==m1:
    print("yes")
else:
    print("no")


print(str(person1))
print(person1.__str__())
print(person1)


# hash function in classes
class Person:
    def __init__(self, name, family):
        self.__name=  name
        self._family = family
        
    def showInfo(self):
       print(self.__name)
       print(self._family)

    def __eq__(self,obj2):
        if not isinstance(obj2,Person):
            return False
        return self.__name==obj2.__name and self._family==obj2._family

    def __hash__(self):
        return hash(self.__name)-hash(self._family)



x=100
y='ghobad'
print(hash(x))
print(hash(y))

person1=Person('ghobad',32)
print(hash(person1))




#another axample

class Person:
    def __init__(self, name, family):
        self.__name=name
        self._family =family
        
    def showInfo(self):
       print(self.__name)
       print(self._family)

    def __eq__(self,obj2):
        if not isinstance(obj2,Person):
            return False
        return self.__name==obj2.__name and self._family==obj2._family

    def __hash__(self):
        return hash(self.__name)-hash(self._family)
    
    def __str__(self):
        return f"{self.__name}\t\t{self._family}"
    
    
person1=Person('ghobad','soltani')
person2=Person('ahmad','asgari')
person3=Person('ghobad','soltani')
person4=Person('arash','heidari')
person5=Person('ahmad','soltani')

set1={person1,person2,person3,person4,person5}
for person in set1:
    print (person)



# abstraction in classes

from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,family):
        self.name=name
        self.family=family
    
    @abstractmethod          
    def showInfo(self):
        pass
        
class teacher(Employee):
    def __init__(self,name,family,id):
        Employee.__init__(self,name,family)
        self.id=id
        
    def showInfo(self):          #nesassary
        print(f'{self.name}\t\t{self.family}\t\t{self.id}')
        
  
  
class student(Employee):
    def __init__(self,name,family,address):
        Employee.__init__(self,name,family)
        self.address=address  

    def showInfo(self):           #nesassary
        print(f'Name is: {self.name}\t\t family is:{self.family}\t\t address is: {self.address}')
    
student1=student('ahmad','asgari','kerman')
teacher1=teacher('ghobad','soltani',253)
student1.showInfo()
teacher1.showInfo()
        
        






    