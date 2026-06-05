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

        dni = input("Ingrese DNI del cliente: ")

        query_cliente = """
        SELECT nombre, apellido
        FROM tutor
        WHERE dni = %s
        """

        cursor.execute(query_cliente, (dni,))

        cliente = cursor.fetchone()

        if cliente is None:

            print("El cliente no existe")

        else:

            query_mascotas = """
            SELECT mascota_id, nombre
            FROM mascota
            WHERE dni_tutor = %s
            """

            cursor.execute(query_mascotas, (dni,))

            mascotas = cursor.fetchall()

            if len(mascotas) == 0:

                print("El cliente no tiene mascotas")

            else:

                print("\n===== MASCOTAS DISPONIBLES =====\n")

                for fila in mascotas:

                    print(f"ID: {fila[0]} | Mascota: {fila[1]}")

                mascota_id = input("\nSeleccione ID mascota: ")

                query_verificar_mascota = """
                SELECT nombre
                FROM mascota
                WHERE mascota_id = %s
                """

                cursor.execute(query_verificar_mascota, (mascota_id,))

                mascota = cursor.fetchone()

                if mascota is None:

                    print("La mascota no existe")

                else:

                    query_servicios = """
                    SELECT servicio_id, tipo_servicio
                    FROM servicio
                    """

                    cursor.execute(query_servicios)

                    servicios = cursor.fetchall()

                    print("\n===== SERVICIOS DISPONIBLES =====\n")

                    for fila in servicios:

                        print(f"ID: {fila[0]} | Servicio: {fila[1]}")

                    servicio_id = input("\nSeleccione ID servicio: ")

                    query_verificar_servicio = """
                    SELECT tipo_servicio
                    FROM servicio
                    WHERE servicio_id = %s
                    """

                    cursor.execute(query_verificar_servicio, (servicio_id,))

                    servicio = cursor.fetchone()

                    if servicio is None:

                        print("El servicio no existe")

                    else:

                        query_profesionales = """
                        SELECT dni, nombre, apellido
                        FROM profesional
                        WHERE servicio_id = %s
                        """

                        cursor.execute(query_profesionales, (servicio_id,))

                        profesionales = cursor.fetchall()

                        print("\n===== PROFESIONALES DISPONIBLES =====\n")

                        for fila in profesionales:

                            print(f"DNI: {fila[0]} | Profesional: {fila[1]} {fila[2]}")

                        dni_profesional = input("\nIngrese DNI profesional: ")

                        query_verificar_profesional = """
                        SELECT nombre, apellido
                        FROM profesional
                        WHERE dni = %s
                        """

                        cursor.execute(query_verificar_profesional, (dni_profesional,))

                        profesional = cursor.fetchone()

                        if profesional is None:

                            print("El profesional no existe")

                        else:

                            fecha_hora = input("Ingrese fecha y hora (AAAA-MM-DD HH:MM): ")

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

        if len(resultados) == 0:

            print("El cliente no tiene turnos")

        else:

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

        if len(resultados) == 0:

            print("El cliente no tiene turnos")

        else:

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
        """

        cursor.execute(query, (dni,))

        resultados = cursor.fetchall()

        if len(resultados) == 0:

            print("El cliente no tiene turnos")

        else:

            print("\n===== TURNOS =====\n")

            for fila in resultados:

                profesional = f"{fila[3]} {fila[4]}"

                print(
                    f"ID: {fila[0]} | "
                    f"Mascota: {fila[1]} | "
                    f"Servicio: {fila[2]} | "
                    f"Profesional: {profesional} | "
                    f"Fecha: {fila[5]} | "
                    f"Estado: {fila[6]}"
                )


    # SALIR
    elif opcion == "0":

        print("Saliendo...")
        break


    else:

        print("Opcion invalida")


cursor.close()
conexion.close()