

==================================================

w=float(input("enter your score :"))
if w>=18:
    print("exclent")
elif w>=15 and w<18 :
    print("very good")
elif w>=13 and w<15:
    print ("good")
elif w>=10 and w<13:
    print("not good")
else:
    print("youn loos")


if w>=15: print("very good")
print("very good") if w>=15 else print ("you felt") 



x=input("enter your age:")
match x:
    case "28":
        print("you have to marry")
    case "25":
        print("you have to find a job")
    case "19" :
        print("you have to go university")
    case '18':
        print ('you have to go soldiary')
    case _:
        print("you have to decide")
            
            
            
for x in range(1,12,2):
    print("hi")



c=0
Num=int(input("enter your score:"))
while Num>20:
    m=Num//10
    c+=1
    print(m)
    Num=int(input("enter your score:"))
print(f"your repetition number is: {c+1}")




#13
for i in range(1,80):
    if i/4==3:
        print("yes")
        continue
    if i/7==6 :
        break
    print(i)
    
    
#14
list1=["sdf",'df','dfg','g','dfg','fg','dfg','g','fgh','fgh','sdf','tyuj','io','rth','fg','sf','asd','ae','asd','dfg','dfhy','ghj','ytu']

list1.append('dfsdf')
list1.extend(['dsv','sfsdcx','fggh','fghh','ghjh'])
print(len(list1))
list1.remove('ytu')
print(list1)
print('*'*20)
print(list1.count('fgh'))
print(list1)
print(len(list1))



str="ghobad soltani ghaleh"
list2=list(str)
for i in list2:
    if i=="g":
        i='G'
    if i=="s":
        i="S"
    print (i)


temp=list(str)
temp=' '.join(temp)
print(temp)
    


#16
tuple1=('dfkjgsklas','ldkpsaodfjls','dmfasdljbfhj','adbfkjsadfnlza')
print(tuple1[1][5])



#17
set1={'xdfh',321,'zxdfg',6541,'hjk','ghjl',32546,'sdfg','fghk'}
set1.add('dfhreft')
set1.remove(321)
print(set1)




# 18
dict1={"ghobad":20,'ahmad':18 , "arash": 15}
print(dict1["ghobad"])
dict1['ahmad']=19
print(dict1["ahmad"])      
print(dict1.keys())        #>list
print(dict1.values())      #>list
print(dict1.items())       #>tuple
print(dict1.get('arash'))


#19
def SumAvg(a,b,c,d):
    s=a+b+c+d
    avg=s/4
    print(f'{s},,,{avg}')          # and return

SumAvg(15,26,58,43)


# 20
def div(a,b=3):       #3default
    if a/b>1:
        print(f"{a}>{b}")
    else:
        print(f'{a}<{b}')
    
div(8)



list1=[31,546,6489,74564,133516,64894,65,5,689]
def showList(list):
    for i in list:
        print(i, end='\t')
showList(list1)





more excercise needed (the code is wrong)

import random

dfg=('51654','56','44','864','64651','54','1564','47565','468','4984','651','684','8946')

def fun1(*args):
    a= random.randint(*args)
    print(a)
    
fun1(dfg,1)


21 lambda      funName= lambdaInputs : mainFunction
name=lambda a,b,c:a*b*c
print (name(25,36,14))




toodartoo functions

def AB(c,d):
    print(c*d)

def EF(g,h,AB):
    AB(g,h)

EF(40, 20, AB)
    
toodartoo lambda
fun=lambda x,y,funcName:funcName(x,y)
print(fun(100,40,lambda num1,num2:num1*num2))

=
print=(lambda x,y,funcName:funcName(x,y)(100,40,lambda num1,num2:num1*num2))




names=('ghobad','ahmad','arash','jasem','ali','ehsan','javad')
print(sorted(names,key=lambda x:x[2:]))


22  built in functions for integers
sum()
max(list)
min(list)
print(pow(2,3))         #8
print(abs(-6589))        #6589
range()

