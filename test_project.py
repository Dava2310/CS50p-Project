import pytest
import project
from materia import Materia
from estudiante import Estudiante
from estudiante_materia import Estudiante_Materia
from unittest.mock import patch

@pytest.fixture(autouse=True)
def run_around_tests():
    global project
    project.lista_estudiantes = [] # Asegura que la lista_estudiantes de project se reinicie antes de cada prueba
    project.lista_materias = []
    yield
    project.lista_estudiantes = [] # Reinicia la lista_estudiantes de project después de cada prueba
    project.lista_materias = []

# NOTA: No se debe agregar test_ a las funciones de crear estudiante o materia
# Sino, los datos que estas creen se borraran.

def crear_estudiante(nombre, cedula, edad, estatura, peso):
    inputs = ["1"]  # Simula la entrada de "1" para aceptar la verificación
    with patch('builtins.input', side_effect=inputs):
        project.crear_estudiante(nombre, cedula, edad, estatura, peso)

def crear_materia(codigo, nombre):
    inputs = ["1"]  # Simula la entrada de "1" para aceptar la creación de la materia
    with patch('builtins.input', side_effect=inputs):
        project.crear_materia(codigo, nombre)

def anexar_materia(codigo_materia, num_semestre, estudiante):
    inputs = [codigo_materia, "s", num_semestre]
    with patch('builtins.input', side_effect=inputs):
        return project.anexar_materia(estudiante)


def test_obtener_datos_estudiante_cedula_no_existente():
    # Simula los datos que se ingresaran a traves del input
    nombre = "Juan Perez"
    cedula = "12345678"
    edad = "20"
    estatura = "180.5"
    peso = "75.0"

    # Define las entradas simuladas
    inputs = [cedula, nombre, edad, estatura, peso]

    with patch('builtins.input', side_effect=inputs):
            resultado = project.obtener_datos_estudiante()

    assert resultado == (nombre, cedula, int(edad), float(estatura), float(peso))

def test_obtener_datos_estudiante_cedula_existente():
    # Primero creamos un estudiante auxiliar
    nombre = "Juan Perez"
    cedula = "12345678"
    edad = 20
    estatura = 180.5
    peso = 75.0

    # Define las entradas simuladas para crear el estudiante
    inputs = ["1"]  # Simula la entrada de "1" para aceptar la verificación

    with patch('builtins.input', side_effect=inputs):
        project.crear_estudiante(nombre, cedula, edad, estatura, peso)

    # Ahora que ya tenemos un estudiante registrado, intentamos ingresar el mismo estudiante
    nombre = "Juan Perez"
    cedula = "12345678"
    edad = "20"
    estatura = "180.5"
    peso = "75.0"

    # Define las entradas simuladas
    inputs = [cedula, nombre, edad, estatura, peso]

    with patch('builtins.input', side_effect=inputs):
        resultado = project.obtener_datos_estudiante()

    # Verificando que no se hayan podido obtener los datos
    assert resultado is None

def test_crear_estudiante_aceptado():
    nombre = "Juan Perez"
    cedula = "12345678"
    edad = 20
    estatura = 180.5
    peso = 75.0

    # Define las entradas simuladas para crear el estudiante
    inputs = ["1"]  # Simula la entrada de "1" para aceptar la verificación

    with patch('builtins.input', side_effect=inputs):
        resultado = project.crear_estudiante(nombre, cedula, edad, estatura, peso)

    # Verifica que el estudiante haya sido agregado a la lista de estudiantes si el proceso fue aceptado
    assert resultado is True
    assert len(project.lista_estudiantes) == 1
    assert project.lista_estudiantes[0].nombre == nombre
    assert project.lista_estudiantes[0].cedula == cedula
    assert project.lista_estudiantes[0].edad == edad
    assert project.lista_estudiantes[0].estatura == estatura
    assert project.lista_estudiantes[0].peso == peso

def test_crear_estudiante_revertido():
    nombre = "Juan Perez"
    cedula = "12345678"
    edad = 20
    estatura = 180.5
    peso = 75.0

    # Define las entradas simuladas para crear el estudiante
    inputs = ["2"]  # Simula la entrada de "1" para aceptar la verificación

    with patch('builtins.input', side_effect=inputs):
        resultado = project.crear_estudiante(nombre, cedula, edad, estatura, peso)

    # Verifica que el estudiante no haya sido agregado a la lista de estudiantes si el proceso fue revertido
    assert resultado is False
    assert len(project.lista_estudiantes) == 0

