# Final project by Dava2310 called: "StudentHub"

"""
project.py (Main File)

Este archivo contiene toda la logica para el correcto manejo del sistema.
Contiene todos los metodos que permiten la creacion, modificacion, busquedas, validaciones
de estudiantes, materias, notas, reportes como listas, entre otros.

Ademas, contiene las variables globales necesarias para manejar a los estudiantes y a las
materias del sistema.

Por ultimo, contiene en la funcion main el menu de opciones principal, y otra funcion que es
el menu_estudiantes que gestiona las opciones cuando un estudiante ha ingresado al sistema.

Dependencias:
- Clase Estudiante desde estudiante.py
- Clase Materia desde materia.py
- Clase Nota desde nota.py
- Clase Estudiante_Materia desde estudiante_materia.py

Uso:
Para ejecutar este archivo, use el siguiente comando:

python project.py

Notas importantes:
- Este archivo debe ejecutarse en un entorno donde estén disponibles todas las dependencias especificadas.
- En caso de cambiar la estructura del proyecto, como la ubicacion de las clases, cambie las rutas en la seccion de "Importacion de las clases"
"""

# Modulos
import re
import os
from typing import List

# Importacion de las clases
from estudiante import Estudiante
from materia import Materia
from estudiante_materia import Estudiante_Materia
from nota import Nota

# Lista global que almacena objetos de tipo Estudiante.
lista_estudiantes:List[Estudiante] = []

"""
Lista global que almacena objetos de tipo Estudiante.

Esta lista se utiliza para mantener un registro de todos los estudiantes
que están siendo gestionados por el sistema. Cada elemento de la lista
es un objeto de la clase Estudiante.

Uso:
    - Los objetos Estudiante se añaden a esta lista cuando se crean desde su funcion respectiva.
    - Se puede acceder a los estudiantes y modificar sus datos a través
      de esta lista global.

Consideraciones:
    - Asegúrese de mantener actualizada esta lista con los estudiantes
      correctos y completos para garantizar la integridad de los datos
      y las operaciones relacionadas con los estudiantes.
    - Siempre maneje esta lista con cuidado para evitar pérdida de datos
      o inconsistencias.

Notas:
    - Esta variable global debe inicializarse vacía al inicio del programa.
"""

# Lista global que almacena objetos de tipo Materia.
lista_materias:List[Materia] = []

"""
Lista global que almacena objetos de tipo Materia.

Esta lista se utiliza para mantener un registro de todas las materias
que están siendo gestionados por el sistema. Cada elemento de la lista
es un objeto de la clase Materia.

Uso:
    - Los objetos Materia se añaden a esta lista cuando se crean desde su funcion respectiva.
    - Se puede acceder a las materias y modificar sus datos a través
      de esta lista global.

Consideraciones:
    - Asegúrese de mantener actualizada esta lista con las materias
      correctos y completos para garantizar la integridad de los datos
      y las operaciones relacionadas con las materias.
    - Siempre maneje esta lista con cuidado para evitar pérdida de datos
      o inconsistencias.

Notas:
    - Esta variable global debe inicializarse vacía al inicio del programa.
"""

