
try:
    x=int(input("enter NUMBER: "))
    y=int(input('enter Number: '))
    print(x/y)
    
    list1=[23,45,78,90,78]
    n=int(input('enter index: '))
    print(list1[n])
    f=open('D:/codding/file1.txt','r')
    print(f.readlines())
    
except ZeroDivisionError:
    print("Error123")
    
except FileNotFoundError:
    print('error2')

except IndexError:
    print('error3')
    
    
    
    
    
try:
    x=int(input("enter NUMBER: "))
    y=int(input('enter Number: '))
    print(x/y)
    
    list1=[23,45,78,90,78]
    n=int(input('enter index: '))
    print(list1[n])
    f=open('D:/codding/file1.txt','r')
    print(f.readlines())
    
except ZeroDivisionError:
    print("Error123")
    
except FileNotFoundError:
    print('error2')

except IndexError:
    print('error3')
    
else:
    print('ok')
    
finally:
    print('the end...')





def ageValidate(age):
    if not isinstance(age,int):
        raise RuntimeError('type is not valide...')
    if age<1 or 120<age:
        raise RuntimeError('out of range...')
    return age

try:
    age=ageValidate('34')
    print(f'age is : {age}')
except RuntimeError as error:
    print(error)


try:
    age=ageValidate(150)
    print(f'age is : {age}')
except RuntimeError as error:
    print(error)



try:
    age=ageValidate(50)
    print(f'age is : {age}')
except RuntimeError as error:
    print(error)









class MyException(Exception):
    def __init__(self,message):
        super().__init__(message)
        self.message=message
        
    def __str__(self):
        return 'error is: '+self.message
        
    def avgValidate(avg):
        if not isinstance(avg,float):
            raise MyException('type is not valide')
        if avg>0 or avg>20:
            raise MyException('out of range')
        return avg
    
    
try:
    avg=avgValidate(15.65)
    print(f'avg is : {avg}')
    
except MyException as error:
    print(error)
    
else:
    print('ok')

finally:
    print('the end ...')
    

        