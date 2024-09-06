import re
from tkinter import messagebox

def validar_entrada(nombre, apellido, edad):
    """
    Valida los datos de entrada del usuario.
    
    Args:
        nombre (str): Nombre del alumno.
        apellido (str): Apellido del alumno.
        edad (str): Edad del alumno.
        
    Returns:
        bool: True si todas las entradas son válidas, False en caso contrario.
    """

    if not re.match(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s-]+$', nombre):
        messagebox.showerror('Error', 'El nombre solo debe contener letras.')
        return False

    if not re.match(r'^[A-Za-záéíóúÁÉÍÓÚñÑ\s-]+$', apellido):
        messagebox.showerror('Error', 'El apellido solo debe contener letras.')
        return False

    if not re.match(r'^\d+$', edad):
        messagebox.showerror('Error', 'La edad solo debe contener números.')
        return False

    return True
