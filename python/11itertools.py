import itertools
for i in itertools.count(0,8):
    if i >100:
        break
    print(i,end='   ')
    
    
counter=0
for i in itertools.cycle("Ghobad"):        #input has to be iterable
    if counter>15:
        break
    print(i , end="")
    counter+=1
    

for i in itertools.repeat("Ghobad",3):
    print(i , end= " ")
    
    
print(list(itertools.product([1,2,3],["a","b","c"])))       #ضرب دکارتی
print(list(itertools.product([1,2,3],repeat=2)))       #ضرب دکارتی در خود
print(list(itertools.product([1,2,3],'ali')))       #ضرب دکارتی در خود

print(list(itertools.permutations([1,2,3,4,5],3)))       # جایگشت

print(list(itertools.combinations([1,2,3,4,5],3)))       #ترکیب (رعایت ترتیب )

print(list(itertools.combinations_with_replacement([1,2,3,4,5],3)))       #ترکیب (رعایت ترتیب و با عناصر تکراری )


import operator
list1=[65,351,684,84,689]
list2=list(itertools.accumulate(list1,operator.add))
print(list2)
list2=list(itertools.accumulate(list1,operator.sub))
print(list2)
list2=list(itertools.accumulate(list1,operator.mul))
print(list2)
list2=list(itertools.accumulate(list1,operator.mod))
print(list2)



list1=[321,684,6851,3215,65848]
list2=["ghobad",'ahmad','arash']
list3=[1200,True]
list4=["ghobad"]
print(list(itertools.chain.from_iterable([list1,list2,list3,list4])))




print(list(itertools.compress('Ghobad soltani',[1,0,1,0,1,0,0,0,1,1,0,0,1,1])))    #گشتن در iterable و برگرداندن آنهایی که با 1 مطابقت دارند


list1=[321,683,6852,3215,65848]
print(list(itertools.dropwhile(lambda x :x%2==1,list1)))       #برگرداندن داده ها از اولین نادرست

print(list(itertools.takewhile(lambda x :x%2==1,list1)))       #برگرداندن داده ها تا اولین نادرست

print(list(itertools.filterfalse(lambda x :x%2==1,list1)))       #برگرداندن داده های نادرست با شرط ما



list1=[351,654,68,468,45,1,654,6,168,46,165,186,6]       
print(list(itertools.islice(list1 , 2 , 8 , 2)))        # ورودی ها به ترتیب منبع قابل شمارش و نقطه شروع و نقطه پایان و گام



