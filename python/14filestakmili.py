#مفاهیم تکمیلی کار با فایلها
file1=open("file1.txt",'r')
print(file1.tell())                    #موقعیت حال حاضر در فایل را برمی گرداند
print(file1.readline())
print(file1.tell())

print(file1.seek(4,0))
print(file1.readline())

print(file1.read(5))
print(file1.name)
print(file1.mode)
print(file1.closed)
file1.close()
print(file1.closed)




#context manager
try:                                                          #کاربرد ترای برای مدیریت فضای مورد نیاز برنامه(پر کردن و آزاد کردن فضاها)
    with open("file1.txt",'r') as file1:
        print(file1.readline())
except Exception as error:
    print('Error:',error)
finally:
    file1.close
    
    
class FileWritable:
    def __init__(self,filepath):
        self.filepath=filepath
    def __enter__(self):
        self.fileObject=open(self.filepath, "w")
        return self.fileObject
    def __exit__(self,*exc):
        if self.fileObject==True:
            self.fileObject.close()
            

with FileWritable("file1.txt") as f1:
    f1.write('HELLO PYTHON')