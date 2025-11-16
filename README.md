# Motor de Inferencia por Enumeración - Red Bayesiana

Sistema completo de Red Bayesiana con Motor de Inferencia por Enumeración implementado en Python.

> 📚 **[Ver Índice Completo de Documentación](INDICE.md)** - Guía para navegar todos los archivos del proyecto

## 📋 Descripción

Este proyecto implementa:

1. **Red Bayesiana**: Estructura de datos para modelar redes bayesianas con nodos y relaciones de dependencia.
2. **Motor de Inferencia por Enumeración**: Algoritmo para calcular probabilidades a posteriori utilizando enumeración completa.
3. **Carga desde archivos**: Sistema flexible para definir la estructura de la red y las tablas de probabilidad en archivos de texto.
4. **Visualización**: Funciones para mostrar la estructura de la red y las tablas de probabilidad en formato texto.
5. **Trazabilidad**: Generación de trazas detalladas del proceso de inferencia.

## 📁 Archivos del Proyecto

- `nodo.py`: Clase Nodo que representa un nodo en la Red Bayesiana
- `red_bayesiana.py`: Clase RedBayesiana para gestionar la red completa
- `motor_inferencia.py`: Motor de Inferencia por Enumeración
- `main.py`: Programa principal con ejemplos y menú interactivo
- `estructura_red.txt`: Archivo de configuración con la estructura de la red
- `probabilidades.txt`: Archivo con las tablas de probabilidad condicional

## 🎯 Ejemplo Implementado

El proyecto incluye un ejemplo completo basado en el problema de asistir a una cita:

- **Rain** (Lluvia): {none, light, heavy}
- **Maintenance** (Mantenimiento): {yes, no}
- **Train** (Tren): {on_time, delayed}
- **Appointment** (Cita): {attend, miss}

### Relaciones de Dependencia

```
Rain ────────┐
             ├──→ Train ──→ Appointment
Maintenance ─┘
```

## 🚀 Uso

### Ejecución del programa principal

```bash
python main.py
```

### Menú Interactivo

El programa ofrece varias opciones:

1. **Ejecutar ejemplos predefinidos**: Muestra 5 ejemplos de inferencia con diferentes escenarios
2. **Realizar consulta personalizada**: Permite hacer consultas personalizadas sobre la red
3. **Mostrar estructura de la red**: Visualiza la estructura jerárquica de la red
4. **Mostrar tablas de probabilidad**: Muestra todas las tablas de probabilidad condicional
5. **Salir**: Termina el programa

### Ejemplos de Inferencia Incluidos

1. `P(Appointment | Rain=light, Maintenance=yes)`
2. `P(Train)` - Sin evidencia
3. `P(Train | Rain=none)`
4. `P(Appointment | Rain=heavy)`
5. `P(Appointment | Train=on_time)`

## 📝 Formato de Archivos

### Estructura de la Red (`estructura_red.txt`)

```
# Formato: Nodo_Padre -> Nodo_Hijo
Rain -> Maintenance
Rain -> Train
Maintenance -> Train
Train -> Appointment
```

### Probabilidades (`probabilidades.txt`)

```
[NombreNodo]
values: valor1, valor2, valor3
parents: Padre1, Padre2  # Si tiene padres
P(NombreNodo=valor1 | Padre1=valorA, Padre2=valorB) = 0.8
```

## 🔧 Características Técnicas

### Clase Nodo
- Almacena valores posibles
- Gestiona relaciones padre-hijo
- Mantiene tabla de probabilidad condicional
- Permite consultar probabilidades dadas condiciones

### Clase RedBayesiana
- Carga estructura desde archivo
- Parsea y almacena probabilidades
- Visualiza estructura jerárquica
- Muestra tablas de probabilidad
- Proporciona orden topológico

### Motor de Inferencia
- Implementa algoritmo de enumeración
- Calcula `P(X | e) = α * Σ_y P(X, e, y)`
- Genera traza detallada del proceso
- Normaliza resultados automáticamente
- Soporta múltiples consultas

## 💡 Algoritmo de Inferencia

El motor implementa inferencia por enumeración:

1. Identifica variables observadas (evidencia) y ocultas
2. Para cada valor de la variable de consulta:
   - Enumera todas las combinaciones de variables ocultas
   - Calcula la probabilidad conjunta de cada configuración
   - Suma todas las probabilidades
3. Normaliza los resultados con factor α

### Fórmula

```
P(X | e) = α * Σ_y P(X, e, y)
```

donde:
- `X`: variable de consulta
- `e`: evidencia
- `y`: variables ocultas
- `α`: constante de normalización

## 🎓 Uso Educativo

Este proyecto es ideal para:
- Aprender sobre Redes Bayesianas
- Entender inferencia probabilística
- Visualizar el proceso de enumeración
- Experimentar con diferentes configuraciones

## 🔍 Traza de Ejecución

El motor genera una traza detallada que muestra:
- Variables observadas y ocultas
- Proceso de enumeración
- Cálculo de probabilidades conjuntas
- Normalización de resultados

Esto permite verificar el correcto funcionamiento y entender cada paso del algoritmo.

## 📊 Extensibilidad

El sistema es genérico y puede usarse con cualquier dominio:

1. Crea un archivo `estructura_red.txt` con las dependencias
2. Define las probabilidades en `probabilidades.txt`
3. El sistema automáticamente:
   - Carga la red
   - Construye las relaciones
   - Permite realizar inferencias

## 🛠️ Requisitos

- Python 3.6 o superior
- No requiere librerías externas

## 👥 Autor

Proyecto desarrollado para el curso de Inteligencia Artificial
Universidad Javeriana - Semestre 6

## 📄 Licencia

Proyecto educativo de código abierto.
