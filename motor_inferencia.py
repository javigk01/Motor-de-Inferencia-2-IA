"""
Motor de Inferencia por Enumeración para Redes Bayesianas.
Implementa el algoritmo de inferencia por enumeración para calcular probabilidades
a posteriori en una Red Bayesiana.
"""

from red_bayesiana import RedBayesiana
from itertools import product

class MotorInferencia:
    def __init__(self, red_bayesiana):
        """
        Inicializa el motor de inferencia.
        
        Args:
            red_bayesiana (RedBayesiana): Red Bayesiana sobre la que se realizará la inferencia
        """
        self.red = red_bayesiana
        self.traza = []  # Para almacenar la traza de ejecución
        self.nivel_traza = 0  # Para la indentación en la traza
    
    def limpiar_traza(self):
        """
        Limpia la traza de ejecución.
        """
        self.traza = []
        self.nivel_traza = 0
    
    def agregar_traza(self, mensaje):
        """
        Agrega un mensaje a la traza.
        
        Args:
            mensaje (str): Mensaje a agregar
        """
        indentacion = "  " * self.nivel_traza
        self.traza.append(f"{indentacion}{mensaje}")
    
    def mostrar_traza(self):
        """
        Muestra la traza de ejecución.
        """
        print(f"\n{'='*70}")
        print("TRAZA DE EJECUCIÓN DEL MOTOR DE INFERENCIA")
        print(f"{'='*70}\n")
        for linea in self.traza:
            print(linea)
        print()
    
    def inferencia(self, consulta, evidencia, return_parciales=False):
        """
        Realiza inferencia por enumeración.
        
        Calcula P(consulta | evidencia) utilizando:
        P(X | e) = α * Σ_y P(X, e, y)
        
        donde:
        - X es la variable de consulta
        - e son las variables de evidencia
        - y son las variables ocultas
        - α es la constante de normalización
        
        Args:
            consulta (dict): Diccionario con la variable de consulta y sus valores
                            Ejemplo: {'Appointment': None} para obtener todas las probabilidades
                            o {'Appointment': 'attend'} para un valor específico
            evidencia (dict): Diccionario con las variables de evidencia y sus valores
                            Ejemplo: {'Rain': 'light', 'Maintenance': 'yes'}
        
        Returns:
            dict: Distribución de probabilidad normalizada para la consulta
        """
        self.limpiar_traza()
        
        # Obtener la variable de consulta
        var_consulta = list(consulta.keys())[0]
        nodo_consulta = self.red.obtener_nodo(var_consulta)
        
        if not nodo_consulta:
            raise ValueError(f"Nodo {var_consulta} no encontrado en la red")
        
        self.agregar_traza(f"{'='*70}")
        self.agregar_traza(f"INICIO DE INFERENCIA POR ENUMERACIÓN")
        self.agregar_traza(f"{'='*70}")
        self.agregar_traza(f"Consulta: P({var_consulta} | {evidencia})")
        self.agregar_traza("")
        
        # Identificar todas las variables en la red
        todas_variables = set(self.red.nodos.keys())
        self.agregar_traza(f"Variables en la red: {sorted(todas_variables)}")
        
        # Variables observadas (evidencia + consulta si tiene valor específico)
        variables_observadas = set(evidencia.keys())
        if consulta[var_consulta] is not None:
            variables_observadas.add(var_consulta)
        
        self.agregar_traza(f"Variables observadas (evidencia): {sorted(evidencia.keys())}")
        
        # Variables ocultas (no observadas)
        variables_ocultas = todas_variables - variables_observadas - {var_consulta}
        self.agregar_traza(f"Variables ocultas: {sorted(variables_ocultas)}")
        self.agregar_traza("")
        
        # Calcular la distribución para cada valor posible de la variable de consulta
        resultados = {}
        parciales = {}
        for valor_consulta in nodo_consulta.valores:
            self.agregar_traza(f"{'─'*70}")
            self.agregar_traza(f"Calculando P({var_consulta}={valor_consulta} | {evidencia})")
            self.agregar_traza(f"{'─'*70}")
            # Crear asignación completa con la consulta
            asignacion_consulta = evidencia.copy()
            asignacion_consulta[var_consulta] = valor_consulta
            # Enumerar sobre todas las variables ocultas
            probabilidad = self._enumerar_todo(
                list(self.red.nodos.keys()),
                asignacion_consulta,
                variables_ocultas
            )
            resultados[valor_consulta] = probabilidad
            parciales[valor_consulta] = probabilidad
            self.agregar_traza(f"\nResultado parcial: P({var_consulta}={valor_consulta}, {evidencia}) = {probabilidad:.6f}")
            self.agregar_traza("")
        
        # Normalizar
        self.agregar_traza(f"{'='*70}")
        self.agregar_traza(f"NORMALIZACIÓN")
        self.agregar_traza(f"{'='*70}")
        
        suma_total = sum(resultados.values())
        self.agregar_traza(f"Suma total (α⁻¹): {suma_total:.6f}")
        
        if suma_total == 0:
            self.agregar_traza("ERROR: La suma total es 0. Verifica las probabilidades en las tablas.")
            return {valor: 0 for valor in resultados.keys()}
        
        self.agregar_traza(f"Constante de normalización (α): {1/suma_total:.6f}")
        self.agregar_traza("")
        
        resultados_normalizados = {}
        for valor, prob in resultados.items():
            prob_normalizada = prob / suma_total if suma_total > 0 else 0
            resultados_normalizados[valor] = prob_normalizada
            self.agregar_traza(f"P({var_consulta}={valor} | {evidencia}) = {prob:.6f} / {suma_total:.6f} = {prob_normalizada:.6f}")
        self.agregar_traza("")
        self.agregar_traza(f"{'='*70}")
        self.agregar_traza(f"RESULTADO FINAL")
        self.agregar_traza(f"{'='*70}")
        for valor, prob in resultados_normalizados.items():
            self.agregar_traza(f"P({var_consulta}={valor} | {evidencia}) = {prob:.6f} ({prob*100:.2f}%)")
        if return_parciales:
            return resultados_normalizados, parciales
        return resultados_normalizados
    
    def _enumerar_todo(self, variables, evidencia, variables_ocultas):
        """
        Función recursiva para enumerar todas las asignaciones posibles de las variables ocultas.
        
        Args:
            variables (list): Lista de todas las variables a considerar
            evidencia (dict): Asignación actual de variables
            variables_ocultas (set): Variables que aún no están asignadas
        
        Returns:
            float: Probabilidad de la asignación
        """
        # Caso base: no quedan variables ocultas
        if not variables_ocultas:
            # Calcular probabilidad conjunta
            return self._probabilidad_conjunta(evidencia)
        
        # Seleccionar una variable oculta
        variable = list(variables_ocultas)[0]
        variables_ocultas_restantes = variables_ocultas - {variable}
        
        nodo = self.red.obtener_nodo(variable)
        
        self.nivel_traza += 1
        self.agregar_traza(f"Enumerando variable oculta: {variable}")
        self.agregar_traza(f"Valores posibles: {nodo.valores}")
        
        # Sumar sobre todos los valores posibles de la variable
        suma = 0
        for valor in nodo.valores:
            # Crear nueva asignación con este valor
            nueva_evidencia = evidencia.copy()
            nueva_evidencia[variable] = valor
            
            self.agregar_traza(f"  Probando {variable}={valor}")
            
            # Recursión
            prob = self._enumerar_todo(variables, nueva_evidencia, variables_ocultas_restantes)
            suma += prob
        
        self.agregar_traza(f"Suma para {variable}: {suma:.6f}")
        self.nivel_traza -= 1
        
        return suma
    
    def _probabilidad_conjunta(self, asignacion):
        """
        Calcula la probabilidad conjunta de una asignación completa.
        
        P(X1, X2, ..., Xn) = Π P(Xi | padres(Xi))
        
        Args:
            asignacion (dict): Asignación completa de todas las variables
        
        Returns:
            float: Probabilidad conjunta
        """
        probabilidad = 1.0
        detalles = []
        
        # Obtener orden topológico para procesar nodos
        orden_topologico = self.red.obtener_orden_topologico()
        
        for nodo in orden_topologico:
            if nodo.nombre not in asignacion:
                continue
            
            valor = asignacion[nodo.nombre]
            
            # Obtener valores de los padres
            condiciones = {}
            for padre in nodo.padres:
                if padre.nombre in asignacion:
                    condiciones[padre.nombre] = asignacion[padre.nombre]
            
            # Obtener probabilidad
            prob = nodo.obtener_probabilidad(valor, condiciones)
            probabilidad *= prob
            
            # Agregar detalle
            if condiciones:
                cond_str = ", ".join([f"{k}={v}" for k, v in condiciones.items()])
                detalles.append(f"P({nodo.nombre}={valor} | {cond_str})={prob:.4f}")
            else:
                detalles.append(f"P({nodo.nombre}={valor})={prob:.4f}")
        
        self.nivel_traza += 1
        self.agregar_traza(f"Probabilidad conjunta para {asignacion}:")
        for detalle in detalles:
            self.agregar_traza(f"  {detalle}")
        self.agregar_traza(f"  Producto: {probabilidad:.6f}")
        self.nivel_traza -= 1
        
        return probabilidad
    
    def consulta_multiple(self, consultas, evidencia):
        """
        Realiza múltiples consultas de inferencia con la misma evidencia.
        
        Args:
            consultas (list): Lista de variables a consultar
            evidencia (dict): Diccionario con las variables de evidencia
        
        Returns:
            dict: Diccionario con los resultados de cada consulta
        """
        resultados = {}
        
        for var_consulta in consultas:
            resultado = self.inferencia({var_consulta: None}, evidencia)
            resultados[var_consulta] = resultado
        
        return resultados
