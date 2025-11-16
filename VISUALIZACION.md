# 🎨 Visualización de la Red Bayesiana - Ejemplo del Proyecto

## Estructura de la Red

```
                    ┌──────────────┐
                    │     Rain     │
                    │ {none, light,│
                    │    heavy}    │
                    └──────┬───────┘
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     │
        ┌───────────────┐             │
        │  Maintenance  │             │
        │   {yes, no}   │             │
        └───────┬───────┘             │
                │                     │
                └──────────┬──────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Train     │
                    │  {on_time,   │
                    │   delayed}   │
                    └──────┬───────┘
                           │
                           │
                           ▼
                    ┌──────────────┐
                    │ Appointment  │
                    │{attend, miss}│
                    └──────────────┘
```

---

## Tablas de Probabilidad

### 1. Rain (Nodo Raíz)

```
┌────────────────────────────┐
│  P(Rain)                   │
├──────────┬─────────────────┤
│  none    │  0.7  (70%)    │
│  light   │  0.2  (20%)    │
│  heavy   │  0.1  (10%)    │
└──────────┴─────────────────┘
```

### 2. Maintenance (Nodo Raíz)

```
┌────────────────────────────┐
│  P(Maintenance)            │
├──────────┬─────────────────┤
│  yes     │  0.4  (40%)    │
│  no      │  0.6  (60%)    │
└──────────┴─────────────────┘
```

### 3. Train (Depende de Rain y Maintenance)

```
┌─────────────┬────────────┬─────────┬──────────┐
│    Rain     │ Maintenance│  Train  │   Prob   │
├─────────────┼────────────┼─────────┼──────────┤
│    none     │    yes     │on_time  │   0.8    │
│    none     │    yes     │delayed  │   0.2    │
├─────────────┼────────────┼─────────┼──────────┤
│    none     │    no      │on_time  │   0.9    │
│    none     │    no      │delayed  │   0.1    │
├─────────────┼────────────┼─────────┼──────────┤
│   light     │    yes     │on_time  │   0.6    │
│   light     │    yes     │delayed  │   0.4    │
├─────────────┼────────────┼─────────┼──────────┤
│   light     │    no      │on_time  │   0.7    │
│   light     │    no      │delayed  │   0.3    │
├─────────────┼────────────┼─────────┼──────────┤
│   heavy     │    yes     │on_time  │   0.4    │
│   heavy     │    yes     │delayed  │   0.6    │
├─────────────┼────────────┼─────────┼──────────┤
│   heavy     │    no      │on_time  │   0.5    │
│   heavy     │    no      │delayed  │   0.5    │
└─────────────┴────────────┴─────────┴──────────┘
```

### 4. Appointment (Depende de Train)

```
┌──────────┬─────────────┬──────────┐
│  Train   │ Appointment │   Prob   │
├──────────┼─────────────┼──────────┤
│ on_time  │   attend    │   0.9    │
│ on_time  │   miss      │   0.1    │
├──────────┼─────────────┼──────────┤
│ delayed  │   attend    │   0.6    │
│ delayed  │   miss      │   0.4    │
└──────────┴─────────────┴──────────┘
```

---

## Interpretación de las Probabilidades

### Rain (Lluvia)
- **70%** días sin lluvia
- **20%** días con lluvia ligera
- **10%** días con lluvia fuerte
- *Basado en promedio climático*

### Maintenance (Mantenimiento)
- **40%** probabilidad de mantenimiento programado
- **60%** probabilidad de no haber mantenimiento
- *Basado en calendario de mantenimiento*

### Train (Tren)
- La **lluvia** y el **mantenimiento** afectan la puntualidad
- **Mejor escenario**: Sin lluvia + Sin mantenimiento → 90% puntual
- **Peor escenario**: Lluvia fuerte + Mantenimiento → 40% puntual
- *La lluvia tiene mayor impacto que el mantenimiento*

### Appointment (Cita)
- **Tren a tiempo**: 90% de asistir a la cita
- **Tren retrasado**: 60% de asistir (aún hay posibilidad)
- *El estado del tren es el factor determinante*

---

## Flujo de Inferencia - Ejemplo Visual

### Consulta: P(Appointment | Rain=light, Maintenance=yes)

```
                    ┌──────────────┐
                    │     Rain     │
                    │  light ✓     │ ← Evidencia
                    └──────┬───────┘
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     │
        ┌───────────────┐             │
        │  Maintenance  │             │
        │   yes ✓       │ ← Evidencia │
        └───────┬───────┘             │
                │                     │
                └──────────┬──────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Train     │
                    │   ????       │ ← Variable Oculta
                    └──────┬───────┘   (Enumerar)
                           │
                           │
                           ▼
                    ┌──────────────┐
                    │ Appointment  │
                    │   ????       │ ← Variable de Consulta
                    └──────────────┘
```

### Enumeración de Train

