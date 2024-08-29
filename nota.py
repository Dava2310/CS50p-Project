# Constantes que definen el limite de calificacion del sistema.
MAXIMA_NOTA = 10
MENOR_NOTA = 0

class Nota:
    """
    Esta clase maneja los datos referentes a una nota, que son la calificacion y su descripcion.
    Permite agregar o modificar estos datos, asi como inicializar un objeto de esta clase.
    Contiene ademas validaciones que permiten que se manejen notas con puntuaciones unicamente entre 0 a 10.

    Atributos:
        puntuacion (float): El valor cuantitativo de la nota.
        descripcion_examen (str): Representa la razon de la nota, una descripcion breve del examen.
    """

    #==========================='Constructor'===========================
    def __init__(self, puntuacion:float, descripcion_examen:str) -> None:
        """
        Inicializa la clase con los atributos dados.

        Args:
            puntuacion (float): El valor cuantitativo de la nota.
            descripcion_examen (str): Representa la razon de la nota, una descripcion breve del examen.
        """
        # Atributes
        self.puntuacion = puntuacion
        self.descripcion_examen = descripcion_examen

    #==========================='Puntuacion'===========================
    @property
    def puntuacion(self) -> float:
        """
        Devuelve la puntuacion de la nota establecida.

        Returns:
            float: La puntuacion de la nota.
        """
        return self._puntuacion

    @puntuacion.setter
    def puntuacion(self, puntuacion:float) -> None:
        """
        Establece la puntuacion o valor cuantitativo de la nota, después de validar que esté en el rango establecido para el sistema.

        Args:
            puntuacion (float): La puntuacion de la nota.

        Raises:
            ValueError: Si la puntuacion no es de tipo flotante o si no esta en el rango establecido para el sistema.

        """

        if not type(puntuacion) == float:
            raise ValueError("Invalid score")

        if puntuacion < MENOR_NOTA or puntuacion > MAXIMA_NOTA:
            raise ValueError(f"Range of score is within {MENOR_NOTA}-{MAXIMA_NOTA}")

        self._puntuacion = puntuacion

    #==========================='Descripcion'===========================

    @property
    def descripcion_examen(self) -> str:
        """
        Devuelve la descripcion del examen que se adjunta a esta nota.

        Returns:
            str: La descripcion del examen que se adjunta a esta nota.
        """
        return self._descripcion_examen

    @descripcion_examen.setter
    def descripcion_examen(self, descripcion:str) -> None:
        """
        Establece la descripcion del examen que se adjunta a esta nota, despues de verificar que no este vacia.

        Args:
            descripcion (str): La descripcion del examen de la nota.

        Raises:
            ValueError: Si la descripcion esta vacia.
        """
        if len(descripcion) == 0:
            raise ValueError("Invalid description")

        self._descripcion_examen = descripcion