def test_obtener_datos_materia_codigo_no_existente():
    # Simula los datos que se ingresaran a traves del input
    nombre = "Matematica I"
    codigo_materia = "12345"

    # Define las entradas simuladas
    inputs = [codigo_materia, nombre]

    with patch('builtins.input', side_effect = inputs):
        resultado = project.obtener_datos_materia()

    assert resultado == (codigo_materia, nombre)

def test_obtener_datos_materia_codigo_existente():
    # Primero creamos una materia auxiliar
    codigo_materia = "12345"
    nombre = "Matematica I"

    # Define las entradas simuladas para crear la materia
    inputs = ["1"]  # Simula la entrada de "1" para aceptar la verificación

    with patch('builtins.input', side_effect=inputs):
        project.crear_materia(codigo_materia, nombre)

    # Ahora que ya se tiene a una materia registrada, intentamos ingresar una materia con el mismo codigo
    codigo_materia = "12345"
    nombre = "Matematica II"

    # Define las entradas simuladas para crear la materia
    inputs = [codigo_materia, nombre]  # Simula la entrada de "1" para aceptar la verificación

    with patch('builtins.input', side_effect=inputs):
        resultado = project.obtener_datos_materia()

    assert resultado is None

def test_crear_materia_aceptado():

    # Datos de la materia
    codigo_materia = "12345"
    nombre = "Matematica I"

    # Define la entrada de usuario para la verificacion del proceso
    inputs = ["1"]

    with patch('builtins.input', side_effect=inputs):
        resultado = project.crear_materia(codigo_materia, nombre)

    # Verifica que la materia haya sido agregada a la lista de materias si el proceso fue aceptado
    assert resultado is True
    assert len(project.lista_materias) == 1
    assert project.lista_materias[0].nombre == nombre
    assert project.lista_materias[0].codigo_materia == "12345"

def test_crear_materia_revertido():

    # Datos de la materia
    codigo_materia = "12345"
    nombre = "Matematica I"

    # Define la entrada de usuario para la verificacion del proceso
    inputs = ["2"] # En este caso no es 1, por tanto, no se deberia registrar

    with patch('builtins.input', side_effect=inputs):
        resultado = project.crear_materia(codigo_materia, nombre)

    # Verifica que la materia no haya sido agregada a la lista de materias si el proceso fue negado o revertido
    assert resultado is False
    assert len(project.lista_materias) == 0


def test_verificar_existencia_materia():

    """
    Este test probara si con el codigo de la materia, existe o no dentro del sistema.

    Para ello, debemos crear materias en la lista del sistema, y despues verificar con varios
    codigos si las materias se encuentran o no en la lista.
    """

    crear_materia("12345", "Matematica I")
    crear_materia("123456", "Matematica II")
    crear_materia("1234567", "Matematica III")

    # Ahora verificaremos con diferentes codigos si existe la materia o no

    # Pruebas de que no deberia existir
    assert project.verificar_existencia_materia("12") is None
    assert project.verificar_existencia_materia("123") is None
    assert project.verificar_existencia_materia("122342") is None

    # Pruebas de que deberia existir
    assert isinstance(project.verificar_existencia_materia("12345"),Materia) == True
    assert isinstance(project.verificar_existencia_materia("123456"),Materia) == True
    assert isinstance(project.verificar_existencia_materia("1234567"),Materia) == True

    # Prueba de que existen tres materias
    assert len(project.lista_materias) == 3

def test_manejar_decision_inscripcion():
    """
    Este test simple probara si se captura correctamente la respuesta del usuario.

    Debemos primero crear una materia, para poderla ingresar por parametro.
    """

    # No es necesario crear la materia en el sistema
    obj_materia = Materia("Matematica I", "12345")

    # Verificar si se recoge correctamente la decision del usuario
    inputs = ["s"]
    with patch('builtins.input', side_effect=inputs):
        resultado = project.manejar_decision_inscripcion(obj_materia)
        assert resultado == True

    inputs = ["S"]
    with patch('builtins.input', side_effect=inputs):
        resultado = project.manejar_decision_inscripcion(obj_materia)
        assert resultado == True

    inputs = ["N"]
    with patch('builtins.input', side_effect=inputs):
        resultado = project.manejar_decision_inscripcion(obj_materia)
        assert resultado == False

    inputs = ["HFHG"]
    with patch('builtins.input', side_effect=inputs):
        resultado = project.manejar_decision_inscripcion(obj_materia)
        assert resultado == False

