import time
import os
from datos import *
from validador import VN
import random
import preguntas as p

def choose_level(tot_preg,res):
    preg={}
    random.shufle(preguntas_basicas)
    for a in range(tot_preg+1):
            if  tot_preg == 3:
                if   a == 1: preg[a]=[nb],['preguntas_basicas'],[''],['']
                elif a == 2: preg[a]=[ni],['preguntas_intermedias'],[''],['']
                elif a == 3: preg[a]=[na],['preguntas_avanzadas'],[''],['']
            elif tot_preg == 6:
                if   a == 1 or a == 2: preg[a]=[nb],['preguntas_basicas'],[''],['']
                elif a == 3 or a == 4: preg[a]=[ni],['preguntas_intermedias'],[''],['']
                elif a == 5 or a == 6: preg[a]=[na],['preguntas_avanzadas'],[''],['']
            else:
                if   a == 1 or a == 2 or a == 3: preg[a]=[nb],['preguntas_basicas'],[''],['']
                elif a == 4 or a == 5 or a == 6: preg[a]=[ni],['preguntas_intermedias'],[''],['']
                elif a == 7 or a == 8 or a == 9: preg[a]=[na],['preguntas_avanzadas'],[''],['']
    lista=preg[res]
    return(lista[0])


                res = VN(input(f"Ingrese n°de la pregunta que quiere responder (hasta {tot_preg}) ó 0 para Salir: \n")) 
       
#     # print(choose_level(2, 2)) # básicas
#     # print(choose_level(3, 2)) # intermedias
#     # print(choose_level(7, 2)) # avanzadas
#     # print(choose_level(4, 3)) # intermedias