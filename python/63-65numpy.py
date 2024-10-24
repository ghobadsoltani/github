import numpy as np
list1=[1,2,3,4,5,6,7,8,9]
tuple1=("a","b","c","d","e","f")
arr1=np.array(list1)
# print(arr1)
arr2=np.array(tuple1)
# print(arr2)

list2=[[1,2,3],[4,5,6],[7,8,9]]
arr3=np.array(list2)
# print(arr3)

# print(100*"=")
list3=[[[1,2,3],[4,5,6],[7,8,9]],[[21,22,23],[25,26,27],[28,29,30]]]
arr4=np.array(list3)
# print(arr4)

# number of dimentions
print(arr1.ndim)    #1
print(arr2.ndim)    #1
print(arr3.ndim)    #2    
print(arr4.ndim)    #3

print(list2[1][2])    #6
print(arr3[2][0])    #7
print(arr4[1,1,2])    #1


print(arr4[1,1:3])       #[[25 26 27] \n [28 29 30]]

print(arr4[0:1,1:2])       #[[[4 5 6]]]

print(arr4[0,1:,1:3])       #[[5 6] \n [8 9]]
 
print(arr4.dtype)
  

newArr4=arr4.astype('float64')
print(newArr4)



arr1=np.array([1,2,3,4,5])
arr2=arr1.copy()
arr1[0]=100
print(arr1)
print(arr2)


arr1=np.array([1,2,3,4,5])
arr2=arr1.view()
arr1[0]=100
print(arr1)
print(arr2)



print(arr4.shape)
print(arr3.shape)

print(arr4.reshape(2,9))
print(arr4.reshape(3,6))
print(arr4.reshape(-1))


arr1=np.array([[12,3,54],[45,654,8452],[526,54,84],[54,3269,9415]])
for row in arr1:
    for col in row:
        print(col, end='\t')
    print()


arr1=np.array([[12,3,54],[45,65,84],[52,54,84],[54,32,95]])
arr2=np.array([[52,55,45],[55,28,54],[54,85,71],[59,54,57]])
arr3=np.concatenate((arr1,arr2))
print(arr3)



arr1=np.array([[12,3,54],[45,65,84],[52,54,84],[54,32,95]])
arr2=np.array([[52,55,45],[55,28,54],[54,85,71],[59,54,57]])
arr3=np.concatenate((arr1,arr2), axis=1)
print(arr3)
print(20*'-')
print(arr3.reshape(4,6))
print(arr3.reshape(3,8))


print(20*'-')
arr4=np.stack((arr1,arr2))
print(arr3)
print(20*'-')
print(arr3.shape)
print(20*'-')
print(arr3.reshape(3,8))

