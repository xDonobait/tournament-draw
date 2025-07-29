import random

# --- CONFIGURACIÓN DE RANGOS ---
RANGOS = {
    1: (4.0, 5.0),
    2: (3.0, 3.99),
    3: (2.0, 2.99),
    4: (1.0, 1.99)
}

def ingresar_duos():
    """Pide los 16 dúos con su valoración."""
    duos = []
    print("=== INGRESO DE 16 DÚOS ===")
    for i in range(1, 17):
        nombre = input(f"Nombre del dúo {i}: ").strip()
        while True:
            try:
                valor = float(input(f"Valoración (1 a 5) de {nombre}: "))
                if 1 <= valor <= 5:
                    valor = round(valor, 2)  # se redondea solo si tiene decimales
                    break
                else:
                    print("❌ Debe estar entre 1 y 5.")
            except ValueError:
                print("❌ Entrada inválida, ingrese un número válido.")
        duos.append((nombre, valor))
    return duos

def clasificar_bombos(duos):
    """Clasifica los dúos en 4 bombos según el rango de valoración."""
    bombos = {1: [], 2: [], 3: [], 4: []}
    for nombre, valor in duos:
        for b, (min_v, max_v) in RANGOS.items():
            if min_v <= valor <= max_v:
                bombos[b].append(nombre)
                break
    
    # Verificación: deben ser 4 equipos en cada bombo
    for b, equipos in bombos.items():
        if len(equipos) != 4:
            print(f"\n❌ ERROR: El Bombo {b} tiene {len(equipos)} equipos (deben ser 4).")
            return None
    return bombos

def sortear_grupos(bombos):
    """Asigna aleatoriamente 1 equipo de cada bombo a cada grupo."""
    grupos = {"A": [], "B": [], "C": [], "D": []}
    for b, equipos in bombos.items():
        random.shuffle(equipos)
        for i, equipo in enumerate(equipos):
            grupos[list(grupos.keys())[i % 4]].append(equipo)
    return grupos

def mostrar_resultados(bombos, grupos):
    """Muestra bombos y grupos en consola."""
    print("\n=== BOMBO POR CLASIFICACIÓN ===")
    for b, eq in bombos.items():
        print(f"Bombo {b}: {', '.join(eq)}")
    
    print("\n=== GRUPOS RESULTANTES ===")
    for g, eq in grupos.items():
        print(f"Grupo {g}: {', '.join(eq)}")

def guardar_resultado(grupos):
    """Guarda el resultado del sorteo en un archivo."""
    with open("sorteo.txt", "w", encoding="utf-8") as f:
        f.write("=== RESULTADO DEL SORTEO ===\n\n")
        for g, eq in grupos.items():
            f.write(f"Grupo {g}: {', '.join(eq)}\n")
    print("\n✅ Resultado guardado en 'sorteo.txt'")

def main():
    """Flujo principal del programa."""
    while True:
        duos = ingresar_duos()
        bombos = clasificar_bombos(duos)
        if bombos:
            break
        print("\n🔄 Los datos no cumplen los requisitos, vuelve a ingresarlos.\n")

    while True:
        print("\n🎲 REALIZANDO SORTEO...")
        grupos = sortear_grupos(bombos)
        mostrar_resultados(bombos, grupos)

        if input("\n¿Guardar resultado en archivo? (s/n): ").lower() == "s":
            guardar_resultado(grupos)

        if input("¿Realizar otro sorteo con los mismos dúos? (s/n): ").lower() != "s":
            print("\n✅ Sorteo finalizado. ¡Éxitos con el torneo!")
            break

if __name__ == "__main__":
    main()
