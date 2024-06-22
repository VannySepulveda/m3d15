import time
def validate(opciones, eleccion):
    while eleccion not in opciones:
        if eleccion== '0':
            print('Adios =)')
            time.sleep(5)
            exit()
        elif eleccion == '1':
            print ('JUGUEMOS')
        else:
            eleccion=input('Debe ingresar si desea Jugar [1] o Salir [0] : ')
    if eleccion== '0':
        print('Adios =)')
        time.sleep(3)
        exit()
    elif eleccion == '1':
        print ('JUGUEMOS')     
    return eleccion
       

def VN (opcion):
    if str.isdigit(opcion) == True and type(opcion) is str: opc=int(opcion) 
    else:
        print("Opción no valida") 
        opc = 0
    return opc
    # eleccion=input('Debe ingresar si desea Jugar [1] o Salir [0] : ')
    # if eleccion== '0':
    #     print('Adios =)')
    #     time.sleep(3)
    #     exit()
    # elif eleccion == '1':
    #     print ('JUGUEMOS')     
    # return eleccion