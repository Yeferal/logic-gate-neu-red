def paint_table(datos):
    # Obtener la longitud máxima de cada columna
    anchos_columnas = [max(map(len, columna)) for columna in zip(*datos)]

    # Imprimir encabezado
    separador = '+'.join('-' * (ancho + 2) for ancho in anchos_columnas)
    encabezado = '|'.join(f'{titulo:^{ancho + 2}}' for titulo, ancho in zip(datos[0], anchos_columnas))
    print(f'+{separador}+')
    print(f'|{encabezado}|')
    print(f'+{separador}+')

    # Imprimir filas de datos
    for fila in datos[1:]:
        fila_formateada = '|'.join(f'{dato:^{ancho + 2}}' for dato, ancho in zip(fila, anchos_columnas))
        print(f'|{fila_formateada}|')

    print(f'+{separador}+')
