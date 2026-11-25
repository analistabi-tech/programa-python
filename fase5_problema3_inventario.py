# ====================================================================
# Nombre del estudiante: Cristhian Andrés Camelo Barrera
# Cédula: 1016064880
# Tutor: Diomar Antonio Pineda Cervantes
# Programa: Ingeniería en Inteligencia Artificial y Ciencia de Datos
# Código Fuente: autoría propia
# Curso: Fundamentos de Programación - (213022)
# Fase 5 - Evaluación Final POA
# Problema 3: Control de inventario y cálculo de reabastecimiento
# ====================================================================

# 1. DATOS INICIALES (Matriz con 5 artículos de inventario)
# Formato de cada fila: [Código, Nombre del artículo, Stock actual, Stock mínimo]
inventario = [
    ["A001", "Teclado Mecánico", 4, 10],
    ["A002", "Mouse Inalámbrico", 15, 10],
    ["A003", "Monitor 24 Pulgadas", 2, 8],
    ["A004", "Diadema USB", 12, 12],
    ["A005", "Cable HDMI", 5, 20]
]


# 2. DEFINICIÓN DE FUNCIÓN (Módulo de lógica de negocio)
def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """
    Determina la cantidad exacta de unidades a solicitar.
    Si el stock actual es menor que el mínimo, pide la diferencia.
    En caso contrario, retorna 0.
    """
    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
        return cantidad_pedir
    else:
        return 0


# 3. PROCESAMIENTO Y SALIDA DE RESULTADOS
def mostrar_informe_reabastecimiento(matriz_inventario):
    """
    Recorre la matriz de inventario, calcula el pedido para cada artículo
    y muestra el listado final en pantalla.
    """
    print("=" * 68)
    print("        SISTEMA DE CONTROL DE INVENTARIO Y REABASTECIMIENTO")
    print("=" * 68)
    print(f"{'Código':<10}{'Nombre del Artículo':<24}{'Stock Actual':<15}{'Stock Mín.':<12}{'A Pedir'}")
    print("-" * 68)

    # Recorremos cada fila (artículo) de la matriz con un ciclo for
    for fila in matriz_inventario:
        codigo = fila[0]
        nombre = fila[1]
        stock_actual = fila[2]
        stock_minimo = fila[3]

        # Llamamos a nuestra función para saber cuánto pedir
        unidades_a_pedir = calcular_cantidad_pedir(stock_actual, stock_minimo)

        # Mostramos los datos de cada artículo
        print(f"{codigo:<10}{nombre:<24}{stock_actual:<15}{stock_minimo:<12}{unidades_a_pedir} uds.")

    print("=" * 68)


# Ejecución del programa principal
if __name__ == "__main__":
    mostrar_informe_reabastecimiento(inventario)
