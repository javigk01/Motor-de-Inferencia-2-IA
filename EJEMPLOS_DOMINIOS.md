# Ejemplos de Redes Bayesianas para Otros Dominios

Este archivo contiene plantillas y ejemplos para crear tus propias Redes Bayesianas en diferentes dominios.

## Ejemplo 1: Diagnóstico Médico Simple

### Archivo: estructura_medica.txt
```
# Red Bayesiana para diagnóstico médico simple
# Dominio: Gripe y sus síntomas

Gripe -> Fiebre
Gripe -> DolorCabeza
Gripe -> Cansancio
```

### Archivo: probabilidades_medica.txt
```
# Nodo raíz: Gripe
[Gripe]
values: si, no
P(Gripe=si) = 0.1
P(Gripe=no) = 0.9

# Síntoma: Fiebre
[Fiebre]
values: alta, normal
parents: Gripe
P(Fiebre=alta | Gripe=si) = 0.8
P(Fiebre=normal | Gripe=si) = 0.2
P(Fiebre=alta | Gripe=no) = 0.1
P(Fiebre=normal | Gripe=no) = 0.9

# Síntoma: Dolor de Cabeza
[DolorCabeza]
values: si, no
parents: Gripe
P(DolorCabeza=si | Gripe=si) = 0.7
P(DolorCabeza=no | Gripe=si) = 0.3
P(DolorCabeza=si | Gripe=no) = 0.2
P(DolorCabeza=no | Gripe=no) = 0.8

# Síntoma: Cansancio
[Cansancio]
values: alto, normal
parents: Gripe
P(Cansancio=alto | Gripe=si) = 0.9
P(Cansancio=normal | Gripe=si) = 0.1
P(Cansancio=alto | Gripe=no) = 0.3
P(Cansancio=normal | Gripe=no) = 0.7
```

### Consultas de Ejemplo
- `P(Gripe | Fiebre=alta, DolorCabeza=si)` - ¿Probabilidad de gripe con fiebre y dolor de cabeza?
- `P(Cansancio | Gripe=si)` - ¿Probabilidad de cansancio si hay gripe?

---

## Ejemplo 2: Sistema de Seguridad del Hogar

### Archivo: estructura_seguridad.txt
```
# Red Bayesiana para sistema de seguridad
# Dominio: Alarma de casa

Robo -> Alarma
Terremoto -> Alarma
Alarma -> JuanLlama
Alarma -> MariaLlama
```

### Archivo: probabilidades_seguridad.txt
```
# Evento: Robo
[Robo]
values: si, no
P(Robo=si) = 0.001
P(Robo=no) = 0.999

# Evento: Terremoto
[Terremoto]
values: si, no
P(Terremoto=si) = 0.002
P(Terremoto=no) = 0.998

# Sistema: Alarma
[Alarma]
values: suena, no_suena
parents: Robo, Terremoto
P(Alarma=suena | Robo=si, Terremoto=si) = 0.95
P(Alarma=no_suena | Robo=si, Terremoto=si) = 0.05
P(Alarma=suena | Robo=si, Terremoto=no) = 0.94
P(Alarma=no_suena | Robo=si, Terremoto=no) = 0.06
P(Alarma=suena | Robo=no, Terremoto=si) = 0.29
P(Alarma=no_suena | Robo=no, Terremoto=si) = 0.71
P(Alarma=suena | Robo=no, Terremoto=no) = 0.001
P(Alarma=no_suena | Robo=no, Terremoto=no) = 0.999

# Observación: Juan llama
[JuanLlama]
values: si, no
parents: Alarma
P(JuanLlama=si | Alarma=suena) = 0.90
P(JuanLlama=no | Alarma=suena) = 0.10
P(JuanLlama=si | Alarma=no_suena) = 0.05
P(JuanLlama=no | Alarma=no_suena) = 0.95

# Observación: Maria llama
[MariaLlama]
values: si, no
parents: Alarma
P(MariaLlama=si | Alarma=suena) = 0.70
P(MariaLlama=no | Alarma=suena) = 0.30
P(MariaLlama=si | Alarma=no_suena) = 0.01
P(MariaLlama=no | Alarma=no_suena) = 0.99
```

### Consultas de Ejemplo
- `P(Robo | JuanLlama=si, MariaLlama=si)` - ¿Hubo robo si ambos llaman?
- `P(Alarma | Terremoto=si)` - ¿Suena la alarma si hay terremoto?

---

## Ejemplo 3: Predicción del Clima

