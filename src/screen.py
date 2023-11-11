import tkinter as tk
from tkinter import messagebox
from game_resolver import resolve


def show(matriz):
    def update_lights():
        for row in range(filas):
            for col in range(columnas):
                if matriz[row][col] == 1:
                    canvas.itemconfig(shapes[row][col], fill='yellow')
                else:
                    canvas.itemconfig(shapes[row][col], fill='white')

    ventana = tk.Tk()
    ventana.title("Matriz resultado")

    # Definir el tamaño de la cuadrícula.
    filas = len(matriz)
    columnas = len(matriz)

    # Crear un lienzo (canvas) para mostrar las formas.
    canvas = tk.Canvas(ventana, width=1000, height=1000)
    canvas.pack()

    # Crear formas geométricas para representar las luces.
    shapes = [[None for _ in range(columnas)] for _ in range(filas)]
    espacio_entre_formas = 5
    for row in range(filas):
        for col in range(columnas):
            x1 = col * 80 + espacio_entre_formas * col
            y1 = row * 80 + espacio_entre_formas * row
            x2 = x1 + 80
            y2 = y1 + 80
            shapes[row][col] = canvas.create_rectangle(x1, y1, x2, y2, fill='white')
            canvas.tag_bind(shapes[row][col], '<Button-1>')

    # Inicializar la apariencia de las luces según la matriz dada.
    update_lights()

    # Ejecutar la aplicación.
    ventana.mainloop()


def open_screen(num):
    # Función para cambiar el estado de una luz y actualizar su apariencia.
    def toggle_light(row, col):
        lights[row][col] = 1 - lights[row][col]  # Cambiar entre 0 y 1
        update_lights()

    # Función para actualizar la apariencia de las luces en el lienzo.
    def update_lights():
        for row in range(filas):
            for col in range(columnas):
                color = 'yellow' if lights[row][col] == 1 else 'white'
                canvas.itemconfig(shapes[row][col], fill=color)

    # Crear la ventana de la aplicación.
    ventana = tk.Tk()
    ventana.title("Lights Out")

    def mostrar_solucion():
        vectorResulting = resolve(lights)
        matrizResulting = []
        for i in range(int(num)):
            matrizResulting.append([])
        i = 0
        d = 0
        for number in vectorResulting:
            matrizResulting[i].append(number)
            d += 1
            if d == (num):
                i += 1
                d = 0
        show(matrizResulting)

    resultado_boton = tk.Button(ventana, text="Mostrar Solución", command=mostrar_solucion)
    resultado_boton.pack()
    # Definir el tamaño de la cuadrícula y la cuadrícula de luces (ajusta según tus preferencias).
    filas = int(num)
    columnas = int(num)
    # Crear un lienzo (canvas) para mostrar las formas.
    canvas = tk.Canvas(ventana, width=1000, height=1000)
    canvas.pack()

    # Inicializar la matriz de luces (puedes configurarla según tus preferencias).
    lights = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Crear formas geométricas para representar las luces.
    shapes = [[None for _ in range(columnas)] for _ in range(filas)]
    espacio_entre_formas = 5
    for row in range(filas):
        for col in range(columnas):
            x1 = col * 80 + espacio_entre_formas * col
            y1 = row * 80 + espacio_entre_formas * row
            x2 = x1 + 80
            y2 = y1 + 80
            shapes[row][col] = canvas.create_rectangle(x1, y1, x2, y2, fill='white')
            canvas.tag_bind(shapes[row][col], '<Button-1>', lambda event, r=row, c=col: toggle_light(r, c))

    # Ejecutar la aplicación.
    ventana.mainloop()


def init():
    ventanaPrevia = tk.Tk()
    ventanaPrevia.title("Lights Out")

    etiqueta = tk.Label(ventanaPrevia, text="Ingresa el tamaño de la matriz:")
    etiqueta.pack()

    # Campo de entrada numérica.
    numero_entry = tk.Entry(ventanaPrevia)
    numero_entry.pack()

    def procesar_numero():
        numero = numero_entry.get()
        try:
            numero = float(numero)
            if numero.is_integer():
                ventanaPrevia.destroy()
                open_screen(numero)

        except ValueError:
            messagebox.showinfo("Error", "¡Ingresa un número válido!")

    # Botón para procesar el número.
    procesar_boton = tk.Button(ventanaPrevia, text="Procesar", command=procesar_numero)
    procesar_boton.pack()

    ventanaPrevia.mainloop()


init()
