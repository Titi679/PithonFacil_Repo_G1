# Crear una matriz 4x4 vacía
matriz = [[' ' for _ in range(4)] for _ in range(4)]

# Lista para almacenar los nombres y sus propiedades
elementos = []

# Función para añadir un nombre a la matriz
def añadir_nombre():
    while True:
        nombre = input("Introduce el alimento (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        categoria = input("Introduce la categoría : ")

        # Buscar la primera posición vacía en la matriz
        posX, posY = buscar_posicion(elementos, acategoria)

        if posX is None or posY is None:
            print("La matriz está llena. No se puede añadir más nombres.")
            break

        # Añadir el nombre a la lista y a la matriz
        elementos.append({'nombre': nombre, 'posX': posX, 'posY': posY, 'categoria': categoria})
        matriz[posX][posY] = nombre

        # Mostrar mensaje de éxito
        print(f"Nombre '{nombre}' añadido en la posición ({posX}, {posY}) con categoría '{categoria}'.")
        actualizar_matriz()

# Función para buscar la primera posición vacía en la matriz
def buscar_posicion(elementos, categoria):
    for i in range(4):
        for j in range(4):
          for item in elementos:
            if item['categoria'] == categoria and matriz[i][j+1] != ' ':
              #Si encuentra una celda de la misma categoria y la celda de la derecha esta llena, mueve todo lo que tiene a la derecha una posicion
              if j + 1 < 4 and matriz[i][j+1] != ' ':
                    return i, j + 1

          if matriz[i][j] == ' ':
            return i, j
    return None, None  # Si no hay espacio vacío

# Función para actualizar la visualización de la matriz
def actualizar_matriz():
    print("\nMatriz actualizada:")
    for i in range(4):
        row = "|"
        for j in range(4):
            row += f" {matriz[i][j]} |"
        print(row)
    print("\n")

# Llamar a la función para añadir nombres
añadir_nombre()
