import prediccion as pred
import tkinter as tk

# Definimos la ventana y su tamaño
ventana = tk.Tk()
ventana.title("Predicción")
ventana.resizable(0,0)
ventana.geometry("500x350")

def mostrarPrediccion():
    # Pasamos los datos recogidos en elos entry a float
    plenght = float(e1.get())
    pwidth = float(e2.get())
    slenght = float(e3.get())
    swidth = float(e4.get())
    # Introducimos esos datos en el orden correcto en una matriz 2x2
    prueba = [[slenght, swidth, plenght, pwidth]]

    # Realizamos la predicción y la mostramos en la ventana
    res = pred.predecir(prueba)
    tk.Label(ventana, text=res).place(x=300, y=270)


tk.Label(ventana, text = "INGRESE LOS DATOS DE LA FLOR PARA REALIZAR SU PREDICCIÓN").place(x=75, y=20)
tk.Label(ventana, text = "Longitud del pétalo(cm): ").place(x=100, y=70)
tk.Label(ventana, text = "Ancho del pétalo(cm): ").place(x=100, y=120)
tk.Label(ventana, text = "Longitud del sépalo(cm): ").place(x=100, y=170)
tk.Label(ventana, text = "Ancho del sépalo(cm): ").place(x=100, y=220)

# Entrada de datos
e1 = tk.Entry(ventana)
e1.place(x=300, y=70)
e2 = tk.Entry(ventana)
e2.place(x=300, y=120)
e3 = tk.Entry(ventana)
e3.place(x=300, y=170)
e4 = tk.Entry(ventana)
e4.place(x=300, y=220)

# Botón que activa la función para predecir los datos y mostrar el resultado
tk.Button(ventana, text="Predecir", fg="White", bg="green", command=mostrarPrediccion).place(x=130, y=270)

ventana.mainloop()