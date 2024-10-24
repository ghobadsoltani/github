import operator
print(operator.add(659,525))       #adding
print(operator.sub(355,645))       #Subtraction
print(operator.mul(526,23))        #Multiplication
print(operator.truediv(36,5))      #division
print(operator.floordiv(32,3))     #rounded division
print(operator.mod(34,8))          #Modulus

print(operator.le(7,3))    #lower and equal
print(operator.ge(7,3))    #greater and equal
print(operator.eq(7,3))    #equality
print(operator.gt(7,3))    #greater than
print(operator.lt(7,3))    #lower than

print(operator.not_(False))
print(operator.not_(34>3))

print(operator.lshift(25,1))
print(operator.lshift(25,2))
print(operator.rshift(25,1))
print(operator.rshift(25,2))

list1=[23,65,98,99,84,52,65,91]
print(operator.contains(list1,65))
print(operator.contains("ghobad soltani","n"))

list1=[23,65,98,99,84,52,65,91]
operator.delitem(list1,3)
print(list1)

name1='ghobad soltani'
print(operator.countOf(name1,'o'))

list1=[23,65,98,99,84,52,65,91]
getter=operator.itemgetter(2)
print(getter(list1))

people=[('ali','soltani',44),('javad','soltani',46),('parisa','soltani',39),('jasem','soltani',38)]
print(sorted(people,key=operator.itemgetter(2),reverse=True))

# list1=[23,65,98,99,84,52,65,91]
# slicer=operator.slice(0,2)
# print(slice(list1))
