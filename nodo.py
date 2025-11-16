"""
Clase Nodo para representar un nodo en una Red Bayesiana.
Cada nodo tiene un nombre, valores posibles, padres y una tabla de probabilidad condicional.
"""

class Nodo:
    def __init__(self, nombre):
        """
        Inicializa un nodo de la Red Bayesiana.
        
        Args:
            nombre (str): Nombre del nodo
        """
        self.nombre = nombre
        self.valores = []  # Valores posibles que puede tomar el nodo
        self.padres = []   # Lista de nodos padres
        self.hijos = []    # Lista de nodos hijos
        self.tabla_probabilidad = {}  # Tabla de probabilidad condicional
    
    def agregar_valores(self, valores):
        """
        Agrega los valores posibles que puede tomar el nodo.
        
        Args:
            valores (list): Lista de valores posibles
        """
        self.valores = valores
    
    def agregar_padre(self, nodo_padre):
        """
        Agrega un nodo padre a este nodo.
        
        Args:
            nodo_padre (Nodo): Nodo padre a agregar
        """
        if nodo_padre not in self.padres:
            self.padres.append(nodo_padre)
    
    def agregar_hijo(self, nodo_hijo):
        """
        Agrega un nodo hijo a este nodo.
        
        Args:
            nodo_hijo (Nodo): Nodo hijo a agregar
        """
        if nodo_hijo not in self.hijos:
            self.hijos.append(nodo_hijo)
    
    def establecer_probabilidad(self, condiciones, valor, probabilidad):
        """
        Establece una probabilidad en la tabla de probabilidad condicional.
        
        Args:
            condiciones (dict): Diccionario con los valores de los nodos padres
            valor (str): Valor del nodo actual
            probabilidad (float): Probabilidad condicional
        """
        # Convertir condiciones a tupla para usar como clave
        clave_condiciones = tuple(sorted(condiciones.items())) if condiciones else ()
        
        if clave_condiciones not in self.tabla_probabilidad:
            self.tabla_probabilidad[clave_condiciones] = {}
        
        self.tabla_probabilidad[clave_condiciones][valor] = probabilidad
    
    def obtener_probabilidad(self, valor, condiciones=None):
        """
        Obtiene la probabilidad de un valor dado las condiciones de los padres.
        
        Args:
            valor (str): Valor del nodo
            condiciones (dict): Diccionario con los valores de los nodos padres
            
        Returns:
            float: Probabilidad condicional
        """
        if condiciones is None:
            condiciones = {}
        
        clave_condiciones = tuple(sorted(condiciones.items()))
        
        if clave_condiciones in self.tabla_probabilidad:
            if valor in self.tabla_probabilidad[clave_condiciones]:
                return self.tabla_probabilidad[clave_condiciones][valor]
        
        return 0.0
    
    def es_raiz(self):
        """
        Verifica si el nodo es una raíz (sin padres).
        
        Returns:
            bool: True si es raíz, False en caso contrario
        """
        return len(self.padres) == 0
    
    def __str__(self):
        """
        Representación en string del nodo.
        
        Returns:
            str: Representación del nodo
        """
        return f"Nodo: {self.nombre}"
    
    def __repr__(self):
        return self.__str__()
