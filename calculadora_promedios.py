def ingresar_calificaciones():
    """
    Solicita al usuario nombres y calificaciones de materias,
    validando que estén entre 0 y 10.
    """
    materias = []
    calificaciones = []

    while True:
        nombre_materia = input("Ingrese el nombre de la materia: ").strip()

        while True:
            try:
                calificacion = float(
                    input(f"Ingrese la calificación para {nombre_materia} (0 a 10): ")
                )
                if 0 <= calificacion <= 10:
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")

        materias.append(nombre_materia)
        calificaciones.append(calificacion)

        continuar = input("¿Desea ingresar otra materia? (s/n): ").strip().lower()
        if continuar != 's':
            break

    return materias, calificaciones


def determinar_estado(calificaciones, umbral=5.0):
    """
    Recibe una lista de calificaciones y un umbral.
    Devuelve dos listas con los índices de aprobadas y reprobadas.
    """
    aprobadas_indices = []
    reprobadas_indices = []
    
    for i, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas_indices.append(i)
        else:
            reprobadas_indices.append(i)
            
    return aprobadas_indices, reprobadas_indices


def encontrar_extremos(calificaciones):
    """
    Identifica y devuelve el índice de la calificación más alta y el de la más baja.
    """
    if not calificaciones:
        return None, None
    
    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))
    
    return indice_max, indice_min


def main():
    print("=== CALCULADORA DE PROMEDIOS Y RENDIMIENTO ACADÉMICO ===")
    
    # 1. Obtener datos del usuario
    materias, calificaciones = ingresar_calificaciones()
    
    # 2. Manejo de caso especial: lista vacía
    if not calificaciones:
        print("\nNo se ingresó ninguna materia. Finalizando el programa.")
        print("¡Hasta luego!")
        return

    # 3. Calcular el promedio general
    promedio_general = sum(calificaciones) / len(calificaciones)
    
    # 4. Determinar materias aprobadas y reprobadas (umbral por defecto: 5.0)
    aprobadas_idx, reprobadas_idx = determinar_estado(calificaciones, umbral=5.0)
    
    # 5. Encontrar extremos
    idx_max, idx_min = encontrar_extremos(calificaciones)
    
    # 6. Mostrar resumen final
    print("\n" + "="*40)
    print("           RESUMEN FINAL ACADÉMICO")
    print("="*40)
    
    print("\n📚 Listado completo de materias y calificaciones:")
    for m, c in zip(materias, calificaciones):
        print(f" - {m}: {c}")
        
    print(f"\n📊 Promedio general: {promedio_general:.2f}")
    
    print(f"\n✅ Materias Aprobadas ({len(aprobadas_idx)}):")
    if aprobadas_idx:
        for i in aprobadas_idx:
            print(f" - {materias[i]} ({calificaciones[i]})")
    else:
        print(" - Ninguna")
        
    print(f"\n❌ Materias Reprobadas ({len(reprobadas_idx)}):")
    if reprobadas_idx:
        for i in reprobadas_idx:
            print(f" - {materias[i]} ({calificaciones[i]})")
    else:
        print(" - Ninguna")
        
    print(f"\n🏆 Mejor calificación:")
    print(f" - {materias[idx_max]} con un valor de {calificaciones[idx_max]}")
    
    print(f"\n⚠️ Peor calificación:")
    print(f" - {materias[idx_min]} con un valor de {calificaciones[idx_min]}")
    
    # 7. Mensaje de despedida
    print("\n" + "="*40)
    print("¡Gracias por utilizar el sistema! ¡Hasta pronto!")
    print("="*40)


if __name__ == "__main__":
    main()