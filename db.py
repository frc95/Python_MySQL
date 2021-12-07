import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='prueba'
)

#cursor nos permite interactuar con la base en lenguaje mysql
cursor = midb.cursor()


#Listar datos
#cursor.execute('select * from Usuario')
#resultado = cursor.fetchall() #devuleve todas las instancias de los elementos que encontro en la base
#resultado = cursor.fetchone() #devuelve el primer elemento
#print(resultado)


#Limitando los resultados
cursor.execute('select * from Usuario limit 2')
resultado = cursor.fetchall() #devuleve todas las instancias de los elementos que encontro en la base
#resultado = cursor.fetchone() #devuelve el primer elemento
print(resultado)


#ver definiciones de tablas
#cursor.execute('show create table Usuario')


#Insertar datos
#sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)'
#values = ('micorreo@gmail.com', 'nombreUsuario', 45)


#Actualizar datos
#sql = 'update Usuario set email = %s where id = %s'
#values = ('micorreo@correo.com',4)


#Eliminar datos
#sql = 'delete from Usuario where id = %s'
#values = (4, )

#El codigo de abajo siempre se utilizara para insert update y delete
#cursor.execute(sql, values)
#midb.commit()
#print(cursor.rowcount)

