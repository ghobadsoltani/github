import os
print(os.getcwd())                #نشان دادن مسیر پوشه موجود
if not os.path.exists('test1'):             # ایجاد یک پوشه جدید در مسیر حال حاضر اگر پوشه همنام آن موجود نباشد
    os.mkdir('test1')
    

os.chdir("../")                        #رفتن به یک پوشه عقب تر

print(os.getcwd())               

print(os.listdir())             #لیست پوشه های موجود در پوشه حال حاضر

for item in os.listdir():
    print(os.path.isdir(item))            #برگرداندن بولین برای پوشه های موجود در پوشه حاضر
    
    
for item in os.listdir():
    print(os.path.isfile(item))            #برگرداندن بولین برای فایلهای موجود در پوشه حاضر
    
    
    
print(os.path.basename('D:\codding\file1.txt'))            #برگرداندن  اسم یک فایل که برای ورودی به آن آدرس را میدهیم


print("=======================================")

print(os.path.dirname("D:\codding\python\codes"))        #برگرداندن نام پوشه های منتهی به مسیر ورودی 
print("=======================================")
print(os.path.normpath('D:\codding\file1.txt'))           #برگرداندن نام فایل حاضر و مسیر منتهی به آن
print("=======================================")

print(os.path.realpath('D:\codding\file1.txt'))          #آوردن نشانی کامل فایل
print("=======================================")

print(os.path.lexists('D:\codding\file1.txt'))           #برگرداندن بولین برای وجود یا عدم وجود مسیر آورده شده در ورودی
print("=======================================")

print(os.path.getctime('D:\codding\IMG_20171126_125805.jpg'))          #تعداد ثانیه از ساخته شدن فایل تا الان
from datetime import datetime
DATE=datetime.fromtimestamp(int(os.path.getctime('D:\codding\IMG_20171126_125805.jpg')))
print(DATE.strftime('%Y-%m-%d %H:%M:%S'))                       #تبدیل تعداد ثانیه به زمان تولید فایل
print("=======================================")

print(os.path.getmtime('D:\codding\IMG_20171126_125805.jpg'))    #زمان تا آخرین تغییرات بر روی فایل

print("=======================================")

print(os.path.getsize('D:\codding\IMG_20171126_125805.jpg'))      # برگرداندن سایز فایل موجود بر حسب بیت

print("=======================================")

print(os.path.join("c:/","windows","fonts"))                   #چسباندن چند نشانی به هم و ساخت یم نشانی جدید


print("=======================================")
s1=os.path.split("D:\TooshehFiles\log.txt")             #ساخت یک تاپل از نشانی فایل ورودی و جدا کردن هر قسمت از نشانی و دسترسی به هر کدام
print(s1)
print(s1[0])
print(s1[1])
print("=======================================")
s2=os.path.splitext("D:\TooshehFiles\log.txt")           #برگرداندن تاپلی که آخرین عضو آن پسوند فایل ورودی باشد
print(s2)
print(s2[1])            #دسترسی به اسم پسوند فایل ورودی

print("=======================================")
import mimetypes
print(mimetypes.MimeTypes().guess_type('IMG_20171126_125805.jpg')[0])        #بدست آوردن نوع فایل (عکس، موسیقی،فیلم و ...)

print("=======================================")

# os.remove('D:\codding\IMG_20171126_125805.jpg')                #حذف فایل با نشانی به عنوان ورودی

print("=======================================")
os.rmdir('D:/codding/test1')                               #حذف پوشه خالی 