def main():
    """
    Función principal que maneja el flujo de control del sistema de registro de estudiantes, materias y notas.

    Esta función muestra un menú interactivo al usuario donde puede realizar diversas operaciones,
    como crear estudiantes, acceder a operaciones específicas de estudiantes, listar estudiantes y salir del sistema.

    Uso:
        - Ejecute esta función para iniciar el sistema de registro.
        - Muestra un menú de opciones y ejecuta las operaciones correspondientes según la opción seleccionada por el usuario.

    Consideraciones:
        - Este sistema debe ejecutarse en un entorno que admita la limpieza de pantalla usando `os.system('cls')`.
        - Las operaciones que involucren estudiantes dependen de la correcta implementación de las funciones `crear_estudiante()`,
          `encontrar_estudiante()`, `menu_estudiantes()` y `listar_estudiantes()`.

    Raises:
        ValueError: Si el usuario ingresa una opción inválida que no esté en el rango del 1 al 4.

    """

    opcion = 0 # Almacena la opcion elegida por el usuario
    salir = 0  # En caso de que el usuario haya elegido salir, se almacena aqui: 0 para no salir, 1 para salir.

    # Mensaje de bienvenida al sistema.
    print("\t\tBIENVENIDO AL SISTEMA DE REGISTRO DE ESTUDIANTES, MATERIAS Y NOTA (MADE BY: Dava2310)\n")

    while salir != 1:
        input("Presione Enter para continuar")
        # os.system('cls')

        # Menú principal
        print("\n\t\t MENU PRINCIPAL DEL SISTEMA \n")
        print("1- Crear un estudiante")
        print("2- Crear una materia")
        print("3- Acceder a las operaciones de estudiantes")
        print("4- Listar Estudiantes")
        print("5- Salir")

        # Solicitar y procesar la opción del usuario
        try:
            opcion = int(input("Ingrese una opción válida del 1 al 5: "))
            print("")

            # Manejar las opciones del usuario
            match opcion:
                case 1:
                    print("\t\t INGRESE LOS DATOS DEL ESTUDIANTE A CONTINUACION: \n")
                    datos = obtener_datos_estudiante()

                    if datos:
                        nombre, cedula, edad, estatura, peso = datos
                        crear_estudiante(nombre, cedula, edad, estatura, peso)
                case 2:
                    print("\t\t INGRESE LOS DATOS DE LA MATERIA A CONTINUACION: \n")
                    datos = obtener_datos_materia()

                    if datos:
                        codigo_materia, nombre = datos
                        crear_materia(codigo_materia, nombre)
                case 3:
                    estudiante = encontrar_estudiante()
                    if isinstance(estudiante, Estudiante):
                        menu_estudiantes(estudiante)
                    else:
                        print("ERROR: Estudiante no encontrado")
                case 4:
                    listar_estudiantes()
                case 5:
                    salir = int(input("¿Está seguro de salir? Se borrarán todos los datos. 1-Si, 2-No: "))
                case _:
                    print("Opción inválida")

        except ValueError as e:
            if str(e).startswith("invalid literal for int() with base 10"):
                print("Error: Por favor ingrese un número entero válido del 1 al 5.")
            else:
                print(f"Error: {e}")

    print("************MUCHAS GRACIAS POR USAR EL SISTEMA, HASTA LUEGO.***************")


def menu_estudiantes(estudiante: Estudiante):
    """
    Función que muestra un menú de opciones para operaciones relacionadas con un estudiante específico.

    Este menú permite realizar diversas acciones como inscribir materias, listar materias inscritas,
    agregar notas a una materia específica, listar todas las notas del estudiante y salir del menú.

    Args:
        estudiante (Estudiante): Objeto de la clase Estudiante sobre el cual se realizarán las operaciones.

    Uso:
        - Llamar esta función pasando un objeto Estudiante como argumento para mostrar el menú de opciones.
        - Proporciona interactividad para que el usuario seleccione y ejecute operaciones sobre el estudiante.

    Consideraciones:
        - Las operaciones dependen de la correcta implementación de las funciones `registrar_materia()`,
          `listar_materias()`, `registrar_notas_main()` y `listar_notas()` que trabajan con objetos Estudiante.

    Raises:
        ValueError: Si el usuario ingresa una opción inválida que no esté en el rango del 1 al 5.

    """
    opcion = 0

    while opcion != 5:
        input("Presione Enter para continuar")
        # os.system("cls")

        print(f"\t\t MENU DE OPCIONES PARA EL ESTUDIANTE: {estudiante.nombre} (C.I: {estudiante.cedula})\n")

        print("1- Inscribir materia")
        print("2- Listar materias")
        print("3- Agregar notas a una materia")
        print("4- Listado de notas general del estudiante")
        print("5- Salir")

        try:
            opcion = int(input("Ingrese una opción del 1 al 5: "))
            print("")

            # Manejar las opciones del usuario
            match opcion:
                case 1:
                    anexar_materia(estudiante)
                case 2:
                    listar_materias(estudiante)
                case 3:
                    datos = registrar_notas_main(estudiante)
                    if datos:
                        materia, semestre = datos
                        registrar_notas(estudiante, materia, semestre)
                case 4:
                    listar_notas(estudiante)
                case 5:
                    print("Saliendo del menú de estudiante\n")
                case _:
                    print("Ingrese una opción válida del 1 al 5")

        except ValueError:
            print("Error: Por favor ingrese un número entero válido del 1 al 5.")

