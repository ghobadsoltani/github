from mysql.connector import connect,Error
try:
    with connect(host='localhost',user='root',password='Qwqw1212') as db:
        mycursor=db.cursor()
        mycursor.execute('SHOW DATABASES')
        for database in mycursor:
            print(database)
        # mycursor.execute('Drop database dbtest')
        mycursor.execute('create Database dbTest')
        print('database created...')
        
except Error as error:
    print(error)
    
    