def test_verificar_duplicacion_materia():
    """
    Este test verifica si funciona correctamente la funcion que verifica que no existan duplicaciones de
    materia. Para que exista una duplicacion, es que se intenta ingresar la misma materia en un mismo
    semestre para un estudiante.

    Los requisitos para hacer esta prueba es crear una materia, crear un estudiante, anexarle la materia
    a dicho estudiante para un semestre, y probar con el mismo semestre y con semestres diferentes
    """

    # Crear el Estudiante
    obj_estudiante = Estudiante("Daniel", "29517648", 20, 160.5, 60.5)

    # Crear Materias
    obj_materia = Materia("Matematica I", "12345")
    obj_materia_dos = Materia("Matematica II", "123456")

    # Anexando la materia al estudiante de forma interna
    obj_estudiante.incluir_materia(obj_materia, 1)
    obj_estudiante.incluir_materia(obj_materia_dos, 2)

    # Prueba de que existe duplicacion
    resultado = project.verificar_duplicacion_materia(obj_materia, obj_estudiante, 1)
    assert resultado == True

    resultado = project.verificar_duplicacion_materia(obj_materia_dos, obj_estudiante, 2)
    assert resultado == True

    # Prueba de que no existe duplicacion
    resultado = project.verificar_duplicacion_materia(obj_materia, obj_estudiante, 2)
    assert resultado == False

    resultado = project.verificar_duplicacion_materia(obj_materia, obj_estudiante, 3)
    assert resultado == False

    resultado = project.verificar_duplicacion_materia(obj_materia_dos, obj_estudiante, 1)
    assert resultado == False

    resultado = project.verificar_duplicacion_materia(obj_materia_dos, obj_estudiante, 3)
    assert resultado == False

    # Prueba cuando se intenta ingresar un semestre invalido
    resultado = project.verificar_duplicacion_materia(obj_materia, obj_estudiante, 0)
    assert resultado is None

def test_anexar_materia():
    """
    Este test buscara verificar si el anexo de una materia a un estudiante funciona de forma correcta.

    Para ello, debemos primero crear a un estudiante y a una materia dentro del sistema,
    despues simular la entrada del codigo de la materia existente, la decision de que si
    queremos inscribirla, y el semestre en que la vera.

    Y, verificar si el estudiante tiene dicha materia en su lista de materias.
    """

    # Crear a un estudiante dentro del sistema
    nombre = "Juan Perez"
    cedula = "12345678"
    edad = 20
    estatura = 180.5
    peso = 75.0

    crear_estudiante(nombre, cedula, edad, estatura, peso)
    estudiante = project.lista_estudiantes[0]
    assert isinstance(estudiante, Estudiante)

    # Crear a una materia dentro del sistema
    nombre_materia = "Matematica I"
    codigo_materia = "12345"

    crear_materia(codigo_materia, nombre_materia)
    materia = project.lista_materias[0]
    assert isinstance(materia, Materia)

    # Anexando la materia
    resultado = anexar_materia("12345", 1, estudiante)

    # Cuando el proceso es valido, verificamos si primero la funcion devuelve True
    assert resultado == True

    # Despues verificamos si se encuentra en la lista del estudiante
    lista_materias = estudiante.lista_materias
    assert len(lista_materias) == 1

    # Ahora verifiquemos anexar la misma materia
    inputs = ["12345", "s", 1]
    with patch('builtins.input', side_effect=inputs):
        resultado = project.anexar_materia(estudiante)

    assert resultado == None

    # Ahora verifiquemos anexar una materia no existente
    inputs = ["123456", "s", 1]
    with patch('builtins.input', side_effect=inputs):
        resultado = project.anexar_materia(estudiante)

    assert resultado == None

    # Ahora verifiquemos anexar una materia diciendo que no al proceso
    inputs = ["123456", "n", 1]
    with patch('builtins.input', side_effect=inputs):
        resultado = project.anexar_materia(estudiante)

    assert resultado == None

    # Por ultimo, verifiquemos anexar la misma materia pero en otro semestre
    inputs = ["12345", "s", 2]
    with patch('builtins.input', side_effect=inputs):
        resultado = project.anexar_materia(estudiante)

    assert resultado == True

    # Para este momento, deberian de haber 2 materias para el mismo estudiante
    assert len(lista_materias) == 2

