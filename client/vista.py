import tkinter as tk
from tkinter import ttk, messagebox
from client.utilities import validar_entrada
from model.modelo import Alumno, guardar, listar, editar, eliminar

class Frame(tk.Frame):
    """
    Clase que representa la interfaz gráfica para la gestión de alumnos.

    Args:
        root (tk.Tk): Ventana principal de la aplicación.
    """
    
    def __init__(self, root=None):
        """
        Inicializa la clase Frame.

        Configura la ventana principal y los componentes de la interfaz gráfica.
        """
        super().__init__(root, width=800, height=600)
        self.root = root
        self.configure(bg='lightblue')
        self.root.title('Gestión de Alumnos')
        self.pack()
        self.config(bg='#B0E0E6', padx=10, pady=10)

        self.selected_alumno_id = None

        self.campos_alumno()
        self.deshabilitar_campos()
        self.tabla_alumnos()

    def campos_alumno(self):
        """
        Configura los campos de entrada de datos y los botones de la interfaz gráfica.

        Este método crea y organiza los elementos de la interfaz gráfica, como entradas de texto y botones.
        """
        # Nombre
        self.label_nombre = tk.Label(self, text='Nombre:', bg='#B0E0E6')
        self.label_nombre.config(font=('Times New Roman', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        # Entrada Nombre
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(font=('Times New Roman', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        # Apellido
        self.label_apellido = tk.Label(self, text='Apellido:', bg='#B0E0E6')
        self.label_apellido.config(font=('Times New Roman', 12, 'bold'))
        self.label_apellido.grid(row=1, column=0, padx=10, pady=10)
        # Entrada Apellido
        self.entry_apellido = tk.Entry(self)
        self.entry_apellido.config(font=('Times New Roman', 12))
        self.entry_apellido.grid(row=1, column=1, padx=10, pady=10)
        # Género
        self.label_genero = tk.Label(self, text='Género:', bg='#B0E0E6')
        self.label_genero.config(font=('Times New Roman', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)
        # Entrada de Género es un Combobox
        self.combo_genero = ttk.Combobox(self, state='readonly')
        self.combo_genero.config(font=('Times New Roman', 12))
        self.combo_genero['values'] = ('Masculino', 'Femenino', 'Otro')
        self.combo_genero.grid(row=2, column=1, padx=10, pady=10)
        # Edad
        self.label_edad = tk.Label(self, text='Edad:', bg='#B0E0E6')
        self.label_edad.config(font=('Times New Roman', 12, 'bold'))
        self.label_edad.grid(row=3, column=0, padx=10, pady=10)

        self.entry_edad = tk.Entry(self)
        self.entry_edad.config(font=('Times New Roman', 12))
        self.entry_edad.grid(row=3, column=1, padx=10, pady=10)

        # Configurar botones #

        # Botón Agregar
        self.boton_agregar = tk.Button(self, text='Agregar', command=self.habilitar_campos)
        self.boton_agregar.config(width=15, height=2, font=('Times New Roman', 10, 'bold'), fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.boton_agregar.grid(row=4, column=0, padx=5, pady=10)
        # Botón Guardar
        self.boton_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.boton_guardar.config(width=15, height=2, font=('Times New Roman', 10, 'bold'), fg='#DAD5D6', bg='#1658A2', cursor='hand2', activebackground='#35BD6F')
        self.boton_guardar.grid(row=4, column=1, padx=5, pady=10)
        # Botón Cancelar
        self.boton_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.boton_cancelar.config(width=15, height=2, font=('Times New Roman', 10, 'bold'), fg='#DAD5D6', bg='#BD152E', cursor='hand2', activebackground='#35BD6F')
        self.boton_cancelar.grid(row=4, column=2, padx=5, pady=10)
        # Botón Editar
        self.boton_editar = tk.Button(self, text='Editar', command=self.editar_alumno)
        self.boton_editar.config(width=15, height=2, font=('Times New Roman', 10, 'bold'), fg='#DAD5D6', bg='#1658A2', cursor='hand2', activebackground='#35BD6F')
        self.boton_editar.grid(row=10, column=0, padx=5, pady=10)
        # Botón Eliminar
        self.boton_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_alumno)
        self.boton_eliminar.config(width=15, height=2, font=('Times New Roman', 10, 'bold'), fg='#DAD5D6', bg='#BD152E', cursor='hand2', activebackground='#35BD6F')
        self.boton_eliminar.grid(row=10, column=1, padx=5, pady=10)

    def habilitar_campos(self):
        """
        Habilita los campos de entrada para permitir la edición de datos.
        """
        self.entry_nombre.config(state='normal')
        self.entry_apellido.config(state='normal')
        self.combo_genero.config(state='readonly')
        self.entry_edad.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')
        self.boton_editar.config(state='disabled')
        self.boton_eliminar.config(state='disabled')

    def deshabilitar_campos(self):
        """
        Deshabilita los campos de entrada para evitar la edición de datos.
        También limpia los campos y reinicia los botones de acción.
        """
        self.entry_nombre.config(state='disabled')
        self.entry_apellido.config(state='disabled')
        self.combo_genero.config(state='disabled')
        self.entry_edad.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
        self.boton_editar.config(state='normal')
        self.boton_eliminar.config(state='normal')
        self.limpiar_campos()

    def guardar_datos(self):
        """
        Guarda los datos ingresados en los campos a la base de datos.
        
        Verifica si los datos son válidos y determina si se debe crear un nuevo registro o editar uno existente.
        """
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        genero = self.combo_genero.get()
        edad = self.entry_edad.get()

        # Validacion de campos a travès de REGEX (expresiones regulares) en utilities

        if not validar_entrada(nombre, apellido, edad):
            messagebox.showwarning('Advertencia', 'Todos los campos deben ser validos.')
            return 

        if not nombre or not apellido or not genero or not edad:
            messagebox.showwarning('Advertencia', 'Todos los campos deben estar llenos.')
            return

        # Comprobamos si estamos editando un alumno o creando uno nuevo en base al ID seleccionado
        if self.selected_alumno_id:
            # Estamos editando un alumno existente
            alumno = Alumno(nombre, apellido, genero, edad)
            editar(alumno, self.selected_alumno_id)  # Llamar a la función editar con el ID del alumno
        else:
            # Creando un nuevo alumno
            alumno = Alumno(nombre, apellido, genero, edad)
            guardar(alumno)  # Llamamos a la función guardar para crear un nuevo alumno

        self.limpiar_campos()
        self.tabla_alumnos()
        self.deshabilitar_campos()
        self.selected_alumno_id = None  # Reiniciamos el ID seleccionado después de guardar

    def limpiar_campos(self):
        """
        Limpia todos los campos de entrada en la interfaz gráfica.
        """
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido.delete(0, tk.END)
        self.combo_genero.set('')  # Limpiar el Combobox
        self.entry_edad.delete(0, tk.END)

    def tabla_alumnos(self):
        """
        Configura y llena la tabla de alumnos con los registros de la base de datos.
        """
        self.lista_alumnos = listar()

        if hasattr(self, 'tabla'):
            for row in self.tabla.get_children():
                self.tabla.delete(row)
        else:
            self.tabla = ttk.Treeview(self)
            self.tabla.config(columns=('nombre', 'apellido', 'genero', 'edad'))

            # Configuramos el ancho y centrado de la columna ID de forma individual
            self.tabla.column('#0', width=50, anchor='center')

            # Configuración del Scrollbar
            self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
            self.tabla.configure(yscrollcommand=self.scroll.set)

            # Configuración de la posición del Treeview y Scrollbar
            self.tabla.grid(row=6, column=0, columnspan=4, padx=5, pady=10, sticky='nsew')  # Colocar la tabla
            self.scroll.grid(row=6, column=4, sticky='ns')  # Colocar el scroll al lado derecho de la tabla

            self.tabla.heading('#0', text='ID')
            self.tabla.heading('nombre', text='Nombre')
            self.tabla.heading('apellido', text='Apellido')
            self.tabla.heading('genero', text='Género')
            self.tabla.heading('edad', text='Edad')

            # Ajustamos el ancho de las columnas para que ocupen el espacio disponible
            self.tabla.column('nombre', width=150, anchor='w')
            self.tabla.column('apellido', width=150, anchor='w')
            self.tabla.column('genero', width=100, anchor='w')
            self.tabla.column('edad', width=50, anchor='center')

        for alumno in self.lista_alumnos:
            self.tabla.insert('', 'end', text=alumno[0], values=(alumno[1], alumno[2], alumno[3], alumno[4]))

        # Para que la tabla pueda expandirse
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)


    def editar_alumno(self):
        """
        Permite editar los datos del alumno seleccionado en la tabla.

        Los datos del alumno seleccionado se cargan en los campos de entrada para su edición.
        """
        try:
            # Obtenevimos la ID del alumno seleccionado y los valores asociados a esa fila
            self.selected_alumno_id = self.tabla.item(self.tabla.selection())['text']
            alumno_info = self.tabla.item(self.tabla.selection())['values']

            # Comprobamos si se ha seleccionado una fila y que 'alumno_info' contiene datos
            if not alumno_info:
                raise IndexError("No se ha seleccionado ningún alumno.")

            # Habilitamos los campos para edición antes de insertar datos
            self.habilitar_campos()

            # Establecer los valores en los campos de entrada
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, alumno_info[0])  # Nombre

            self.entry_apellido.delete(0, tk.END)
            self.entry_apellido.insert(0, alumno_info[1])  # Apellido

            self.combo_genero.set(alumno_info[2])  # Género

            self.entry_edad.delete(0, tk.END)
            self.entry_edad.insert(0, alumno_info[3])  # Edad

        except IndexError:
            titulo = 'Error'
            mensaje = 'Debe seleccionar un registro para editar'
            messagebox.showerror(titulo, mensaje)
        except Exception as e:
            # Capturamos cualquier otro error que pueda ocurrir
            titulo = 'Error'
            mensaje = f'Error inesperado: {str(e)}'
            messagebox.showerror(titulo, mensaje)

    def eliminar_alumno(self):
        """
        Elimina el alumno seleccionado de la tabla y de la base de datos.

        Pide confirmación antes de eliminar el registro seleccionado.
        """
        try:
            alumno_id = self.tabla.item(self.tabla.selection())['text']
            titulo = 'Eliminar registro'
            mensaje = f'¿Está seguro de eliminar el registro {alumno_id}?'
            respuesta = messagebox.askyesno(titulo, mensaje)
            if respuesta:
                eliminar(alumno_id)
                self.tabla_alumnos()
        except IndexError:
            titulo = 'Error'
            mensaje = 'Debe seleccionar un registro para eliminar'
            messagebox.showerror(titulo, mensaje)