### Archivo: estructura_clima.txt
```
# Red Bayesiana para predicción del clima
# Dominio: Pronóstico simple

Estacion -> Temperatura
Estacion -> Lluvia
Temperatura -> Humedad
Lluvia -> Humedad
Humedad -> Comodidad
```

### Archivo: probabilidades_clima.txt
```
# Nodo raíz: Estación del año
[Estacion]
values: verano, invierno, primavera, otono
P(Estacion=verano) = 0.25
P(Estacion=invierno) = 0.25
P(Estacion=primavera) = 0.25
P(Estacion=otono) = 0.25

# Variable: Temperatura
[Temperatura]
values: calida, fria
parents: Estacion
P(Temperatura=calida | Estacion=verano) = 0.9
P(Temperatura=fria | Estacion=verano) = 0.1
P(Temperatura=calida | Estacion=invierno) = 0.1
P(Temperatura=fria | Estacion=invierno) = 0.9
P(Temperatura=calida | Estacion=primavera) = 0.6
P(Temperatura=fria | Estacion=primavera) = 0.4
P(Temperatura=calida | Estacion=otono) = 0.5
P(Temperatura=fria | Estacion=otono) = 0.5

# Variable: Lluvia
[Lluvia]
values: si, no
parents: Estacion
P(Lluvia=si | Estacion=verano) = 0.2
P(Lluvia=no | Estacion=verano) = 0.8
P(Lluvia=si | Estacion=invierno) = 0.6
P(Lluvia=no | Estacion=invierno) = 0.4
P(Lluvia=si | Estacion=primavera) = 0.7
P(Lluvia=no | Estacion=primavera) = 0.3
P(Lluvia=si | Estacion=otono) = 0.5
P(Lluvia=no | Estacion=otono) = 0.5

# Variable: Humedad
[Humedad]
values: alta, baja
parents: Temperatura, Lluvia
P(Humedad=alta | Temperatura=calida, Lluvia=si) = 0.95
P(Humedad=baja | Temperatura=calida, Lluvia=si) = 0.05
P(Humedad=alta | Temperatura=calida, Lluvia=no) = 0.5
P(Humedad=baja | Temperatura=calida, Lluvia=no) = 0.5
P(Humedad=alta | Temperatura=fria, Lluvia=si) = 0.8
P(Humedad=baja | Temperatura=fria, Lluvia=si) = 0.2
P(Humedad=alta | Temperatura=fria, Lluvia=no) = 0.3
P(Humedad=baja | Temperatura=fria, Lluvia=no) = 0.7

# Variable: Comodidad
[Comodidad]
values: confortable, incomodo
parents: Humedad
P(Comodidad=confortable | Humedad=alta) = 0.3
P(Comodidad=incomodo | Humedad=alta) = 0.7
P(Comodidad=confortable | Humedad=baja) = 0.8
P(Comodidad=incomodo | Humedad=baja) = 0.2
```

---

## Ejemplo 4: Decisión de Compra Simple

### Archivo: estructura_compra.txt
```
# Red Bayesiana para decisión de compra
# Dominio: Compra de producto

Ingreso -> Necesidad
Oferta -> Precio
Precio -> Decision
Necesidad -> Decision
```

### Archivo: probabilidades_compra.txt
```
[Ingreso]
values: alto, medio, bajo
P(Ingreso=alto) = 0.3
P(Ingreso=medio) = 0.5
P(Ingreso=bajo) = 0.2

[Oferta]
values: si, no
P(Oferta=si) = 0.3
P(Oferta=no) = 0.7

[Necesidad]
values: urgente, moderada, baja
parents: Ingreso
P(Necesidad=urgente | Ingreso=alto) = 0.2
P(Necesidad=moderada | Ingreso=alto) = 0.5
P(Necesidad=baja | Ingreso=alto) = 0.3
P(Necesidad=urgente | Ingreso=medio) = 0.3
P(Necesidad=moderada | Ingreso=medio) = 0.5
P(Necesidad=baja | Ingreso=medio) = 0.2
P(Necesidad=urgente | Ingreso=bajo) = 0.5
P(Necesidad=moderada | Ingreso=bajo) = 0.3
P(Necesidad=baja | Ingreso=bajo) = 0.2

[Precio]
values: caro, economico
parents: Oferta
P(Precio=caro | Oferta=si) = 0.2
P(Precio=economico | Oferta=si) = 0.8
P(Precio=caro | Oferta=no) = 0.7
P(Precio=economico | Oferta=no) = 0.3

[Decision]
values: compra, no_compra
parents: Precio, Necesidad
P(Decision=compra | Precio=caro, Necesidad=urgente) = 0.7
P(Decision=no_compra | Precio=caro, Necesidad=urgente) = 0.3
P(Decision=compra | Precio=caro, Necesidad=moderada) = 0.3
P(Decision=no_compra | Precio=caro, Necesidad=moderada) = 0.7
P(Decision=compra | Precio=caro, Necesidad=baja) = 0.1
P(Decision=no_compra | Precio=caro, Necesidad=baja) = 0.9
P(Decision=compra | Precio=economico, Necesidad=urgente) = 0.95
P(Decision=no_compra | Precio=economico, Necesidad=urgente) = 0.05
P(Decision=compra | Precio=economico, Necesidad=moderada) = 0.7
P(Decision=no_compra | Precio=economico, Necesidad=moderada) = 0.3
P(Decision=compra | Precio=economico, Necesidad=baja) = 0.4
P(Decision=no_compra | Precio=economico, Necesidad=baja) = 0.6
```