def test_verificar_existencia_materias_estudiante():
    """
    Esta prueba se encarga de testear la funcion: verificar_existencia_materias_estudiante

    Esa funcion verifica si el estudiante tiene materias inscritas o no, por tanto es necesario:
    1. Crear a un estudiante en el sistema
    2. Crear a una materia en el sistema.
    3. Anexarle la materia en el sistema.
    4. Verificar si devuelve True la funcion.

    Tambien se debe verificar antes de anexarle la materia si devuelve False la funcion.
    """

    # 1. Crear a un estudiante en el sistema
    crear_estudiante("Daniel Vetencourt", "29517648", 23, 160.5, 70.5)
    estudiante = project.lista_estudiantes[0]

    # 2. Crear a una materia en el sistema
    crear_materia("12345", "Matematica I")

    # Verificar que el estudiante no tiene materias inscritas
    assert project.verificar_existencia_materias_estudiante(estudiante) == False

    # 3. Anexarle al estudiante la materia en el sistema
    anexar_materia("12345", 1, estudiante)

    # 4. Ahora verificar que el estudiante si tiene materias inscritas
    assert project.verificar_existencia_materias_estudiante(estudiante) == True


def test_registrar_notas_main():
    """
    Esta prueba verifica si se podra correctamente anexar notas a un estudiante con unas notas particulares

    Prueba de Exito:

    Consiste en probar que se registraran notas con una materia anexada.
    Tiene que ser el mismo codigo de materia y el mismo semestre.

    Prueba de Fracaso:

    1. Probar que se registraran notas con una materia no anexada.
    Una materia no anexada es una materia existente pero no en el semestre correcto

    2. Probar que se registraran notas con una materia inexistente
    para el sistema.
    """

    # Crear a un estudiante dentro del sistema
    crear_estudiante("Juan Perez", "12345678", 20, 180.5, 75.0)
    estudiante = project.lista_estudiantes[0]
    assert isinstance(estudiante, Estudiante)

    # Crear a una materia dentro del sistema
    crear_materia("12345", "Matematica I")
    materia = project.lista_materias[0]
    assert isinstance(materia, Materia)

    # Anexarle la materia al estudiante
    anexar_materia("12345", 1, estudiante)

    # Prueba de Exito
    inputs = ["12345", "1"]
    with patch('builtins.input', side_effect=inputs):
        resultado = project.registrar_notas_main(estudiante)

    assert resultado == (materia, 1)

    # Prueba 1 de Fracaso
    inputs = ["12345", "2"]
    with patch('builtins.input', side_effect=inputs):
        resultado = project.registrar_notas_main(estudiante)

    assert resultado == None

    # Prueba 2 de Fracaso
    inputs = ["123456", "1"]
    with patch('builtins.input', side_effect=inputs):
        resultado = project.registrar_notas_main(estudiante)

    assert resultado == None

def test_encontrar_objeto():

    """
    Esta prueba se encargara de testear la funcion encontrar_objeto
    Para ello, debemos:

    1. Crear a un estudiante
    2. Crear una materia
    3. Anexar la materia al estudiante

    Casos de Prueba:
        Exito: Verificar si con los datos validos, devuelve un objeto de tipo Estudiante_Materia
        Fracaso: Con datos no validos, verificar que devuelva None
    """

    # 1. Crear estudiante
    crear_estudiante("Daniel Vetencourt", "29517648", 22, 160.5, 70.5)
    estudiante = project.lista_estudiantes[0]

    # 2. Crear Materia
    crear_materia("12345", "Matematica I")
    crear_materia("123456", "Matematica II")

    materia_uno = project.lista_materias[0]
    materia_dos = project.lista_materias[1]

    # 3. Anexar la materia
    anexar_materia("12345", 1, estudiante)
    anexar_materia("123456", 2, estudiante)

    # Prueba Exito
    assert isinstance(project.encontrar_objeto(estudiante, materia_uno, 1), Estudiante_Materia)
    assert isinstance(project.encontrar_objeto(estudiante, materia_dos, 2), Estudiante_Materia)

    # Prueba Fracaso
    assert project.encontrar_objeto(estudiante, materia_uno, 2) is None
    assert project.encontrar_objeto(estudiante, materia_dos, 1) is None

def test_verificar_cedula():
    """
    Esta prueba se encargara de probar la funcion verificar_cedula()

    Para ello, debemos registrar al menos dos o tres estudiantes, y verificar
    con las cedulas de los estudiantes, que devuelva True, y con cedulas de
    estudiantes inexistentes, que devuelva False
    """

    # Registrando estudiantes
    crear_estudiante("Daniel Vetencourt", "29517648", 22, 160.5, 70.5)
    crear_estudiante("Carlos Vetencourt", "7383981", 57, 159.0, 123.0)
    crear_estudiante("Gabriel Antuarez", "28216052", 57, 175.0, 90.0)

    # Pruebas de Exito
    assert project.verificar_cedula("29517648") == True
    assert project.verificar_cedula("28216052") == True
    assert project.verificar_cedula("7383981") == True

    # Pruebas de Fracaso
    assert project.verificar_cedula("123456") == False
    assert project.verificar_cedula("ABCV") == False

