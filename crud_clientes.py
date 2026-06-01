from conexion import conectar

def agregar_cliente():

    conexion = conectar()
    cursor = conexion.cursor()

    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    telefono = input("Ingrese teléfono: ")
    mail = input("Ingrese mail: ")
    direccion = input("Ingrese dirección: ")

    query = "INSERT INTO tutor (nombre, apellido, telefono, mail, direccion) VALUES (%s, %s, %s, %s, %s)"

    valores = (nombre, apellido, telefono, mail, direccion)

    cursor.execute(query, valores)

    conexion.commit()

    print("Cliente agregado correctamente")

    cursor.close()
    conexion.close()

def ver_clientes():

    conexion = conectar()
    cursor = conexion.cursor()

    query = "SELECT * FROM tutor"

    cursor.execute(query)

    resultados = cursor.fetchall()

    print("\n===== LISTA DE CLIENTES =====\n")

    print(f"{'ID':<5} {'NOMBRE':<15} {'APELLIDO':<15} {'TELÉFONO':<15}")

    print("-" * 55)

    for fila in resultados:

        print(f"{fila[0]:<5} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15}")

    cursor.close()
    conexion.close()