from conexion import conectar

def agregar_cliente():

    conexion = conectar()
    cursor = conexion.cursor()

    dni = int(input("Ingrese su DNI: "))

    query_verificar = "SELECT * FROM tutor WHERE dni = %s"

    cursor.execute(query_verificar, (dni,))

    cliente = cursor.fetchone()

    if cliente is not None:

        print("Ya existe un cliente con ese DNI")

        cursor.close()
        conexion.close()

        return


    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    telefono = input("Ingrese teléfono: ")
    mail = input("Ingrese mail: ")
    direccion = input("Ingrese dirección: ")

    

    query = "INSERT INTO tutor (dni, nombre, apellido, telefono, mail, direccion) VALUES (%s, %s, %s, %s, %s, %s)"

    valores = (dni, nombre, apellido, telefono, mail, direccion)

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

    print(f"{'DNI':<15} {'NOMBRE':<15} {'APELLIDO':<15} {'TELÉFONO':<15}")

    print("-" * 55)

    for fila in resultados:

        print(f"{fila[0]:<15} {fila[1]:<15} {fila[2]:<15} {fila[3]:<15}")

    cursor.close()
    conexion.close()