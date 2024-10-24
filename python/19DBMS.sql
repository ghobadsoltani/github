--sql server 2019
use master
GO
Create Database SQLServer
--Create Database SQLServer
--	on (Name='MyDatabase',FileaName='D:\.........mdf, size=8MB)
--	Log on(Name='MyDatabase',FileaName='D:\........._Log.ldf, size=4MB
GO
use SQLServer
GO
--Drop database SQLServer

--Create Schema sch1

--Drop Schems sch1


Create Table States(
	stateCode int Primary Key NOT NULL,
	StateName NVarChar(30) NOT NULL
	)

Create Table Cities(
	CityCode Int Primary key NOT NULL Identity(1000,5),
	CityName NVarChar(30) NOT NULL,
	StateId Int NOT NULL ,
	Foreign Key(StateId) References States(stateCode)
	--constraint FK-Cities-StateId Foreign Key(StateId) References States(stateCode)
	--constraint unique-State-Name Unique(StateName)   قرار دادن یک فیلد به عنوا فیلد یونیک
	--constraint CK-StateCode check(1<[StateCode] AND [StateCode]<=40)   قرار دادن شرط برای یک فیلد با نام دلخواه	
	--on Update set NULL      --اگر در والد کلید خارجی حذف|تغییر کرد در فرزند هم حدف|تغییر کند
	--on Update set NULL     اگر در والد تغییر یا حذف شد در فرزند مقدار پیشفرض در فرزند وارد شود
	)

use SQLServer
GO
Insert INTO States(stateCode,StateName)
			Values(4,N'چهارمحال و بختیاری'),
				  ( 5,N'خوزستان'),
				  (6,N'ایلام'),
				  (7,N'اصفهان'),
				  (8,N'سیستان'),
				  (9,N'فارس')


Insert INTO Cities( [CityName], [StateId])
			Values(N'اهواز',5 ),
			(N'شهرکرد', 4),
			(N'ایلان',6 ),
			(N'فولادشهر', 7),
			(N'زاهدان', 8),
			(N'شیراز', 9),
			(N'آباده',9 )

select [stateCode], [StateName]
From States



select [CityCode], [CityName], [StateId]
From Cities


select *
From Cities



select  [CityName] as 'نام شهر' , [StateId] as 'کد استان'
From Cities


select Top(2) *
From Cities




use master
Drop database SQLServer

---------------------------------------------------------------------------------
Create Database Users
GO 
Use Users
GO 
Create Table PeopleGroup(
	peopleGroupId int PRIMARY KEY NOT NULL,
	PeopleGroupTitle NVarChar(300) NOT NULL
	)

GO 
INSERT INTO PeopleGroup(peopleGroupId,PeopleGroupTitle)
			Values(1,'دانشجویان'),
			(2,'مهندسین'),
			(3,'پزشکان'),
			(4,'معماران'),
			(5,'وکلا'),
			(6,'پرستاران'),
			(7,'فرهنگیان')



Create Table People(
	personId int Identity(100,1) NOT NULL,
	[Name] NVarChar(30) NOT NULL,
	Family NVarChar(30) NOT NULL,
	Age tinyint NULL,
	[Avg] decimal(4,2) NOT NULL,
	PhoneNumber char(15) NULL,
	PeopleGroupId int NULL ,
	Constraint PK_People PRIMARY KEY(personId),
	Foreign Key(personId) References PeopleGroup(peopleGroupId)
	--CONSTRANINT FK_People_PersonID forign  Key(PeopleGroupId) REFERENCES PeopleGroup(PeopleGrouoId)
	)
GO
INSERT INTO People
			Values(N'محمد',N'صاقی',23,17.25,'021-2351651',6),
				  (N'یاسی',N'شاه پیر',25,18.25,'031-3216541',2),
				  (N'یاشار',N'جانی',29,17.36,'0913-6359856',7),
				  (N'سارا',N'باقری',31,19.25,'0915-3527459',6),
				  (N'میترا',N'حجار',36,16.85,'0912-3654781',4),
				  (N'ساقی',N'حیدری',27,17.85,'0915-3541896',2),
				  (N'آرش',N'حیدری',31,15.84,'0913-2541879',3),
				  (N'قباد',N'سلطانی',32,16.84,'0913-6741920',1),
				  (N'احمد',N'عسگری',31,15.68,'0932-6851475',2),
				  (N'احسان',N'سلطانی',34,15.26,'0913-7013596',2),
				  (N'تیمور',N'نوربخش',33,15.24,'0913-6581234',5)




























	