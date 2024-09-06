import tkinter as tk
from client.vista import Frame
from model.modelo import crear_tabla

def main():
    """
    Función principal para iniciar la aplicación de gestión de alumnos.

    Esta función configura la ventana principal de la aplicación utilizando tkinter,
    crea la tabla de alumnos en la base de datos (si no existe) y lanza la interfaz
    gráfica de usuario.

    La ventana de la aplicación se configura con un tamaño de 1080x600 píxeles,
    un fondo de color azul claro, y tiene un margen de 30 píxeles a los lados y
    10 píxeles en la parte superior e inferior. La ventana no es redimensionable.

    Se llama a la función `crear_tabla` para asegurar que la tabla de alumnos
    existe en la base de datos antes de iniciar la aplicación.

    Finalmente, se crea una instancia de la clase `Frame` que define la interfaz
    gráfica y se inicia el bucle principal de la aplicación con `mainloop()`.
    """
    root = tk.Tk()
    root.title('Gestión de Alumnos')
    root.geometry('800x600')
    root.configure(bg='#ADD8E6', padx=30, pady=10)
    root.resizable(0, 0)

    # Creamos la tabla antes de iniciar la aplicación
    crear_tabla()

    # Inicializamos y ejecutamos la interfaz gráfica de la aplicación
    app = Frame(root)
    app.mainloop()

if __name__ == '__main__':
    main()
