# 🎯 Motor de Inferencia por Enumeración - Resumen del Proyecto

## 📦 Archivos Creados

```
Motor-de-Inferencia-2-IA/
│
├── 📄 nodo.py                        # Clase para nodos individuales
├── 📄 red_bayesiana.py               # Gestión de la red completa
├── 📄 motor_inferencia.py            # Algoritmo de inferencia por enumeración
├── 📄 main.py                        # Programa principal interactivo
├── 📄 prueba_simple.py               # Script de prueba rápida
│
├── 📋 estructura_red.txt             # Estructura del ejemplo (Rain/Train)
├── 📋 probabilidades.txt             # Tablas de probabilidad del ejemplo
│
├── 📖 README.md                      # Documentación general del proyecto
├── 📖 INSTRUCCIONES.md              # Guía de instalación y ejecución
├── 📖 EJEMPLOS_DOMINIOS.md          # Plantillas para otros dominios
├── 📖 DOCUMENTACION_TECNICA.md      # Fundamentos teóricos y algoritmo
└── 📖 RESUMEN.md                    # Este archivo
```

---

## 🎓 Cumplimiento de Requisitos

### ✅ Parte 1: Red Bayesiana

#### Requisito 1.1: Estructura desde archivo
- **Archivo**: `red_bayesiana.py` - método `cargar_estructura()`
- **Formato**: `estructura_red.txt` con relaciones `Padre -> Hijo`
- **Funcionalidad**: Lee y construye el grafo de dependencias

#### Requisito 1.2: Visualización de estructura
- **Archivo**: `red_bayesiana.py` - método `mostrar_estructura()`
- **Salida**: Muestra jerarquía de nodos, padres, hijos y valores posibles
- **Formato**: Texto indentado mostrando la estructura desde raíces

#### Requisito 1.3: Lectura de tablas de probabilidad
- **Archivo**: `red_bayesiana.py` - método `cargar_probabilidades()`
- **Formato**: `probabilidades.txt` similar a tablas de clase
- **Modificabilidad**: Formato legible y fácil de editar

#### Requisito 1.4: Visualización de tablas
- **Archivo**: `red_bayesiana.py` - método `mostrar_tablas_probabilidad()`
- **Salida**: Todas las CPTs en formato tabular claro

### ✅ Parte 2: Motor de Inferencia

#### Requisito 2.1: Inferencia por enumeración
- **Archivo**: `motor_inferencia.py` - clase `MotorInferencia`
- **Método principal**: `inferencia(consulta, evidencia)`
- **Fórmula**: Implementa P(X | e) = α · Σ_y P(X, e, y)

#### Requisito 2.2: Toma de decisiones
- **Funcionalidad**: Calcula probabilidades para decidir entre opciones
- **Ejemplo**: "¿Asistir a la cita?" basado en evidencia del clima

#### Requisito 2.3: Traza de ejecución
- **Archivo**: `motor_inferencia.py` - método `mostrar_traza()`
- **Contenido**: 
  - Variables identificadas (consulta, evidencia, ocultas)
  - Proceso de enumeración paso a paso
  - Cálculos de probabilidades conjuntas
  - Normalización con factor α
  - Resultados finales

#### Requisito 2.4: Genericidad
- **Diseño**: Sistema completamente genérico
- **Flexibilidad**: Funciona con cualquier dominio
- **Ejemplos**: 4 dominios diferentes en `EJEMPLOS_DOMINIOS.md`

---

## 🏗️ Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────┐
│                      main.py                            │
│              (Interfaz del Usuario)                     │
└────────────┬───────────────────────────────────────────┘
             │
             ├──→ Menú Interactivo
             ├──→ Ejemplos Predefinidos
             └──→ Consultas Personalizadas
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
┌──────────────────┐           ┌─────────────────────┐
│ RedBayesiana     │           │ MotorInferencia     │
│                  │           │                     │
│ - Cargar struct. │◄──────────┤ - inferencia()      │
│ - Cargar probs.  │           │ - enumerar_todo()   │
│ - Visualizar     │           │ - prob_conjunta()   │
└────────┬─────────┘           └─────────────────────┘
         │
         ▼
┌──────────────────┐
│      Nodo        │
│                  │
│ - valores[]      │
│ - padres[]       │
│ - hijos[]        │
│ - tabla_prob{}   │
└──────────────────┘
         ▲
         │
┌────────┴─────────────────────┐
│  Archivos de Datos           │
│                              │
│  - estructura_red.txt        │
│  - probabilidades.txt        │
└──────────────────────────────┘
```

---

## 🔄 Flujo de Ejecución

### 1. Inicialización
```
Inicio
  ↓
Cargar estructura_red.txt
  ↓
Construir grafo de nodos
  ↓
Cargar probabilidades.txt
  ↓
Parsear y almacenar CPTs
  ↓
Red Bayesiana lista
```

### 2. Consulta de Inferencia
```
Usuario ingresa consulta
  ↓
P(X | evidencia)
  ↓
Identificar variables:
  - Consulta: X
  - Evidencia: e
  - Ocultas: Y
  ↓
Para cada valor x de X:
  ↓
  Enumerar sobre Y:
    ↓
    Calcular P(x, e, y)
    ↓
    Sumar todas las combinaciones
  ↓
Normalizar con α
  ↓
Retornar distribución P(X|e)
```

### 3. Traza Detallada
```
Cada paso registra:
  - Variables procesadas
  - Valores probados
  - Probabilidades calculadas
  - Operaciones realizadas
  
