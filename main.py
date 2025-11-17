"""
Programa principal para demostrar el funcionamiento del Motor de Inferencia
por Enumeración con Redes Bayesianas.

Este programa carga una Red Bayesiana desde archivos, visualiza su estructura
y tablas de probabilidad, y realiza inferencias utilizando el algoritmo de
enumeración.

Ejemplo basado en el problema de:
- Rain (lluvia)
- Maintenance (mantenimiento)
- Train (tren)
- Appointment (cita)
"""

from red_bayesiana import RedBayesiana
from motor_inferencia import MotorInferencia

def imprimir_titulo(titulo):
    """
    Imprime un título formateado.
    
    Args:
        titulo (str): Título a imprimir
    """
    print(f"\n{'#'*80}")
    print(f"# {titulo.center(76)} #")
    print(f"{'#'*80}\n")

def imprimir_resultados(resultados):
    """
    Imprime los resultados de una inferencia en formato tabla, incluyendo las probabilidades parciales (no normalizadas) si están disponibles.
    
    Args:
        resultados (dict): Diccionario con los resultados de la inferencia (normalizados)
        parciales (dict, opcional): Diccionario con las probabilidades parciales (no normalizadas)
    """
    parciales = None
    if isinstance(resultados, tuple) and len(resultados) == 2:
        resultados, parciales = resultados
    print("\n" + "─"*70)
    print("RESULTADOS DE LA INFERENCIA")
    print("─"*70)
    encabezado = f"{'Valor':<20} {'Probabilidad':<15} {'Porcentaje':<15}"
    if parciales:
        encabezado += f"{'Parcial':<15}"
    print(encabezado)
    print("─"*70)
    for valor, prob in sorted(resultados.items(), key=lambda x: x[1], reverse=True):
        fila = f"{valor:<20} {prob:<15.6f} {prob*100:<14.2f}%"
        if parciales:
            fila += f"{parciales.get(valor, 0):<15.6f}"
        print(fila)
    print("─"*70 + "\n")

def ejecutar_ejemplo_basico(archivo_estructura, archivo_probabilidades):
    """
    Ejecuta el ejemplo básico de la Red Bayesiana con inferencias usando los archivos de entrada.
    """
    imprimir_titulo("MOTOR DE INFERENCIA POR ENUMERACIÓN - RED BAYESIANA")

    # Crear red bayesiana
    red = RedBayesiana()

    # Cargar estructura y probabilidades
    red.cargar_estructura(archivo_estructura)
    red.cargar_probabilidades(archivo_probabilidades)

    # Mostrar estructura
    red.mostrar_estructura()

    # Mostrar tablas de probabilidad
    red.mostrar_tablas_probabilidad()

    # Crear motor de inferencia
    motor = MotorInferencia(red)

    # Pausa para que el usuario pueda revisar
    print("\n" + "="*80)
    input("Presiona ENTER para continuar con los ejemplos de inferencia...")

    # Detectar nodos para ejemplos automáticos
    nodos = list(red.nodos.keys())
    if len(nodos) < 2:
        print("No hay suficientes nodos para ejemplos automáticos.")
        return

    # Ejemplo 1: Probabilidad del primer nodo dado el segundo (si es posible)
    imprimir_titulo(f"EJEMPLO 1: P({nodos[0]} | {nodos[1]})")
    print(f"Pregunta: ¿Cuál es la probabilidad de {nodos[0]} dado {nodos[1]}?")
    print()
    evidencia1 = {nodos[1]: red.nodos[nodos[1]].valores[0]}
    resultado1, parciales1 = motor.inferencia({nodos[0]: None}, evidencia1, return_parciales=True)
    motor.mostrar_traza()
    imprimir_resultados((resultado1, parciales1))
    print("INTERPRETACIÓN:")
    print(f"  Con {nodos[1]}={red.nodos[nodos[1]].valores[0]}, la probabilidad de {nodos[0]} es:")
    for val in resultado1:
        print(f"  {val}: {resultado1[val]*100:.2f}%")
    print()
    input("Presiona ENTER para continuar con el siguiente ejemplo...")

    # Ejemplo 2: Probabilidad del segundo nodo sin evidencia
    imprimir_titulo(f"EJEMPLO 2: P({nodos[1]}) - Sin evidencia")
    print(f"Pregunta: ¿Cuál es la probabilidad de {nodos[1]} sin evidencia?")
    print()
    evidencia2 = {}
    resultado2, parciales2 = motor.inferencia({nodos[1]: None}, evidencia2, return_parciales=True)
    motor.mostrar_traza()
    imprimir_resultados((resultado2, parciales2))
    print("INTERPRETACIÓN:")
    for val in resultado2:
        print(f"  {val}: {resultado2[val]*100:.2f}%")
    print()
    input("Presiona ENTER para continuar con el siguiente ejemplo...")

    # Ejemplo 3: Probabilidad del último nodo dado el primero
    imprimir_titulo(f"EJEMPLO 3: P({nodos[-1]} | {nodos[0]})")
    print(f"Pregunta: ¿Cuál es la probabilidad de {nodos[-1]} dado {nodos[0]}?")
    print()
    evidencia3 = {nodos[0]: red.nodos[nodos[0]].valores[0]}
    resultado3, parciales3 = motor.inferencia({nodos[-1]: None}, evidencia3, return_parciales=True)
    motor.mostrar_traza()
    imprimir_resultados((resultado3, parciales3))
    print("INTERPRETACIÓN:")
    for val in resultado3:
        print(f"  {val}: {resultado3[val]*100:.2f}%")
    print()

