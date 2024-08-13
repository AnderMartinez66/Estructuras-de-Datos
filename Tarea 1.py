import csv

csv_file = "C:/Users/pc/Downloads/Presencia Redes Sociales.csv"

with open(csv_file, mode='r', newline='', encoding='iso-8859-1') as file:
    reader = csv.reader(file)
    
    header = next(reader)
    
    filas = list(reader)

    fila_deseada = 7


    fila = filas[fila_deseada]

    index_valor1 = header.index('ENERO')
    index_valor2 = header.index('JUNIO')
    valor1 = float(fila[index_valor1])
    valor2 = float(fila[index_valor2])

    diferencia = valor2 - valor1

    print(f"Diferencia de seguidores en Twitter entre Enero y Junio: {diferencia}")


        # Diferencia de visualizaciones en Youtube
    print('Diferencia de visualizaciones en Youtube:')
    columna1_mes = input("Ingrese el primer mes: ")
    columna2_mes = input("Ingrese el segundo mes: ")
    fila_deseada = int(input("Ingrese el número de la fila: ")) - 1 

    if fila_deseada >= len(filas):
        print(f"No se encontró la fila {fila_deseada + 1}. El archivo tiene {len(filas)} filas de datos.")
    elif columna1_mes not in header or columna2_mes not in header:
        print("Nombres de columna no válidos. Verifique los nombres ingresados.")
    else:
        index_valor1 = header.index(columna1_mes)
        index_valor2 = header.index(columna2_mes)

        fila = filas[fila_deseada]


        try:
            valor1 = float(fila[index_valor1])
            valor2 = float(fila[index_valor2])
                
            diferencia = valor1 - valor2
            diferencia_absoluta = abs(diferencia)
                
            print(f"Diferencia de visualizaciones en Youtube: {diferencia_absoluta}")
        except ValueError:
            print("Error: No se pudo convertir uno de los valores a número.")
        
        # Promedio de crecimiento de Facebook
    columnas = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO']
    numero_fila = 1 
    fila = filas[numero_fila]
    indices = [header.index(col) for col in columnas]
    suma_fila = sum(float(fila[index]) for index in indices)
    print(f"El promedio de crecimiento de Facebook entre Enero y Junio es: {suma_fila/6}")

        #Promedio de crecimiento de Twitter
    numero_fila = 8 
    fila = filas[numero_fila]
    indices = [header.index(col) for col in columnas]
    suma_fila = sum(float(fila[index]) for index in indices)
    print(f"El promedio de crecimiento de Twitter entre Enero y Junio es: {suma_fila/6}")
        
        #Promedio de likes de Facebok
    columnas = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
    numero_fila = 4
    fila = filas[numero_fila]
    indices = [header.index(col) for col in columnas]
    suma_fila = sum(float(fila[index]) for index in indices)
    print(f"El promedio de likes de Facebook entre Enero y Diciembre es: {suma_fila/12}")

        #Promedio de likes de Twitter
    columnas = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
    numero_fila = 12
    fila = filas[numero_fila]
    indices = [header.index(col) for col in columnas]
    suma_fila = sum(float(fila[index]) for index in indices)
    print(f"El promedio de likes de Twitter entre Enero y Diciembre es: {suma_fila/12}")

        #Promedio de likes de Youtube
    columnas = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
    numero_fila = 17
    fila = filas[numero_fila]
    indices = [header.index(col) for col in columnas]
    suma_fila = sum(float(fila[index]) for index in indices)
    print(f"El promedio de likes de Youtube entre Enero y Diciembre es: {suma_fila/12}")