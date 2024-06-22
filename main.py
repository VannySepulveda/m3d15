
# No modificar
from verify import verificar
import preguntas as p
import datos as d
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import *

import time
import os
import sys

# valores iniciales - 
n_pregunta = 0
continuar = 'y'
correcto = True
p_level = 10
op_sys = 'cls' if sys.platform == 'win32' else 'clear'


# ----------------------------------------

os.system(op_sys) # limpiar pantalla


print (f"Bienvenido a la Trivia\n\ ")
opcion = input('''Ingrese una opción
Jugar [1]
Salir [0]         
... > ''')
# validacion de entrada
opcion = validate(opcion,['0','1'])

opcion=0
opcion=VN(input(d.menu)) 
while True:
    if opcion==4: 
        exit()
    elif opcion ==0 or opcion >4: 
         os.system('cls')
         opcion=VN(input(d.menu)) 
    else: 
        tot_preg=opcion*3
        res= VN(input(f"Ingrese n° de pregunta que quiere responder(hasta {tot_preg}) ó 0 para Salir: \n"))
        while True:
            if  res>0 and res<=tot_preg:
                p_level=res
                preg=choose_level(tot_preg,res)
                res=6
                print(f"Pregunta Nivel: {preg}")
                break
            elif res == 0:
                    print("chao")
                    exit()
            else:
                while correcto and n_pregunta < 3*p_level:
                
                    if n_pregunta == 0:
                        p_level = input('¿Cuántas preguntas por nivel? (Máximo 3): ')
                        # 3. Validar el número de preguntas por nivel
                        p_level = 
                        
                    if continuar == 'y':
                        #contador de preguntas
                        n_pregunta += 1
                        # 4. Escoger el nivel de la pregunta
                        nivel = print(f'Pregunta {n_pregunta}:')
                        # 5. Escoger el enunciado y las alternativas de una pregunta según el nivel escogido
                        enunciado, alternativas = 
                        #6. Imprimir el enunciado y sus alternativas en pantalla
                        
                        
                        respuesta = input('Escoja la alternativa correcta:\n> ').lower()
                        # 7. Validar la respuesta entregada
                        respuesta = 
                        # 8. Verificar si la respuesta es correcta o no
                        correcto = 
                        
                        if correcto and n_pregunta < 3*p_level:
                            print('Muy bien sigue así!')
                            continuar = input('Desea continuar? [y/n]: ').lower()
                            #9. Validar si es que se responde y o n
                            continuar = 
                            os.system(op_sys)
                        elif correcto and n_pregunta == 3*p_level:
                            print(f'Felicitaciones, Has respondido {3*p_level} preguntas correctas. \n Has ganado la Trivia \n Gracias por Jugar, hasta luego!!!')
                            time.sleep(3)
                            os.system(op_sys)
                        else: 
                            print(f'Lo siento, conseguiste {n_pregunta - 1} respuestas correctas,\n Sigue participando!!')
                            time.sleep(3)
                            exit()
                    else: 
                        print('Nos vemos la proxima vez, sigue practicando')
                        time.sleep(3)
                        exit()
                            
                            
