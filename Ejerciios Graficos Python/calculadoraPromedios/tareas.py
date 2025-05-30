import tkinter as tk
from tkinter import messagebox, font

def agregar_tarea():
    tarea = entrada.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Escribe una tarea antes de agregar.")

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)
    else:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def marcar_completada():
    seleccion = lista_tareas.curselection()
    if seleccion:
        tarea = lista_tareas.get(seleccion)
        if not tarea.startswith("✔️"):
            lista_tareas.delete(seleccion)
            lista_tareas.insert(seleccion, f"✔️ {tarea}")
            lista_tareas.itemconfig(seleccion, fg="gray")
    else:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def salir():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("420x550")
ventana.configure(bg="#f4fff4")  # Verde muy claro

fuente_boton = font.Font(family="Arial", size=14, weight="bold")
fuente = font.Font(family="Arial", size=12)

entrada = tk.Entry(ventana, width=28, bg="#e8f5e9", fg="#145a32", font=fuente, relief="flat", highlightthickness=2, highlightbackground="#b2dfdb")
entrada.pack(pady=(30,10))

btn_agregar = tk.Button(
    ventana, text="Agregar tarea", command=agregar_tarea,
    bg="#e0f2f1", fg="#145a32", font=fuente_boton, relief="raised", bd=2, padx=10, pady=10, activebackground="#b2dfdb"
)
btn_agregar.pack(pady=(0,10))

lista_tareas = tk.Listbox(
    ventana, width=40, height=10, bg="#ffffff", fg="#145a32", font=fuente, selectbackground="#b2dfdb", relief="flat", highlightthickness=1, highlightbackground="#b2dfdb"
)
lista_tareas.pack(pady=10)

btn_eliminar = tk.Button(
    ventana, text="Eliminar tarea", command=eliminar_tarea,
    bg="#ffebee", fg="#b71c1c", font=fuente_boton, relief="raised", bd=2, padx=10, pady=10, activebackground="#ffcdd2"
)
btn_eliminar.pack(pady=5)

btn_completar = tk.Button(
    ventana, text="Marcar como completada", command=marcar_completada,
    bg="#e0f7fa", fg="#00695c", font=fuente_boton, relief="raised", bd=2, padx=10, pady=10, activebackground="#b2ebf2"
)
btn_completar.pack(pady=5)

# Botón de salir bien visible al final
btn_salir = tk.Button(
    ventana, text="Salir", command=salir,
    bg="#e0e0e0", fg="#212121", font=fuente_boton, relief="raised", bd=2, padx=10, pady=10, activebackground="#bdbdbd"
)
btn_salir.pack(pady=(30,10))

ventana.mainloop()