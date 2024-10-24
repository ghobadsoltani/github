import re
str="""
Name:Ahmad,Family:Ghaderi,Mobile:09123458765,Postal Code:1417466191,city:Tehran,Mailing Address: No.29 Ardeshir Alley Hashtbehesht St. Golha Square Dr. Fatemi St.
Name:Zahra,Family:Miraee,Mobile:09367006534,Postal Code:1115586391,city:Tehran,Mailing Address:No.18 4th Bahman St. North Kanal Ab St. Khavaran Rd. Khatoun Abad.
Name:Ziba,Family:Nalbandi,Mobile:09356546534,Postal Code:3185679365,city:Karaj,Mailing Address:No.49 Razi St. Haft_e_Tir crossroad.
Name:Fatemeh,Family:Moradi,Mobile:09133047777,Postal Code:8174673441,city:Isfahan,Mailing Address:No. 510 3rd Fl. Kowsar Trading Complex Beginning of Chahar Bagh Bala. 
Name:Ahmad,Family:Akbari,Mobile:09123124455,Postal Code:1587544133,city:Tehran,Mailing Address:No.51 Safi Alley Sattar Khan Ave. Tohid Sq.
Name:Reza,Family:Rafiee,Mobile:09121446216,Postal Code:3225639365,city:Tehran,Mailing Address:No. 5 Niam St. Dr. Shariati Ave.
Name:Hossien,Family:Saai,Mobile:09130123993,Postal Code:8165673242,city:Isfahan,Mailing Address:No. 132 Azadi St. Hezar Jarib St. 
Name:Asghar,Family:Hossaini,Mobile:09131170730,Postal Code:8171663343,city:Isfahan,Mailing Address:No. 159 Mir St.
Name:Masoud,Family:Sorami,Mobile:09122122962,Postal Code:1465865163,city:Tehran,Mailing Address:No.26 Tavanir Ave. Vali-e-Asr Ave.
Name:Amir,Family:Hajamini,Mobile:09121303804,Postal Code:1585988713,city:Tehran,Mailing Address:No.5 Farivar Alley Ghaem Magham Street.
Name:Lida,Family:Abedi,Mobile:09142418085,Postal Code:5166616471,city:Tabriz,Mailing Address:No.47 Kamyar Takhti St. Valiasr. 
Name:Babak,Family:Hamedi,Mobile:09141149921,Postal Code:5163315441,city:Tabriz,Mailing Address:No.21 St. Salimi Industrial town. 
"""

res=re.search(r'm.?\s',str)
print(res)                                  #چاپ موقعیت عبارت در رشته
print(res.group())                      #چاپ خروجی به صورت رشته
print(re.findall(r'm.?\s',str))
phone=re.findall(r'09\d{9}',str)          #تمامی شماره های موبایل درون متن
print(phone)             

emails=re.findall(r'\w+\@.+\..{2,3}',str)          #پیدا کردن ایمیلها
print(emails)

emails=re.findall(r'\[A-Za-z]+\@.+\..{2,3}',str)          #پیدا کردن ایمیلهایی که با حرف شروع می شوند
print(emails)



phone=re.finditer(r'09\d{9}',str)          #  تمامی شماره های موبایل درون متن که خروجی به صورت کالیبل می باشد
for item in phone:
    print(item.group())   
    
res=re.sub(r'09\d{9}','####\s',str)             #برای جایگزین کردن یک متن به جای متن دیگراستفاده می شود
print(res)                                         #چارامتر اول متن جستجو و پارامتر دوم متن جایگزین و مورد سوم متن اصلی است



res="Name,Family,Mobile,Postal Code,city,Mailing address"          #ایجاد گروه بندی در جستجو ها و ذخیره به صورت فایل سی اس وی که با اکسل بازش کنیم
res+=re.sub(r'Name is:(\w+)-Family is:(\w+)-Mobile is:(\d+)-Postal Code is:(\d{10})-city is:(\w+)-Mailing address is:(.+)','g<1>,g<2>,g<3>,g<4>,g<5>,g<6>',str)
with open("file1.csv","w")as file1:
    file1.write(res)
    
    
