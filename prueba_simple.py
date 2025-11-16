"""
Script de prueba simple para verificar que el Motor de Inferencia funciona correctamente.
Este script realiza una prueba básica sin interacción del usuario.
"""

from red_bayesiana import RedBayesiana
from motor_inferencia import MotorInferencia

def prueba_simple():
    """
    Realiza una prueba simple del motor de inferencia.
    """
    print("="*80)
    print("PRUEBA SIMPLE DEL MOTOR DE INFERENCIA")
    print("="*80)
    print()
    
    # Crear y cargar la red
    print("1. Cargando Red Bayesiana...")
    red = RedBayesiana()
    red.cargar_estructura('estructura_red.txt')
    red.cargar_probabilidades('probabilidades.txt')
    print("   ✓ Red cargada exitosamente")
    print()
    
    # Mostrar estructura básica
    print("2. Estructura de la red:")
    print(f"   Nodos: {list(red.nodos.keys())}")
    print(f"   Nodos raíz: {[n.nombre for n in red.raices]}")
    print()
    
    # Crear motor de inferencia
    print("3. Creando motor de inferencia...")
    motor = MotorInferencia(red)
    print("   ✓ Motor creado exitosamente")
    print()
    
    # Realizar una inferencia de prueba
    print("4. Realizando inferencia de prueba:")
    print("   Consulta: P(Appointment | Rain=light, Maintenance=yes)")
    print()
    
    evidencia = {'Rain': 'light', 'Maintenance': 'yes'}
    resultado = motor.inferencia({'Appointment': None}, evidencia)
    
    print("   RESULTADOS:")
    print(f"   P(Appointment=attend | Rain=light, Maintenance=yes) = {resultado['attend']:.4f}")
    print(f"   P(Appointment=miss | Rain=light, Maintenance=yes) = {resultado['miss']:.4f}")
    print()
    
    # Verificar que las probabilidades suman 1
    suma = sum(resultado.values())
    print(f"5. Verificación de normalización:")
    print(f"   Suma de probabilidades: {suma:.6f}")
    if abs(suma - 1.0) < 0.0001:
        print("   ✓ Las probabilidades están correctamente normalizadas")
    else:
        print("   ✗ ERROR: Las probabilidades no suman 1")
    print()
    
    print("="*80)
    print("PRUEBA COMPLETADA EXITOSAMENTE")
    print("="*80)
    print()
    print("Para ejecutar el programa completo con ejemplos interactivos, usa:")
    print("  python main.py")
    print()

if __name__ == "__main__":
    try:
        prueba_simple()
    except Exception as e:
        print(f"\nERROR durante la prueba: {e}")
        import traceback
        traceback.print_exc()
