#menu y contenedores básicos
def menu():
    print("Seleccione una opción que tipo de conversión necesita:")
    print("              1.DMS a DD")
    print("              2.DD a DMS")
    opcion=int(input())
    if opcion==1:
        #coversexa()
        pedir_datos_sexa()
    elif opcion==2:
        pedir_datos_deci()

#peticion de datos en caso de ser sexagesimal
def pedir_datos_sexa():
    latsexa=input('Ingrese latitud en sexagesimal (grados minutos segundos): ')
    lonsexa=input('Ingrese latitud en sexagesimal (grados minutos segundos): ')
    sexa=covern(latsexa,lonsexa)
    coversad(sexa)
    return 0


#peticion de datos en caso de ser decimal
def pedir_datos_deci():
    datdeclat=input('Ingrese latitud en decimales: ')
    datdeclon=input('Ingrese longitud en decimales: ')
    deci=covern(datdeclat,datdeclon)
    coverdas(deci)
    return 0

#conversion a cadena de numeros ingresados
def covern(dat1, dat2):
    xlat=str(dat1)
    xlon=str(dat2)
    return xlat,xlon


# conversion de decimales a grados sexagesimales
def coverdas(data):
    # Asignacion de variables a argumentos
    lat = data[0]  # Division para la conversion de la tupla
    lon = data[1]  # División para la conversion de la tupla
    conlat = lat.split(sep='.')  # Se utiliza un separador en python
    conlon = lon.split(sep='.')  # Se utiliza un separador en python en estos casos el punto

    # print(conlat[0],conlon)
    # Tratamiento con latitud en decimales a sexagecimales
    conlat[1] = float("0." + conlat[1]) * 60
    # print(conlat[1])
    res = str(conlat[1]).split(sep='.')
    seg = float("0." + res[1]) * 60
    print("######################################################")
    print(" ")
    print("Los grados latitud : " + conlat[0] + "°" + " " + res[0] + "' " + str(seg) + "''")

    # Tratamiento de datos en longitud
    conlon[1] = float("0." + conlon[1]) * 60
    # print(conlat[1])
    res1 = str(conlon[1]).split(sep='.')
    seg1 = float("0." + res1[1]) * 60
    print("Los grados longitud: " + conlon[0] + "°" + " " + res1[0] + "' " + str(seg1) + "''")


def coversad(data):
    lat = data[0]  # Division para la conversion de la tupla
    lon = data[1]  # División para la conversion de la tupla
    conlat = lat.split()  # Se utiliza un separador en python
    conlon = lon.split()  # Se utiliza un separador en python

    # Tratamiento de latitud e impresion
    conlat[2] = float(conlat[2]) / 60
    conlat[1] = ((float(conlat[1])) + conlat[2]) / 60
    if float(conlat[0]) < 0:
        res = float(conlat[0]) - conlat[1]
    else:
        res = float(conlat[0]) + conlat[1]
    print("######################################################")
    print("Latitud en decimales: ", res)

    # Tratamiento de longitud e Impresion
    # Tratamiento de latitud e impresion
    conlon[2] = float(conlon[2]) / 60
    conlon[1] = ((float(conlon[1])) + conlon[2]) / 60
    if float(conlon[0]) < 0:
        res1 = float(conlon[0]) - conlon[1]
    else:
        res1 = float(conlon[0]) + conlon[1]
    print(" ")
    print("Longitud en decimales: ", res)

    return 0


menu()