```
Escenario 1: Train = on_time
─────────────────────────────────────────
P(Rain=light) × P(Maintenance=yes) × 
P(Train=on_time | Rain=light, Maintenance=yes) × 
P(Appointment=attend | Train=on_time)

= 0.2 × 0.4 × 0.6 × 0.9 = 0.0432

P(Appointment=miss | Train=on_time)
= 0.2 × 0.4 × 0.6 × 0.1 = 0.0048


Escenario 2: Train = delayed
─────────────────────────────────────────
P(Rain=light) × P(Maintenance=yes) × 
P(Train=delayed | Rain=light, Maintenance=yes) × 
P(Appointment=attend | Train=delayed)

= 0.2 × 0.4 × 0.4 × 0.6 = 0.0192

P(Appointment=miss | Train=delayed)
= 0.2 × 0.4 × 0.4 × 0.4 = 0.0128


Suma Total (antes de normalizar)
─────────────────────────────────────────
P(Appointment=attend, evidencia) = 0.0432 + 0.0192 = 0.0624
P(Appointment=miss, evidencia)   = 0.0048 + 0.0128 = 0.0176


Normalización
─────────────────────────────────────────
α = 1 / (0.0624 + 0.0176) = 1 / 0.08 = 12.5

P(Appointment=attend | evidencia) = 12.5 × 0.0624 = 0.78 (78%)
P(Appointment=miss | evidencia)   = 12.5 × 0.0176 = 0.22 (22%)
```

---

## Escenarios Comparativos

### Escenario A: Mejor caso para asistir
```
Evidencia: Rain=none, Maintenance=no

      Rain=none (70%)
            +
    Maintenance=no (60%)
            ↓
    Train=on_time (90%)
            ↓
  Appointment=attend (90%)

Resultado: ~81% probabilidad de asistir
```

### Escenario B: Peor caso
```
Evidencia: Rain=heavy, Maintenance=yes

     Rain=heavy (10%)
            +
    Maintenance=yes (40%)
            ↓
    Train=on_time (40%) o delayed (60%)
            ↓
  Appointment=attend (?)

Resultado: ~52% probabilidad de asistir
```

### Escenario C: Caso del ejemplo
```
Evidencia: Rain=light, Maintenance=yes

     Rain=light (20%)
            +
    Maintenance=yes (40%)
            ↓
    Train=on_time (60%) o delayed (40%)
            ↓
  Appointment=attend (?)

Resultado: 78% probabilidad de asistir
```

---

## Análisis de Sensibilidad

### Impacto de la Lluvia en el Tren (sin mantenimiento)

```
┌─────────┬──────────────────┬──────────────────┐
│  Rain   │ P(Train=on_time) │  P(Train=delay)  │
├─────────┼──────────────────┼──────────────────┤
│  none   │      0.9         │       0.1        │
│  light  │      0.7         │       0.3        │
│  heavy  │      0.5         │       0.5        │
└─────────┴──────────────────┴──────────────────┘

Impacto: La lluvia reduce significativamente la puntualidad
```

### Impacto del Mantenimiento en el Tren (sin lluvia)

```
┌──────────────┬──────────────────┬──────────────────┐
│ Maintenance  │ P(Train=on_time) │  P(Train=delay)  │
├──────────────┼──────────────────┼──────────────────┤
│     yes      │      0.8         │       0.2        │
│     no       │      0.9         │       0.1        │
└──────────────┴──────────────────┴──────────────────┘

Impacto: El mantenimiento reduce moderadamente la puntualidad
```

### Impacto del Tren en la Cita

```
┌──────────┬─────────────────────┬────────────────────┐
│  Train   │ P(Appointment=attend)│P(Appointment=miss) │
├──────────┼─────────────────────┼────────────────────┤
│ on_time  │       0.9           │        0.1         │
│ delayed  │       0.6           │        0.4         │
└──────────┴─────────────────────┴────────────────────┘

Impacto: El tren es el factor más crítico para la cita
```

---

## Decisiones Basadas en Probabilidades

### Regla de Decisión Simple

```
SI P(Appointment=attend | evidencia) > 0.7
    ENTONCES: "Ir a la cita (alta probabilidad de llegar)"
SI P(Appointment=attend | evidencia) entre 0.5 y 0.7
    ENTONCES: "Salir con tiempo extra (probabilidad moderada)"
SI P(Appointment=attend | evidencia) < 0.5
    ENTONCES: "Reprogramar la cita (baja probabilidad)"
```

### Ejemplos de Aplicación

```
1. Rain=none, Maintenance=no
   → P(attend) ≈ 0.81
   → DECISIÓN: "Ir a la cita"

2. Rain=light, Maintenance=yes
   → P(attend) ≈ 0.78
   → DECISIÓN: "Ir a la cita (con precaución)"

3. Rain=heavy, Maintenance=yes
   → P(attend) ≈ 0.52
   → DECISIÓN: "Salir mucho más temprano"

4. Si además observamos Train=delayed
   → P(attend) = 0.60
   → DECISIÓN: "Considerar transporte alternativo"
```

---

## Resumen Visual

```
┌─────────────────────────────────────────────────────┐
│           FACTORES DE INFLUENCIA                    │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Lluvia ──────┐                                    │
│               ├─→ Puntualidad del Tren ──┐         │
│  Mantenimiento┘                          │         │
│                                          ├─→ Asistir│
│                                    (Factor crítico) │
│                                                     │
└─────────────────────────────────────────────────────┘

CADENA CAUSAL:
Clima/Mantenimiento → Transporte → Asistencia a Cita
```

---

Esta visualización ayuda a entender cómo las diferentes variables interactúan y cómo el motor de inferencia calcula las probabilidades paso a paso.
