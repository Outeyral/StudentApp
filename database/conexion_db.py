import sqlite3
import os

class ConexionDB:
    """
    Clase para manejar la conexión y las operaciones con la base de datos SQLite.

    Esta clase proporciona métodos para conectar, ejecutar sentencias SQL, 
    consultar datos y cerrar la conexión a una base de datos SQLite.

    Attributes:
        alumnos_db (str): Ruta completa al archivo de la base de datos SQLite.
        conexion (sqlite3.Connection): Objeto de conexión a la base de datos SQLite.
        cursor (sqlite3.Cursor): Cursor para ejecutar comandos SQL.
    """

    def __init__(self, nombre_db):
        """
        Inicializa la clase ConexionDB creando una conexión a la base de datos SQLite.

        Args:
            nombre_db (str): Nombre del archivo de la base de datos SQLite.
        """
        directorio_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        carpeta_db = os.path.join(directorio_raiz, 'database')

        if not os.path.exists(carpeta_db):
            os.makedirs(carpeta_db)

        self.alumnos_db = os.path.join(carpeta_db, nombre_db)
        self.conexion = sqlite3.connect(self.alumnos_db)
        self.cursor = self.conexion.cursor()

    def cerrar_conexion(self):
        """
        Cierra la conexión a la base de datos SQLite.
        """
        if self.conexion:
            self.conexion.close()

    def commit(self):
        """
        Realiza un commit de la transacción actual en la base de datos.
        """
        self.conexion.commit()

    
