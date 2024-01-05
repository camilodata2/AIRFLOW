import psycopg2

def conectar_bd():
    dbname = 'nombre_basedatos'
    user = 'usuario'
    password = 'contraseña'
    host = 'localhost'  # Puede cambiar dependiendo de la configuración de tu servidor PostgreSQL
    port = '5432'  # Puerto predeterminado de PostgreSQL
    """
    Esta es una forma muy util de usar la conexion a una base de datos,pero mi forma favorita es
    usando dbeaver
         """

    try:
        # Establecer la conexión a la base de datos
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

        # Retornar la conexión y un cursor
        return conn, conn.cursor()

    except psycopg2.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None, None

def main():
    conexion, cursor = conectar_bd()

    # Verificar si la conexión fue exitosa antes de utilizar el cursor
    if conexion and cursor:
        try:
            # Ejemplo: Ejecutar una consulta
            cursor.execute("SELECT * FROM tabla_ejemplo")

            # Obtener los resultados si es necesario
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        
        except psycopg2.Error as e:
            print("Error al ejecutar la consulta:", e)

        finally:
            # Cerrar el cursor y la conexión al terminar
            cursor.close()
            conexion.close()
    else:
        print("No se pudo establecer la conexión a la base de datos.")

if __name__ == "__main__":
    main()
