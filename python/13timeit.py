import timeit
# روش اول
startTime=timeit.default_timer()
x=900*3000+10000
endTime=timeit.default_timer()
print(endTime-endTime)


#روش دوم
#محاسبه زمان انجام عملیات توسط چهار ورودی
codeSetup='import random'
mycode="""""
def fun1():
    return  random.randint(0,100)
"""
    
print(timeit.timeit(setup=codeSetup,stmt=mycode,number=20))



def checkprofit(n,m):
    for i in range(n):
        a=m*0.15
        m+=a
    return f" dollars={m} ,toman= {m*40000}" 

    
print(checkprofit(10,100))





#map , filter and reduce               میتوانند در جای مناسب سرعت عمل کدنویسی را بالا ببرند

#map             cook , [cow . potato . chiken  . maz]   >>>>>>> [burger . chiken fries . potato fries . pop corn]
def fun1(n):
    return n*n*n
list1=[1,6,8,5,3,856,455,863]
print(list(map(fun1,list1)))                   #مپ دارای دو ورودی است که اولی تابع مورد نظر(که میتواند تابع لامبدا باشد) و دومی یک iterable

print(list(map(lambda x:x*x*x,list1)))



# map for many lists
list2=[12,16,18,12,15,19]
list3=[16,20,20,18,16,18]
def fun2(*args):
    return sum(args)/len(args)
print(list(map(fun2,list2,list3)))     #[14.0, 18.0, 19.0, 15.0, 15.5, 18.5]



#filter               از لیست آنهایی را برمیگرداند که در تابع مورد نظرمان صادق باشند
def fun1(n):
    return n%3==0
list1=[32515,654,8941,9874153,32165,984685,3213516,984946,651588]
print(list(filter(fun1,list1)))
print(list(filter(lambda x:x>10,list1)))


list2=['ghobad','32148','ahmad','32165',"arash",'321']
print(list(filter(lambda x:x.isalpha(),list2)))
print(list(filter(lambda x:x.isnumeric(),list2)))



list3=[3518,6848,357,3,6897684,9878456,987561,6548,9879,987456,354987]
print(list(filter(lambda x:str(x).find('7')!=-1,list3)))           #آنهایی را برمی گرداند که درونشان 7 دارند



#REDUCE                           کم کردن داده ها به تعداد کمتری که ارزش بیشتری دارند
from functools import reduce
list1=[321,654,98,321]
def fun1(x,y):
    return x+y
print(reduce(fun1,list1))
print(reduce(lambda x,y:x+y,list1))