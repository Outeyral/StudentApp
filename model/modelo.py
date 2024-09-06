from database.conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion_db = ConexionDB('gestion_alumnos.db')
    try:
        # Comprobar si la tabla ya existe
        sql_check = "SELECT name FROM sqlite_master WHERE type='table' AND name='alumnos';"
        conexion_db.cursor.execute(sql_check)
        resultado = conexion_db.cursor.fetchone()

        if resultado:
            # La tabla ya existe
            print("La tabla 'alumnos' ya existe.")
        else:
            # Crear la tabla ya que no existe
            conexion_db.ejecutar_sentencia('''
                CREATE TABLE IF NOT EXISTS alumnos(
                    id_alumno INTEGER PRIMARY KEY,
                    nombre VARCHAR(100),
                    apellido VARCHAR(100),
                    genero VARCHAR(100),
                    edad INTEGER
                )
            ''')
            titulo = 'Tabla creada'
            mensaje = 'La tabla alumnos se ha creado correctamente'
            messagebox.showinfo(titulo, mensaje)

    except Exception as e:
        titulo = 'Error'
        mensaje = f'Ha ocurrido un error al crear la tabla: {e}'
        messagebox.showwarning(titulo, mensaje)
    finally:
        conexion_db.cerrar_conexion()

class Alumno:
    def __init__(self, nombre, apellido, genero, edad) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.edad = edad

    def __str__(self) -> str:
        return f'Alumno[Nombre: {self.nombre}, Apellido: {self.apellido}, Género: {self.genero}, Edad: {self.edad}]'

def guardar(alumno):
    conexion_db = ConexionDB('gestion_alumnos.db')
    try:
        sql = '''
            INSERT INTO alumnos (nombre, apellido, genero, edad)
            VALUES (?, ?, ?, ?)
        '''
        conexion_db.cursor.execute(sql, (alumno.nombre, alumno.apellido, alumno.genero, alumno.edad))
        conexion_db.commit()  # Asegúrate de que esto llama al método commit
        titulo = 'Datos guardados'
        mensaje = 'Los datos del alumno se han guardado correctamente'
        messagebox.showinfo(titulo, mensaje)
    except Exception as e:
        titulo = 'Error'
        mensaje = f'Ha ocurrido un error al guardar el alumno: {e}'
        messagebox.showerror(titulo, mensaje)
    finally:
        conexion_db.cerrar_conexion()


def consultar():
    conexion = ConexionDB('gestion_alumnos.db')
    sql = 'SELECT * FROM alumnos'
    try:
        datos = conexion.consultar_datos(sql)
        return datos
    except Exception as e:
        titulo = 'Error'
        mensaje = f'Ha ocurrido un error al consultar los registros: {e}'
        messagebox.showerror(titulo, mensaje)
        return []
    finally:
        conexion.cerrar_conexion()

def listar():
    conexion = ConexionDB('gestion_alumnos.db')
    try:
        conexion.cursor.execute("SELECT * FROM alumnos")
        alumnos = conexion.cursor.fetchall()
        return alumnos
    except Exception as e:
        messagebox.showerror('Error', f'Ha ocurrido un error al listar los alumnos: {e}')
        return []
    finally:
        conexion.cerrar_conexion()

def editar(alumno, id_alumno):
    conexion = ConexionDB('gestion_alumnos.db')
    try:
        sql = '''
            UPDATE alumnos
            SET nombre = ?, apellido = ?, genero = ?, edad = ?
            WHERE id_alumno = ?
        '''
        conexion.cursor.execute(sql, (alumno.nombre, alumno.apellido, alumno.genero, alumno.edad, id_alumno))
        conexion.commit()
        messagebox.showinfo('Datos actualizados', 'Los datos del alumno se han actualizado correctamente')
    except Exception as e:
        messagebox.showerror('Error', f'Ha ocurrido un error al editar el alumno: {e}')
    finally:
        conexion.cerrar_conexion()

def eliminar(id_alumno):
    conexion = ConexionDB('gestion_alumnos.db')
    try:
        sql = 'DELETE FROM alumnos WHERE id_alumno = ?'
        conexion.cursor.execute(sql, (id_alumno,))
        conexion.commit()
        messagebox.showinfo('Registro eliminado', 'El registro del alumno se ha eliminado correctamente')
    except Exception as e:
        messagebox.showerror('Error', f'Ha ocurrido un error al eliminar el alumno: {e}')
    finally:
        conexion.cerrar_conexion()
