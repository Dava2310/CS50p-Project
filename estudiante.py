# Modulos
import re
from typing import List
from estudiante_materia import Estudiante_Materia
from materia import Materia

class Estudiante:

    """
    Esta clase maneja todos los datos referentes a un estudiante, además de sus operaciones básicas.
    Permite inicializar un objeto de tipo estudiante, obtener o modificar sus datos, y contiene una función
    que agrega una materia al estudiante.

    Atributos:
        nombre (str): Nombre del Estudiante.
        cedula (str): Cédula o ID del Estudiante, que lo identifica como único al resto de los demás estudiantes.
        edad (int): La Edad del Estudiante.
        estatura (float): La estatura o altura del estudiante, en CM.
        peso (float): El peso en KG del Estudiante.
        lista_materias (List[Estudiante_Materia]): Representa una lista de las materias que contiene el estudiante.
    """

    #==========================='Constructor'===========================

    def __init__(self, nombre: str, cedula: str, edad: int, estatura: float, peso: float) -> None:
        """
        Inicializa la clase con los atributos dados.

        Args:
            nombre (str): Nombre del Estudiante.
            cedula (str): Cédula o ID del estudiante, que lo identifica como único al resto de los demás estudiantes.
            edad (int): La Edad del Estudiante.
            estatura (float): La estatura o altura del estudiante, en CM.
            peso (float): El peso en KG del Estudiante.
        """
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.estatura = estatura
        self.peso = peso
        self._lista_materias: List[Estudiante_Materia] = []


    #==========================='Lista de Materias'===========================

    @property
    def lista_materias(self):
        """
        Devuelve la lista de materias asignadas a este estudiante.

        La lista contiene, por cada posición, un objeto que representa una materia, el número de semestre
        y las notas obtenidas.

        Returns:
            list: Una lista de objetos `Estudiante_Materia`, cada uno representando una materia asignada al estudiante.
        """
        return self._lista_materias

    #==========================='Nombre'===========================
    @property
    def nombre(self) -> str:
        """
        Devuelve el nombre del estudiante.

        Returns:
            str: El nombre del estudiante.
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """
        Establece el nombre del estudiante después de validar que cumple con el formato adecuado.

        Args:
            nombre (str): El nombre del estudiante.

        Raises:
            ValueError: Si el nombre no es válido.
        """
        regex = r'^[a-zA-ZÀ-ÿ\s]{2,40}$'
        if not re.match(regex, nombre, re.IGNORECASE):
            raise ValueError("Nombre inválido: debe contener solo letras y espacios, y tener entre 2 y 40 caracteres.")
        self._nombre = nombre

    #==========================='Cedula'===========================
    @property
    def cedula(self) -> str:
        """
        Devuelve la cédula del estudiante.

        Returns:
            str: La cédula del estudiante.
        """
        return self._cedula

    @cedula.setter
    def cedula(self, cedula: str):
        """
        Establece la cédula del estudiante después de validar que cumple con el formato adecuado.

        Args:
            cedula (str): La cédula del estudiante.

        Raises:
            ValueError: Si la cédula no es válida con el formato de Venezuela (6 a 9 digitos numericos).
        """
        regex = r'^\d{6,9}$'
        if not re.match(regex, cedula, re.IGNORECASE):
            raise ValueError("Cedula inválida: solo puede tener números, y debe ser entre 6 a 9 digitos.")
        self._cedula = cedula

    #==========================='Edad'===========================
    @property
    def edad(self) -> int:
        """
        Devuelve la edad del estudiante.

        Returns:
            int: La edad del estudiante.
        """
        return self._edad

    @edad.setter
    def edad(self, edad: int):
        """
        Establece la edad del estudiante después de validar que cumple con el formato adecuado.

        Args:
            edad (int): La edad del estudiante.

        Raises:
            ValueError: Si la edad no es un entero o si el estudiante es menor de 18 años.
        """
        if not isinstance(edad, int):
            raise ValueError("La edad debe ser un número entero.")
        if edad < 18:
            raise ValueError("El estudiante debe ser mayor de edad.")
        self._edad = edad

    #==========================='Estatura'===========================
    @property
    def estatura(self) -> float:
        """
        Devuelve la estatura del estudiante.

        Returns:
            float: La estatura del estudiante en CM.
        """
        return self._estatura

    @estatura.setter
    def estatura(self, estatura: float):
        """
        Establece la estatura del estudiante después de validar que cumple con el formato adecuado.

        Args:
            estatura (float): La estatura del estudiante en CM.

        Raises:
            ValueError: Si la estatura no es un valor de tipo float.
        """
        if not isinstance(estatura, float):
            raise ValueError("La estatura debe ser un valor numérico de coma flotante.")
        self._estatura = estatura

    #==========================='Peso'===========================
    @property
    def peso(self) -> float:
        """
        Devuelve el peso del estudiante.

        Returns:
            float: El peso del estudiante en KG.
        """
        return self._peso

    @peso.setter
    def peso(self, peso: float):
        """
        Establece el peso del estudiante después de validar que cumple con el formato adecuado.

        Args:
            peso (float): El peso del estudiante en KG.

        Raises:
            ValueError: Si el peso no es un valor de tipo float o si está fuera del rango válido.
        """
        if not isinstance(peso, float):
            raise ValueError("El peso debe ser un valor numérico de coma flotante.")
        if peso >= 1000 or peso < 0:
            raise ValueError("Este peso esta fuera de los límites esperandos.")
        self._peso = peso

    #==========================='MÉTODOS'===========================

    #==========================='Incluir Materia'===========================
    def incluir_materia(self, obj_materia: Materia, num: int):
        """
        Agrega una nueva materia a la lista de materias del estudiante.

        Args:
            obj_materia (Materia): El objeto materia a agregar.
            num (int): El número de semestre en el que se cursa la materia.
        """
        nuevo_objeto = Estudiante_Materia(obj_materia, num)
        self._lista_materias.append(nuevo_objeto)

    #==========================='Str(Self)'===========================
    def __str__(self) -> str:
        """
        Devuelve una representación en cadena de los datos del estudiante.

        Returns:
            str: Los datos del estudiante en formato de cadena.
        """
        return (" ==========  Datos del estudiante =============:\n"
                f"Nombre: {self.nombre}\n"
                f"Cédula: {self.cedula}\n"
                f"Edad: {self.edad}\n"
                f"Estatura: {self.estatura}\n"
                f"Peso: {self.peso}")