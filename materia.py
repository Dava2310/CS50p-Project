# Modulos
import re

class Materia:

    """
    Esta clase maneja todos los datos referentes a una materia.
    Permite inicializar un objeto de tipo materia, obtener y/o modificar sus datos.

    Atributos:
        nombre (str): El Nombre de la Materia.
        codigo_materia (str): El Codigo de la Materia, que la identifica como unica al resto de las materias.
    """

    #==========================='Constructor'===========================
    def __init__(self, nombre:str, codigo_materia:str) -> None:
        """
        Inicializa la clase con los atributos dados.

        Args:
            nombre (str): Nombre de la Materia.
            codigo_materia (str): Codigo de la Materia, que la identifica como unica al resto de las materias.
        """

        self.nombre = nombre
        self.codigo_materia = codigo_materia

    #==========================='Nombre'===========================
    @property
    def nombre(self) -> str:
        """
        Devuelve el nombre de la materia.

        Returns:
            str: El nombre de la materia.
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """
        Establece el nombre de la materia.

        Args:
            nombre (str): El nombre de la materia.
        """
        self._nombre = nombre

    #==========================='Codigo de la Materia'===========================
    @property
    def codigo_materia(self) -> str:
        """
        Devuelve el Codigo de la Materia.

        Returns:
            str: El Codigo de la Materia.
        """
        return self._codigo_materia

    @codigo_materia.setter
    def codigo_materia(self, codigo_materia: str):
        """
        Establece el codigo de la materia.

        Args:
            codigo_materia (str): El codigo de la materia.
        """
        self._codigo_materia = codigo_materia

    #==========================='Str(Self)'===========================
    def __str__(self) -> str:
        """
        Devuelve una representacion en cadena de los datos de la materia.

        Returns:
            str: Los datos de la materia en formato de cadena
        """

        return (" ==========  Datos de la Materia =============:\n"
                f"Nombre: {self.nombre}\n"
                f"Codigo: {self.codigo_materia}")