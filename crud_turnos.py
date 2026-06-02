from conexion import conectar


def generar_turno():

    conexion = conectar()
    cursor = conexion.cursor()

    dni = input("Ingrese DNI del cliente: ")

    query_cliente = "SELECT nombre, apellido FROM tutor WHERE dni = %s"

    cursor.execute(query_cliente, (dni,))

    cliente = cursor.fetchone()

    if cliente is None:

        print("El cliente no existe")

        cursor.close()
        conexion.close()

        return

    print(f"\nCliente: {cliente[0]} {cliente[1]}")

    query_mascotas = "SELECT mascota_id, nombre, especie FROM mascota WHERE dni_tutor = %s"

    cursor.execute(query_mascotas, (dni,))

    mascotas = cursor.fetchall()

    if len(mascotas) == 0:

        print("El cliente no tiene mascotas registradas")

        cursor.close()
        conexion.close()

        return

    print("\n===== MASCOTAS DISPONIBLES =====\n")

    print(f"{'ID':<5} {'NOMBRE':<15} {'ESPECIE':<15}")

    print("-" * 35)

    for fila in mascotas:

        print(f"{fila[0]:<5} {fila[1]:<15} {fila[2]:<15}")

    mascota_id = input("\nSeleccione ID de la mascota: ")

    print("\n===== SERVICIOS DISPONIBLES =====\n")

    query_servicios = "SELECT servicio_id, tipo_servicio FROM servicio"

    cursor.execute(query_servicios)

    servicios = cursor.fetchall()

    for fila in servicios:

        print(f"{fila[0]} - {fila[1]}")

    servicio_id = input("\nSeleccione ID del servicio: ")

    query_profesionales = "SELECT dni, nombre, apellido FROM profesional WHERE servicio_id = %s"

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

    dni_profesional = profesionales[opcion_profesional - 1][0]

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

    query_verificar_turno = "SELECT turno_id FROM turno WHERE dni_profesional = %s AND fecha_hora_atencion = %s"

    cursor.execute(query_verificar_turno, (dni_profesional, fecha_hora))

    turno_existente = cursor.fetchone()

    if turno_existente is not None:

        print("El profesional ya tiene un turno en ese horario")

        cursor.close()
        conexion.close()

        return

    query_turno = "INSERT INTO turno (mascota_id, servicio_id, dni_profesional, fecha_hora_atencion) VALUES (%s, %s, %s, %s)"

    valores = (mascota_id, servicio_id, dni_profesional, fecha_hora)

    cursor.execute(query_turno, valores)

    conexion.commit()

    print("Turno generado correctamente")

    cursor.close()
    conexion.close()

def ver_turnos():

    conexion = conectar()
    cursor = conexion.cursor()

    query = "SELECT turno.turno_id, mascota.nombre, servicio.tipo_servicio, profesional.nombre, profesional.apellido, turno.fecha_hora_atencion, turno.estado FROM turno INNER JOIN mascota ON turno.mascota_id = mascota.mascota_id INNER JOIN servicio ON turno.servicio_id = servicio.servicio_id INNER JOIN profesional ON turno.dni_profesional = profesional.dni ORDER BY turno.fecha_hora_atencion"

    cursor.execute(query)

    resultados = cursor.fetchall()

    print("\n===== LISTA DE TURNOS =====\n")

    print(f"{'ID':<5} {'MASCOTA':<15} {'SERVICIO':<20} {'PROFESIONAL':<25} {'FECHA Y HORA':<22} {'ESTADO':<15}")

    print("-" * 110)

    for fila in resultados:

        profesional = f"{fila[3]} {fila[4]}"

        print(f"{fila[0]:<5} {fila[1]:<15} {fila[2]:<20} {profesional:<25} {str(fila[5]):<22} {fila[6]:<15}")

    cursor.close()
    conexion.close()

def cancelar_turno():

    conexion = conectar()
    cursor = conexion.cursor()

    dni = input("Ingrese DNI del cliente: ")

    query_cliente = "SELECT nombre, apellido FROM tutor WHERE dni = %s"

    cursor.execute(query_cliente, (dni,))

    cliente = cursor.fetchone()

    if cliente is None:

        print("El cliente no existe")

        cursor.close()
        conexion.close()

        return

    query_turnos = """
    SELECT turno.turno_id,
           mascota.nombre,
           servicio.tipo_servicio,
           profesional.nombre,
           profesional.apellido,
           turno.fecha_hora_atencion,
           turno.estado
    FROM turno
    INNER JOIN mascota
        ON turno.mascota_id = mascota.mascota_id
    INNER JOIN servicio
        ON turno.servicio_id = servicio.servicio_id
    INNER JOIN profesional
        ON turno.dni_profesional = profesional.dni
    WHERE mascota.dni_tutor = %s
    AND turno.estado = 'pendiente'
    """

    cursor.execute(query_turnos, (dni,))

    turnos = cursor.fetchall()

    if len(turnos) == 0:

        print("El cliente no tiene turnos pendientes")

        cursor.close()
        conexion.close()

        return

    print("\n===== TURNOS DISPONIBLES =====\n")

    print(f"{'ID':<5} {'MASCOTA':<15} {'SERVICIO':<20} {'PROFESIONAL':<25} {'FECHA Y HORA':<22}")

    print("-" * 95)

    for fila in turnos:

        profesional = f"{fila[3]} {fila[4]}"

        print(f"{fila[0]:<5} {fila[1]:<15} {fila[2]:<20} {profesional:<25} {str(fila[5]):<22}")

    turno_id = input("\nSeleccione ID del turno a cancelar: ")

    query_update = "UPDATE turno SET estado = 'cancelado' WHERE turno_id = %s"

    cursor.execute(query_update, (turno_id,))

    conexion.commit()

    print("Turno cancelado correctamente")

    cursor.close()
    conexion.close()