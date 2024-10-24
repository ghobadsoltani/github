import collections
list1=[321,651,3215,64856,321,654,684,654,651,984,8974,561]
print(collections.Counter(list1))
print(collections.Counter(list1).most_common(3))

dic1=collections.defaultdict(object)
dic1['ahmad']=31
dic1['ghobad']=32
dic1['arash']=30
print(dic1)




dic1=collections.defaultdict(object)     #make empty dictionary
dic1['ahmad']=31
dic1['ghobad']=32
dic1['arash']=30
dic2=collections.OrderedDict(sorted(dic1.items(), key=lambda t: t[1],reverse=True))      #ordering dictionary
dic3=collections.OrderedDict(sorted(dic1.items(), key=lambda t: t[1]))                   #ordering dictionary
print(dic2==dic3)
print(dic2)

for k,v in dic2.items():
    print(f"{k} : {v}")

#chain map
d1={"x":"y","z":"w",'b':'c'}
d2={'t':100,"u":200,"i":300}
print(collections.ChainMap(d1,d2))



#named tupple
person=collections.namedtuple('person',"name age avg children")
person1=person('ghobad',32,16.67,['hamoon'])
person2=person('ahmad',31,15.69,['yashar'])
person3=person('arash',30,13.82,[])
person1.children.append('mahan')

for item in person._make(person2):
    print(item)
    
print(person1._asdict())
print(person2._asdict())
print(person3._asdict())

print(person1._fields)
print(person2._fields)
print(person3._fields)



#deque  (make que)
dq1=collections.deque([1,2,3])
dq1.append(4)
print(dq1)
dq1.appendleft(6)
print(dq1)
dq1.pop()
print(dq1)
dq1.popleft()
print(dq1)



#user changes in lists
list1=[321,651,3215,64856,321,654,684,654,651,984,8974,561]
list1.remove(8974)
print(list1)


class MyList(collections.UserList):
    def remove(self):
        raise RuntimeError('delete not allowed')
    
list1=MyList([321,651,3215,64856,321,654,684,654,651,984,8974,561])
print(list1)
list1.remove(684)                    #not allowed for remove
print(list1)
    


class MyString(collections.UserString):      #make a class for change in strings
    def remove(self,s):
        self.data=self.data.replace(s,"")
        
str1=MyString('ghobad soltani')
str1.remove('o')
print(str1)