""" OPERACIONES DE CREACION: ESTUDIANTE, MATERIAS, NOTAS """

def obtener_datos_estudiante():
    """
    Recolecta los datos del estudiante desde la entrada estandar
    """

    # Recolectando la Cedula
    cedula = input("Cedula (Formato: 123456789, 6 a 9 digitos): ")

    # Verificando que la Cedula no exista en otro estudiante
    if verificar_cedula(cedula):
        print("ERROR: Se ha encontrado a un estudiante registrado con la misma cedula ingresada, no se pudo proceder.")
        return None # Devolvemos None para indicar que no se puede proceder

    # Obteniendo el resto de los datos del estudiante
    nombre = input("Nombre y Apellido: ")
    edad = int(input("Edad: "))
    estatura = float(input("Estatura (cm): "))
    peso = float(input("Peso (kg): "))

    return nombre, cedula, edad, estatura, peso

def crear_estudiante(nombre: str, cedula: str, edad: int, estatura: float, peso: float) -> bool:

    """
    Crea un Objeto Estudiante y lo agrega a la lista de Estudiantes

    Args:
        nombre (str): Nombre del Estudiante
        cedula (str): La cedula o ID que identifica al estudiante
        edad (int): Edad del Estudiante
        estatura (float): La estatura o altura en CM del estudiante
        peso (float): El Peso en KG del Estudiante
    """

    # Creacion del objeto estudiante
    obj_stud = Estudiante(nombre, cedula, edad, estatura, peso)

    # Se le indica al usuario cuales fueron los datos ingresados por si desea aceptar o no el ingreso del estudiante
    print("\t\t VERIFIQUE LOS DATOS INGRESADOS\n")
    print(obj_stud)

    # Verificacion de ingreso en el sistema
    verificacion = input("Ingrese 1 si quiere ingresar al estudiante, 2 para revertir el proceso: ")

    if verificacion == "1":
        lista_estudiantes.append(obj_stud)
        return True
    else:
        print("Se ha revertido el proceso\n")
        return False

def obtener_datos_materia():
    """
    Recolecta los datos de la materia a registrar en el sistema y,
    verifica que el codigo de la materia no se repita.

    Returns:
        str: El codigo de la materia
        str: El nombre de la materia
    """

    # Obteniendo el codigo de la materia
    codigo_materia = input("Codigo de la materia: ")

    if isinstance(encontrar_materia(codigo_materia), Materia):
        print("ERROR: Se ha encontrado a una materia registrada con el mismo codigo, no se puede proceder.")
        return None

    # Obteniendo el resto de los datos de la materia
    nombre = input("Nombre de la materia: ")

    return codigo_materia, nombre

def crear_materia(codigo_materia: str, nombre:str):
    """
    Esta funcion se encarga de registrar una materia al sistema.
    """

    # Creacion del objeto materia
    obj_materia = Materia(nombre, codigo_materia)

    # Se le indica al usuario cuales fueron los datos ingresados por si desea aceptar o no el proceso
    print("\t\t VERIFIQUE LOS DATOS INGRESADOS\n")
    print(obj_materia)

    # Verificacion de ingreso en el sistema
    verificacion = input("Ingrese 1 si quiere ingresar la materia, 2 para revertir el proceso: ")

    if verificacion == "1":
        lista_materias.append(obj_materia)
        return True
    else:
        print("Se ha revertido el proceso\n")
        return False

def verificar_existencia_materia(codigo_materia:str):
    materia = encontrar_materia(codigo_materia)
    if isinstance(materia, Materia):
        return materia
    else:
        return None

def manejar_decision_inscripcion(materia:Materia):
    opcion = input(f"Se ha encontrado la materia '{materia.nombre}'. ¿Desea inscribirla? (S/N): ")
    if opcion.lower() != 's':
        print("Se ha cancelado el proceso de registrar la materia")
        return False
    return True

