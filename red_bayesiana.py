"""
Clase RedBayesiana para representar y manipular una Red Bayesiana completa.
Incluye funcionalidades para cargar la estructura desde archivo, cargar probabilidades,
y visualizar la red y sus tablas de probabilidad.
"""

from nodo import Nodo
import re

class RedBayesiana:
    def __init__(self):
        """
        Inicializa una Red Bayesiana vacía.
        """
        self.nodos = {}  # Diccionario de nodos (nombre -> Nodo)
        self.raices = []  # Lista de nodos raíz
    
    def agregar_nodo(self, nombre):
        """
        Agrega un nodo a la red si no existe.
        
        Args:
            nombre (str): Nombre del nodo
            
        Returns:
            Nodo: El nodo creado o existente
        """
        if nombre not in self.nodos:
            self.nodos[nombre] = Nodo(nombre)
        return self.nodos[nombre]
    
    def obtener_nodo(self, nombre):
        """
        Obtiene un nodo de la red.
        
        Args:
            nombre (str): Nombre del nodo
            
        Returns:
            Nodo: El nodo solicitado o None si no existe
        """
        return self.nodos.get(nombre)
    
    def cargar_estructura(self, archivo_estructura):
        """
        Carga la estructura de la red desde un archivo.
        
        Formato del archivo:
        Nodo_Padre -> Nodo_Hijo
        
        Args:
            archivo_estructura (str): Ruta al archivo de estructura
        """
        print(f"\n{'='*60}")
        print("CARGANDO ESTRUCTURA DE LA RED BAYESIANA")
        print(f"{'='*60}")
        
        with open(archivo_estructura, 'r', encoding='utf-8') as f:
            for linea in f:
                linea = linea.strip()
                
                # Ignorar líneas vacías y comentarios
                if not linea or linea.startswith('#'):
                    continue
                
                # Parsear la relación padre -> hijo
                if '->' in linea:
                    partes = linea.split('->')
                    nombre_padre = partes[0].strip()
                    nombre_hijo = partes[1].strip()
                    
                    # Crear o obtener nodos
                    nodo_padre = self.agregar_nodo(nombre_padre)
                    nodo_hijo = self.agregar_nodo(nombre_hijo)
                    
                    # Establecer relaciones
                    nodo_hijo.agregar_padre(nodo_padre)
                    nodo_padre.agregar_hijo(nodo_hijo)
                    
                    print(f"  Relación agregada: {nombre_padre} -> {nombre_hijo}")
        
        # Identificar nodos raíz
        self.raices = [nodo for nodo in self.nodos.values() if nodo.es_raiz()]
        
        print(f"\n  Nodos raíz identificados: {[r.nombre for r in self.raices]}")
        print(f"  Total de nodos en la red: {len(self.nodos)}")
    
    def cargar_probabilidades(self, archivo_probabilidades):
        """
        Carga las tablas de probabilidad desde un archivo.
        
        Args:
            archivo_probabilidades (str): Ruta al archivo de probabilidades
        """
        print(f"\n{'='*60}")
        print("CARGANDO TABLAS DE PROBABILIDAD")
        print(f"{'='*60}")
        
        with open(archivo_probabilidades, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # Dividir por secciones de nodos [NombreNodo]
        secciones = re.split(r'\[(\w+)\]', contenido)
        
        i = 1
        while i < len(secciones):
            nombre_nodo = secciones[i].strip()
            contenido_seccion = secciones[i + 1].strip()
            
            if nombre_nodo in self.nodos:
                nodo = self.nodos[nombre_nodo]
                print(f"\n  Procesando nodo: {nombre_nodo}")
                
                lineas = contenido_seccion.split('\n')
                padres = []
                
                for linea in lineas:
                    linea = linea.strip()
                    if not linea or linea.startswith('#'):
                        continue
                    
                    # Parsear valores posibles
                    if linea.startswith('values:'):
                        valores_str = linea.replace('values:', '').strip()
                        valores = [v.strip() for v in valores_str.split(',')]
                        nodo.agregar_valores(valores)
                        print(f"    Valores: {valores}")
                    
                    # Parsear padres
                    elif linea.startswith('parents:'):
                        padres_str = linea.replace('parents:', '').strip()
                        padres = [p.strip() for p in padres_str.split(',')]
                        print(f"    Padres: {padres}")
                    
                    # Parsear probabilidades
                    elif linea.startswith('P('):
                        self._parsear_probabilidad(linea, nodo, padres)
            
            i += 2
        
        print(f"\n  Probabilidades cargadas exitosamente")
    
    def _parsear_probabilidad(self, linea, nodo, padres):
        """
        Parsea una línea de probabilidad y la agrega al nodo.
        
        Args:
            linea (str): Línea con la probabilidad
            nodo (Nodo): Nodo al que pertenece la probabilidad
            padres (list): Lista de nombres de padres
        """
        # Ejemplo: P(Train=on_time | Rain=none, Maintenance=yes) = 0.8
        # o: P(Rain=none) = 0.7
        
        # Extraer valor y probabilidad
        match = re.match(r'P\(([^)]+)\)\s*=\s*([\d.]+)', linea)
        if not match:
            return
        
        expresion = match.group(1)
        probabilidad = float(match.group(2))
        
        # Separar por |
        if '|' in expresion:
            partes = expresion.split('|')
            variable_parte = partes[0].strip()
            condiciones_parte = partes[1].strip()
            
            # Parsear variable=valor
            var_match = re.match(r'(\w+)=(\w+)', variable_parte)
            if var_match:
                valor = var_match.group(2)
            
            # Parsear condiciones
            condiciones = {}
            condiciones_items = condiciones_parte.split(',')
            for cond in condiciones_items:
                cond = cond.strip()
                cond_match = re.match(r'(\w+)=(\w+)', cond)
                if cond_match:
                    cond_var = cond_match.group(1)
                    cond_val = cond_match.group(2)
                    condiciones[cond_var] = cond_val
            
            nodo.establecer_probabilidad(condiciones, valor, probabilidad)
        else:
            # Sin condiciones (nodo raíz)
            var_match = re.match(r'(\w+)=(\w+)', expresion)
            if var_match:
                valor = var_match.group(2)
                nodo.establecer_probabilidad({}, valor, probabilidad)
    
    def mostrar_estructura(self):
        """
        Muestra la estructura de la red en formato texto.
        Recorre la red desde las raíces mostrando la jerarquía.
        """
        print(f"\n{'='*60}")
        print("ESTRUCTURA DE LA RED BAYESIANA")
        print(f"{'='*60}\n")
        
        visitados = set()
        
        for raiz in self.raices:
            self._mostrar_nodo_recursivo(raiz, visitados, nivel=0)
    
    def _mostrar_nodo_recursivo(self, nodo, visitados, nivel=0):
        """
        Muestra un nodo y sus descendientes de forma recursiva.
        
        Args:
            nodo (Nodo): Nodo a mostrar
            visitados (set): Set de nodos ya visitados
            nivel (int): Nivel de profundidad para la indentación
        """
        if nodo.nombre in visitados:
            return
        
        visitados.add(nodo.nombre)
        
        indentacion = "  " * nivel
        
        # Mostrar información del nodo
        print(f"{indentacion}├─ {nodo.nombre}")
        print(f"{indentacion}│  Valores: {nodo.valores}")
        
        if nodo.padres:
            padres_nombres = [p.nombre for p in nodo.padres]
            print(f"{indentacion}│  Padres: {padres_nombres}")
        else:
            print(f"{indentacion}│  (Nodo Raíz)")
        
        if nodo.hijos:
            hijos_nombres = [h.nombre for h in nodo.hijos]
            print(f"{indentacion}│  Hijos: {hijos_nombres}")
        
        print(f"{indentacion}│")
        
        # Recursión para los hijos
        for hijo in nodo.hijos:
            self._mostrar_nodo_recursivo(hijo, visitados, nivel + 1)
    
    def mostrar_tablas_probabilidad(self):
        """
        Muestra las tablas de probabilidad de todos los nodos.
        """
        print(f"\n{'='*60}")
        print("TABLAS DE PROBABILIDAD CONDICIONAL")
        print(f"{'='*60}\n")
        
        for nombre_nodo in sorted(self.nodos.keys()):
            nodo = self.nodos[nombre_nodo]
            print(f"{'─'*60}")
            print(f"Nodo: {nodo.nombre}")
            print(f"{'─'*60}")
            print(f"Valores posibles: {nodo.valores}")
            
            if nodo.padres:
                padres_nombres = [p.nombre for p in nodo.padres]
                print(f"Padres: {padres_nombres}\n")
                
                # Agrupar por condiciones
                for condiciones_tupla, probabilidades in sorted(nodo.tabla_probabilidad.items()):
                    if condiciones_tupla:
                        # Convertir tupla de condiciones a string legible
                        condiciones_str = ", ".join([f"{k}={v}" for k, v in condiciones_tupla])
                        print(f"  P({nodo.nombre} | {condiciones_str}):")
                    else:
                        print(f"  P({nodo.nombre}):")
                    
                    for valor, prob in sorted(probabilidades.items()):
                        print(f"    {valor}: {prob}")
                    print()
            else:
                print("(Nodo raíz - sin padres)\n")
                
                for condiciones_tupla, probabilidades in sorted(nodo.tabla_probabilidad.items()):
                    print(f"  P({nodo.nombre}):")
                    for valor, prob in sorted(probabilidades.items()):
                        print(f"    {valor}: {prob}")
                    print()
            
            print()
    
    def obtener_todos_nodos(self):
        """
        Retorna una lista con todos los nodos de la red.
        
        Returns:
            list: Lista de nodos
        """
        return list(self.nodos.values())
    
    def obtener_orden_topologico(self):
        """
        Retorna los nodos en orden topológico (padres antes que hijos).
        
        Returns:
            list: Lista de nodos en orden topológico
        """
        visitados = set()
        orden = []
        
        def visitar(nodo):
            if nodo.nombre in visitados:
                return
            visitados.add(nodo.nombre)
            
            # Visitar primero los padres
            for padre in nodo.padres:
                visitar(padre)
            
            orden.append(nodo)
        
        # Visitar todos los nodos
        for nodo in self.nodos.values():
            visitar(nodo)
        
        return orden
