def busqueda_lineal (data, a_buscar):
    n= len(data)
    i = 0
    while i < len(data):
        if data[i] == element:
            return i
        i += 1
    return -1

def busqueda_lineal_centinela (data, a_buscar):
    data.append(element)

    i = 0
    while data[i] != element:
        i += 1

    data.pop()

    if i < len(data):
        return i
    else:
        return -1

def busqueda_binaria(data, element):

    i = 0
    fin = len(data) - 1

    while i <= fin:
        medio = (i + fin) // 2

        if data[medio] == element:
            return medio

        elif data[medio] > element:
            fin = medio - 1

        else:
            i = medio + 1

    return -1


list = [10, 23, 45, 70, 11, 15]
element = 23
resultado = busqueda_binaria(list, element)

busqueda_binaria(list, element)


if resultado != -1:
    print(f"Elemento encontrado en el índice: {resultado}")
else:
    print("Elemento no encontrado")

