from conexion import conectar


def agregar_mascota():

    conexion = conectar()
    cursor = conexion.cursor()

    dni_tutor = input("Ingrese DNI del cliente: ")

    query_verificar = "SELECT * FROM tutor WHERE dni = %s"

    cursor.execute(query_verificar, (dni_tutor,))

    tutor = cursor.fetchone()

    if tutor is None:

        print("El cliente no existe. Debe ingresar un DNI de un cliente registrado.")

        cursor.close()
        conexion.close()

        return

    nombre = input("Ingrese nombre de la mascota: ")
    especie = input("Ingrese especie: ")
    raza = input("Ingrese raza: ")
    fecha_nacimiento = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")

    print(f"\nCliente seleccionado: {tutor[1]} {tutor[2]}\n")

    query = "INSERT INTO mascota (dni_tutor, nombre, especie, raza, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s)"

    valores = (dni_tutor, nombre, especie, raza, fecha_nacimiento)

    cursor.execute(query, valores)

    conexion.commit()

    print("Mascota agregada correctamente")

    cursor.close()
    conexion.close()


def ver_mascotas():

    conexion = conectar()
    cursor = conexion.cursor()

    query ="SELECT mascota.mascota_id, mascota.nombre, mascota.especie, mascota.raza, tutor.nombre, tutor.apellido FROM mascota INNER JOIN tutor ON mascota.dni_tutor = tutor.dni"

    cursor.execute(query)

    resultados = cursor.fetchall()

    print("\n===== LISTA DE MASCOTAS =====\n")

    print(f"{'ID':<5} {'NOMBRE':<15} {'ESPECIE':<15} {'RAZA':<15} {'DUEÑO':<20}")

    print("-" * 70)

    for fila in resultados:

        dueño = f"{fila[4]} {fila[5]}"

        print(f"{fila[0]:<5} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15} {dueño:<20}")

    cursor.close()
    conexion.close()



def agregar_historia_clinica():

    conexion = conectar()
    cursor = conexion.cursor()

    dni = input("Ingrese DNI del cliente: ")

    query_tutor = "SELECT * FROM tutor WHERE dni = %s"

    cursor.execute(query_tutor, (dni,))

    tutor = cursor.fetchone()

    if tutor is None:

        print("El cliente no existe")

        cursor.close()
        conexion.close()

        return

    query_mascotas = "SELECT mascota_id, nombre, especie FROM mascota WHERE dni_tutor = %s"

    cursor.execute(query_mascotas, (dni,))

    mascotas = cursor.fetchall()

    if len(mascotas) == 0:

        print("El cliente no tiene mascotas registradas")

        cursor.close()
        conexion.close()

        return

    print("\n===== MASCOTAS DEL CLIENTE =====\n")

    print(f"{'ID':<5} {'NOMBRE':<15} {'ESPECIE':<15}")

    print("-" * 35)

    for fila in mascotas:

        print(f"{fila[0]:<5} {fila[1]:<15} {fila[2]:<15}")

    mascota_id = input("\nSeleccione ID de la mascota: ")

    antecedente_salud = input("Ingrese antecedentes de salud: ")
    tipo_sangre = input("Ingrese tipo de sangre: ")
    vacuna = input("Ingrese vacuna: ")

    try:

        peso = float(input("Ingrese peso: "))

    except ValueError:

        print("El peso debe ser numérico")

        cursor.close()
        conexion.close()

        return

    query = "INSERT INTO historia_clinica (mascota_id, antecedente_salud, tipo_sangre, vacuna, peso) VALUES (%s, %s, %s, %s, %s)"

    valores = (mascota_id, antecedente_salud, tipo_sangre, vacuna, peso)

    cursor.execute(query, valores)

    conexion.commit()

    print("Historia clínica agregada correctamente")

    cursor.close()
    conexion.close()