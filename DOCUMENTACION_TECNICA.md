# Documentación Técnica del Motor de Inferencia

## 📘 Fundamentos Teóricos

### Red Bayesiana

Una Red Bayesiana es un grafo acíclico dirigido (DAG) donde:
- Los **nodos** representan variables aleatorias
- Las **aristas** representan dependencias directas
- Cada nodo tiene una **Tabla de Probabilidad Condicional (CPT)** asociada

### Representación de Probabilidad Conjunta

Una Red Bayesiana representa una distribución de probabilidad conjunta:

```
P(X₁, X₂, ..., Xₙ) = ∏ᵢ P(Xᵢ | padres(Xᵢ))
```

Esta factorización es la clave de la eficiencia de las Redes Bayesianas.

---

## 🔍 Algoritmo de Inferencia por Enumeración

### Objetivo

Calcular **P(X | e)** donde:
- **X**: variable de consulta
- **e**: evidencia (variables observadas)

### Fórmula Base

```
P(X | e) = α · P(X, e) = α · Σᵧ P(X, e, y)
```

donde:
- **α**: constante de normalización (α = 1 / P(e))
- **y**: conjunto de variables ocultas (no observadas)
- **Σᵧ**: suma sobre todas las posibles asignaciones de y

### Proceso Paso a Paso

#### 1. Identificación de Variables

```python
Variables_Total = todas las variables en la red
Variables_Consulta = {X}
Variables_Evidencia = {e₁, e₂, ..., eₖ}
Variables_Ocultas = Variables_Total - Variables_Consulta - Variables_Evidencia
```

#### 2. Enumeración

Para cada valor posible x de X:

```
P(X=x, e) = Σᵧ P(X=x, e, y)
           = Σᵧ ∏ᵢ P(Xᵢ | padres(Xᵢ))
```

Esta suma se calcula recursivamente enumerando todas las combinaciones de variables ocultas.

#### 3. Normalización

```
α = 1 / Σₓ P(X=x, e)

P(X=x | e) = α · P(X=x, e)
```

---

## 💻 Implementación

### Estructura de Clases

#### Clase `Nodo`

Representa un nodo en la Red Bayesiana.

**Atributos principales:**
```python
nombre: str                    # Nombre del nodo
valores: List[str]             # Valores posibles
padres: List[Nodo]             # Nodos padres
hijos: List[Nodo]              # Nodos hijos
tabla_probabilidad: Dict       # CPT del nodo
```

**Métodos clave:**
```python
obtener_probabilidad(valor, condiciones)
    # Retorna P(valor | condiciones)
    # Ej: nodo.obtener_probabilidad('on_time', {'Rain': 'light'})
```

#### Clase `RedBayesiana`

Gestiona la estructura completa de la red.

**Métodos principales:**
```python
cargar_estructura(archivo)
    # Lee relaciones Padre -> Hijo desde archivo
    # Construye el grafo de dependencias

cargar_probabilidades(archivo)
    # Parsea y almacena las CPTs
    # Formato: P(Nodo=valor | Padre=valorP) = prob

obtener_orden_topologico()
    # Retorna nodos ordenados (padres antes que hijos)
    # Útil para calcular probabilidades conjuntas
```

#### Clase `MotorInferencia`

Implementa el algoritmo de enumeración.

**Método principal:**
```python
inferencia(consulta, evidencia)
    # Entrada:
    #   consulta: {'Appointment': None}
    #   evidencia: {'Rain': 'light', 'Maintenance': 'yes'}
    # Salida:
    #   {'attend': 0.645833, 'miss': 0.354167}
```

### Algoritmo Recursivo de Enumeración

```python
def _enumerar_todo(variables, evidencia, variables_ocultas):
    """
    Suma sobre todas las asignaciones de variables ocultas.
    """
    # Caso base: no quedan variables ocultas
    if not variables_ocultas:
        return probabilidad_conjunta(evidencia)
    
    # Seleccionar una variable oculta Y
    Y = seleccionar_variable(variables_ocultas)
    
    # Sumar sobre todos los valores de Y
    suma = 0
    for valor_y in valores_posibles(Y):
        nueva_evidencia = evidencia ∪ {Y: valor_y}
        suma += _enumerar_todo(
            variables,
            nueva_evidencia,
            variables_ocultas - {Y}
        )
    
    return suma
```

