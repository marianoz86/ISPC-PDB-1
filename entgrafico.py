import tkinter as tk
from tkinter import messagebox
import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pet_care_db"
)

cursor = conexion.cursor()


# ---------------- GENERAR ----------------

def generar_turno():

    mascota_id = entry_mascota.get()
    servicio_id = entry_servicio.get()
    dni_profesional = entry_profesional.get()
    fecha_hora = entry_fecha.get()

    query_mascota = """
    SELECT nombre
    FROM mascota
    WHERE mascota_id = %s
    """

    cursor.execute(query_mascota, (mascota_id,))

    mascota = cursor.fetchone()

    if mascota is None:

        messagebox.showerror("Error", "La mascota no existe")
        return

    query_profesional = """
    SELECT nombre
    FROM profesional
    WHERE dni = %s
    """

    cursor.execute(query_profesional, (dni_profesional,))

    profesional = cursor.fetchone()

    if profesional is None:

        messagebox.showerror("Error", "El profesional no existe")
        return

    query = """
    INSERT INTO turno
    (mascota_id, servicio_id, dni_profesional, fecha_hora_atencion)
    VALUES (%s, %s, %s, %s)
    """

    valores = (
        mascota_id,
        servicio_id,
        dni_profesional,
        fecha_hora
    )

    cursor.execute(query, valores)

    conexion.commit()

    messagebox.showinfo("Correcto", "Turno generado correctamente")


# ---------------- CONSULTAR ----------------

def consultar_turnos():

    dni = entry_dni.get()

    query = """
    SELECT turno.turno_id,
           mascota.nombre,
           servicio.tipo_servicio,
           turno.fecha_hora_atencion,
           turno.estado
    FROM turno
    INNER JOIN mascota
        ON turno.mascota_id = mascota.mascota_id
    INNER JOIN servicio
        ON turno.servicio_id = servicio.servicio_id
    WHERE mascota.dni_tutor = %s
    """

    cursor.execute(query, (dni,))

    resultados = cursor.fetchall()

    texto_resultados.delete("1.0", tk.END)

    for fila in resultados:

        texto_resultados.insert(
            tk.END,
            f"ID: {fila[0]} | "
            f"Mascota: {fila[1]} | "
            f"Servicio: {fila[2]} | "
            f"Fecha: {fila[3]} | "
            f"Estado: {fila[4]}\n"
        )


# ---------------- ELIMINAR ----------------

def eliminar_turno():

    turno_id = entry_turno.get()

    query = """
    DELETE FROM turno
    WHERE turno_id = %s
    """

    cursor.execute(query, (turno_id,))

    conexion.commit()

    messagebox.showinfo("Correcto", "Turno eliminado")


# ---------------- MODIFICAR ----------------

def modificar_turno():

    turno_id = entry_turno.get()
    nueva_fecha = entry_nueva_fecha.get()

    query = """
    UPDATE turno
    SET fecha_hora_atencion = %s
    WHERE turno_id = %s
    """

    valores = (
        nueva_fecha,
        turno_id
    )

    cursor.execute(query, valores)

    conexion.commit()

    messagebox.showinfo("Correcto", "Turno modificado")


# ---------------- VENTANA ----------------

ventana = tk.Tk()

ventana.title("Sistema Veterinaria")
ventana.geometry("700x600")


# GENERAR

tk.Label(ventana, text="ID Mascota").pack()
entry_mascota = tk.Entry(ventana)
entry_mascota.pack()

tk.Label(ventana, text="ID Servicio").pack()
entry_servicio = tk.Entry(ventana)
entry_servicio.pack()

tk.Label(ventana, text="DNI Profesional").pack()
entry_profesional = tk.Entry(ventana)
entry_profesional.pack()

tk.Label(ventana, text="Fecha y Hora").pack()
entry_fecha = tk.Entry(ventana)
entry_fecha.pack()

tk.Button(
    ventana,
    text="Generar Turno",
    command=generar_turno
).pack(pady=10)


# CONSULTAR

tk.Label(ventana, text="DNI Cliente").pack()
entry_dni = tk.Entry(ventana)
entry_dni.pack()

tk.Button(
    ventana,
    text="Consultar Turnos",
    command=consultar_turnos
).pack(pady=10)


# RESULTADOS

texto_resultados = tk.Text(
    ventana,
    height=10,
    width=80
)

texto_resultados.pack()


# ELIMINAR

tk.Label(ventana, text="ID Turno").pack()
entry_turno = tk.Entry(ventana)
entry_turno.pack()

tk.Button(
    ventana,
    text="Eliminar Turno",
    command=eliminar_turno
).pack(pady=10)


# MODIFICAR

tk.Label(ventana, text="Nueva Fecha y Hora").pack()
entry_nueva_fecha = tk.Entry(ventana)
entry_nueva_fecha.pack()

tk.Button(
    ventana,
    text="Modificar Turno",
    command=modificar_turno
).pack(pady=10)


ventana.mainloop()


cursor.close()
conexion.close()