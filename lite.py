import mysql.connector


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="pet_care_db"
)

cursor = conexion.cursor()


while True:

    print("\n===== MENU TURNOS =====")
    print("1 - Generar turno")
    print("2 - Modificar turno")
    print("3 - Eliminar turno")
    print("4 - Consultar turnos")
    print("0 - Salir")

    opcion = input("Seleccione una opcion: ")


    # GENERAR TURNO
    if opcion == "1":

        mascota_id = input("Ingrese ID mascota: ")
        servicio_id = input("Ingrese ID servicio: ")
        dni_profesional = input("Ingrese DNI profesional: ")
        fecha_hora = input("Ingrese fecha y hora (AAAA-MM-DD HH:MM:SS): ")

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

        print("Turno generado correctamente")


    # MODIFICAR TURNO
    elif opcion == "2":

        dni = input("Ingrese DNI del cliente: ")

        query = """
        SELECT turno.turno_id,
               mascota.nombre,
               turno.fecha_hora_atencion
        FROM turno
        INNER JOIN mascota
            ON turno.mascota_id = mascota.mascota_id
        WHERE mascota.dni_tutor = %s
        """

        cursor.execute(query, (dni,))

        resultados = cursor.fetchall()

        print("\n===== TURNOS =====\n")

        for fila in resultados:

            print(f"ID: {fila[0]} | Mascota: {fila[1]} | Fecha: {fila[2]}")

        turno_id = input("\nIngrese ID turno a modificar: ")

        nueva_fecha = input("Ingrese nueva fecha y hora: ")

        query_update = """
        UPDATE turno
        SET fecha_hora_atencion = %s
        WHERE turno_id = %s
        """

        valores = (
            nueva_fecha,
            turno_id
        )

        cursor.execute(query_update, valores)

        conexion.commit()

        print("Turno modificado correctamente")


    # ELIMINAR TURNO
    elif opcion == "3":

        dni = input("Ingrese DNI del cliente: ")

        query = """
        SELECT turno.turno_id,
               mascota.nombre,
               turno.fecha_hora_atencion
        FROM turno
        INNER JOIN mascota
            ON turno.mascota_id = mascota.mascota_id
        WHERE mascota.dni_tutor = %s
        """

        cursor.execute(query, (dni,))

        resultados = cursor.fetchall()

        print("\n===== TURNOS =====\n")

        for fila in resultados:

            print(f"ID: {fila[0]} | Mascota: {fila[1]} | Fecha: {fila[2]}")

        turno_id = input("\nIngrese ID turno a eliminar: ")

        query_delete = """
        DELETE FROM turno
        WHERE turno_id = %s
        """

        cursor.execute(query_delete, (turno_id,))

        conexion.commit()

        print("Turno eliminado correctamente")


    # CONSULTAR TURNOS
    elif opcion == "4":

        dni = input("Ingrese DNI del cliente: ")

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

        print("\n===== TURNOS =====\n")

        for fila in resultados:

            print(
                f"ID: {fila[0]} | "
                f"Mascota: {fila[1]} | "
                f"Servicio: {fila[2]} | "
                f"Fecha: {fila[3]} | "
                f"Estado: {fila[4]}"
            )


    # SALIR
    elif opcion == "0":

        print("Saliendo...")
        break


    else:

        print("Opcion invalida")


cursor.close()
conexion.close()