def verificar_duplicacion_materia(materia:Materia, obj_estudiante:Estudiante, semestre:int):
    if semestre < 1:
        print("ERROR: El número del semestre no puede ser menor a 1")
        return None  # Indica un error

    if verificar_materia(materia, obj_estudiante, semestre):
        return True  # Indica duplicación

    return False # Indica que no hay duplicación

def anexar_materia(obj_estudiante:Estudiante):
    # os.system('cls')

    print("\t\t INGRESE A CONTINUACION LOS DATOS DE LA MATERIA \n")

    codigo_materia = input("Codigo de la materia: ")
    materia = verificar_existencia_materia(codigo_materia)

    if not isinstance(materia, Materia):
        print("ERROR: Materia no encontrada en el sistema")
        return None

    if not manejar_decision_inscripcion(materia):
        return None

    semestre = int(input("\nIngrese el número de semestre en el que se cursará la materia: "))
    if verificar_duplicacion_materia(materia, obj_estudiante, semestre):
        print("ERROR: Se ha intentado ingresar la misma materia dos veces para el mismo semestre")
        return None

    obj_estudiante.incluir_materia(materia, semestre)
    return True

def verificar_existencia_materias_estudiante(obj_estudiante:Estudiante):
    """
    Esta materia verifica si el estudiante tiene materias inscritas o no.

    Args:
        obj_estudiante (Estudiante): El estudiante a hacerle la verificación.

    Returns:
        False: Si el estudiante no tiene materias inscritas.
        True: Si el estudiante tiene materias inscritas.
    """
    if len(obj_estudiante.lista_materias) < 1:
        return False
    else:
        return True


def registrar_notas_main(obj_estudiante:Estudiante):

    # Si el estudiante no tiene materias inscritas
    if not verificar_existencia_materias_estudiante(obj_estudiante):
        return None

    # Se listan las materias inscritas de ese estudiante para que el usuario pueda escoger
    listar_materias(obj_estudiante)

    codigo_materia = input("Ingrese el codigo de la materia a agregar notas: ")
    print("")

    materia = verificar_existencia_materia(codigo_materia)
    if not isinstance(materia, Materia):
        print("ERROR: Materia no encontrada en el sistema")
        return None

    semestre = int(input("Ingrese el numero de semestre en el que esta cursando la materia: "))
    print("")

    if not verificar_duplicacion_materia(materia, obj_estudiante, semestre):
        print("ERROR: El estudiante no tiene inscrita esta materia")
        return None

    # Se devuelve la materia y el semestre
    return materia, semestre

def registrar_notas(obj_estudiante:Estudiante, obj_materia:Materia, num:int):

    while(True):

        """
            Informacion importante:
            1. Una nota tiene que estar en el rango de NOTA_MINIMA y NOTA_MAXIMA segun lo describa la clase `Nota`
            2. Se muestran las anteriores notas cargadas
            3. Se pide el valor de la nota
            4. Se carga a la lista de notas de la relacion EstudianteMateria
        """

        # Encontrar al objeto relacion Estudiante Materia
        relacion = encontrar_objeto(obj_estudiante, obj_materia, num)

        if not isinstance(relacion, Estudiante_Materia):
            print("ERROR AL AGREGAR NOTAS.\n")
            return None

        # Se muestran las anteriores notas cargadas
        if len(relacion.notas) > 0:

            vector_notas = relacion.notas

            print("\nNOTAS CARGADAS ANTERIORES: \n")

            print("+------------------------------------------+----------------------+")
            print("|Descripcion del examen                    |Puntuacion            |")
            print("+------------------------------------------+----------------------+")

            # Recorriendo el vector de notas
            for i in range(0, len(vector_notas)):

                # Obteniendo la nota actual
                obj_nota:Nota = vector_notas[i]

                # Obteniendo los valores al imprimir del objeto nota actual
                descripcion = obj_nota.descripcion_examen
                puntuacion = obj_nota.puntuacion

                print(f"|{descripcion}", end="")
                print(" " * (42 - len(descripcion)), end="")

                print("|", end="")
                print("{:.2f}".format(puntuacion), end="")

                if puntuacion == 10:
                    print("                 |")
                else:
                    print("                  |")

            print("+------------------------------------------+----------------------+\n")
        else:
            print("No existe ninguna nota cargada previamente.\n")

        # Pedir el valor de la nota
        puntuacion = float(input("Ingrese la nota del examen: "))

        descripcion = input("Ingrese la descripcion o nombre del examen: ")

        # Si la nota esta en el rango
        if puntuacion >= 0 and puntuacion <= 10:
            # Cargar el valor de la nota
            relacion.incluir_nota(puntuacion, descripcion)
        else:
            print("La nota debe estar en un rango de 0 a 10pts.")

        opcion = input("Desea agregar otra nota? (Y/N): ")
        print("")

        if opcion.lower() != 'y':
            print("\nTerminando proceso de agregar notas a esta materia.")
            return True


