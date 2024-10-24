import json
jsonString="""[
    {"id":1,"name":"ghobad","family":"soltani","age":32},
    {"id":2,"name":"ahmad","family":"asgari","age":31},
    {"id":3,"name":"arash","family":"heidari","age":30},
    {"id":4,"name":"ali","family":"soltani","age":42},
    {"id":4,"name":"jasem","family":"soltani","age":38},
    {"id":4,"name":"ehsan","family":"soltani","age":34}
]"""
obj1=json.loads(jsonString)
# for i in obj1:
#     print(i)
# for i in obj1:
#     print(type(i))
# for i in obj1:
#     print(type(i))
for i in obj1:
    print(obj1["name"])
    
    
    
    
with open("file1.json","r") as file1:   #نیازی نیست که نشانی اصلی را بیاوریم. اگر فایل در پوشه حال حاضر قرار دارد فقط نامش را می آوریم
    objectList=json.load(file1)
    print(objectList)
    print(type(objectList))
    print(objectList[0]['Name'])
        





jsonString=[
    {"Name":"Ahmad","Family":"Ghaderi","Mobile":"09123458765","Postal Code":1417466191,"city":"Tehran"},
    {"Name":"Zahra","Family":"Miraee","Mobile":"09367006534","Postal Code":1115586391,"city":"Tehran"},
    {"Name":"Ziba","Family":"Nalbandi","Mobile":"09356546534","Postal Code":3185679365,"city":"Isfahan"},
    {"Name":"Babak","Family":"Naimee","Mobile":"09121235678","Postal Code":1996715433,"city":"Tehran"},
    {"Name":"Fatemeh","Family":"Moradi","Mobile":"09133047777","Postal Code":8174673441,"city":"Isfahan" },
    {"Name":"Ahmad","Family":"Akbari","Mobile":"09123124455","Postal Code":1587544133,"city":"Tehran"}

]

# print(json.dumps(jsonString))           #تبدیل دیکشنری به یک متن جیسونی


with open("file2.json","w") as file2:      #اضافه کردن یک متن جیسونی به یک فایل 
    json.dump(jsonString,file2,indent=4)


person1={"id":1,"name":"ghobad","family":"soltani","age":32,"avg":16.78}
person2={"id":2,"name":"ahmad","family":"asgari","age":30,"avg":14.86}
people=[person1,person2]

print(json.dumps(people))

with open("file1.json","w")as file1:
    json.dump(people,file1,indent=4)
    

import demjson
#متدهای انکود برای تبدیل آبجکت به جیسون (معادل دامپ)
#متدهای دیکود برای تبدیل جیسون به آبجکت   (معادل سریالایز کردن)

class person:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def __str__(self):
        return f"id:{self.id}\tname:{self.name}\tage:{self.age}"
    
person1=person(26,"ghobad",32)
# jstr=demjson.encode(person1.__dict__)          #هم انود و هم دیکود ،دیکشنری را به صورت ورودی میپذیرند و با آوردن دیکت آبجکت را به آنها میدهیم که این حالت برای دامپ و دامپس هم صادق است
# print(jstr)



person2=person(36,"ahmad",30)
person3=person(56,"arash",30)
list1=[]
list1.append(person1.__dict__)
list1.append(person2.__dict__)
list1.append(person3.__dict__)
jstr=demjson.encode(list1)           #encoding
print(jstr)


list2=demjson.decode(jstr)                      #docoding
for i in list1:
    print(i)
    
    


import jmespath
people=[
    {
        "Name": "Ahmad",
        "Family": "Ghaderi",
        "age":25 , 
        "Mobile": "09123458765",
        "Postal Code": 1417466191,
        "city": "Tehran"
    },
    {
        "Name": "Zahra",
        "Family": "Miraee",
        "age":30 , 
        "Mobile": "09367006534",
        "Postal Code": 1115586391,
        "city": "Tehran"
    },
    {
        "Name": "Ziba",
        "Family": "Nalbandi",
        "age":52 , 
        "Mobile": "09356546534",
        "Postal Code": 3185679365,
        "city": "Isfahan"
    },
    {
        "Name": "Babak",
        "Family": "Naimee",
        "age":38 , 
        "Mobile": "09121235678",
        "Postal Code": 1996715433,
        "city": "Tehran"
    },
    {
        "Name": "Fatemeh",
        "Family": "Moradi",
        "age":44 , 
        "Mobile": "09133047777",
        "Postal Code": 8174673441,
        "city": "Isfahan"
    },
    {
        "Name": "Ahmad",
        "Family": "Akbari",
        "age":35 , 
        "Mobile": "09123124455",
        "Postal Code": 1587544133,
        "city": "Tehran"
    }
]

print(jmespath.search("people[?age>'40'].Name",people))
print(jmespath.search("people[1].Mobile",people))




