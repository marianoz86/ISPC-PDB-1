from conexion import conectar


def agregar_mascota():

    conexion = conectar()
    cursor = conexion.cursor()

    tutor_id = input("Ingrese ID del cliente: ")

    query_verificar = "SELECT * FROM tutor WHERE tutor_id = %s"

    cursor.execute(query_verificar, (tutor_id,))

    tutor = cursor.fetchone()

    if tutor is None:

        print("El cliente no existe. Debe ingresar ID de un cliente registrado.")

        cursor.close()
        conexion.close()

        return

    nombre = input("Ingrese nombre de la mascota: ")
    especie = input("Ingrese especie: ")
    raza = input("Ingrese raza: ")
    fecha_nacimiento = input("Ingrese fecha de nacimiento (YYYY-MM-DD): ")

    query = "INSERT INTO mascota (tutor_id, nombre, especie, raza, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s)"

    valores = (tutor_id, nombre, especie, raza, fecha_nacimiento)

    cursor.execute(query, valores)

    conexion.commit()

    print("Mascota agregada correctamente")

    cursor.close()
    conexion.close()

from conexion import conectar


def ver_mascotas():

    conexion = conectar()
    cursor = conexion.cursor()

    query = "SELECT mascota.mascota_id, mascota.nombre, mascota.especie, mascota.raza, tutor.nombre, tutor.apellido FROM mascota INNER JOIN tutor ON mascota.tutor_id = tutor.tutor_id"

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

from conexion import conectar


def agregar_historia_clinica():

    conexion = conectar()
    cursor = conexion.cursor()

    mascota_id = input("Ingrese ID de la mascota: ")

    query_verificar = "SELECT * FROM mascota WHERE mascota_id = %s"

    cursor.execute(query_verificar, (mascota_id,))

    mascota = cursor.fetchone()

    if mascota is None:

        print("La mascota no existe. Debe ingresar el id de una mascota registrada.")

        cursor.close()
        conexion.close()

        return

    antecedente_salud = input("Ingrese antecedentes de salud: ")
    tipo_sangre = input("Ingrese tipo de sangre: ")
    vacuna = input("Ingrese vacuna: ")
    peso = float(input("Ingrese peso en KG: "))

    query = "INSERT INTO historia_clinica (mascota_id, antecedente_salud, tipo_sangre, vacuna, peso) VALUES (%s, %s, %s, %s, %s)"

    valores = (mascota_id, antecedente_salud, tipo_sangre, vacuna, peso)

    cursor.execute(query, valores)

    conexion.commit()

    print("Historia clínica agregada correctamente")

    cursor.close()
    conexion.close()