""" ======================= OPERACIONES DE BUSQUEDA  ======================="""

def encontrar_estudiante():

    # Se hara el proceso para encontrar a un estudiante segun la cedula
    cedula = input("Ingrese la cedula del estudiante que desea manipular: ")

    # Proceso de busqueda
    for i in range(0, len(lista_estudiantes)):

        estudiante:Estudiante = lista_estudiantes[i]

        if estudiante.cedula == cedula:
            return estudiante

    return False

def encontrar_materia(codigo_materia):

    for i in range(0, len(lista_materias)):

        if lista_materias[i].codigo_materia == codigo_materia:
            return lista_materias[i]

    return None

def encontrar_objeto(obj_estudiante:Estudiante, obj_materia:Materia, num_semestre:int) -> Estudiante_Materia:

    # Obteniendo la lista de materias del estudiante
    lista = obj_estudiante.lista_materias

    for i in range(0, len(lista)):

        materia_temp:Materia = lista[i].materia

        if obj_materia.codigo_materia == materia_temp.codigo_materia and num_semestre == lista[i].num_semestre:
            return lista[i]

    return None

""" ================= OPERACIONES DE LISTADO: ESTUDIANTE, MATERIAS, NOTAS =================="""
def listar_estudiantes():

    if len(lista_estudiantes) < 1:
        print("No hay estudiantes inscritos\n")
        return

    print("\t\t LISTADO DE ESTUDIANTES \n")

    """    ENCABEZADO DE LA TABLA   """

    bordes()

    print("|Nombre y Apellido", end="")
    print(" " * 23, end="")
    print("|Cedula", end="")
    print(" " * 4, end="")
    print("|Edad |Estatura |Peso    |")

    bordes()

    for i in range(0, len(lista_estudiantes)):

        estudiante:Estudiante = lista_estudiantes[i]

        nombre = estudiante.nombre
        cedula = estudiante.cedula
        edad = estudiante.edad
        estatura = estudiante.estatura
        peso = estudiante.peso

        """ IMPRESION DE LOS VALORES DE CADA ESTUDIANTE """

        # Nombre
        print("|" + nombre, end="")
        print(" " * (40 - len(nombre)), end="")

        # Cedula
        print("|" + cedula, end="")
        print(" " * (10 - len(cedula)), end="")

        # Edad
        print("|" + str(edad), end="")

        if edad < 100:
            print("   ", end="")
        else:
            print("  ", end="")

        # Estatura
        print("|{:.2f}".format(estatura), end="")
        print("   ", end="")

        # Peso
        formatted_peso = "{:4.2f}".format(peso)
        print(f"|{formatted_peso}", end="")

        if peso < 100:
            print("   |", end="")
        else:
            print("  |", end="")

        print("")

    bordes()

def listar_materias(obj_estudiante:Estudiante):

    lista_materias_estudiante = obj_estudiante.lista_materias

    if len(lista_materias_estudiante) < 1:
        print("ERROR: El estudiante no tiene materias inscritas.")
        return

    print(f"\t\t LISTADO DE MATERIAS DEL ESTUDIANTE: {obj_estudiante.nombre} C.I: {obj_estudiante.cedula}\n")

    # Primer borde
    bordes2()

    # Centro con los titulos
    print("|Nombre", end="")
    print(" " * 13, end="")
    print("|Codigo de Materia |Num. del Semestre |")

    # Segundo borde
    bordes2()

    # Recorrido e impresion de los datos de las materias
    for i in range(0, len(lista_materias_estudiante)):

        # Obteniendo temporalmente en un objeto la relacion estudiante materia
        materia_temp = lista_materias_estudiante[i].materia

        # Repartiendo la informacion en variables separadas
        nombre = materia_temp.nombre
        codigo_materia = materia_temp.codigo_materia
        num_semestre = lista_materias_estudiante[i].num_semestre

        # Impresion de los datos
        print(f"|{nombre}", end="")
        print(" " * (19 - len(nombre)), end="")
        print(f"|{codigo_materia}", end="")
        print(" " * (18 - len(codigo_materia)), end="")
        print(f"|{num_semestre}", end="")

        if num_semestre > 10:
            print(" " * 16, end="")
        else:
            print(" " * 17, end="")

        print("|")

    # Borde de cierre de la tabla
    bordes2()