Al final, muestra traza completa
```

---

## 🎯 Características Principales

### 1. **Modularidad**
- Clases independientes y reutilizables
- Separación clara de responsabilidades
- Fácil extensión y mantenimiento

### 2. **Genericidad**
- No limitado a un dominio específico
- Carga dinámica desde archivos
- Funciona con cualquier estructura de red

### 3. **Claridad**
- Código bien documentado
- Variables y funciones con nombres descriptivos
- Trazas detalladas para debugging

### 4. **Usabilidad**
- Menú interactivo intuitivo
- Ejemplos predefinidos
- Consultas personalizadas
- Múltiples archivos de documentación

### 5. **Educativo**
- Implementación clara del algoritmo
- Trazas paso a paso
- Documentación técnica completa
- Ejemplos en diferentes dominios

---

## 📊 Ejemplo del Proyecto

### Red Implementada
```
     Rain                    Maintenance
   {none, light, heavy}        {yes, no}
          \                       /
           \                     /
            \                   /
             ▼                 ▼
              Train (on_time, delayed)
                      │
                      │
                      ▼
         Appointment (attend, miss)
```

### Consultas de Ejemplo

1. **P(Appointment | Rain=light, Maintenance=yes)**
   - Probabilidad de asistir con lluvia ligera y mantenimiento

2. **P(Train | Rain=none)**
   - Probabilidad de puntualidad sin lluvia

3. **P(Appointment | Train=on_time)**
   - Probabilidad de asistir si el tren llega a tiempo

---

## 🚀 Cómo Empezar

### Instalación Rápida
```powershell
# 1. Instalar Python (si no está instalado)
# Descargar de python.org

# 2. Navegar al directorio
cd "c:\Users\javie\OneDrive\Documentos\unijaveriana\SEMESTRE 6\IA\Motor-de-Inferencia-2-IA"

# 3. Ejecutar prueba simple
python prueba_simple.py
```

### Uso Básico
```powershell
# Ejecutar programa completo
python main.py

# Seleccionar opción 1 para ver todos los ejemplos
# o opción 2 para hacer consultas personalizadas
```

---

## 📚 Documentación Disponible

### Para Usuarios
- **README.md**: Visión general del proyecto
- **INSTRUCCIONES.md**: Guía paso a paso de instalación y uso

### Para Desarrolladores
- **DOCUMENTACION_TECNICA.md**: Algoritmo y fundamentos teóricos
- **EJEMPLOS_DOMINIOS.md**: Plantillas para crear nuevas redes

### Para Aprendizaje
- **Código fuente**: Comentarios detallados en todos los archivos
- **Trazas**: Visualización paso a paso del algoritmo
- **Ejemplos**: 5 casos de uso en main.py

---

## 💡 Aplicaciones Posibles

### Diagnóstico
- Sistemas médicos
- Detección de fallas en equipos
- Análisis de problemas de software

### Predicción
- Pronóstico del tiempo
- Análisis de riesgos
- Predicción de comportamiento

### Toma de Decisiones
- Sistemas de recomendación
- Planificación bajo incertidumbre
- Análisis de inversiones

### Educación
- Herramienta didáctica para IA
- Visualización de inferencia probabilística
- Experimentación con diferentes escenarios

---

## 🎓 Conceptos Aprendidos

### Teóricos
✓ Redes Bayesianas y representación de incertidumbre  
✓ Inferencia probabilística  
✓ Probabilidad condicional  
✓ Regla de Bayes  
✓ Factorización de probabilidades conjuntas  

### Prácticos
✓ Diseño de estructuras de datos para grafos  
✓ Parseo de archivos de configuración  
✓ Algoritmos recursivos  
✓ Debugging con trazas  
✓ Programación modular en Python  

---

## 🔧 Tecnologías Utilizadas

- **Lenguaje**: Python 3.6+
- **Paradigma**: Programación Orientada a Objetos
- **Algoritmo**: Inferencia por Enumeración
- **Estructura de Datos**: Grafos Acíclicos Dirigidos (DAG)
- **Formato de Datos**: Archivos de texto plano

---

## 📈 Posibles Mejoras Futuras

### Optimizaciones
1. Caché de resultados intermedios
2. Ordenamiento inteligente de variables
3. Poda de ramas imposibles
4. Paralelización de enumeraciones

### Nuevas Características
1. Interfaz gráfica (GUI)
2. Visualización gráfica de la red
3. Exportación de resultados a CSV/JSON
4. Carga desde bases de datos

### Algoritmos Adicionales
1. Eliminación de Variables
2. Clustering
3. Propagación de Creencias
4. Muestreo Monte Carlo

---

## ✨ Conclusión

Este proyecto implementa un **Motor de Inferencia por Enumeración** completo y funcional para Redes Bayesianas, cumpliendo con todos los requisitos especificados:

✅ Carga de estructura desde archivo  
✅ Visualización de la red  
✅ Carga de probabilidades desde archivo  
✅ Visualización de tablas de probabilidad  
✅ Inferencia por enumeración con trazas  
✅ Sistema genérico para cualquier dominio  
✅ Documentación completa  

El código es **modular**, **extensible** y **educativo**, ideal para aprender sobre Redes Bayesianas y razonamiento probabilístico.

---

**Autor**: Proyecto de IA - Universidad Javeriana  
**Curso**: Inteligencia Artificial - Semestre 6  
**Fecha**: Noviembre 2025  

---

## 📞 Siguiente Paso

**Para empezar a usar el proyecto:**

```powershell
python prueba_simple.py
```

**Para el programa completo:**

```powershell
python main.py
```

¡Disfruta explorando el mundo de las Redes Bayesianas! 🚀