### Cálculo de Probabilidad Conjunta

```python
def probabilidad_conjunta(asignacion):
    """
    Calcula ∏ᵢ P(Xᵢ | padres(Xᵢ)) para asignación completa.
    """
    probabilidad = 1.0
    
    for nodo in orden_topologico:
        valor = asignacion[nodo.nombre]
        
        # Obtener valores de padres
        condiciones = {
            padre.nombre: asignacion[padre.nombre]
            for padre in nodo.padres
        }
        
        # Multiplicar por P(nodo | padres)
        probabilidad *= nodo.obtener_probabilidad(valor, condiciones)
    
    return probabilidad
```

---

## 📊 Ejemplo de Traza

### Consulta
```
P(Appointment | Rain=light, Maintenance=yes)
```

### Variables
- **Consulta**: Appointment
- **Evidencia**: {Rain=light, Maintenance=yes}
- **Ocultas**: {Train}

### Enumeración

Para **Appointment=attend**:

```
P(Appointment=attend, Rain=light, Maintenance=yes) = 
    Σ_train P(Appointment=attend, Rain=light, Maintenance=yes, Train=train)

= P(Appointment=attend, Rain=light, Maintenance=yes, Train=on_time)
  + P(Appointment=attend, Rain=light, Maintenance=yes, Train=delayed)

= P(Rain=light) · P(Maintenance=yes) · P(Train=on_time | Rain=light, Maintenance=yes) · P(Appointment=attend | Train=on_time)
  + P(Rain=light) · P(Maintenance=yes) · P(Train=delayed | Rain=light, Maintenance=yes) · P(Appointment=attend | Train=delayed)

= 0.2 · 0.4 · 0.6 · 0.9
  + 0.2 · 0.4 · 0.4 · 0.6

= 0.0432 + 0.0192
= 0.0624
```

Para **Appointment=miss**:

```
P(Appointment=miss, Rain=light, Maintenance=yes) = 
= 0.2 · 0.4 · 0.6 · 0.1
  + 0.2 · 0.4 · 0.4 · 0.4

= 0.0048 + 0.0128
= 0.0176
```

### Normalización

```
α = 1 / (0.0624 + 0.0176) = 1 / 0.08 = 12.5

P(Appointment=attend | Rain=light, Maintenance=yes) = 12.5 · 0.0624 = 0.78
P(Appointment=miss | Rain=light, Maintenance=yes) = 12.5 · 0.0176 = 0.22
```

---

## ⚡ Complejidad

### Temporal

**O(n · d^m)**

donde:
- **n**: número de nodos
- **d**: número máximo de valores por variable
- **m**: número de variables ocultas

### Espacial

**O(n · d^k)**

donde:
- **k**: número máximo de padres de un nodo

### Optimizaciones Posibles

1. **Ordenamiento de Variables**: Elegir variables ocultas en orden óptimo
2. **Poda**: Eliminar ramas con probabilidad 0
3. **Caché**: Almacenar resultados intermedios
4. **Eliminación de Variables**: Alternativa más eficiente para algunas consultas

---

## 🎯 Ventajas y Limitaciones

### Ventajas

✅ **Correcto y completo**: Siempre encuentra la respuesta exacta  
✅ **Simple de implementar**: Lógica directa y clara  
✅ **Genérico**: Funciona con cualquier Red Bayesiana  
✅ **Intuitivo**: Fácil de entender y depurar  

### Limitaciones

❌ **Complejidad exponencial**: No escala bien con muchas variables ocultas  
❌ **No explota independencias**: Calcula más de lo necesario  
❌ **Memoria**: Puede requerir mucha para redes grandes  

### Alternativas más Eficientes

