from conexion import conectar


def agregar_servicio():

    conexion = conectar()
    cursor = conexion.cursor()

    tipo_servicio = input("Ingrese nombre del servicio: ")

    query = "INSERT INTO servicio (tipo_servicio) VALUES (%s)"

    valores = (tipo_servicio,)

    cursor.execute(query, valores)

    conexion.commit()

    print("Servicio agregado correctamente")

    cursor.close()
    conexion.close()

def ver_servicios():

    conexion = conectar()
    cursor = conexion.cursor()

    query = "SELECT * FROM servicio"

    cursor.execute(query)

    resultados = cursor.fetchall()

    print("\n===== LISTA DE SERVICIOS =====\n")

    print(f"{'ID':<5} {'SERVICIO':<25}")

    print("-" * 30)

    for fila in resultados:

        print(f"{fila[0]:<5} {fila[1]:<25}")

    cursor.close()
    conexion.close()

def agregar_profesional():

    conexion = conectar()
    cursor = conexion.cursor()

    dni = input("Ingrese DNI: ")

    query_verificar = "SELECT nombre FROM profesional WHERE dni = %s"

    cursor.execute(query_verificar, (dni,))

    profesional = cursor.fetchone()

    if profesional is not None:

        print("Ya existe un profesional con ese DNI")

        cursor.close()
        conexion.close()

        return

    print("\n===== SERVICIOS DISPONIBLES =====\n")

    query_servicios = "SELECT * FROM servicio"

    cursor.execute(query_servicios)

    servicios = cursor.fetchall()

    for fila in servicios:

        print(f"{fila[0]} - {fila[1]}")

    servicio_id = input("\nSeleccione ID del servicio: ")

    query_servicio = "SELECT * FROM servicio WHERE servicio_id = %s"

    cursor.execute(query_servicio, (servicio_id,))

    servicio = cursor.fetchone()

    if servicio is None:

        print("El servicio no existe")

        cursor.close()
        conexion.close()

        return

    print(f"\n===== ALTA DE PROFESIONAL EN EL SERVICIO DE {servicio[1].upper()} =====\n")

    matricula = input("Ingrese matrícula: ")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    telefono = input("Ingrese teléfono: ")
    mail = input("Ingrese mail: ")
    direccion = input("Ingrese dirección: ")

    query = "INSERT INTO profesional (dni, matricula, servicio_id, nombre, apellido, telefono, mail, direccion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    valores = (dni, matricula, servicio_id, nombre, apellido, telefono, mail, direccion)

    cursor.execute(query, valores)

    conexion.commit()

    print("Profesional agregado correctamente")

    cursor.close()
    conexion.close()

def ver_profesionales():

    conexion = conectar()
    cursor = conexion.cursor()

    query = "SELECT profesional.dni, profesional.matricula, profesional.nombre, profesional.apellido, profesional.telefono, servicio.tipo_servicio FROM profesional INNER JOIN servicio ON profesional.servicio_id = servicio.servicio_id"

    cursor.execute(query)

    resultados = cursor.fetchall()

    print("\n===== LISTA DE PROFESIONALES =====\n")

    print(f"{'DNI':<15} {'MATRÍCULA':<15} {'NOMBRE':<15} {'APELLIDO':<15} {'TELÉFONO':<15} {'SERVICIO':<20}")

    print("-" * 95)

    for fila in resultados:

        print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {fila[4]:<15} {fila[5]:<20}")

    cursor.close()
    conexion.close()