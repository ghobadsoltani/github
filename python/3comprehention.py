# list comprehentions

list1=[]
for i in range(1,11):
    list1.append(i*i)
print(list1)


list1=[x*x for x in range(1,11)]
print(list1)


list1=[(x+100)*x for x in range(1,11)]
print(list1)



def fun1(n):
    y=n-1
    z=n+5
    return y+z-n

list1=[fun1(i) for i in range(1,11)]
print(list1)



list1=[10,20,30,40,50]
list2=[i*i*i for i in list1]
print(list2)


list1=[10,20,30,40,50]
list2=[i*i*i for i in list1 if i>20]
print(list2)




list1=[1,2,3,4,5,6,7,8,9]
list2=[i*i*i if i%2==0 else i+100 for i in list1]
print(list2)



# dictionary comprehentions

dic1={x:x*x for x in range(1,11)}
print(dic1)


dic1={x:str(x*x) for x in range(1,11)}
print(dic1)


def getColore(n):
    if n==1:
        return "blue"
    elif n==2:
        return "red"
    return "green"
list1=[1,2,2,3,4,5]
dic1={x:getColore(x) for x in list1}
print(dic1)



def getColore(n):
    if n==1:
        return "blue"
    elif n==2:
        return "red"
    return "green"
list1=[1,2,2,3,4,5]
dic1={x*x:getColore(x) for x in list1}
print(dic1)

zip
list1=[1,2,3,4,5,6]
list2=['ghobad','ahmad','arash','jasem','ali']
zip1=zip(list1,list2)
print(zip1)
print(type(zip1))

for key,value in zip1:
    print(f'{key} : {value}')



list1=[1,2,3,4,5,6]
list2=['ghobad','ahmad','arash','jasem','ali']
zip1=zip(list2,list1)
print(zip1)
print(type(zip1))

for key,value in zip1:
    print(f'{key} : {value}')




list1=[1,2,3,4,5,6]
list2=['ahmad','arash','jasem','ali']
zip1=zip(list1,list2)
print(zip1)
print(type(zip1))

for key,value in zip1:
    print(f'{key} : {value}')


list1=[1,2,3,4,5,6]
list2=['ghobad','ahmad','arash','jasem','ali']
dic1={key:value for key,value in zip(list1,list2)}
print(dic1)


# set comprehension

list1=[1,5,2,3,9,8,8,8,6,5,6]
set1={ x for x in list1}
set2={ x*x for x in list1}
print(list1)
print(set1)
print(set2)



# nested comprehansion

matrix=[]
for i in range(0,3):
    matrix.append([])
    for j in range(1,6):
        matrix[i].append(j)
print(matrix)


matrix=[[j for j in range(1,6)]for i in range(0,3)]
print(matrix)



def printrMatrix(matrix):
    for row in matrix:
        for col in row:
            print(col , end="\t")
        print()
        
matrix=[[j*i for j in range(1,11)]for i in range(1,11)]
printrMatrix(matrix)


def printr3D(m):
    for k in m:
        for row in k:
            for col in row:
                print(col , end="\t")
            print()
        print("********************************************")
        
m1=[[[k*j for k in range(1,11)] for j in range(1,11)]for i in range(1,11)]
printr3D(m1)




def printr3D(m):
    for k in m:
        for row in k:
            for col in row:
                print(col , end="\t")
            print()
        print("********************************************")
        
m1=[[[k for k in ['red', 'green', 'blue']] for j in range(1,11)]for i in range(1,3)]
printr3D(m1)

