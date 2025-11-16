# 📚 Índice de Documentación - Motor de Inferencia por Enumeración

## 🚀 Inicio Rápido

**Si es tu primera vez con el proyecto, comienza aquí:**

1. 📖 [INSTRUCCIONES.md](INSTRUCCIONES.md) - Guía de instalación y primeros pasos
2. ▶️ Ejecuta `python prueba_simple.py` para una prueba rápida
3. ▶️ Ejecuta `python main.py` para el programa completo
4. 📖 [RESUMEN.md](RESUMEN.md) - Visión general del proyecto

---

## 📁 Archivos del Proyecto

### 🔧 Código Fuente (Python)

| Archivo | Descripción | Líneas |
|---------|-------------|--------|
| [`nodo.py`](nodo.py) | Clase Nodo para la Red Bayesiana | ~120 |
| [`red_bayesiana.py`](red_bayesiana.py) | Gestión completa de la Red Bayesiana | ~290 |
| [`motor_inferencia.py`](motor_inferencia.py) | Motor de Inferencia por Enumeración | ~250 |
| [`main.py`](main.py) | Programa principal con menú interactivo | ~360 |
| [`prueba_simple.py`](prueba_simple.py) | Script de prueba rápida | ~70 |

**Total: ~1,090 líneas de código**

### 📋 Archivos de Datos

| Archivo | Descripción | Contenido |
|---------|-------------|-----------|
| [`estructura_red.txt`](estructura_red.txt) | Define la estructura de la red | Relaciones Padre → Hijo |
| [`probabilidades.txt`](probabilidades.txt) | Tablas de probabilidad condicional | CPTs de todos los nodos |

### 📖 Documentación

| Archivo | Audiencia | Contenido |
|---------|-----------|-----------|
| [`README.md`](README.md) | **Todos** | Descripción general del proyecto |
| [`INSTRUCCIONES.md`](INSTRUCCIONES.md) | **Usuarios** | Instalación y guía de uso |
| [`RESUMEN.md`](RESUMEN.md) | **Todos** | Resumen ejecutivo del proyecto |
| [`DOCUMENTACION_TECNICA.md`](DOCUMENTACION_TECNICA.md) | **Desarrolladores** | Algoritmo y fundamentos teóricos |
| [`EJEMPLOS_DOMINIOS.md`](EJEMPLOS_DOMINIOS.md) | **Usuarios avanzados** | Plantillas para otros dominios |
| [`VISUALIZACION.md`](VISUALIZACION.md) | **Estudiantes** | Diagramas y ejemplos visuales |
| [`INDICE.md`](INDICE.md) | **Todos** | Este archivo |

---

## 🎯 Guías por Objetivo

### 🆕 Quiero aprender sobre Redes Bayesianas
1. 📖 [README.md](README.md) - Introducción al proyecto
2. 📖 [VISUALIZACION.md](VISUALIZACION.md) - Diagramas y ejemplos visuales
3. 📖 [DOCUMENTACION_TECNICA.md](DOCUMENTACION_TECNICA.md) - Teoría y algoritmo
4. ▶️ Ejecutar `python main.py` → Opción 1 (ver ejemplos)

### 🔧 Quiero usar el programa
1. 📖 [INSTRUCCIONES.md](INSTRUCCIONES.md) - Instalación
2. ▶️ `python prueba_simple.py` - Verificar instalación
3. ▶️ `python main.py` - Programa completo
4. 📖 [VISUALIZACION.md](VISUALIZACION.md) - Entender el ejemplo

### 🛠️ Quiero crear mi propia red
1. 📖 [EJEMPLOS_DOMINIOS.md](EJEMPLOS_DOMINIOS.md) - Plantillas y ejemplos
2. 📝 Editar `estructura_red.txt` - Tu estructura
3. 📝 Editar `probabilidades.txt` - Tus probabilidades
4. ▶️ `python main.py` - Probar tu red

### 👨‍💻 Quiero entender el código
1. 📖 [DOCUMENTACION_TECNICA.md](DOCUMENTACION_TECNICA.md) - Algoritmo
2. 💻 [`nodo.py`](nodo.py) - Empezar por lo básico
3. 💻 [`red_bayesiana.py`](red_bayesiana.py) - Estructura de red
4. 💻 [`motor_inferencia.py`](motor_inferencia.py) - Algoritmo de inferencia

### 🎓 Quiero presentar/explicar el proyecto
1. 📖 [RESUMEN.md](RESUMEN.md) - Visión general
2. 📖 [VISUALIZACION.md](VISUALIZACION.md) - Diagramas para presentación
3. ▶️ `python main.py` → Opción 1 - Demo en vivo
4. 📖 [README.md](README.md) - Características y estructura