def listar_notas(obj_estudiante:Estudiante):

    # Obtener la lista de materas inscritas del estudiante
    materias_inscritas = obj_estudiante.lista_materias

    # Verificar si el estudiante tiene materias inscritas
    if len(materias_inscritas) < 1:
        print("El estudiante no tiene materias inscritas.\n")
        return

    print(f"\t\t LISTADO DE NOTAS COMPLETO DEL ESTUDIANTE: {obj_estudiante.nombre}, C.I: {obj_estudiante.cedula}\n")

    # Recorrer la lista de materias inscritas
    for i in range(0, len(materias_inscritas)):

        materia_inscrita = materias_inscritas[i]

        obj_materia:Materia = materia_inscrita.materia

        # Obteniendo la lista de notas de la materia inscrita

        notas = materia_inscrita.notas

        # Si no tiene notas asignadas, se continua a la siguiente materia

        if len(notas) < 1:
            continue

        print(f"\nNotas para la materia: {obj_materia.nombre} | Codigo: {obj_materia.codigo_materia} | Semestre: {materia_inscrita.num_semestre}\n")

        print("+------------------------------------------+----------------------+")
        print("|Descripcion del examen                    |Puntuacion            |")
        print("+------------------------------------------+----------------------+")

        # Recorriendo el vector de notas
        for j in range(0, len(notas)):

            # Obteniendo la nota actual
            obj_nota:Nota = notas[j]

            # Obteniendo los valores al primir del objeto nota actual
            descripcion = obj_nota.descripcion_examen
            puntuacion = obj_nota.puntuacion

            print(f"|{descripcion}", end="")
            print(" " * (42 - len(descripcion)), end="")

            print("|", end="")
            print("{:.2f}".format(puntuacion), end="")

            if puntuacion == 10:
                print("                 |")
            else:
                print("                  |")

        print("+------------------------------------------+----------------------+")


""" ======================= OPERACIONES PARA: VERIFICAR ==================="""

def verificar_cedula(cedula) -> bool:

    for i in range(0, len(lista_estudiantes)):

        estudiante_temporal = lista_estudiantes[i]
        if estudiante_temporal.cedula == cedula:
            return True

    return False

def verificar_materia(obj_materia:Materia, obj_estudiante:Estudiante, semestre:int) -> bool:

    # Recorrer el vector de EstudiantesMaterias que son las materias inscritas por el estudiante junto a sus notas
    lista:Estudiante_Materia = obj_estudiante.lista_materias

    for i in range(0, len(lista)):

        materia_temp:Materia = lista[i].materia
        num_semestre = lista[i].num_semestre

        if materia_temp.codigo_materia == obj_materia.codigo_materia and num_semestre == semestre:
            # Esto significa que el codigo de la materia coincide con una de las materias inscrita en su lista
            # Y ademas, los semestres coinciden
            return True

    return False

def bordes():

    print("+", end="")

    # For name
    print("-" * 40, end="")

    print("+", end="")

    # Cedula (ID)
    print("-" * 10, end="")

    print("+", end="")

    # Other
    print("-" * 5, end="")

    print("+", end="")

    # Other
    print("-" * 9, end="")

    print("+", end="")

    # Other
    print("-" * 8, end="")

    print("+")

def bordes2():

    print("+", end="")
    print("-" * 19, end="")
    print("+", end="")
    print("-" * 18, end="")
    print("+", end="")
    print("-" * 18, end="")
    print("+")

if __name__ == "__main__":
    main()