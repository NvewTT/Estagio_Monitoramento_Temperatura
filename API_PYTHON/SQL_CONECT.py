import mysql.connector
import json
class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)

def connect(Dados):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sensores"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO sensores (NOME, TEMP) VALUES (%s, %s)"
    val = (Dados[0], Dados[1])
    mycursor.execute(sql, val)

    mydb.commit()
    
def GetDados(Dados):
    print(Dados)
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sensores"
    )

    mycursor = mydb.cursor()
    sql = "SELECT * FROM sensores WHERE NOME = '"+ Dados +"'ORDER BY ID DESC"
    mycursor.execute(sql)
    records = mycursor.fetchmany(60)
    records.sort(key=lambda tup: tup[0]) 
    result = map(lambda x: x[2::1], records)
    
    return(json.dumps(tuple(result), cls=DatetimeEncoder))
    
    