---

## 🔍 Búsqueda Rápida

### Conceptos Teóricos

| Concepto | Ubicación |
|----------|-----------|
| Red Bayesiana | [DOCUMENTACION_TECNICA.md](DOCUMENTACION_TECNICA.md#red-bayesiana) |
| Inferencia por Enumeración | [DOCUMENTACION_TECNICA.md](DOCUMENTACION_TECNICA.md#algoritmo-de-inferencia-por-enumeración) |
| Probabilidad Conjunta | [DOCUMENTACION_TECNICA.md](DOCUMENTACION_TECNICA.md#representación-de-probabilidad-conjunta) |
| Normalización | [VISUALIZACION.md](VISUALIZACION.md#enumeración-de-train) |
| Complejidad | [DOCUMENTACION_TECNICA.md](DOCUMENTACION_TECNICA.md#complejidad) |

### Funcionalidades

| Funcionalidad | Archivo | Método/Función |
|---------------|---------|----------------|
| Cargar estructura | `red_bayesiana.py` | `cargar_estructura()` |
| Cargar probabilidades | `red_bayesiana.py` | `cargar_probabilidades()` |
| Visualizar red | `red_bayesiana.py` | `mostrar_estructura()` |
| Visualizar tablas | `red_bayesiana.py` | `mostrar_tablas_probabilidad()` |
| Realizar inferencia | `motor_inferencia.py` | `inferencia()` |
| Mostrar traza | `motor_inferencia.py` | `mostrar_traza()` |

### Ejemplos de Código

| Ejemplo | Ubicación |
|---------|-----------|
| Uso básico | [prueba_simple.py](prueba_simple.py) |
| Menú interactivo | [main.py](main.py) |
| 5 casos de inferencia | [main.py](main.py) → función `ejecutar_ejemplo_basico()` |
| Consulta personalizada | [main.py](main.py) → función `ejecutar_consulta_personalizada()` |

### Dominios de Ejemplo

| Dominio | Ubicación |
|---------|-----------|
| Transporte/Citas | Archivos principales (`estructura_red.txt`, `probabilidades.txt`) |
| Diagnóstico Médico | [EJEMPLOS_DOMINIOS.md](EJEMPLOS_DOMINIOS.md#ejemplo-1-diagnóstico-médico-simple) |
| Sistema de Seguridad | [EJEMPLOS_DOMINIOS.md](EJEMPLOS_DOMINIOS.md#ejemplo-2-sistema-de-seguridad-del-hogar) |
| Predicción del Clima | [EJEMPLOS_DOMINIOS.md](EJEMPLOS_DOMINIOS.md#ejemplo-3-predicción-del-clima) |
| Decisión de Compra | [EJEMPLOS_DOMINIOS.md](EJEMPLOS_DOMINIOS.md#ejemplo-4-decisión-de-compra-simple) |

---

## 📊 Estadísticas del Proyecto

### Archivos
- **Código Python**: 5 archivos (~1,090 líneas)
- **Datos**: 2 archivos
- **Documentación**: 7 archivos (Markdown)
- **Total**: 14 archivos

### Clases Principales
- `Nodo`: Representación de un nodo
- `RedBayesiana`: Gestión de la red
- `MotorInferencia`: Algoritmo de inferencia

### Características
- ✅ Carga desde archivos
- ✅ Visualización de estructura
- ✅ Visualización de tablas
- ✅ Inferencia por enumeración
- ✅ Trazas detalladas
- ✅ Menú interactivo
- ✅ Genérico para cualquier dominio
- ✅ Completamente documentado

---

## 🎯 Requisitos del Proyecto (Cumplimiento)

### Parte 1: Red Bayesiana
- [x] Estructura desde archivo → `red_bayesiana.py`
- [x] Visualización de estructura → `mostrar_estructura()`
- [x] Probabilidades desde archivo → `cargar_probabilidades()`
- [x] Visualización de tablas → `mostrar_tablas_probabilidad()`

### Parte 2: Motor de Inferencia
- [x] Inferencia por enumeración → `motor_inferencia.py`
- [x] Toma de decisiones → Ejemplos en `main.py`
- [x] Traza de ejecución → `mostrar_traza()`
- [x] Genericidad → Funciona con cualquier dominio
- [x] Verificación con ejemplo de clase → `VISUALIZACION.md`

---

## 🔗 Enlaces Rápidos

### Para Empezar
- [Instalación](INSTRUCCIONES.md#instalación-rápida)
- [Primer uso](INSTRUCCIONES.md#ejecución-del-proyecto)
- [Entender el ejemplo](VISUALIZACION.md)

### Para Aprender
- [Teoría](DOCUMENTACION_TECNICA.md#fundamentos-teóricos)
- [Algoritmo](DOCUMENTACION_TECNICA.md#algoritmo-de-inferencia-por-enumeración)
- [Ejemplos visuales](VISUALIZACION.md)

### Para Desarrollar
- [Arquitectura](RESUMEN.md#arquitectura-del-sistema)
- [API de clases](DOCUMENTACION_TECNICA.md#implementación)
- [Crear nuevas redes](EJEMPLOS_DOMINIOS.md#cómo-usar-estos-ejemplos)

---

## 💡 Consejos de Navegación

1. **Si tienes poco tiempo**: Lee [RESUMEN.md](RESUMEN.md) y ejecuta `python prueba_simple.py`

2. **Si quieres entender a fondo**: Lee en orden:
   - [README.md](README.md)
   - [VISUALIZACION.md](VISUALIZACION.md)
   - [DOCUMENTACION_TECNICA.md](DOCUMENTACION_TECNICA.md)

3. **Si quieres experimentar**: 
   - Lee [EJEMPLOS_DOMINIOS.md](EJEMPLOS_DOMINIOS.md)
   - Crea tus archivos de datos
   - Modifica `main.py` para cargarlos

4. **Si hay problemas**: 
   - Revisa [INSTRUCCIONES.md](INSTRUCCIONES.md#solución-de-problemas)
   - Verifica la instalación de Python
   - Ejecuta `python prueba_simple.py` para diagnóstico

---

## 📞 Estructura de Comandos

### Comandos Principales

```powershell
# Navegar al directorio
cd "c:\Users\javie\OneDrive\Documentos\unijaveriana\SEMESTRE 6\IA\Motor-de-Inferencia-2-IA"

# Prueba rápida (sin interacción)
python prueba_simple.py

# Programa completo (interactivo)
python main.py

# Ver archivos
ls
```

### Menú del Programa (main.py)

```
1. Ejecutar ejemplos predefinidos    → Ver 5 casos de inferencia
2. Realizar consulta personalizada   → Hacer tu propia consulta
3. Mostrar estructura de la red      → Ver grafo de dependencias
4. Mostrar tablas de probabilidad    → Ver todas las CPTs
5. Salir                             → Terminar programa
```

---

## 🎓 Orden Sugerido de Lectura

### Para Estudiantes (Primera Vez)
1. [RESUMEN.md](RESUMEN.md) - 5 min
2. [INSTRUCCIONES.md](INSTRUCCIONES.md) - 10 min
3. Ejecutar `python prueba_simple.py` - 2 min
4. [VISUALIZACION.md](VISUALIZACION.md) - 15 min
5. Ejecutar `python main.py` → Opción 1 - 20 min
6. [DOCUMENTACION_TECNICA.md](DOCUMENTACION_TECNICA.md) - 30 min

**Total: ~82 minutos**

### Para Profesores/Revisores
1. [RESUMEN.md](RESUMEN.md) - Verificar cumplimiento
2. Ejecutar `python main.py` → Opción 1 - Ver ejemplos
3. [DOCUMENTACION_TECNICA.md](DOCUMENTACION_TECNICA.md) - Validar algoritmo
4. Revisar código: `motor_inferencia.py` - Implementación

**Total: ~45 minutos**

### Para Desarrolladores
1. [DOCUMENTACION_TECNICA.md](DOCUMENTACION_TECNICA.md) - Arquitectura
2. Código en orden: `nodo.py` → `red_bayesiana.py` → `motor_inferencia.py`
3. [EJEMPLOS_DOMINIOS.md](EJEMPLOS_DOMINIOS.md) - Extensibilidad
4. Experimentar con nuevas redes

**Total: ~90 minutos**

---

## ✨ Resumen

Este proyecto es un **sistema completo** de Red Bayesiana con Motor de Inferencia por Enumeración:

- **1,090+ líneas** de código Python bien documentado
- **7 archivos** de documentación exhaustiva
- **5 ejemplos** predefinidos de inferencia
- **4 dominios** adicionales como plantillas
- **Completamente funcional** y listo para usar

**Todo lo que necesitas está aquí. ¡Comienza explorando!** 🚀

---

*Última actualización: Noviembre 2025*
*Proyecto: Motor de Inferencia por Enumeración - Universidad Javeriana*
