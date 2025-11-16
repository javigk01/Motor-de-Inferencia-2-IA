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
    Imprime los resultados de una inferencia en formato tabla.
    
    Args:
        resultados (dict): Diccionario con los resultados de la inferencia
    """
    print("\n" + "─"*50)
    print("RESULTADOS DE LA INFERENCIA")
    print("─"*50)
    print(f"{'Valor':<20} {'Probabilidad':<15} {'Porcentaje':<15}")
    print("─"*50)
    
    for valor, prob in sorted(resultados.items(), key=lambda x: x[1], reverse=True):
        print(f"{valor:<20} {prob:<15.6f} {prob*100:<14.2f}%")
    
    print("─"*50 + "\n")

def ejecutar_ejemplo_basico():
    """
    Ejecuta el ejemplo básico de la Red Bayesiana con inferencias.
    """
    imprimir_titulo("MOTOR DE INFERENCIA POR ENUMERACIÓN - RED BAYESIANA")
    
    # Crear red bayesiana
    red = RedBayesiana()
    
    # Cargar estructura y probabilidades
    red.cargar_estructura('estructura_red.txt')
    red.cargar_probabilidades('probabilidades.txt')
    
    # Mostrar estructura
    red.mostrar_estructura()
    
    # Mostrar tablas de probabilidad
    red.mostrar_tablas_probabilidad()
    
    # Crear motor de inferencia
    motor = MotorInferencia(red)
    
    # Pausa para que el usuario pueda revisar
    print("\n" + "="*80)
    input("Presiona ENTER para continuar con los ejemplos de inferencia...")
    
    # =========================================================================
    # EJEMPLO 1: ¿Cuál es la probabilidad de llegar a la cita dado que 
    #            hay lluvia ligera y hay mantenimiento?
    # =========================================================================
    imprimir_titulo("EJEMPLO 1: P(Appointment | Rain=light, Maintenance=yes)")
    
    print("Pregunta: ¿Cuál es la probabilidad de llegar a la cita (attend/miss)")
    print("          dado que hay lluvia ligera y hay mantenimiento programado?")
    print()
    
    evidencia1 = {'Rain': 'light', 'Maintenance': 'yes'}
    resultado1 = motor.inferencia({'Appointment': None}, evidencia1)
    
    motor.mostrar_traza()
    imprimir_resultados(resultado1)
    
    # Interpretación
    print("INTERPRETACIÓN:")
    print(f"  Con lluvia ligera y mantenimiento, la probabilidad de asistir a la cita es")
    print(f"  {resultado1['attend']*100:.2f}% y de perderla es {resultado1['miss']*100:.2f}%")
    print()
    
    input("Presiona ENTER para continuar con el siguiente ejemplo...")
    
    # =========================================================================
    # EJEMPLO 2: ¿Cuál es la probabilidad de que el tren llegue a tiempo
    #            sin ninguna evidencia?
    # =========================================================================
    imprimir_titulo("EJEMPLO 2: P(Train) - Sin evidencia")
    
    print("Pregunta: ¿Cuál es la probabilidad de que el tren llegue a tiempo")
    print("          sin conocer ninguna información adicional?")
    print()
    
    evidencia2 = {}
    resultado2 = motor.inferencia({'Train': None}, evidencia2)
    
    motor.mostrar_traza()
    imprimir_resultados(resultado2)
    
    print("INTERPRETACIÓN:")
    print(f"  Sin información adicional, la probabilidad de que el tren llegue a tiempo es")
    print(f"  {resultado2['on_time']*100:.2f}% y de que se retrase es {resultado2['delayed']*100:.2f}%")
    print()
    
    input("Presiona ENTER para continuar con el siguiente ejemplo...")
    
    # =========================================================================
    # EJEMPLO 3: ¿Cuál es la probabilidad del estado del tren dado que
    #            no hay lluvia?
    # =========================================================================
    imprimir_titulo("EJEMPLO 3: P(Train | Rain=none)")
    
    print("Pregunta: ¿Cuál es la probabilidad del estado del tren")
    print("          sabiendo que no hay lluvia?")
    print()
    
    evidencia3 = {'Rain': 'none'}
    resultado3 = motor.inferencia({'Train': None}, evidencia3)
    
    motor.mostrar_traza()
    imprimir_resultados(resultado3)
    
    print("INTERPRETACIÓN:")
    print(f"  Sin lluvia, la probabilidad de que el tren llegue a tiempo es")
    print(f"  {resultado3['on_time']*100:.2f}% y de que se retrase es {resultado3['delayed']*100:.2f}%")
    print()
    
    input("Presiona ENTER para continuar con el siguiente ejemplo...")
    
    # =========================================================================
    # EJEMPLO 4: ¿Cuál es la probabilidad de asistir a la cita sabiendo
    #            que hay lluvia fuerte?
    # =========================================================================
    imprimir_titulo("EJEMPLO 4: P(Appointment | Rain=heavy)")
    
    print("Pregunta: ¿Cuál es la probabilidad de asistir a la cita")
    print("          sabiendo que hay lluvia fuerte?")
    print()
    
    evidencia4 = {'Rain': 'heavy'}
    resultado4 = motor.inferencia({'Appointment': None}, evidencia4)
    
    motor.mostrar_traza()
    imprimir_resultados(resultado4)
    
    print("INTERPRETACIÓN:")
    print(f"  Con lluvia fuerte, la probabilidad de asistir a la cita es")
    print(f"  {resultado4['attend']*100:.2f}% y de perderla es {resultado4['miss']*100:.2f}%")
    print()
    
    input("Presiona ENTER para continuar con el siguiente ejemplo...")
    
    # =========================================================================
    # EJEMPLO 5: ¿Cuál es la probabilidad de asistir a la cita sabiendo
    #            que el tren llegó a tiempo?
    # =========================================================================
    imprimir_titulo("EJEMPLO 5: P(Appointment | Train=on_time)")
    
    print("Pregunta: ¿Cuál es la probabilidad de asistir a la cita")
    print("          sabiendo que el tren llegó a tiempo?")
    print()
    
    evidencia5 = {'Train': 'on_time'}
    resultado5 = motor.inferencia({'Appointment': None}, evidencia5)
    
    motor.mostrar_traza()
    imprimir_resultados(resultado5)
    
    print("INTERPRETACIÓN:")
    print(f"  Si el tren llega a tiempo, la probabilidad de asistir a la cita es")
    print(f"  {resultado5['attend']*100:.2f}% (directamente de la tabla de probabilidad)")
    print()
    
    # =========================================================================
    # RESUMEN
    # =========================================================================
    imprimir_titulo("RESUMEN DE RESULTADOS")
    
    print("Comparación de escenarios:\n")
    
    print(f"1. Con lluvia ligera y mantenimiento:")
    print(f"   P(attend) = {resultado1['attend']*100:.2f}%\n")
    
    print(f"2. Sin evidencia (caso general):")
    print(f"   P(Train=on_time) = {resultado2['on_time']*100:.2f}%\n")
    
    print(f"3. Sin lluvia:")
    print(f"   P(Train=on_time) = {resultado3['on_time']*100:.2f}%\n")
    
    print(f"4. Con lluvia fuerte:")
    print(f"   P(attend) = {resultado4['attend']*100:.2f}%\n")
    
    print(f"5. Si el tren llega a tiempo:")
    print(f"   P(attend) = {resultado5['attend']*100:.2f}%\n")
    
    print("Conclusiones:")
    print("  - El mantenimiento y la lluvia afectan negativamente la puntualidad del tren")
    print("  - La puntualidad del tren es el factor más determinante para asistir a la cita")
    print("  - Incluso con lluvia fuerte, hay una probabilidad razonable de asistir")
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
    resultado = motor.inferencia({var_consulta: None}, evidencia)
    
    motor.mostrar_traza()
    imprimir_resultados(resultado)

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
    # Cargar la red bayesiana
    red = RedBayesiana()
    
    try:
        red.cargar_estructura('estructura_red.txt')
        red.cargar_probabilidades('probabilidades.txt')
    except FileNotFoundError as e:
        print(f"\nError: No se pudo cargar la red bayesiana.")
        print(f"Asegúrese de que los archivos 'estructura_red.txt' y 'probabilidades.txt' existen.")
        print(f"Detalle: {e}")
        return
    
    motor = MotorInferencia(red)
    
    while True:
        opcion = menu_principal()
        
        if opcion == '1':
            ejecutar_ejemplo_basico()
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
    main()
