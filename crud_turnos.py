from conexion import conectar


def generar_turno():

    conexion = conectar()
    cursor = conexion.cursor()

    mascota_id = input("Ingrese ID de la mascota: ")

    query_mascota = "SELECT * FROM mascota WHERE mascota_id = %s"

    cursor.execute(query_mascota, (mascota_id,))

    mascota = cursor.fetchone()

    if mascota is None:

        print("La mascota no existe")

        cursor.close()
        conexion.close()

        return

    print(f"\nMascota seleccionada: {mascota[2]}\n")

    print("===== SERVICIOS DISPONIBLES =====\n")

    query_servicios = "SELECT * FROM servicio"

    cursor.execute(query_servicios)

    servicios = cursor.fetchall()

    for fila in servicios:

        print(f"{fila[0]} - {fila[1]}")

    servicio_id = input("\nSeleccione ID del servicio: ")

    query_profesionales = "SELECT matricula, nombre, apellido FROM profesional WHERE servicio_id = %s"

    cursor.execute(query_profesionales, (servicio_id,))

    profesionales = cursor.fetchall()

    if len(profesionales) == 0:

        print("No hay profesionales disponibles para ese servicio")

        cursor.close()
        conexion.close()

        return

    print("\n===== PROFESIONALES DISPONIBLES =====\n")

    for i, fila in enumerate(profesionales, start=1):

        print(f"{i} - {fila[1]} {fila[2]}")

    opcion_profesional = int(input("\nSeleccione un profesional: "))

    if opcion_profesional < 1 or opcion_profesional > len(profesionales):

        print("Opción inválida")

        cursor.close()
        conexion.close()

        return

    matricula = profesionales[opcion_profesional - 1][0]

    fecha = input("Ingrese fecha del turno (YYYY-MM-DD): ")

    horarios = [
        "09:00:00",
        "10:00:00",
        "11:00:00",
        "12:00:00",
        "13:00:00",
        "16:00:00",
        "17:00:00",
        "18:00:00",
        "19:00:00",
        "20:00:00"
    ]

    print("\n===== HORARIOS DISPONIBLES =====\n")

    for i, horario in enumerate(horarios, start=1):

        print(f"{i} - {horario}")

    opcion_horario = int(input("\nSeleccione un horario: "))

    if opcion_horario < 1 or opcion_horario > len(horarios):

        print("Horario inválido")

        cursor.close()
        conexion.close()

        return

    hora = horarios[opcion_horario - 1]

    fecha_hora = f"{fecha} {hora}"

    query_verificar_turno = "SELECT * FROM turno WHERE matricula = %s AND fecha_hora_atencion = %s"

    cursor.execute(query_verificar_turno, (matricula, fecha_hora))

    turno_existente = cursor.fetchone()

    if turno_existente is not None:

        print("El profesional ya tiene un turno en ese horario")

        cursor.close()
        conexion.close()

        return

    query_turno = "INSERT INTO turno (mascota_id, servicio_id, matricula, fecha_hora_atencion) VALUES (%s, %s, %s, %s)"

    valores = (mascota_id, servicio_id, matricula, fecha_hora)

    cursor.execute(query_turno, valores)

    conexion.commit()

    print("Turno generado correctamente")

    cursor.close()
    conexion.close()

from conexion import conectar


def ver_turnos():

    conexion = conectar()
    cursor = conexion.cursor()

    query = "SELECT turno.turno_id, mascota.nombre, servicio.tipo_servicio, profesional.nombre, profesional.apellido, turno.fecha_hora_atencion FROM turno INNER JOIN mascota ON turno.mascota_id = mascota.mascota_id INNER JOIN servicio ON turno.servicio_id = servicio.servicio_id INNER JOIN profesional ON turno.matricula = profesional.matricula ORDER BY turno.fecha_hora_atencion"

    cursor.execute(query)

    resultados = cursor.fetchall()

    print("\n===== LISTA DE TURNOS =====\n")

    print(f"{'ID':<5} {'MASCOTA':<15} {'SERVICIO':<20} {'PROFESIONAL':<25} {'FECHA Y HORA':<20}")

    print("-" * 90)

    for fila in resultados:

        profesional = f"{fila[3]} {fila[4]}"

        print(f"{fila[0]:<5} {fila[1]:<15} {fila[2]:<20} {profesional:<25} {str(fila[5]):<20}")

    cursor.close()
    conexion.close()

    
def cancelar_turno():

    conexion = conectar()
    cursor = conexion.cursor()

    turno_id = input("Ingrese ID del turno a cancelar: ")

    query_verificar = "SELECT * FROM turno WHERE turno_id = %s"

    cursor.execute(query_verificar, (turno_id,))

    turno = cursor.fetchone()

    if turno is None:

        print("El turno no existe")

        cursor.close()
        conexion.close()

        return

    query_eliminar = "DELETE FROM turno WHERE turno_id = %s"

    cursor.execute(query_eliminar, (turno_id,))

    conexion.commit()

    print("Turno cancelado correctamente")

    cursor.close()
    conexion.close()