---

## Cómo Usar Estos Ejemplos

### Paso 1: Crea los archivos
Copia el contenido de "estructura_XXX.txt" y "probabilidades_XXX.txt" en archivos nuevos.

### Paso 2: Modifica main.py
En la función `main()`, cambia las líneas de carga:

```python
red.cargar_estructura('estructura_medica.txt')  # Cambia el nombre
red.cargar_probabilidades('probabilidades_medica.txt')  # Cambia el nombre
```

### Paso 3: Ejecuta el programa
```powershell
python main.py
```

### Paso 4: Realiza consultas
Usa el menú interactivo para hacer consultas según el dominio que elegiste.

---

## Consejos para Crear Tu Propia Red

### 1. Define las Variables
- Identifica las variables relevantes de tu dominio
- Determina los valores posibles de cada variable
- Mantén el número de valores pequeño (2-4 valores por variable idealmente)

### 2. Establece las Dependencias
- ¿Qué variables influyen en otras?
- Dibuja un diagrama con flechas: A → B significa "A influye en B"
- Evita ciclos (A → B → C → A no está permitido)

### 3. Estima las Probabilidades
- Para nodos raíz: probabilidades a priori (basadas en datos o conocimiento experto)
- Para otros nodos: probabilidades condicionales P(hijo | padres)
- Asegúrate de que las probabilidades sumen 1 para cada configuración

### 4. Valida la Red
- Las probabilidades de cada nodo deben sumar 1 para cada combinación de padres
- Verifica que las relaciones de dependencia tengan sentido
- Prueba con consultas cuyas respuestas conozcas

---

## Reglas de Formato

### Archivo de Estructura
```
# Comentarios comienzan con #
Padre -> Hijo
OtroPadre -> MismoHijo
```

### Archivo de Probabilidades
```
[NombreNodo]
values: valor1, valor2, valor3
parents: Padre1, Padre2  # Omitir si no tiene padres
P(NombreNodo=valor1 | Padre1=valorA, Padre2=valorB) = 0.XX
```

### Reglas Importantes
1. Los nombres de nodos no deben contener espacios
2. Los valores no deben contener espacios (usa guiones bajos: `muy_alto`)
3. Las probabilidades deben estar entre 0 y 1
4. Para cada combinación de valores de padres, las probabilidades del nodo hijo deben sumar 1

---

## Ejemplo de Conversión

Si tienes este concepto: "El éxito en un examen depende del estudio y el sueño"

### 1. Variables
- Estudio: {mucho, poco}
- Sueno: {suficiente, insuficiente}
- Exito: {aprobo, reprobo}

### 2. Dependencias
```
Estudio -> Exito
Sueno -> Exito
```

### 3. Probabilidades (ejemplo)
```
[Estudio]
values: mucho, poco
P(Estudio=mucho) = 0.6
P(Estudio=poco) = 0.4

[Sueno]
values: suficiente, insuficiente
P(Sueno=suficiente) = 0.7
P(Sueno=insuficiente) = 0.3

[Exito]
values: aprobo, reprobo
parents: Estudio, Sueno
P(Exito=aprobo | Estudio=mucho, Sueno=suficiente) = 0.9
P(Exito=reprobo | Estudio=mucho, Sueno=suficiente) = 0.1
# ... y así para todas las combinaciones
```

---

¡Ahora estás listo para crear tus propias Redes Bayesianas en cualquier dominio!
