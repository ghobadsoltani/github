from datetime import time,datetime,timedelta
import pytz
from khayyam import *
print(datetime.today())
print(datetime.now())
print(datetime(1991,2,11))
print(datetime.year)
print(datetime.month)
print(datetime.day)
print(datetime.utcnow())
print(datetime.now().strftime("%y/%m/%d %H:%M:%S"))
date1=datetime.now().strptime("8/11/2022","%m/%d/%Y")
print(date1.day)
print(date1.month)
print(date1.year)

print(datetime.now(pytz.timezone("asia/Tehran")))
print(datetime.now(pytz.timezone("Us/central")))



date2=datetime(1991,2,11,2,45,31)
date3=datetime(2022,12,29,2,45,31)
timedelta1=timedelta(days=52,hours=12,minutes=52,seconds=28)
print(date2+timedelta1)
print(abs(date3-date2).total_seconds()/(60*60*24*365))


print(JalaliDate(2022,12,29))
print(JalaliDatetime(2022,12,29,23,7,50,3516))
print(JalaliDatetime.now())
print(JalaliDate.today)

datetime1=JalaliDatetime(1369,11,22)
print(datetime1.todate())         #convert jalali to miladi


# another modul for jalali date(JDATETIME)
import jdatetime
gregorian_date = jdatetime.date(1396,2,30).togregorian()            #convert jalali to miladi
jalili_date = jdatetime.date.fromgregorian(day=11,month=2,year=1991)               #convert miladi to jalali 
print(gregorian_date)
print(jalili_date)