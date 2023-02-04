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