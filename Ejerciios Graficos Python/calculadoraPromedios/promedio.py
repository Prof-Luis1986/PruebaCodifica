import tkinter as tk
from tkinter import messagebox

def agregar_calificacion():
    try:
        calificacion = float(entrada_calificacion.get())
        if 0 <= calificacion <= 10:
            calificaciones.append(calificacion)
            lista_calificaciones.insert(tk.END, calificacion)
            entrada_calificacion.delete(0, tk.END)
        else:
            messagebox.showwarning("Valor inválido", "La calificación debe estar entre 0 y 10.")
    except ValueError:
        messagebox.showwarning("Entrada inválida", "Por favor ingresa un número válido.")

def calcular_promedio():
    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)
        etiqueta_resultado.config(text=f"Promedio: {promedio:.2f}")
    else:
        etiqueta_resultado.config(text="No hay calificaciones.")

def limpiar():
    calificaciones.clear()
    lista_calificaciones.delete(0, tk.END)
    etiqueta_resultado.config(text="Promedio:")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Promedios")
ventana.configure(bg="lightblue")
ventana.geometry("300x400")
ventana.resizable(False, False)

calificaciones = []

# Widgets
etiqueta_instruccion = tk.Label(ventana, text="Ingresa una calificación (0-10):")
etiqueta_instruccion.pack()

entrada_calificacion = tk.Entry(ventana)
entrada_calificacion.pack()

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_calificacion)
boton_agregar.pack()

lista_calificaciones = tk.Listbox(ventana)
lista_calificaciones.pack()

boton_promedio = tk.Button(ventana, text="Calcular Promedio", command=calcular_promedio)
boton_promedio.pack()

etiqueta_resultado = tk.Label(ventana, text="Promedio:")
etiqueta_resultado.pack()

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack()

ventana.mainloop()