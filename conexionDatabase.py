import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='Guerra11', host='127.0.0.1', database='covidDetector')
    cursor = cnx.cursor()

    query_data = (3,)
    query = (f"insert into persona (idPersona) values(10);")
    query1 = (f"SELECT * FROM persona;")
    
    cursor.execute(query, query_data, query1)



except mysql.connector.Error as err:

  if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
    
finally:
  cnx.close()
