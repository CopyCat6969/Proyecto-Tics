#Modificar el login para intentos ilimitados (HECHO)
#Modificar para que la busqueda sea por apellido (HECHO)
#Registrar los datos de profesor y las materias
#Agregar codigo para mostrar calificacion mas alta y baja 
#Modificar para que muestre el promedio general del curso 
#Sabado Nos organizamos para terminar el proyecto

Estudiantes = []
Nota_Final = 10
Notas = []


print("------------Bienvenido-----------\n")
print("Sistema de Gestión de Estudiantes ")

usuario_correcto = "admin"
clave_correcta = "890"

while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido\n")
        break
    else:
        print("Acceso denegado. Intente nuevamente.\n")


def agg_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    Estudiantes.append(nombre)
    print(f"Estudiante {nombre} agregado exitosamente.")
    nota = float(input("Ingrese la nota del estudiante: "))
    Notas.append(nota)
    if nota >= Nota_Final:
        print(f"El estudiante {nombre} ha aprobado con una nota de {nota}.\n")
    else:
        print(f"El estudiante {nombre} ha reprobado con una nota de {nota}.\n")
    return

def mostrar_estudiantes():
    if Estudiantes:
        print("Lista de Estudiantes:")
        for estudiante in Estudiantes:
            print(f"- {estudiante}")
        for i in range(len(Estudiantes)):
            print(f"La nota de {Estudiantes[i]} es: {Notas[i]}")    

    else:
        print("No hay estudiantes registrados.\n")
    return

def buscar_estudiante():
    apellido = input("Ingrese el apellido del estudiante a buscar: ")
    encontrado = False
    for i in range(len(Estudiantes)):
        if apellido.lower() in Estudiantes[i].lower():
            print(f"El estudiante {Estudiantes[i]} está registrado.")
            print(f"La nota es: {Notas[i]}\n")
            encontrado = True
    if not encontrado:
        print(f"No se encontró ningún estudiante con el apellido '{apellido}'.\n")
    return

def promedio_general():
    if not Notas:
        print("No hay estudiantes registrados para calcular el promedio.\n")
        return
    
    promedio = sum(Notas) / len(Notas)
    print(f"El promedio general del curso es: {promedio:.2f}\n")
    return

def estudiantes_aprobados():
    print("Los estudiantes aprovados son: .\n")
    for i in range(len(Estudiantes)):
        if Notas[i] >= Nota_Final:
            print(f"- {Estudiantes[i]} con nota {Notas[i]}")
    return

def estudiantes_reprobados():
    print("Los estudiantes reprovados son: .\n")
    for i in range(len(Estudiantes)):
        if Notas[i] < Nota_Final:
            print(f"- {Estudiantes[i]} con nota {Notas[i]}")
    return

while True:
    print("Menú de Opciones:")
    print("1. Agregar Estudiante")
    print("2. Mostrar Estudiantes")
    print("3. Buscar Estudiante")
    print("4. Promedio General")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '1':
        agg_estudiante()
    elif opcion == '2':
        mostrar_estudiantes()
    elif opcion == '3':
        buscar_estudiante()
    elif opcion == '4':
        promedio_general()
    elif opcion == '5':
        print("Saliendo del sistema. ¡Hasta luego!")
        exit()
        break
     
    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 5.\n")
