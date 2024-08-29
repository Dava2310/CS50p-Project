# Modulos
from nota import Nota
from materia import Materia
from typing import List

class Estudiante_Materia:
    """
    Esta clase maneja todos los datos referentes a la relación que existe entre un estudiante
    y una materia. Cada estudiante contiene varios objetos de este tipo, que representan
    una materia, el número de semestre en el que se cursó, y las notas obtenidas en dicha materia.

    El sistema está diseñado para contemplar que el estudiante pueda cursar la misma materia
    varias veces, sin embargo, el objeto es diferente puesto que contendrá notas diferentes y no
    sucederá en el mismo semestre.

    Atributos:
        materia (Materia): Un objeto de la clase Materia, que representa la materia de esta relación.
        num_semestre (int): El número del semestre en el que se cursa la materia.
        notas (List[Nota]): Representa la lista de notas que el estudiante obtiene o obtuvo de la materia.
    """

    #==========================='Constructor'===========================
    def __init__(self, obj_materia: Materia, num: int) -> None:
        """
        Inicializa la clase con los atributos dados.

        Args:
            obj_materia (Materia): La materia que el estudiante está cursando.
            num (int): El número del semestre cuando se cursa la materia.
        """
        self._materia = obj_materia
        self._num_semestre = num
        self._notas: List[Nota] = []  # La lista de objetos de tipo `Nota` que representa esta relación.

    #==========================='Materia'===========================
    @property
    def materia(self) -> Materia:
        """
        Devuelve la materia que representa esta relación.

        Returns:
            Materia: El objeto Materia de esta relación.
        """
        return self._materia

    #==========================='Número del Semestre'===========================
    @property
    def num_semestre(self) -> int:
        """
        Devuelve el número de semestre cuando se cursó la materia de esta relación.

        Returns:
            int: El número del semestre de esta relación.
        """
        return self._num_semestre

    #==========================='Notas'===========================
    @property
    def notas(self) -> List[Nota]:
        """
        Devuelve la lista de notas de esta relación.

        Returns:
            List[Nota]: Una lista de objetos de tipo `Nota`, cada una representa una calificación del estudiante en esta materia.
        """
        return self._notas

    #==========================='Métodos'===========================
    def incluir_nota(self, nota: float, descripcion: str) -> None:
        """
        Este método permite agregar un objeto de tipo `Nota` o calificación a esta relación.

        Args:
            nota (float): La calificación de la nota.
            descripcion (str): La descripción o asunto que refiere a esta nota.
        """
        # Creando el objeto de tipo `Nota`
        nueva_nota = Nota(nota, descripcion)

        # Añadiendo el nuevo objeto de tipo `Nota` a la lista de notas de esta relación.
        self._notas.append(nueva_nota)

        # Mensaje de éxito para el usuario.
        print("\nNota cargada con éxito.\n\n")