23        functions for strings
str="sldfgjlmadleofs   "
print(str.title())    #capital the first character
print(len(str))
print(str.upper())
print(str.lower())
f=(str.split("l"))        #list
for i in f:
    print(' '.join(i))

print(str.startswith("sldf"))
print(str.endswith("sldf"))
print(str.strip())      #delet spece from begin and end
print(str.ljust(20,'u'))
print(str.rjust(20,'u'))
print(str.center(30,'u'))


print(str.isdigit())
print(str.isnumeric())



# 24   functions for lists
list1=['fgh','dfh','sert','dfhg','dfh','rtqew','tyjj']
list2=[325,326,3548,35354,6546,987,321]
print(list2.reverse())
print(sorted(list1))
print(sorted(list2))
print(list1.count('dfh'))
print(list1.pop())
list1.remove('fgh')
print(list1)
list2.append(353555)
print(list2)
list1.extend(list2)
print(list1)
print(list1.index(321))


25 functions for tuples
tuple1=('sdf','sfso','skdjf','epot','rthk','gfjn','adlk','sdflkmf',5654,984,321,654,98,123,684,684)
print(tuple1.count('sdf'))
print(tuple1.index('adlk'))


    #   functions for sets
set1={'XDFBH','FCGJ','GHJ','ZDSGR','FGJ','JK','GHJ','RTHYS','DSRHYH','SDA','DFHY','TGYIFD','DSGS','ESRTS'}
set2={'FGYJFD','CFGH','FGYJ','SDRG','FGK','XFGH','CGHK','XFGJ','DSRHYH','XFGJH','DFH','XFGNJH','GFHK','ECRTS'}
print(set1.difference(set2))
print("*"*50)
print(set1.union(set2))
print("*"*50)
print(set1.intersection(set2))
print("*"*50)
print(set1.issubset(set2))


#   functions for dictionaries
dic1={'fdfd':24635,'cfhg':74856,'dfhg':3553,'fgkh':5435,'ghgd':4312,'xcfb':453,'dghk':435,'sdrt':4534,'dfgh':4352,'sdfgas':453,}
print(dic1.get('xcfb'))
print(dic1.keys())
print(dic1.values())
print(dic1.items())



# class and herritance
class car:
    def __init__(self,brand,color,weight):
        self.brand=brand
        self.color=color
        self.weight=weight
    
    def __str__(self):
        return f"{self.brand} , {self.color} , {self.weight}"
    
    
# car1=car('pegout206','white',  1200)
# print(car1)

class Benz(car):
    def __init__(self,brand,color,weight,model,cylender,maxSpeed):
        super().__init__(brand,color,weight)
        self.model=model
        self.cylender=cylender
        self.maxSpeed=maxSpeed
        
        
    def luxury(brand):
        if brand=="benz" :
            return f"This is a lux car"
        else:
            return f'This car is cheap'
    def sport(cylender , maxSpeed):
        if cylender>=6 and maxSpeed>=300:
            return f'this car is sport'  
        else:
            return f'This car is not sport' 

car2=Benz("benz", "red" , 1380 , "se23" , 6 , 380)
print(car2)
print(Benz.luxury(car2))


# enum classes
import enum
class color (enum.Enum):
    red=1
    blue=2
    green=3
    white=4
    black=5
    yellow=6

print(color.blue.value)



#modules
import random          #for example we bring re for excercise and bring some of its modules
import math            #or we can bring our madule that exist in another file  >> myModule.func1(inputs)
import datetime
print(datetime.datetime.now())
print(math.log(53))
print(random.randint(1,100))



# work with files
file1=open("C:/Users/Ghobad/Desktop/New Text Document.txt", "r")    #r=read , w=write , a=append , x=creat new file
str=file1.read()
print(str)


import os     #for checking if file is in the specific path
if os.path.exists("C:/Users/Ghobad/Desktop/New Text Document.txt"):
    print('file is exist')
    
file1.close()