def test_verificar_materia():
    """
    Esta prueba consiste en probar la funcion de verificar_materia() del archivo principal.
    Para ello, debemos registrar un estudiante, una materia, anexarle la materia

    Y verificar con la misma materia si devuelve True, y verificar con otra materia si devuelve false
    """

    # Registrando estudiante
    crear_estudiante("Daniel Vetencourt", "29517648", 22, 160.5, 70.5)
    estudiante = project.lista_estudiantes[0]

    # Registrando materias
    crear_materia("12345", "Matematica I")
    crear_materia("123456", "Matematica II")

    materia_uno = project.lista_materias[0]
    materia_dos = project.lista_materias[1]

    # Anexando materias
    anexar_materia("12345", 1, estudiante)
    anexar_materia("123456", 2, estudiante)

    # Caso de Prueba de Exito
    assert project.verificar_materia(materia_uno, estudiante, 1) == True
    assert project.verificar_materia(materia_dos, estudiante, 2) == True

    # Caso de Prueba de Frcaso
    assert project.verificar_materia(materia_uno, estudiante, 2) == False
    assert project.verificar_materia(materia_dos, estudiante, 1) == False

def test_registrar_nota():
    """
    Esta prueba testeará la función de registrar_notas

    Para ello, debemos registrar al estudiante, la materia y anexarle la materia.
    Después de ello, simular la carga de una única nota, y verificar si dicha nota
    existe en su relación de Estudiante_Materia
    """

    # 1. Crear el estudiante
    crear_estudiante("Daniel Vetencourt", "29517648", 22, 160.5, 70.5)
    estudiante = project.lista_estudiantes[0]

    # 2. Crear la materia
    crear_materia("12345", "Matematica I")
    materia_uno = project.lista_materias[0]

    # Creando otra materia para probar
    crear_materia("123456", "Matematica II")
    materia_dos = project.lista_materias[1]

    # 3. Anexarle la materia
    anexar_materia("12345", 1, estudiante)

    # Verificar si la materia está anexada
    assert len(estudiante.lista_materias) == 1

    inputs = ["10", "Primer Parcial", "N"]
    with patch('builtins.input', side_effect=inputs):
        resultado = project.registrar_notas(estudiante, materia_uno, 1)

    # Verificando si hasta ahora todo debería estar bien
    assert resultado is True

    # Obteniendo la relación estudiante materia
    relacion = estudiante.lista_materias[0]

    # Verificando los datos de la relación
    assert relacion.materia == materia_uno
    assert relacion.num_semestre == 1

    # Verificando que la relación entre estudiante y materia ya tiene una nota registrada
    assert len(relacion.notas) == 1

    # Obteniendo el objeto nota
    nota = relacion.notas[0]

    # Verificando los datos del objeto nota
    assert nota.puntuacion == 10
    assert nota.descripcion_examen == "Primer Parcial"

    # Haciendo el proceso por segunda vez
    anexar_materia("123456", 2, estudiante)

    # Intentando agregar una nota con una materia pero en el semestre equivocado
    inputs = ["9", "Segundo Parcial", "N"]  # Nota en semestre incorrecto
    with patch('builtins.input', side_effect=inputs):
        resultado = project.registrar_notas(estudiante, materia_dos, 1)

    assert resultado is None

    # Redefinir inputs para la segunda iteración
    inputs_dos = ["9", "Segundo Parcial", "Y", "8.5", "Tercer Parcial", "N"]  # Notas en semestre correcto
    with patch('builtins.input', side_effect=inputs_dos):
        resultado = project.registrar_notas(estudiante, materia_dos, 2)

    assert resultado is True

    # Verificando si la segunda materia tiene dos notas
    relacion_dos = estudiante.lista_materias[1]
    assert len(relacion_dos.notas) == 2

    # Verificando los datos del objeto nota
    nota_uno = relacion_dos.notas[0]
    assert nota_uno.puntuacion == 9
    assert nota_uno.descripcion_examen == "Segundo Parcial"

    nota_dos = relacion_dos.notas[1]
    assert nota_dos.puntuacion == 8.5
    assert nota_dos.descripcion_examen == "Tercer Parcial"