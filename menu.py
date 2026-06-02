import crud_clientes
import crud_mascotas
import crud_admin
import crud_turnos


def menu_principal():
    while True:

        print("\n===== MENU PET CARE =====")
        print("1. Gestionar turnos")
        print("2. Clientes")
        print("3. Administración Pet Care")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_turnos()

        elif opcion == "2":
            menu_clientes()

        elif opcion == "3":
            menu_administracion()

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


def menu_turnos():
    while True:

        print("\n===== GESTIONAR TURNOS =====")
        print("1. Generar turno")
        print("2. Ver turnos")
        print("3. Cancelar turno")
        print("4. Modificar Turno")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Generar turno")
            crud_turnos.generar_turno()

        elif opcion == "2":
            print("Ver turnos")
            crud_turnos.ver_turnos()

        elif opcion == "3":
            print("Cancelar turno")
            crud_turnos.cancelar_turno()

        elif opcion == "4":
            print("Modificar Turno")
            crud_turnos.modificar_turno()

        elif opcion == "0":
            break

        else:
            print("Opción inválida")


def menu_clientes():
    while True:

        print("\n===== CLIENTES =====")
        print("1. Gestionar clientes")
        print("2. Gestionar mascotas")        
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_crud_clientes()

        elif opcion == "2":
            menu_crud_mascotas()      

        elif opcion == "0":
            break

        else:
            print("Opción inválida")


def menu_crud_clientes():
    while True:

        print("\n===== GESTIONAR CLIENTES =====")
        print("1. Agregar cliente")
        print("2. Ver clientes")             
        print("3. Modificar CLiente")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Agregar cliente")
            crud_clientes.agregar_cliente()

        elif opcion == "2":
            print("Ver clientes")
            crud_clientes.ver_clientes()     

        elif opcion == "3":
            print("Modificar clientes")                   

        elif opcion == "0":
            break

        else:
            print("Opción inválida")

def menu_crud_mascotas():
    while True:

        print("\n===== GESTIONAR MASCOTAS =====")
        print("1. Agregar mascota")
        print("2. Ver mascotas")        
        print("3. Historia Clínica")
        print("4. Eliminar Mascota")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Agregar mascota")
            crud_mascotas.agregar_mascota()

        elif opcion == "2":
            print("Ver mascotas")
            crud_mascotas.ver_mascotas()     
        
        elif opcion == "3":            
            print("Historia Clinica")
            menu_historia_clinica()
        
        elif opcion == "4":            
            print("Eliminar Mascota")
            crud_mascotas.eliminar_mascota()

        elif opcion == "0":
            break

        else:
            print("Opción inválida")

def menu_historia_clinica():
    while True:

        print("\n===== HISTORIA CLINICA =====")
        print("1. Agregar historia clínica")
        print("2. Ver historia clínica")
        print("3. Modificar historia clínica")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Agregar historia clínica")
            crud_mascotas.agregar_historia_clinica()

        elif opcion == "2":
            print("Ver historia clínica")

        elif opcion == "3":
            print("Modificar historia clínica")

        elif opcion == "0":
            break

        else:
            print("Opción inválida")

def menu_administracion():
    while True:

        print("\n===== ADMINISTRACION PET CARE =====")
        print("1. Gestionar profesionales")
        print("2. Gestionar servicios")
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Gestionar profesionales")
            menu_profesionales()

        elif opcion == "2":
            print("Gestionar servicios")
            menu_servicios()

        elif opcion == "0":
            break

        else:
            print("Opción inválida")

def menu_servicios():
    while True:

        print("\n===== GESTIONAR SERVICIOS =====")
        print("1. Agregar servicio")
        print("2. Ver servicios")
        print("3. Modificar servicio")
        
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Agregar servicio")
            crud_admin.agregar_servicio()

        elif opcion == "2":
            print("Ver servicios")
            crud_admin.ver_servicios()

        elif opcion == "3":
            print("Modificar servicio")


        elif opcion == "0":
            break

        else:
            print("Opción inválida")

def menu_profesionales():
    while True:

        print("\n===== GESTIONAR PROFESIONALES =====")
        print("1. Agregar profesional")
        print("2. Ver profesionales")
        print("3. Modificar profesional")        
        print("0. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Agregar profesional")
            crud_admin.agregar_profesional()

        elif opcion == "2":
            print("Ver profesionales")
            crud_admin.ver_profesionales()

        elif opcion == "3":
            print("Modificar profesional")
       

        elif opcion == "0":
            break

        else:
            print("Opción inválida")