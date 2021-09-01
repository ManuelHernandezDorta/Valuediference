diccionario = {}

with open(".\database.txt","r") as archivo:
    for linea in archivo:

        partes = linea.split(",")
        nombre = partes[0]
        valor = partes[2]

        if nombre not in diccionario.keys():
            diccionario[nombre] = int(valor)

        else:
            if diccionario[nombre] > int(valor):
                diccionario[nombre] = int(valor)

            else:
                pass

    
with open(".\database.txt","r") as archivo:
    for linea in archivo:

        partes = linea.split(",")
        nombre = partes[0]
        indicador = partes[1]
        valor = partes[2]

        nuevoValor = int(valor) - int(diccionario[nombre])

        with open(".\database2.txt","a") as nuevoArchivo:
            nuevoArchivo.writelines(nombre + "," + indicador + "," + str(nuevoValor) + "\n")