def ejecutar_consulta_personalizada(red, motor):
    """
    Permite al usuario realizar consultas personalizadas.
    
    Args:
        red (RedBayesiana): Red Bayesiana cargada
        motor (MotorInferencia): Motor de inferencia
    """
    imprimir_titulo("CONSULTA PERSONALIZADA")
    
    print("Variables disponibles:")
    for nombre_nodo in sorted(red.nodos.keys()):
        nodo = red.nodos[nombre_nodo]
        print(f"  - {nombre_nodo}: {nodo.valores}")
    print()
    
    # Solicitar variable de consulta
    var_consulta = input("Ingrese la variable a consultar: ").strip()
    
    if var_consulta not in red.nodos:
        print(f"Error: La variable '{var_consulta}' no existe en la red.")
        return
    
    # Solicitar evidencia
    print("\nIngrese la evidencia (presione ENTER sin escribir nada para terminar):")
    evidencia = {}
    
    while True:
        var_evidencia = input("  Variable (o ENTER para terminar): ").strip()
        if not var_evidencia:
            break
        
        if var_evidencia not in red.nodos:
            print(f"  Error: La variable '{var_evidencia}' no existe.")
            continue
        
        nodo = red.nodos[var_evidencia]
        print(f"  Valores posibles: {nodo.valores}")
        valor = input("  Valor: ").strip()
        
        if valor not in nodo.valores:
            print(f"  Error: '{valor}' no es un valor válido.")
            continue
        
        evidencia[var_evidencia] = valor
    
    # Realizar inferencia
    print(f"\nRealizando inferencia: P({var_consulta} | {evidencia})")
    resultado, parciales = motor.inferencia({var_consulta: None}, evidencia, return_parciales=True)
    
    motor.mostrar_traza()
    imprimir_resultados((resultado, parciales))

def menu_principal():
    """
    Muestra el menú principal del programa.
    """
    print("\n" + "="*80)
    print("MOTOR DE INFERENCIA POR ENUMERACIÓN - MENÚ PRINCIPAL")
    print("="*80)
    print("\n1. Ejecutar ejemplos predefinidos")
    print("2. Realizar consulta personalizada")
    print("3. Mostrar estructura de la red")
    print("4. Mostrar tablas de probabilidad")
    print("5. Salir")
    print()
    
    opcion = input("Seleccione una opción: ").strip()
    return opcion

def main():
    """
    Función principal del programa.
    """
    import sys
    if len(sys.argv) != 3:
        print("\nUso obligatorio: py main.py <estructura.txt> <probabilidades.txt>")
        print("Ejemplo: py main.py estructura_red.txt probabilidades.txt\n")
        print("Debe especificar ambos archivos. El programa terminará.\n")
        sys.exit(1)
    archivo_estructura = sys.argv[1]
    archivo_probabilidades = sys.argv[2]

    red = RedBayesiana()
    try:
        red.cargar_estructura(archivo_estructura)
        red.cargar_probabilidades(archivo_probabilidades)
    except FileNotFoundError as e:
        print(f"\nError: No se pudo cargar la red bayesiana.")
        print(f"Asegúrese de que los archivos '{archivo_estructura}' y '{archivo_probabilidades}' existen.")
        print(f"Detalle: {e}")
        sys.exit(1)

    motor = MotorInferencia(red)

    while True:
        opcion = menu_principal()
        if opcion == '1':
            ejecutar_ejemplo_basico(archivo_estructura, archivo_probabilidades)
        elif opcion == '2':
            ejecutar_consulta_personalizada(red, motor)
        elif opcion == '3':
            red.mostrar_estructura()
        elif opcion == '4':
            red.mostrar_tablas_probabilidad()
        elif opcion == '5':
            print("\n¡Gracias por usar el Motor de Inferencia!")
            print("="*80 + "\n")
            break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 5.")


if __name__ == "__main__":
    import sys
    try:
        main()
    except KeyboardInterrupt:
        print("\nAcabando programa...")
        sys.exit(0)