Para redes grandes, considerar:
- **Eliminación de Variables**
- **Clustering de Variables**
- **Propagación de Creencias**
- **Muestreo (Monte Carlo)**

---

## 🔬 Casos de Uso

### Cuando Usar Enumeración

✅ Redes pequeñas (< 10 variables)  
✅ Pocas variables ocultas (< 5)  
✅ Propósito educativo  
✅ Validación de otros algoritmos  
✅ Necesidad de respuesta exacta  

### Cuando No Usar

❌ Redes grandes (> 20 variables)  
❌ Muchas variables ocultas  
❌ Restricciones de tiempo real  
❌ Variables continuas  

---

## 📈 Extensiones Posibles

### 1. Variables Continuas
Usar **distribuciones paramétricas** (Gaussianas) en lugar de tablas discretas.

### 2. Decisiones y Utilidad
Extender a **Redes de Decisión** con nodos de decisión y utilidad.

### 3. Aprendizaje
Implementar **aprendizaje de parámetros** desde datos.

### 4. Estructura Temporal
Extender a **Redes Bayesianas Dinámicas** para modelar secuencias temporales.

### 5. Inferencia Aproximada
Implementar **algoritmos de muestreo** para redes grandes:
- Muestreo por Rechazo
- Muestreo por Ponderación de Probabilidad
- MCMC (Markov Chain Monte Carlo)

---

## 📚 Referencias

### Libros
- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.)
  - Capítulo 13: Cuantificar la Incertidumbre
  - Capítulo 14: Razonamiento Probabilístico

- Koller, D., & Friedman, N. (2009). *Probabilistic Graphical Models*
  - Parte II: Representación
  - Parte III: Inferencia

### Papers Clásicos
- Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems*
- Lauritzen, S. L., & Spiegelhalter, D. J. (1988). "Local Computations with Probabilities"

### Recursos Online
- [Bayes Net Structure Learning](https://www.cs.cmu.edu/~epxing/Class/10708/)
- [Probabilistic Graphical Models (Coursera)](https://www.coursera.org/specializations/probabilistic-graphical-models)

---

## 🧪 Pruebas y Validación

### Verificación de Consistencia

1. **Suma de probabilidades = 1**
   ```python
   for combinación_padres in todas_combinaciones:
       suma = sum(P(nodo=v | padres) for v in valores_nodo)
       assert abs(suma - 1.0) < 1e-6
   ```

2. **Normalización correcta**
   ```python
   resultado = inferencia(consulta, evidencia)
   suma = sum(resultado.values())
   assert abs(suma - 1.0) < 1e-6
   ```

3. **Consistencia con probabilidades marginales**
   ```python
   P(X) = Σ_y P(X, Y=y)  # Debe coincidir
   ```

### Casos de Prueba

1. **Nodo sin padres**: P(X) debe coincidir con la tabla
2. **Evidencia vacía**: P(X | ∅) = P(X)
3. **Evidencia completa**: Resultado determinístico
4. **Simetría**: P(X | Y) y P(Y | X) deben ser consistentes vía Bayes

---

## 💡 Mejores Prácticas

### Diseño de Redes

1. **Mantener simplicidad**: Menos de 10 nodos si es posible
2. **Limitar padres**: Máximo 3-4 padres por nodo
3. **Valores discretos**: 2-4 valores por variable
4. **Evitar ciclos**: Siempre un DAG

### Estimación de Probabilidades

1. **Basarse en datos** cuando estén disponibles
2. **Consultar expertos** para probabilidades subjetivas
3. **Análisis de sensibilidad** para probabilidades inciertas
4. **Validación empírica** comparar con casos conocidos

### Interpretación

1. **Considerar contexto** del dominio
2. **Intervalos de confianza** en lugar de valores puntuales
3. **Análisis de "qué pasa si"** para diferentes escenarios
4. **Visualización** de resultados para comunicación

---

Este documento proporciona la base teórica y práctica para entender e implementar el Motor de Inferencia por Enumeración en Redes Bayesianas.
