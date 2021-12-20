import sqlite3
from sqlite3.dbapi2 import Error

def conexion(db):
    conn = None
    try:
        conn=sqlite3.connect(db)
    except Error as e:
        print (e)
    return conn

def registrarproducto(conn):
    
    print("introduzca un producto")
    producto = input();
    print ("introduzca la cantidad del producto")
    cantidad = input();
    print ("introduzca el numero de serie")
    nserie = input();
    data = (producto,cantidad,nserie)
    
    sql = ''' INSERT INTO inventario(producto,cantidad,nserie) VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

def editarproducto(conn):
    print ("introduzca el producto a editar")
    producto = input();
    print ("introduzca la cantidad")
    cantidad = input();
    
    sql = ''' UPDATE inventario SET cantidad = ? where producto = ? '''
    cur = conn.cursor()
    cur.execute(sql,(cantidad,producto))
    conn.commit()
    return cur.lastrowid
   
def eliminarproducto(conn):
    print ("introduzca producto a eliminar")
    producto = input();
    sql = ''' DELETE FROM inventario WHERE producto = ? '''
    cur = conn.cursor()
    cur.execute(sql,(producto,))
    conn.commit()
    return cur.lastrowid

def buscarproducto(conn):
    print ("introduzca producto a buscar")
    producto = input();
    sql = ''' SELECT * FROM inventario where producto = ? '''
    cur = conn.cursor()
    cur.execute(sql,(producto,))
    records = cur.fetchall()
    for row in records:
        print ("cantidad:", row [2])
    return cur.lastrowid

def main():
    database = r"C:/Users/Cristhian/Downloads/SQLiteStudio/prueba.db"
    conn = conexion(database)
    
    print ("INVETARIO DE PRODUCTOS");
    print ("Menu");
    print ("1 - Agregar Producto");
    print ("2  - Editar Prodcuto");
    print ("3  - Eliminar Producto");
    print ("4  - Buscar pruducto");
    print ("-----------------------------");
    print ("seleccione unas de las opciones anteriores");
    opciones = int(input());

    with conn:

        if opciones == 1:
            print ("Vamos agregar un producto");            
            registrarproducto(conn)
            
        if opciones == 2: 
            print ("Vamos a editar un producto");
            editarproducto(conn)

        if opciones == 3:
            print ("Vamos a eliminar una Palabra");
            eliminarproducto(conn)
        
        if opciones == 4:
            print ("Buscar significado");
            buscarproducto(conn)
    
        
        

if  __name__ == '__main__':
    main()