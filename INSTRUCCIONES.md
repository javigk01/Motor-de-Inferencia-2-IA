# Instrucciones de Instalación y Ejecución

## 📦 Requisitos Previos

### Instalar Python

Este proyecto requiere Python 3.6 o superior. Si aún no tienes Python instalado:

#### Opción 1: Descargar desde el sitio oficial
1. Ve a [python.org](https://www.python.org/downloads/)
2. Descarga Python 3.11 o superior (recomendado)
3. Durante la instalación, **asegúrate de marcar la casilla "Add Python to PATH"**
4. Completa la instalación

#### Opción 2: Microsoft Store (Windows)
1. Abre Microsoft Store
2. Busca "Python 3.11"
3. Instala Python desde allí

### Verificar la instalación

Abre una terminal de PowerShell y ejecuta:

```powershell
python --version
```

Deberías ver algo como: `Python 3.11.x`

## 🚀 Ejecución del Proyecto

### Paso 1: Navegar al directorio del proyecto

```powershell
cd "c:\Users\javie\OneDrive\Documentos\unijaveriana\SEMESTRE 6\IA\Motor-de-Inferencia-2-IA"
```

### Paso 2: Verificar que los archivos existen

```powershell
ls
```

Deberías ver los siguientes archivos:
- `nodo.py`
- `red_bayesiana.py`
- `motor_inferencia.py`
- `main.py`
- `prueba_simple.py`
- `estructura_red.txt`
- `probabilidades.txt`
- `README.md`

### Paso 3: Ejecutar prueba simple

Para una prueba rápida sin interacción:

```powershell
python prueba_simple.py
```

Este script verificará que todo funciona correctamente y mostrará un ejemplo de inferencia.

### Paso 4: Ejecutar programa principal

Para el programa completo con menú interactivo y múltiples ejemplos:

```powershell
python main.py
```

## 📋 Opciones del Menú Principal

Una vez ejecutes `main.py`, verás las siguientes opciones:

1. **Ejecutar ejemplos predefinidos**: 
   - Muestra 5 ejemplos de inferencia diferentes
   - Genera trazas completas del proceso
   - Incluye interpretaciones de los resultados

2. **Realizar consulta personalizada**: 
   - Permite hacer tus propias consultas
   - Puedes elegir cualquier variable y evidencia
   - Ideal para experimentar

3. **Mostrar estructura de la red**: 
   - Visualiza la jerarquía de nodos
   - Muestra relaciones padre-hijo
   - Identifica nodos raíz

4. **Mostrar tablas de probabilidad**: 
   - Muestra todas las CPTs (Conditional Probability Tables)
   - Formato claro y organizado

5. **Salir**: 
   - Termina el programa

## 🎯 Ejemplos de Uso

### Ejemplo 1: Ejecución básica

```powershell
python main.py
# Selecciona opción 1 para ver todos los ejemplos
```

### Ejemplo 2: Consulta personalizada

```powershell
python main.py
# Selecciona opción 2
# Variable a consultar: Appointment
# Variable de evidencia: Rain
# Valor: heavy
```

Esto calculará: `P(Appointment | Rain=heavy)`

## 🔧 Modificar el Ejemplo

### Cambiar la estructura de la red

Edita `estructura_red.txt`:

```
# Formato: Nodo_Padre -> Nodo_Hijo
NuevoPadre -> NuevoHijo
```

### Cambiar las probabilidades

Edita `probabilidades.txt`:

```
[NombreNodo]
values: valor1, valor2
parents: Padre1  # Si tiene padres
P(NombreNodo=valor1 | Padre1=valorA) = 0.8
P(NombreNodo=valor2 | Padre1=valorA) = 0.2
```

### Crear tu propia red

1. Crea un nuevo archivo de estructura (ej: `mi_red.txt`)
2. Crea un nuevo archivo de probabilidades (ej: `mi_probabilidades.txt`)
3. Modifica `main.py` en la función `main()`:

```python
red.cargar_estructura('mi_red.txt')
red.cargar_probabilidades('mi_probabilidades.txt')
```

## 📊 Interpretación de Resultados

El programa muestra:

1. **Traza de ejecución**: Paso a paso del algoritmo de enumeración
2. **Probabilidades parciales**: Valores intermedios del cálculo
3. **Normalización**: Cómo se aplica el factor α
4. **Resultados finales**: Probabilidades normalizadas en formato decimal y porcentaje

### Ejemplo de salida:

```
RESULTADOS DE LA INFERENCIA
──────────────────────────────────────────────────
Valor                Probabilidad    Porcentaje     
──────────────────────────────────────────────────
attend               0.645833        64.58%
miss                 0.354167        35.42%
──────────────────────────────────────────────────
```

## ❗ Solución de Problemas

### Error: "No se encontró Python"
- Asegúrate de haber instalado Python correctamente
- Verifica que Python esté en el PATH del sistema
- Reinicia la terminal después de instalar Python

### Error: "No se pudo cargar la red bayesiana"
- Verifica que los archivos `estructura_red.txt` y `probabilidades.txt` existan
- Asegúrate de estar en el directorio correcto del proyecto

### Error de sintaxis en archivos de datos
- Revisa que el formato sea correcto
- Los comentarios deben empezar con `#`
- Las relaciones usan `->` (guion-mayor que)
- Las probabilidades usan `=` (igual)

## 🎓 Estructura del Código

```
Motor-de-Inferencia-2-IA/
│
├── nodo.py                    # Clase Nodo
├── red_bayesiana.py           # Clase RedBayesiana
├── motor_inferencia.py        # Motor de Inferencia
├── main.py                    # Programa principal interactivo
├── prueba_simple.py           # Script de prueba rápida
│
├── estructura_red.txt         # Estructura de la red
├── probabilidades.txt         # Tablas de probabilidad
│
├── README.md                  # Documentación general
└── INSTRUCCIONES.md          # Este archivo
```

## 💡 Consejos

1. **Prueba primero con `prueba_simple.py`** para verificar que todo funciona
2. **Usa el menú opción 3 y 4** para familiarizarte con la red antes de hacer inferencias
3. **Lee las trazas completas** para entender cómo funciona el algoritmo
4. **Experimenta con diferentes evidencias** para ver cómo cambian las probabilidades
5. **Modifica las tablas de probabilidad** para crear tus propios escenarios

## 📚 Referencias

- **Algoritmo de Enumeración**: Russell & Norvig, "Artificial Intelligence: A Modern Approach"
- **Redes Bayesianas**: Materiales del curso de IA, Universidad Javeriana

## 🤝 Soporte

Si tienes problemas:
1. Verifica que Python esté instalado correctamente
2. Asegúrate de estar en el directorio correcto
3. Revisa que todos los archivos estén presentes
4. Verifica el formato de los archivos de datos

---

**¡Listo para empezar!** Ejecuta `python prueba_simple.py` para comenzar.
