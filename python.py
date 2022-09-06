#ultimo respaldo de seguridad

"""
Será que se puedo crear el juego del agedrez en python con la consola..  yo no lo sé solo quiero intentarlo.... ajajajjajaja
Se inició este proyecto el dia 29/04/2022
fue finikitado el dia          8/06/2022 a las 10:40 pm   pense muchas veces que no lo iba a lograr 
"""
"""
horas concientes de inversion 5 horas  hasta las 8:28  del dia 9/05/2022    5 horas
dia 10/05/2022  el dia de ayer la mitad que hice no sirvio de mucho         1 hora    
11 / 05 / 2022                                                              1 hora  
12 / 05 / 2022                                                              2 horas perdidas     
13 / 05 / 2022                                                              3 horas  se logro identificar el bug XD y se corrigio una parte               
14/ 05 / 2022                                                               3 horas corrigiendo bugs   
15/05/ 2022                                                                 2 horas matando bugs  se aniquiláron los bug maximos no se si habra quedado despues de la aniquilacion maxima 
5:23 PM                                                                     un bug que me quitó el sueño lo pude haver aniquilado en un minuto y estuve horas aniquilandolo JAJAJAJAJAJA
16/05/2020       12:17 AM                                                   1 hora detalles y se puede hacer dos movimientos en la primera jugada 
17/ 05/ 1:12     1.13 AM                                                    1 :20 minutos  hora haciendo la funcionalidad del peon en la posicion 8 hace el cambio por otra ficha
                                                                             terminado  no XD me di cunta de un erorr gravisimo
18/05/2022       7:22 PM  - 9:16 PM                                         3 hora fin del peon y sus funcionalidades  + movimiento torre XD                                                                    
19 /05/2022                                                                 5 horas movimiento de la reina  Y torre corregido 
20 /05/2022      
21/05/ 2022      9:00 am - 11:00 am                                         2 horas movimiento arfil listo
21/05/2022       7:30 - 10:55                                               3 horas y media           caballo a medias  AJJAJAJAJJAJA   estuvo bastante entretenido
22/05/2022       7:28 _ 9:14                                                1 hora 45minutos  errores del caballo terminado y el rey listo
23/05/2022       10:00  - 3:44                                              3 horas  arrgle un bug y leyendo nada mas XD                                              
24/05/2022       7:17am   - 7:10 pm                                         12 horas creando el algoritmo que hace el haquemate incompleto aun hace falta verificar posisciones y establecer el hakemate
25/05/2022       10:00am  - 12:00 am                                        2 horas perfecionando el algoritmo
26/05/2022
27/05/2022       11:00 AM - 12:42 PM     and 11:00 pm - 1:34 am             4 horas cambios       la funcionalidad del haquenate yy el haque terminadas falta es ver los errores
28/05/2022       3:20 PM  _ 4:00pm                                          40 minutos
29/ 05/2022      12:00 am  - 12_00 pm                                       6 horas 
30/05/2022       11:00 am _12:00 am  2:pm - 4pm                             3 horas se esta creado todos los ataques de las fichas
31/05/2022       9:am      3:pm                                             5 horas 
1/06/2022        9:am       12.pm                                           3 horas
2/06 /2022                                                                  1 hora          
3/06/2022                                                                   1 hora
4/06/2022        5:00 Pm     12:Am                                          7 horas
5/06/2022        7:pm        1:00 Am                                        6 horas 
6/06/2022        estudiando teoria de python
7/06/2022                                                                   2 hrs                                                     terminando el enrosque
8/06/2022                                                                   2  media horas se terminas el enrrosque y y empiezo a crear la captura al paso  se Termino el juegoe
Esto Está finikitado me diverti mucho creando esto hubo dias que odiando todo simplemente me ponia a programar en ocaciones 
quise borrar el programa. hubo muchos estrasñochos y momentos llenos de alegria. borre varias veces mas de 200 lineas 
por qu simplemente no servian y debia corregirlas.
aprendi a nunca rendirme no sabia que hacer pero fue un proceso gradual donde hiba subiendo escalones paso a paso cada pedazo del 
rompecabesas cada ves se iba terminamando mas y mas hasta que se pudo lograr.
90 horas de desarrollo aproximadamente 
1 mes aprox
"""
#rama EXPERIMENTAL 2 
from os import system
import math
from time import process_time


#la llave del hake 

llave_del_jaque_maximous = [False]
#todas las funciones importantes


#estas son las fichas del ajedrez representadas en codigo 
B = ["\u2659","\u2656","\u2655","\u2658","\u2654","\u2657"]
N = ["\u265F","\u265C","\u265B","\u265E","\u265A","\u265D"]


Fichas_Blancas = ["\u2659","\u2656","\u2655","\u2658","\u2654","\u2657"]
Fichas_Negras= ["\u265F","\u265C","\u265B","\u265E","\u265A","\u265D"]

#fichas blancas

#peones
P1B = B[0]
P2B = B[0]
P3B = B[0]
P4B = B[0]
P5B = B[0]
P6B = B[0]
P7B = B[0]
P8B = B[0]

#Caballo
C1B = B[3]
C2B = B[3]

#Arfil 
A1B = B[5]
A2B = B[5]

#torres
T1B = B[1]
T2B = B[1]

#rey y reina
RB = B[4]
DB = B[2]

#fichas negras

#peones
P1N = N[0]
P2N = N[0]
P3N = N[0]
P4N = N[0]
P5N = N[0]
P6N = N[0]
P7N = N[0]
P8N = N[0]

#Caballo
C1N = N[3]
C2N = N[3]

#Arfil 
A1N = N[5]
A2N = N[5]

#torres
T1N = N[1]
T2N = N[1]

#rey y reina
RN = N[4]
DN = N[2]


#El tablero 

M=[
    ["+","-","-","-","-","-","-","-","-","-","-","-","-","+"],
    ["|","*","*","A","B","C","D","E","F","G","H","*","*","|"],
    ["|","*","+","-","-","-","-","-","-","-","-","+","*","|"],
    ["|","8","|",T1N,C1N,A1N,DN,RN,A2N,C2N,T2N,"|","8","|"],
    ["|","7","|",P1N,P2N,P3N,P4N,P5N,P6N,P1N,P8N,"|","7","|"],
    ["|","6","|",".",".",".",".",".",".",".",".","|","6","|"],
    ["|","5","|",".",".",".",".",".",".",".",".","|","5","|"],
    ["|","4","|",".",".",".",".",".",".",".",".","|","4","|"],
    ["|","3","|",".",".",".",".",".",".",".",".","|","3","|"],
    ["|","2","|",P1B,P2B,P3B,P4B,P5B,P6B,P7B,P8B,"|","2","|"],
    ["|","1","|",T1B,C1B,A1B,DB,RB,A2B,C2B,T2B,"|","1","|"],
    ["|","*","+","-","-","-","-","-","-","-","-","+","*","|"],
    ["|","*","*","A","B","C","D","E","F","G","H","*","*","|"],
    ["+","-","-","-","-","-","-","-","-","-","-","-","-","+"],
 ]

M.reverse()
for a in range(14):
    M[a].reverse()
    for b in range(14):
        a = 0



#la ubicacion de fila y ocoluman para colocar la ficha
LFicha = [""]

#no se me ocurrio otra manera esta llave sirve para activar el la accion de mover ficha a la posisicon asignada
LLave_cambio_posicion = [""]

#Almacena la ubicacion de la ficha
Ubicacion_ficha = [0,0,0,0]

#se guardarán los movimientos permitidos
MovimientoPeon = []

#congunti de posisiciones
letras = ["a","b","c","d","e","f","g","h"]
#movimientos no permitidos XD 

Movimientos_no_Permitidos = [0,0]

#llave super maestra
llave_supermaestra = [True]


#Movimientos permitidos de la reina 
Movimientos_permitidos_Reina = []
#movimientos torre
Movimientos_Torre = []

#movimientos permitidos del arfil 
Movimiento_Arfil  = []

#Movimiento Cabalo
Movimiento_caballo = []

#Movimiento rey permitido 
Movimiento_Rey = []

#Movimiento peon Permitido
Movimientos_Peon = [[1],[1]]


#Moviemintos en hake 
LLave_enrosque = []

#hacen el movimeinto del enrosque almacenando un dato true
primer_movimiento_1 = []
primer_movimiento_2 = []
primer_movimiento_3 = []

primer_movimiento_11 = []
primer_movimiento_22 = []
primer_movimiento_33 = []


#este e para capturar al paso 
Ubicacion_torre11111 = []
Ubicacion_torre22222 = []

Ubicacion_torre33333 = []
Ubicacion_torre44444 = []


LLave_enrosque1 = []


#la llave dela captura al paso
lavus_maximous_capture = [1]

#esta funcion pasa por parametros las posiciones para intercambiarlas por las letras y numeros dando la posicion exacta del mumero
#funcion de la operacion
def Accion(jugador,n1,n2,n3,n4,n5,n6,n7,n8,n11,n12,n13,n14,n15,n16,n17,n18,Colorde_ficha,Colorde_ficha2,Color_Variable1,Color_Variable2):
    system("cls")
        
    print("Las fichas..")
    print(". ".join(B))
    print(". ".join(N))
    print()

    #se invierte para que se gire cuando le toquen a las fichas negras
    M.reverse()
    for i in range(14):
            
        M[i].reverse()
        for j in range(14):
            print(M[i][j],end = ' ') 
        print()

    #la funcion cambia la pocision de la ficha.... 
    def Funcion_ingresaFicha(ingreso,ingreso2,LLave):
        while True:
            print(jugador)
            #Algoritmo Magistral 2
#________________________________________________________________________________________________________________________________________________________
            Nueva_linea_Peligro = []

            #ataque 
            Ubicacion_Todas_fichas_Arriba= []
            Ubicacion_Todas_fichas_Abajo= []
            #ataques de las fichas de arriba 
            Todos_Los_posiblesAtaques_Arriba = []
            #ataque de las fichas de ababjp
            Todos_Los_posiblesAtaques_Abajo = []
            

            #buscará las fichas  dentro del arreglo 
            for i in range(len(M)):
                for j in range(len(M[i])):
                    if M[i][j] in Colorde_ficha:
                        Ubicacion_Todas_fichas_Arriba.append([i,j])
                    if M[i][j] in Colorde_ficha2:
                        Ubicacion_Todas_fichas_Abajo.append([i,j])

            #este es un clico que va recorreindo todas las posiciones de las fichas de arriba 
            #fichas de arriba 
            def Algorimit_maximous(Color_variable,Color_Opuesto,Ubicacion,Ataques,Operador_positivo,Operador_negativo,The_Key):
                for a in range(len(Ubicacion)):

                    # si son peones......
                    if M[ Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[0]:
                        # print(M[ Ubicacion_Todas_fichas_Arriba[a][0]][Ubicacion_Todas_fichas_Arriba[a][1]])
                        #derecha 
                        if  M[ Ubicacion[a][0]+Operador_positivo][Ubicacion[a][1]+Operador_negativo] in Color_Opuesto or M[ Ubicacion[a][0]+Operador_positivo][Ubicacion[a][1]+Operador_negativo] == ".":
                            Ataques.append([ Ubicacion[a][0]+Operador_positivo,Ubicacion[a][1]+Operador_negativo])
                        #isquierda
                        if  M[ Ubicacion[a][0]+Operador_positivo][Ubicacion[a][1]+Operador_positivo] in Color_Opuesto or M[ Ubicacion[a][0]+Operador_positivo][Ubicacion[a][1]+Operador_positivo] == ".":
                            Ataques.append([ Ubicacion[a][0]+Operador_positivo,Ubicacion[a][1]+Operador_positivo])
                    
                    # ##########################################################################################################################################
                   
                    #esta llave es para que no calcule el ataque del rey que se encuentra abajo para poder verificas el jake ya que esta activando las posibles fichas que pueden defender el kaqie 
                    #si es un rey 
                    if The_Key == True:
                        if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[4]:
                            #arriba
                            def Algoritmo_deciciones_rey(Diagonal,Vertical):
                                if M[Ubicacion[a][0]+Diagonal][Ubicacion[a][1]+Vertical] in Color_Opuesto or M[Ubicacion[a][0]+Diagonal][Ubicacion[a][1]+Vertical] == ".":
                                    Ataques.append([Ubicacion[a][0]+Diagonal,Ubicacion[a][1]+Vertical])
                            #arriba                                              #abajo                                #Derecha                                       isquierda                                     #arriba Derecha                                                 #arriba isquierda                                              #abajo dercha                                                 #abajo isquierda 
                            Algoritmo_deciciones_rey(Operador_positivo,0),Algoritmo_deciciones_rey(Operador_negativo,0),Algoritmo_deciciones_rey(0,Operador_positivo),Algoritmo_deciciones_rey(0,Operador_negativo),Algoritmo_deciciones_rey(Operador_positivo,Operador_positivo),Algoritmo_deciciones_rey(Operador_positivo,Operador_negativo), Algoritmo_deciciones_rey(Operador_negativo,Operador_positivo),Algoritmo_deciciones_rey(Operador_negativo,Operador_negativo)
                            
                    # ##########################################################################################################################################
                    ## ******************************************************************************************************************************************
                    #si es una reina
                    #esta funcion va recorriendo las distintas posisiones   primerio va a buscar cada ficha en la ubiccion comparando cada posicion 

                    if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[2]:
                        def Algoritmo_Deciciones_Reina(Diagonal,Vertical):
                            Fila_mas = Diagonal
                            Columna_mas = Vertical
                            while True:
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_Opuesto or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] == ".":
                                    Ataques.append([Ubicacion[a][0]+Fila_mas,Ubicacion[a][1]+Columna_mas])
                                
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_variable or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] != ".":
                                    El_REY_BLANCO = Color_Variable1[4]
                                    El_REY_NEGRO = Color_Variable2[4]
                                    # print(f"{El_REY_BLANCO} {El_REY_NEGRO}")

                                    if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] == El_REY_BLANCO:
                                        # print("EL logaritmo")
                                        Ataques.append([Ubicacion[a][0]+Fila_mas,Ubicacion[a][1]+Columna_mas])
                                    else:
                                        # print(M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas])
                                        break
                                
                                #este es para que cuando cambie de posicion vaya retrocediendo o disminullendo
                                if not Fila_mas == 0:
                                    if Diagonal == +1:
                                        Fila_mas = Fila_mas + 1
                                    if Diagonal == - 1:
                                        Fila_mas = Fila_mas - 1

                                if not Columna_mas == 0:
                                    if Vertical == -1:
                                        Columna_mas = Columna_mas - 1
                                    if Vertical == +1:
                                        Columna_mas = Columna_mas + 1

                        #arriba                                         #abajo                                          #Derecha                                       isquierda                                     #arriba Derecha                                                 #arriba isquierda                                              #abajo dercha                                                 #abajo isquierda 
                        Algoritmo_Deciciones_Reina(Operador_positivo,0),Algoritmo_Deciciones_Reina(Operador_negativo,0),Algoritmo_Deciciones_Reina(0,Operador_positivo),Algoritmo_Deciciones_Reina(0,Operador_negativo),Algoritmo_Deciciones_Reina(Operador_positivo,Operador_positivo),Algoritmo_Deciciones_Reina(Operador_positivo,Operador_negativo), Algoritmo_Deciciones_Reina(Operador_negativo,Operador_positivo),Algoritmo_Deciciones_Reina(Operador_negativo,Operador_negativo)

                    # ******************************************************************************************************************************************
                    ## ******************************************************************************************************************************************
                    #si es un arfil 
                    if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[5]:
                        def Algoritmo_Deciciones_Arfil(Diagonal,Vertical):
                            Fila_mas = Diagonal
                            Columna_mas = Vertical
                            while True:
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_Opuesto or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] == ".":
                                    Ataques.append([Ubicacion[a][0]+Fila_mas,Ubicacion[a][1]+Columna_mas])
                                
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_variable or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] != ".":
                                    El_REY_BLANCO = Color_Variable1[4]
                                    El_REY_NEGRO = Color_Variable2[4]
                                    
                                    if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] == El_REY_BLANCO:
                                       
                                        Ataques.append([Ubicacion[a][0]+Fila_mas,Ubicacion[a][1]+Columna_mas])
                                    else:
                                        break
                                
                                if not Fila_mas == 0:
                                    if Diagonal == +1:
                                        Fila_mas = Fila_mas + 1
                                    if Diagonal == - 1:
                                        Fila_mas = Fila_mas - 1

                                if not Columna_mas == 0:
                                    if Vertical == -1:
                                        Columna_mas = Columna_mas - 1
                                    if Vertical == +1:
                                        Columna_mas = Columna_mas + 1

                        #arriba Derecha                                                  #arriba isquierda                                              #abajo dercha                                                 #abajo isquierda 
                        Algoritmo_Deciciones_Arfil(Operador_positivo,Operador_positivo),Algoritmo_Deciciones_Arfil(Operador_positivo,Operador_negativo), Algoritmo_Deciciones_Arfil(Operador_negativo,Operador_positivo),Algoritmo_Deciciones_Arfil(Operador_negativo,Operador_negativo)
                    
                    # ******************************************************************************************************************************************
                    # Si es una torre
                    if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[1]:
                        def Algoritmo_Deciciones_Torre(Diagonal,Vertical):
                            Fila_mas = Diagonal
                            Columna_mas = Vertical
                            while True:
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_Opuesto or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] == ".":
                                    Ataques.append([Ubicacion[a][0]+Fila_mas,Ubicacion[a][1]+Columna_mas])
                                
                                if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] in Color_variable or M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] != ".":
                                    El_REY_BLANCO = Color_Variable1[4]
                                    El_REY_NEGRO = Color_Variable2[4]
                                    
                                    if M[Ubicacion[a][0]+Fila_mas][Ubicacion[a][1]+Columna_mas] == El_REY_BLANCO:
                                       
                                        Ataques.append([Ubicacion[a][0]+Fila_mas,Ubicacion[a][1]+Columna_mas])
                                    else:
                                        break
                                
                                
                                if not Fila_mas == 0:
                                    if Diagonal == +1:
                                        Fila_mas = Fila_mas + 1
                                    if Diagonal == - 1:
                                        Fila_mas = Fila_mas - 1

                                if not Columna_mas == 0:
                                    if Vertical == -1:
                                        Columna_mas = Columna_mas - 1
                                    if Vertical == +1:
                                        Columna_mas = Columna_mas + 1

                        #arriba                                         #abajo                                          #Derecha                                        #isquierda                                    
                        Algoritmo_Deciciones_Torre(Operador_positivo,0),Algoritmo_Deciciones_Torre(Operador_negativo,0),Algoritmo_Deciciones_Torre(0,Operador_positivo),Algoritmo_Deciciones_Torre(0,Operador_negativo)

                    # ####################################################################################################################################################
                    #sie es un caballo 
                    if M[Ubicacion[a][0]][Ubicacion[a][1]] == Color_variable[3]:
                        def Algoritmo_Deciciones_Caballo(Diagonal,Vertical):
                            if M[Ubicacion[a][0]+Diagonal][Ubicacion[a][1]+Vertical] in Color_Opuesto or M[Ubicacion[a][0]+Diagonal][Ubicacion[a][1]+Vertical] == ".":
                                Ataques.append([Ubicacion[a][0]+Diagonal,Ubicacion[a][1]+Vertical])
                            
                        # L arriba Derecha           #Aui se pasan numeros si son -2 o +2 y 1 o -1                                                                                                                                #arriba isquierda                                              #abajo dercha                                                 #abajo isquierda 
                        Algoritmo_Deciciones_Caballo(Operador_negativo + Operador_negativo,Operador_positivo)
                        # L arriba isquierda
                        Algoritmo_Deciciones_Caballo(Operador_negativo + Operador_negativo,Operador_negativo)
                        # L Derecha arriba 
                        Algoritmo_Deciciones_Caballo(Operador_negativo,Operador_positivo + Operador_positivo)
                        # L Derecha Abajo 
                        Algoritmo_Deciciones_Caballo(Operador_positivo,Operador_positivo + Operador_positivo)
                        # L Isquierda Arriba
                        Algoritmo_Deciciones_Caballo(Operador_negativo,Operador_negativo + Operador_negativo)
                        # L Isquierda Abajo 
                        Algoritmo_Deciciones_Caballo(Operador_positivo,Operador_negativo + Operador_negativo)
                        # L Abajo Derecha                        
                        Algoritmo_Deciciones_Caballo(Operador_positivo + Operador_positivo,Operador_positivo)
                        # L Abajo isquierda
                        Algoritmo_Deciciones_Caballo(Operador_positivo + Operador_positivo,Operador_negativo)
                    
            #Las fichas de arriba 
            Algorimit_maximous(Color_Variable2,Color_Variable1,Ubicacion_Todas_fichas_Arriba,Todos_Los_posiblesAtaques_Arriba,+1,-1,True)
            #las fuchas de abajo
            Algorimit_maximous(Color_Variable1,Color_Variable2,Ubicacion_Todas_fichas_Abajo,Todos_Los_posiblesAtaques_Abajo,-1,+1,False)
        

           #Esta funcion va a verificar si el rey esta en haque y si lo está va a corroborar si esta en haquemate 
            
            Linea_del_ataque_hacia_el_rey = []
            Las_fichas_que_estan_atacando_al_rey = []

            for a in range(len(Ubicacion_Todas_fichas_Abajo)):
                if M[Ubicacion_Todas_fichas_Abajo[a][0]][Ubicacion_Todas_fichas_Abajo[a][1]] == Color_Variable1[4]:
                    POSICION = [Ubicacion_Todas_fichas_Abajo[a][0],Ubicacion_Todas_fichas_Abajo[a][1]] 
                    if POSICION in Todos_Los_posiblesAtaques_Arriba:
                        print("El REY ESTA EN HAKE POR LA FICHA")

                        llave_del_jaque_maximous.clear()
                        llave_del_jaque_maximous.append(True)

                        def Alagoritmo_logaritmatico_del_cambio_haker(Atacante1,Atacante2,Atacante3,Atacante4,Diagonal1,Vertical1):
                            logaritmo_del_cambio = []
                            Fichas_ataque_Ralla = [Color_Variable2[Atacante1],Color_Variable2[Atacante2],Color_Variable2[Atacante3],Color_Variable2[Atacante4]]
                        
                            Iterador1 = Diagonal1
                            Iterador2 = Vertical1
                            while True:

                                
                                #busca que tipo de haque es si es de una reina torre  arfil fichas de largo alxance 
                                if M[POSICION[0]+Iterador1][POSICION[1]+Iterador2] == ".":
                                    logaritmo_del_cambio.append([POSICION[0]+Iterador1,POSICION[1]+Iterador2])

                                elif M[POSICION[0]+Iterador1][POSICION[1]+Iterador2] in Fichas_ataque_Ralla:
                                    logaritmo_del_cambio.append([POSICION[0]+Iterador1,POSICION[1]+Iterador2])
                                    Las_fichas_que_estan_atacando_al_rey.append(M[POSICION[0]+Iterador1][POSICION[1]+Iterador2])

                                    for logor in range(len(logaritmo_del_cambio)):
                                        Linea_del_ataque_hacia_el_rey.append(logaritmo_del_cambio[logor])
                                    break
                                elif M[POSICION[0]+Iterador1][POSICION[1]+Iterador2] in Color_Variable2:
                                    break
                                else:
                                    break
                                
                                if not Diagonal1 == 0:
                                    if Diagonal1 == +1:
                                        Iterador1 = Iterador1 + 1
                                    if Diagonal1 == - 1:
                                        Iterador1 = Iterador1 - 1

                                if not Vertical1 == 0:
                                    if Vertical1 == -1:
                                        Iterador2 = Iterador2 - 1
                                    if Vertical1 == +1:
                                        Iterador2 = Iterador2+ 1

                            
                           
                            
                        # Arriba 
                        Alagoritmo_logaritmatico_del_cambio_haker(1,2,1,1,-1,0)
                        # Arriba derecha
                        Alagoritmo_logaritmatico_del_cambio_haker(2,2,2,5,-1,-1)
                        # Arriba Isuquierda
                        Alagoritmo_logaritmatico_del_cambio_haker(2,2,2,5,-1,+1)
                        # Derecha 
                        Alagoritmo_logaritmatico_del_cambio_haker(2,1,1,1,0,+1)
                        # Abajo 
                        Alagoritmo_logaritmatico_del_cambio_haker(2,1,1,1,0,-1)
                        #abajo derecha 
                        Alagoritmo_logaritmatico_del_cambio_haker(2,2,2,5,+1,+1)
                        #Abajo isquierda 
                        Alagoritmo_logaritmatico_del_cambio_haker(2,2,2,5,+1,-1)

                        
                        # is the jaque is of the kind is a peon
                        #the jaque is from a peon or a kind
                        
                        #the wachahca 
                        the_wachachaca = [Color_Variable2[0],Color_Variable2[4]]
                        # the wachachaca horse
                        the_wachachaca_horse = [Color_Variable2[3]]
                        #derecha 
                        if  M[POSICION[0]-1][POSICION[1]+1] in the_wachachaca :
                            Linea_del_ataque_hacia_el_rey.append([POSICION[0]-1,POSICION[1]+1])
                            Las_fichas_que_estan_atacando_al_rey.append(M[POSICION[0]-1][POSICION[1]+1])
                        #isquierda
                        if  M[POSICION[0]-1][POSICION[1]-1] in the_wachachaca :
                            Linea_del_ataque_hacia_el_rey.append([POSICION[0]-1,POSICION[1]-1])
                            Las_fichas_que_estan_atacando_al_rey.append(M[POSICION[0]-1][POSICION[1]-1])

                        # the jaque of a horse   
                        def Algoritmo_Deciciones_Caballo(Diagonal12,Vertical12):
                            if M[POSICION[0]+Diagonal12][POSICION[1]+Vertical12] in the_wachachaca_horse:

                                Linea_del_ataque_hacia_el_rey.append([POSICION[0]+Diagonal12,POSICION[1]+Vertical12])
                                Las_fichas_que_estan_atacando_al_rey.append(M[POSICION[0]+Diagonal12][POSICION[1]+Vertical12])
                            
                        # L arriba Derecha                                                                                                                         #arriba isquierda                                              #abajo dercha                                                 #abajo isquierda 
                        Algoritmo_Deciciones_Caballo(-2,+1)
                        # L arriba isquierda
                        Algoritmo_Deciciones_Caballo(-2,-1)
                        # L Derecha arriba 
                        Algoritmo_Deciciones_Caballo(-1,+2)
                        # L Derecha Abajo 
                        Algoritmo_Deciciones_Caballo(+1,+2)
                        # L Isquierda Arriba
                        Algoritmo_Deciciones_Caballo(-1,-2)
                        # L Isquierda Abajo 
                        Algoritmo_Deciciones_Caballo(+1,-2)
                        # L Abajo Derecha                        
                        Algoritmo_Deciciones_Caballo(+2,+1)
                        # L Abajo isquierda
                        Algoritmo_Deciciones_Caballo(+2,-1)
                    
                        


                        print(Las_fichas_que_estan_atacando_al_rey)
                        print("Esta es la linea que está atacando al rey ")
                        
                        print(Linea_del_ataque_hacia_el_rey)

                        #variables de de ubicacion del rey y a la redonda
                        POSICION_actual = [Ubicacion_Todas_fichas_Abajo[a][0],Ubicacion_Todas_fichas_Abajo[a][1]] 
                        POSICION_Arriba = [Ubicacion_Todas_fichas_Abajo[a][0]-1,Ubicacion_Todas_fichas_Abajo[a][1]] 
                        POSICION_Arriba_Derecha = [Ubicacion_Todas_fichas_Abajo[a][0]-1,Ubicacion_Todas_fichas_Abajo[a][1]+1] 
                        POSICION_Arriba_Isquierda = [Ubicacion_Todas_fichas_Abajo[a][0]-1,Ubicacion_Todas_fichas_Abajo[a][1]-1] 
                        POSICION_Derecha = [Ubicacion_Todas_fichas_Abajo[a][0],Ubicacion_Todas_fichas_Abajo[a][1]+1] 
                        POSICION_Isquierda = [Ubicacion_Todas_fichas_Abajo[a][0],Ubicacion_Todas_fichas_Abajo[a][1]-1] 
                        POSICION_Abajo_Derecha = [Ubicacion_Todas_fichas_Abajo[a][0]+1,Ubicacion_Todas_fichas_Abajo[a][1]+1] 
                        POSICION_Abajo_Isquierda = [Ubicacion_Todas_fichas_Abajo[a][0]+1,Ubicacion_Todas_fichas_Abajo[a][1]-1] 
                        POSICION_Abajo = [Ubicacion_Todas_fichas_Abajo[a][0]+1,Ubicacion_Todas_fichas_Abajo[a][1]] 

                        #compara si las posiciones estan libre o si estan siendo atacadas
                        La_llave_haquemate = []
                        La_llave_haquemate12 = []

                        if POSICION_actual in Todos_Los_posiblesAtaques_Arriba:
                            La_llave_haquemate.append(True)
                        if POSICION_Arriba in Todos_Los_posiblesAtaques_Arriba or not M[POSICION_Arriba[0]][POSICION_Arriba[0]] == ".":
                            La_llave_haquemate.append(True)

                        if POSICION_Arriba_Derecha in Todos_Los_posiblesAtaques_Arriba or not M[POSICION_Arriba_Derecha[0]][POSICION_Arriba_Derecha[1]] == ".":
                            La_llave_haquemate.append(True)
                        if POSICION_Arriba_Isquierda in Todos_Los_posiblesAtaques_Arriba  or not M[POSICION_Arriba_Isquierda[0]][POSICION_Arriba_Isquierda[1]] == ".":
                            La_llave_haquemate.append(True)
                        if POSICION_Derecha in Todos_Los_posiblesAtaques_Arriba  or not M[POSICION_Derecha[0]][POSICION_Derecha[1]] == ".":
                            La_llave_haquemate.append(True)
                        if POSICION_Isquierda in Todos_Los_posiblesAtaques_Arriba or not M[POSICION_Isquierda[0]][POSICION_Isquierda[1]] == ".":
                            La_llave_haquemate.append(True)
                        if POSICION_Abajo_Derecha in Todos_Los_posiblesAtaques_Arriba  or not M[POSICION_Abajo_Derecha[0]][POSICION_Abajo_Derecha[1]] == ".":
                            La_llave_haquemate.append(True)
                        if POSICION_Abajo_Isquierda in Todos_Los_posiblesAtaques_Arriba  or not M[POSICION_Abajo_Isquierda[0]][POSICION_Abajo_Isquierda[1]] == ".":
                            La_llave_haquemate.append(True)
                        if POSICION_Abajo in Todos_Los_posiblesAtaques_Arriba   or not M[POSICION_Abajo[0]][POSICION_Abajo[1]] == ".":
                            La_llave_haquemate.append(True)


                        #Verifica si todad las posiciones estan siendo atacadas  y si puede haver una posible ficha para defender
                        for whachachaka in Linea_del_ataque_hacia_el_rey:
                            if whachachaka in Todos_Los_posiblesAtaques_Abajo:
                                La_llave_haquemate12.append(True)
                            else:
                                La_llave_haquemate12.append(False)

                        if len(La_llave_haquemate) == 9 and  not True in La_llave_haquemate12:
                            print(f"Ha ganado el equipo de las fichas {Color_Variable2}")
                            print("Jaque Mate ")
                            exit()

            #Pide la entrada modificada

            while True:
                input_ficha = input(f"{ingreso2} {ingreso}")
                if len(input_ficha) == 2:
                    if input_ficha[1] in letras:
                        if not input_ficha[0].isalpha():
                            if int(input_ficha[0]) > 0 and int(input_ficha[0]) <9:
                                if input_ficha[1].isalpha():
                                    break
                                else:
                                    print("Se equivocó ingresando jugada")
                            else:
                                print("Se equivocó ingresando jugada")
                        else:    
                            print("Se equivocó ingresando jugada")
                    else:
                        print("Se equivocó ingresando jugada")
                else:    
                    print("Se equivocó ingresando jugada")

            Numero_fila2 = int(input_ficha[0])
            Letra_columna2 = input_ficha[1]

            #la convierte en mayuscula si es minuscula 
            Letra_columna2 = Letra_columna2.upper()
            
            #Funcion que cambia las opciones
            
            if Numero_fila2 == 8:
                fila2 = n1
            elif Numero_fila2 == 7:
                fila2 = n2
            elif Numero_fila2 == 6:
                fila2 = n3
            elif Numero_fila2 == 5:
                fila2 = n4
            elif Numero_fila2 == 4:
                fila2 = n5
            elif Numero_fila2 == 3:
                fila2 = n6
            elif Numero_fila2 == 2:
                fila2 = n7
            elif Numero_fila2 == 1:
                fila2 = n8
            else:
                print("Error")
                
            #columnas
            if Letra_columna2 == "A":
                columna2 = n11
            elif Letra_columna2 =="B":
                columna2 = n12
            elif Letra_columna2 =="C":
                columna2 = n13
            elif Letra_columna2 == "D":
                columna2 = n14
            elif Letra_columna2 == "E":
                columna2 = n15
            elif Letra_columna2 == "F":
                columna2 = n16
            elif Letra_columna2 == "G":
                columna2 = n17
            elif Letra_columna2 == "H":
                columna2 = n18
            else: 
                print("Error")
        
            #GUARDARÁ LA POSICION DE LA FICHA PASANDO COMO LLAVE TRUE O FALSE
            #esta llave activa si se puede hacer el movimiento o no 

            LLave1 = LLave
                       
            if LLave1 == True:
                #guarda donde esta
                Ubicacion_ficha.clear()
                Ubicacion_ficha.append(fila2)
                Ubicacion_ficha.append(columna2)

                #Va a calcular todos los ataques de todas las fichas XD 
            elif LLave1 == False:
                #la limpia

                Ubicacion_ficha.append(0)
                Ubicacion_ficha.append(0)
                Ubicacion_ficha.pop(2)
                Ubicacion_ficha.pop(2)

                #guarda donde se moverá
                Ubicacion_ficha.append(fila2)
                Ubicacion_ficha.append(columna2)

                #elimina los ceros de la posicion agregada
                if 0 in Ubicacion_ficha:
                    Ubicacion_ficha.pop(2)
                    Ubicacion_ficha.pop(2)

            else:
                print("Nada por aqui nada por allá")
            
            if LLave1 == True:
            
                #Muestra que ficha es......
                Ficha2 = M[fila2][columna2]
                #frente
                Ficha3 = M[fila2-1][columna2]
                #isquierdda
                Ficha4 = M[fila2-1][columna2-1]
                #derecha 
                Ficha5 = M[fila2-1][columna2+1]

                #guarda la posicion de la ficha tomada
                LFicha.append(Ficha2)
                LFicha.pop(0)
                
                #verifica la ficha elegida y está bacia
                if Ficha2 ==".":
                    print("La ficha no existe")
                
                #verifica si ha ingresado una ficha contraria
                elif Ficha2 == Colorde_ficha[0] or Ficha2 == Colorde_ficha[1] or Ficha2 == Colorde_ficha[2] or Ficha2 == Colorde_ficha[3] or Ficha2 == Colorde_ficha[4] or Ficha2 == Colorde_ficha[5]:
                    print("Error de turno")
                #coloca el punto de la posisicon donde se movia
                else:
                    print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])
                                       
                    #SI es un peon   permite identificar que ficha tiene en frente y a sus lads para ver si el peon está bloqueado 
                    if Ficha2 == B[0] or Ficha2 ==N[0]:
                        Movimientos_Peon.clear()
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])

                        #Posicion actual
                        print(Ubicacion_ficha)

                        Color_que_cambia  = 0
                         #verifica si es blanca o negra
                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Blancas[0]:
                            #es una ficha blanca
                            Color_que_cambia = Fichas_Negras
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Negras[0]:
                            #es una ficha negra 
                            Color_que_cambia = Fichas_Blancas 

                        #llave incomprensible XD
                        llavus_maximous = [False]

                         #si no se ha movido y esta en la pocicion inicial 2 de la casilla entonces permite hacer 2 movimientos 
                        if Ubicacion_ficha[0] == 9:
                            print("El peon se encuentra en la primera casilla ")
                            o = 1
                            i = 0
                            while i < 2:
                                if M[Ubicacion_ficha[0]-o][Ubicacion_ficha[1]] == ".":
                                    Movimientos_Peon.append([Ubicacion_ficha[0]-o,Ubicacion_ficha[1]])
                                    llavus_maximous.append(True)
                                else:
                                    break
                                o = o + 1
                                i = i + 1
                        #verifica si tiene una captura 
                        if lavus_maximous_capture[0] == True:
                            if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] == Color_Variable2[0]:
                                llavus_maximous.append(True)
                                Movimientos_Peon.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]+1])
                                M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] = "."
                            
                            if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] == Color_Variable2[0]:
                                llavus_maximous.append(True)
                                Movimientos_Peon.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]-1])
                                M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] = "."


                        # Verifica que tiene en el frente
                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] == ".":
                            Movimientos_Peon.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]])
                            llavus_maximous.append(True)

                        #verifica que tiene  a la isquierda
                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] in Color_que_cambia:
                            Movimientos_Peon.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]-1])
                            llavus_maximous.append(True)

                        #verifica que tiene  a la Derecha
                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] in Color_que_cambia:
                            Movimientos_Peon.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]+1])
                            llavus_maximous.append(True)

                        if True in llavus_maximous:
                            llavus_maximous.clear()
                            
                            #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimientos_Peon)):
                                    if Movimientos_Peon[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimientos_Peon[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimientos_Peon.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimientos_Peon.append(k)
                                    break    
                                    

                            if llave_del_jaque_maximous[0] == False:
                                break
                        else:
                            print("La ficha esta bloqueada ")
                    
                    #si es una torre
                    if Ficha2 == B[1] or Ficha2 == N[1]:
                        Movimientos_Torre.clear()
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])
                        
                        #Color de la ficha elegida 
                        COLOR_ELEGIDO2 = 0

                         #verifica si es blanca o negra
                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Blancas[1]:
                            #es una ficha blanca
                            COLOR_ELEGIDO2 = Fichas_Blancas 
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Negras[1]:
                            #es una ficha negra 
                            COLOR_ELEGIDO2 = Fichas_Negras
                        print(COLOR_ELEGIDO2)
                        print("!")

                        #Posicion actual
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])

                        #algoritmo 
                        def Algoritmo_Torre():
                        #el algoritmo que busca hacia arriba
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] == ".":
                                    Movimientos_Torre.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]])

                                elif not M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] in COLOR_ELEGIDO2:
                                    Movimientos_Torre.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]])
                                    break
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] in COLOR_ELEGIDO2 or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] == "_":
                                    break

                                i = i + 1
                             #algoritmo Derecha
                            i = 1
                            while True:
                                print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+i])
                                if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+i] == ".":
                                    Movimientos_Torre.append([Ubicacion_ficha[0],Ubicacion_ficha[1]+i])
                                elif not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO2:
                                    Movimientos_Torre.append([Ubicacion_ficha[0],Ubicacion_ficha[1]+i])
                                    break
                                elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+i] in COLOR_ELEGIDO2 or M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] == "|":
                                    break
                                i = i + 1 
                            #algoritmo isquierda
                            i = 1
                            while True:
                                if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] == ".":
                                    Movimientos_Torre.append([Ubicacion_ficha[0],Ubicacion_ficha[1]-i])
                                elif not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO2:
                                    Movimientos_Torre.append([Ubicacion_ficha[0],Ubicacion_ficha[1]-i])
                                    break
                                elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO2 or M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] == "_":
                                    break
                                i = i + 1 

                             #el algoritmo que busca hacia abajo
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] == ".":
                                    Movimientos_Torre.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]])
                                elif not M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] in COLOR_ELEGIDO2:
                                    Movimientos_Torre.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]])
                                    break
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] in COLOR_ELEGIDO2 or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] == "_":
                                    break

                                i = i + 1


                       #Verifica si está bloqueada a su alrededor 
                        #arriba 
                        print(COLOR_ELEGIDO2)
                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] == "." or not  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] in COLOR_ELEGIDO2 and M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] != "-":
                           
                            Algoritmo_Torre()   
                            #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimientos_Torre)):
                                    if Movimientos_Torre[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimientos_Torre[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimientos_Torre.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimientos_Torre.append(k)
                                    break    
                                    

                            if llave_del_jaque_maximous[0] == False:
                                break
                       
                        #derecha
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] == "." or not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO2 and M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] != "|":
                            Algoritmo_Torre()
                            #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimientos_Torre)):
                                    if Movimientos_Torre[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimientos_Torre[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimientos_Torre.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimientos_Torre.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break
                        #isquierda
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] == "." or not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO2 and M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] != "|":
                            Algoritmo_Torre()
                            #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimientos_Torre)):
                                    if Movimientos_Torre[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimientos_Torre[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimientos_Torre.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimientos_Torre.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break
                        #abajo 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] == "." or not  M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] in COLOR_ELEGIDO2 and M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] != "-":
                            Algoritmo_Torre()
                            #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimientos_Torre)):
                                    if Movimientos_Torre[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimientos_Torre[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimientos_Torre.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimientos_Torre.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break
                    
                        else:
                            print("La ficha está bloqueada")
                        
                  
                    #Algoritmo de reina posiciones permitidas 
                    if Ficha2 == B[2] or Ficha2 == N[2]:
                        Movimientos_permitidos_Reina.clear()
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])

                        #color de la ficha elegida
                        COLOR_ELEGIDO1 = 0
                        #verifica si es blanca o negra
                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Blancas[2]:
                            #es una ficha blanca
                            COLOR_ELEGIDO1 = Fichas_Blancas 
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Negras[2]:
                            #es una ficha negra 
                            COLOR_ELEGIDO1 = Fichas_Negras

                        #ALgoritmo ficha
                        def Super_Algoritmo():
                            #el algoritmo que busca hacia arriba
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]])
                                elif not M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]])
                                    break
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] == "-":
                                    break

                                i = i + 1

                            #el algoritmo que busca hacia arriba derecha
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]+i])
                                elif not M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]+i])
                                    break
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] == "+":
                                   break

                                i = i + 1
                            #algoritmo arriba isquierda
                            i = 1
                            while True:
                                if M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]-i])
                                elif not M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]-i])
                                    break
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] == "+":
                                    break
                                i = i + 1 
                            #algoritmo isquierda 
                            i = 1
                            while True:
                                if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0],Ubicacion_ficha[1]-i])
                                elif not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0],Ubicacion_ficha[1]-i])
                                    break
                                elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] == "|":
                                    break
                                i = i + 1 
                            #algoritmo Derecha
                            i = 1
                            while True:
                                if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0],Ubicacion_ficha[1]+i])
                                elif not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0],Ubicacion_ficha[1]+i])
                                    break
                                elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+i] == "|":
                                    break
                                i = i + 1 
                            
                            #el algoritmo que busca hacia abajo
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]])
                                elif not M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]])
                                    break
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] == "-":
                                    break

                                i = i + 1
                            #el algoritmo que busca hacia abajo derecha 
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]+i])
                                elif not M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]+i])
                                    break
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] == "+":
                                    break

                                i = i + 1
                            
                            #el algoritmo que busca hacia abajo isquierda
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] == ".":
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]-i])
                                elif not M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]] in COLOR_ELEGIDO1:
                                    Movimientos_permitidos_Reina.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]-i])
                                    break
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] in COLOR_ELEGIDO1 or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] == "+":
                                    break

                                i = i + 1



                        #Verifica si está bloqueada a su alrededor 
                        #arriba 
                        print(COLOR_ELEGIDO1)
                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] == "." or not  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] in COLOR_ELEGIDO1 and  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] != "-":
                           
                            Super_Algoritmo()  
                            #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimientos_permitidos_Reina)):
                                    if Movimientos_permitidos_Reina[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimientos_permitidos_Reina[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimientos_permitidos_Reina.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimientos_permitidos_Reina.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break  
                           
                           
                        #arriba derecha
                        elif M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] == "." or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1 and M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] != "+" :
                            Super_Algoritmo()
                             #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimientos_permitidos_Reina)):
                                    if Movimientos_permitidos_Reina[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimientos_permitidos_Reina[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimientos_permitidos_Reina.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimientos_permitidos_Reina.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break  
                        #arriba isquierda
                        elif M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] == "."or  not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1 and  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] != "+":
                            Super_Algoritmo()
                             #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimientos_permitidos_Reina)):
                                    if Movimientos_permitidos_Reina[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimientos_permitidos_Reina[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimientos_permitidos_Reina.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimientos_permitidos_Reina.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break  
                        #derecha
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] == "." or not  M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1 and M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] != "|":
                            Super_Algoritmo()
                             #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimientos_permitidos_Reina)):
                                    if Movimientos_permitidos_Reina[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimientos_permitidos_Reina[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimientos_permitidos_Reina.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimientos_permitidos_Reina.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break  
                        #isquierda
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] == "." or not M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1 and M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] != "|":
                            Super_Algoritmo()
                             #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimientos_permitidos_Reina)):
                                    if Movimientos_permitidos_Reina[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimientos_permitidos_Reina[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimientos_permitidos_Reina.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimientos_permitidos_Reina.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break  
                        #abajo 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] == "." or not  M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] in COLOR_ELEGIDO1 and M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] != "-":
                            Super_Algoritmo()
                             #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimientos_permitidos_Reina)):
                                    if Movimientos_permitidos_Reina[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimientos_permitidos_Reina[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimientos_permitidos_Reina.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimientos_permitidos_Reina.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break  
                        #abajo derecha 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] == "." or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1 and M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] != "+":
                            Super_Algoritmo()
                             #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimientos_permitidos_Reina)):
                                    if Movimientos_permitidos_Reina[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimientos_permitidos_Reina[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimientos_permitidos_Reina.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimientos_permitidos_Reina.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break  
                        #abajo isquierda 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1] == "." or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1 and M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1]!="+":
                            Super_Algoritmo()
                             #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimientos_permitidos_Reina)):
                                    if Movimientos_permitidos_Reina[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimientos_permitidos_Reina[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimientos_permitidos_Reina.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimientos_permitidos_Reina.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break  
                        else:
                            print("La ficha está bloqueada")


                    #esto es para el caballo
                    if Ficha2 == B[3] or Ficha2 == N[3]:
                        
                        Movimiento_caballo.clear()
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])

                        Color_ficha_elegida  = 0
                        #verifica si es blanca o negra
                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Blancas[3]:
                            #es una ficha blanca
                            Color_ficha_elegida = Fichas_Negras
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Negras[3]:
                            #es una ficha negra 
                            Color_ficha_elegida = Fichas_Blancas 

                        #la llave incomprensible
                        llave_imcomprensible = [False]

                        #es ta es incompresible HHAHHAHAHHAHAHAHAHHAHA
                        #va moverse una posicion diagonal si siene un dianonal no pasa  luega en la nueva posicion
                        #va a buscar en frente y la isquierda si tiene un gion o si no permite agregar el movimiento           
                        #diagonal Derecha arriba 
                        while True:
                            if not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1]== "-" or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] == "+" or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] == "|":  
                                if not M[Ubicacion_ficha[0]-2][Ubicacion_ficha[1]+1]== "-" :
                                    if  M[Ubicacion_ficha[0]-2][Ubicacion_ficha[1]+1] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]-2,Ubicacion_ficha[1]+1])
                                        llave_imcomprensible.append(True)
                                    
                                
                                if not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+2]== "+" or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+2]== "|":
                                    if  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+2] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]+2])
                                        llave_imcomprensible.append(True)
                                        

                            #diagonal isquierda arriba 
                            if not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1]== "-" or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1]== "+"  or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1]== "|":  
                                if not M[Ubicacion_ficha[0]-2][Ubicacion_ficha[1]-1]== "-":
                                    if  M[Ubicacion_ficha[0]-2][Ubicacion_ficha[1]-1] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]-2,Ubicacion_ficha[1]-1])
                                        llave_imcomprensible.append(True)
                                        
                                
                                if not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-2]== "|" or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-2]== "+":
                                    if  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-2] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]-2])
                                        llave_imcomprensible.append(True)
                                        

                            #digonal isquierda abajo
                            if not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1]== "-" or  not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1]== "+"  or  not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1]== "|":  
                                if not M[Ubicacion_ficha[0]+2][Ubicacion_ficha[1]-1]== "-":
                                    if  M[Ubicacion_ficha[0]+2][Ubicacion_ficha[1]-1] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]+2,Ubicacion_ficha[1]-1])
                                        llave_imcomprensible.append(True)
                                        
                                
                                if not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-2]== "|" or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-2] == "+":
                                    if  M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-2] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]+1,Ubicacion_ficha[1]-2])
                                        llave_imcomprensible.append(True)
                                        

                            #diagonal iderecha abajo           
                            if not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1]== "-" or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1]== "|"  or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1]== "+":  
                                if not M[Ubicacion_ficha[0]+2][Ubicacion_ficha[1]+1]== "-":
                                    if  M[Ubicacion_ficha[0]+2][Ubicacion_ficha[1]+1] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]+2,Ubicacion_ficha[1]+1])
                                        llave_imcomprensible.append(True)
                                        
                            
                                if not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+2]== "|" or not  M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+2]== "+":
                                    if M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+2] in Color_ficha_elegida:
                                        Movimiento_caballo.append([Ubicacion_ficha[0]+1,Ubicacion_ficha[1]+2])
                                        llave_imcomprensible.append(True)
                            break

                       
                        #si sale mal solo colocas if llave_imcomprensible[0] == True   
                        if len(llave_imcomprensible) > 1:
                            llave_imcomprensible.clear()

                            #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimiento_caballo)):
                                    if Movimiento_caballo[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimiento_caballo[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimiento_caballo.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimiento_caballo.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break  

                            break
                        else:
                            print("La ficha está bloquedad")
                        

                    #Esto es para el arfil 
                    if Ficha2 == B[5] or Ficha2 == N[5]:
                        Movimiento_Arfil.clear()
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])

                        Color_ficha_elegida  = 0
                         #verifica si es blanca o negra
                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Blancas[5]:
                            #es una ficha blanca
                            Color_ficha_elegida = Fichas_Blancas 
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Negras[5]:
                            #es una ficha negra 
                            Color_ficha_elegida = Fichas_Negras

                        def Algorito_Arfil():
                            #el algoritmo que busca hacia arriba derecha
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] == ".":
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]+i])
                                elif not M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] in Color_ficha_elegida:
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]+i])
                                    break
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]] in Color_ficha_elegida or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]+i] == "+":
                                   break

                                i = i + 1
                            
                            #el algoritmo que busca hacia arriba isquierda
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] == ".":
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]-i])
                                elif not M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] in Color_ficha_elegida:
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]-i,Ubicacion_ficha[1]-i])
                                    break
                                elif M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] in Color_ficha_elegida or M[Ubicacion_ficha[0]-i][Ubicacion_ficha[1]-i] == "+":
                                   break

                                i = i + 1 

                            #el algoritmo que busca abajo  isquierda
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] == ".":
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]-i])
                                elif not M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] in Color_ficha_elegida:
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]-i])
                                    break
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] in Color_ficha_elegida or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]-i] == "+":
                                   break

                                i = i + 1 

                            #el algoritmo que busca abajo isquierda
                            i  = 1
                            while True:
                                if M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] == ".":
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]+i])
                                elif not M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] in Color_ficha_elegida:
                                    Movimiento_Arfil.append([Ubicacion_ficha[0]+i,Ubicacion_ficha[1]+i])
                                    break
                                elif M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] in Color_ficha_elegida or M[Ubicacion_ficha[0]+i][Ubicacion_ficha[1]+i] == "+":
                                   break

                                i = i + 1 
                        
                        #Verifica si está bloqueada a su alrededor 
                      
                        #arriba derecha
                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] == "." or not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] in Color_ficha_elegida and M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] != "+" :
                            Algorito_Arfil()
                            #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimiento_Arfil)):
                                    if Movimiento_Arfil[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimiento_Arfil[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimiento_Arfil.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimiento_Arfil.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break  
                        #arriba isquierda
                        elif M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] == "."or  not M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] in Color_ficha_elegida and  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] != "+":
                            Algorito_Arfil()
                            #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimiento_Arfil)):
                                    if Movimiento_Arfil[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimiento_Arfil[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimiento_Arfil.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimiento_Arfil.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break  
                      
                        #abajo derecha 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] == "." or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] in Color_ficha_elegida and M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1]  != "+":
                            Algorito_Arfil()
                            #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimiento_Arfil)):
                                    if Movimiento_Arfil[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimiento_Arfil[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimiento_Arfil.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimiento_Arfil.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break  
                        #abajo isquierda 
                        elif M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1] == "." or not M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1] in Color_ficha_elegida and  M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1]  != "+":
                            Algorito_Arfil()
                            #algoritmo que activa el movimiento de la ficha si está en haque 
                            Movimientos_permitidos_para_la_ficha = []
                            if llave_del_jaque_maximous[0] == True:
                                for o in range(len(Movimiento_Arfil)):
                                    if Movimiento_Arfil[o] in Linea_del_ataque_hacia_el_rey:
                                        Movimientos_permitidos_para_la_ficha.append( Movimiento_Arfil[o])
                                if len(Movimientos_permitidos_para_la_ficha) == 0:
                                    print("La ficha no se puede mover el rey está en haque ")
                                else:
                                    Movimiento_Arfil.clear()
                                    for k in Movimientos_permitidos_para_la_ficha:
                                        Movimiento_Arfil.append(k)
                                    break    
                            if llave_del_jaque_maximous[0] == False:
                                break  
                        else:
                            print("La ficha está bloqueada")
    
                    
                    #si es el rey
                    if Ficha2 == B[4] or Ficha2 == N[4]:
                        Movimiento_Rey.clear()
                        print(M[Ubicacion_ficha[0]][Ubicacion_ficha[1]])

                        COLOR_ELEGIDO1  = 0
                         #verifica si es blanca o negra
                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Blancas[4]:
                            #es una ficha blanca
                            COLOR_ELEGIDO1 = Fichas_Negras
                        elif M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] == Fichas_Negras[4]:
                            #es una ficha negra 
                            COLOR_ELEGIDO1 = Fichas_Blancas 

                        #Llava incomprensible 
                        hola = [False]
                        #Verifica si está bloqueada a su alrededor 
                        #arriba 
                        print(COLOR_ELEGIDO1)

                        Movimiento_permitido_arriba111 = [Ubicacion_ficha[0]-1,Ubicacion_ficha[1]]

                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] == "." or  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]] in COLOR_ELEGIDO1:

                            if  Movimiento_permitido_arriba111 in Todos_Los_posiblesAtaques_Arriba:
                                print("La posicion esta Siendo atacada no está permitido el movimiento")

                            elif not Movimiento_permitido_arriba111 in Todos_Los_posiblesAtaques_Arriba:
                                    
                                Movimiento_Rey.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]])
                                hola.append(True)
                           
                        #arriba derecha
                        Movimiento_permitido_arriba_derecha111 = [Ubicacion_ficha[0]-1,Ubicacion_ficha[1]+1]
                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] == "." or M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1:
                            
                            if  Movimiento_permitido_arriba_derecha111 in Todos_Los_posiblesAtaques_Arriba:
                                print("La posicion esta Siendo atacada no está permitido el movimiento")

                            elif not Movimiento_permitido_arriba_derecha111 in Todos_Los_posiblesAtaques_Arriba:
                                Movimiento_Rey.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]+1])
                                hola.append(True)


                        #arriba isquierda
                        Movimiento_permitido_arriba_isquierda111 = [Ubicacion_ficha[0]-1,Ubicacion_ficha[1]-1]
                        if M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] == "."or  M[Ubicacion_ficha[0]-1][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1:
                            
                            if Movimiento_permitido_arriba_isquierda111 in Todos_Los_posiblesAtaques_Arriba:
                                print("La posicion esta Siendo atacada no está permitido el movimiento")
                            elif not Movimiento_permitido_arriba_isquierda111 in Todos_Los_posiblesAtaques_Arriba:
                                
                                Movimiento_Rey.append([Ubicacion_ficha[0]-1,Ubicacion_ficha[1]-1])
                                hola.append(True)
                       
                        #derecha
                        Movimiento_permitido_Derecha111 = [Ubicacion_ficha[0],Ubicacion_ficha[1]+1]

                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] == "." or  M[Ubicacion_ficha[0]][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1:
                           
                            if Movimiento_permitido_Derecha111 in Todos_Los_posiblesAtaques_Arriba:
                               print("La posicion esta Siendo atacada no está permitido el movimiento")
                            elif not Movimiento_permitido_Derecha111 in Todos_Los_posiblesAtaques_Arriba: 

                                Movimiento_Rey.append([Ubicacion_ficha[0],Ubicacion_ficha[1]+1])
                                hola.append(True)

                        #isquierda
                        Movimiento_Permitido_isquierda111 = [Ubicacion_ficha[0],Ubicacion_ficha[1]-1]

                        if M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] == "." or M[Ubicacion_ficha[0]][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1:
                            
                            if Movimiento_Permitido_isquierda111  in Todos_Los_posiblesAtaques_Arriba:
                                print("La posicion esta Siendo atacada no está permitido el movimiento")

                            elif not  Movimiento_Permitido_isquierda111  in Todos_Los_posiblesAtaques_Arriba:
                                Movimiento_Rey.append([Ubicacion_ficha[0],Ubicacion_ficha[1]-1])
                                hola.append(True)
                        #abajo 

                        Movimiento_abajo_111 = [Ubicacion_ficha[0]+1,Ubicacion_ficha[1]]

                        if M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] == "." or  M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]] in COLOR_ELEGIDO1:
                            if Movimiento_abajo_111 in Todos_Los_posiblesAtaques_Arriba:
                                print("La posicion esta Siendo atacada no está permitido el movimiento")
                            elif not Movimiento_abajo_111 in Todos_Los_posiblesAtaques_Arriba:
                                Movimiento_Rey.append([Ubicacion_ficha[0]+1,Ubicacion_ficha[1]])
                                hola.append(True)

                        #abajo derecha 
                        Movimiento_abajo_derecha111 = [Ubicacion_ficha[0]+1,Ubicacion_ficha[1]+1]

                        if M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] == "." or M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]+1] in COLOR_ELEGIDO1:
                            
                            if Movimiento_abajo_derecha111 in Todos_Los_posiblesAtaques_Arriba:
                                print("La posicion esta Siendo atacada no está permitido el movimiento")
                            elif not Movimiento_abajo_derecha111 in Todos_Los_posiblesAtaques_Arriba:
                                Movimiento_Rey.append([Ubicacion_ficha[0]+1,Ubicacion_ficha[1]+1])
                                hola.append(True)


                        #abajo isquierda 
                        Movimiento_abajo_isquierda111 = [Ubicacion_ficha[0]+1,Ubicacion_ficha[1]-1]

                        if M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1] == "." or M[Ubicacion_ficha[0]+1][Ubicacion_ficha[1]-1] in COLOR_ELEGIDO1:
                            
                            if Movimiento_abajo_isquierda111 in Todos_Los_posiblesAtaques_Arriba:
                                print("La posicion esta Siendo atacada no está permitido el movimiento")

                            elif not Movimiento_abajo_isquierda111 in Todos_Los_posiblesAtaques_Arriba:

                                Movimiento_Rey.append([Ubicacion_ficha[0]+1,Ubicacion_ficha[1]-1])
                                hola.append(True)
                        
                        def el_logaritmo_enrrosque(coloring,N_Rey,movi1,movi2,movi3,the_color1,the_color2,suma1,suma2,suma3,sum11,suma22,suma33,ubicator1,ubicator2):

                            #esto es para hacer el enrosque
                            #El primer Movimiento

                            Primer_movimiento_rey = []
                            Primer_movimiento_Torre1 = []
                            Primer_movimiento_Torre2 = []

                            #verifica si el rey ya se mobio
                            if not coloring[4] == M[10][N_Rey]:
                                movi1.append(True)
                                Primer_movimiento_rey.append(True)

                            #verifica si la torre de la isquierda ya se mobio
                            if not  coloring[1] == M[10][3]:
                                movi2.append(True)
                                Primer_movimiento_Torre1.append(True)
                            
                            #verificca si la torre de la derecha ya se movió
                            if not coloring[1] == M[10][10]:
                                movi3.append(True)
                                Primer_movimiento_Torre2.append(True)

                            
                            if len(movi1) == 0 and len(movi2) == 0 or len(movi1) == 0 and len(movi3) == 0 :

                                #este hace que cambie el movimiento son las fichas de abajo son negras

                                #verifica si el enroque a la derecha 
                                if len(Primer_movimiento_Torre1) == 0 and len(Primer_movimiento_rey) == 0:
                                    Ubicacion_wachachaca=  [Ubicacion_ficha[0],Ubicacion_ficha[1]]
                                    Ubicacion_wachachaca1 = [Ubicacion_ficha[0],Ubicacion_ficha[1]+suma1]
                                    Ubicacion_wachachaca2 = [Ubicacion_ficha[0],Ubicacion_ficha[1]+suma2]
                                    Ubicacion_wachachaca3 = [Ubicacion_ficha[0],Ubicacion_ficha[1]+suma3]

                                    if not Ubicacion_wachachaca in Todos_Los_posiblesAtaques_Arriba: 
                                        if M[Ubicacion_wachachaca1[0]][Ubicacion_wachachaca1[1]] == "." and not Ubicacion_wachachaca1 in Todos_Los_posiblesAtaques_Arriba:
                                            if M[Ubicacion_wachachaca2[0]][Ubicacion_wachachaca2[1]] == "." and not Ubicacion_wachachaca2 in Todos_Los_posiblesAtaques_Arriba:
                                                if M[Ubicacion_wachachaca3[0]][Ubicacion_wachachaca3[1]] == "." and not Ubicacion_wachachaca3 in Todos_Los_posiblesAtaques_Arriba:
                                                    Movimiento_Rey.append([Ubicacion_wachachaca2[0],Ubicacion_wachachaca2[1]]) 
                                                    hola.append(True)
                                                    the_color1.append([10,ubicator1])
                                                    


                                #Si es en la idquierda

                                if  len(Primer_movimiento_Torre2) == 0 and len(Primer_movimiento_rey) == 0:
                                    Ubicacion_wachachacat=  [Ubicacion_ficha[0],Ubicacion_ficha[1]]
                                    Ubicacion_wachachaca1t = [Ubicacion_ficha[0],Ubicacion_ficha[1]+sum11]
                                    Ubicacion_wachachaca2t = [Ubicacion_ficha[0],Ubicacion_ficha[1]+suma22]
                                    Ubicacion_wachachaca3t = [Ubicacion_ficha[0],Ubicacion_ficha[1]+suma33]


                                    if not Ubicacion_wachachacat in Todos_Los_posiblesAtaques_Arriba: 
                                        if M[Ubicacion_wachachaca1t[0]][Ubicacion_wachachaca1t[1]] == "." and not Ubicacion_wachachaca1t in Todos_Los_posiblesAtaques_Arriba:
                                            if M[Ubicacion_wachachaca2t[0]][Ubicacion_wachachaca2t[1]] == "." and not Ubicacion_wachachaca2t in Todos_Los_posiblesAtaques_Arriba:
                                                if  M[Ubicacion_wachachaca3t[0]][Ubicacion_wachachaca3t[1]] == "." and not Ubicacion_wachachaca3t in Todos_Los_posiblesAtaques_Arriba:
                                                    Movimiento_Rey.append([Ubicacion_wachachaca2t[0],Ubicacion_wachachaca2t[1]])
                                                    hola.append(True)
                                                    the_color2 .append([10,ubicator2])
                        
                        #si le toca a las blancas
                        if COLOR_ELEGIDO1 == Fichas_Negras:
                            #este es para el rey de abajo
                            el_logaritmo_enrrosque(Fichas_Blancas,7,primer_movimiento_1,primer_movimiento_2,primer_movimiento_3,Ubicacion_torre11111,Ubicacion_torre22222,+1,+2,+2,-1,-2,-3,10,3)

                        #si le toca a las negras
                        if COLOR_ELEGIDO1 == Fichas_Blancas:
                            #para el rey de arriba
                            el_logaritmo_enrrosque(Fichas_Negras,6,primer_movimiento_11,primer_movimiento_22,primer_movimiento_33,Ubicacion_torre33333,Ubicacion_torre44444,+1,+2,+3,-1,-2,-2,3,10)



                        if len(hola) > 1:
                            hola.clear()
                            break
                        else:
                            print("La ficha está bloqueada")
           

            if LLave1 == False:
                #posicion relativa de las fichas
                #ubicavion
                Posicion_Relativa = [0,0]
                #se moverá 
                Movimento_relativo = [0,0]

                def Algoritmo(La_ficha,peon,torre,reina,caballo,rey,arfil):
                    #Ve que ficha es, y  apartir de eso empiezan los algoritmos
                    if La_ficha == peon:
                                               
                        Movimento_relativo.clear() 
                        Movimento_relativo.append(Ubicacion_ficha[2])
                        Movimento_relativo.append(Ubicacion_ficha[3])



                        #Si el peon llega a la ultima posicion entonces se le permite cambiar por una ficha
                        if Movimento_relativo[0] == 3:
                            system("cls")
                            LAS_fichas_del_cambio = [T1B,DB,C1B,A1B]
                            while True:
                                print("Has llegado a la ultima posicion ahora puedes cambiar el peon por la ficha que deses ")
                                for i in range(len(LAS_fichas_del_cambio)):
                                    print(f"{i+1} = {LAS_fichas_del_cambio[i]}.   ",end=" ")
                                    print()
                                while True:
                                    try:    
                                        Que_ficha = int(input("Por que fichas deseas remplasar el peon ingrese un numero "))

                                        if Que_ficha == 1:
                                            LFicha.pop(0)
                                            LFicha.append(LAS_fichas_del_cambio[0])
                                            break
                                        elif Que_ficha == 2:
                                            LFicha.pop(0)
                                            LFicha.append(LAS_fichas_del_cambio[1])
                                            break
                                        elif Que_ficha == 3:
                                            LFicha.pop(0)
                                            LFicha.append(LAS_fichas_del_cambio[2])
                                            break
                                        elif Que_ficha == 4:
                                            LFicha.pop(0)
                                            LFicha.append(LAS_fichas_del_cambio[3])
                                            break
                                        else:
                                            print("No sea pendejo este numero no existe")
                                    except ValueError:
                                        print("No sea bobo le pidieron un numero ")

                                break
                        #Peon
                        print("El Peon está  ")
                        print(Ubicacion_ficha[0],Ubicacion_ficha[1])
                        print("El Peon se va a mover a ")
                        print(Ubicacion_ficha[2],Ubicacion_ficha[3])

                        #esto es para hacer la captura al paso 
                        if Ubicacion_ficha[0] == 9:
                            if Ubicacion_ficha[2]== 7:
                                print()
                                if M[7][Ubicacion_ficha[3]-1 ]== Color_Variable2[0]  or  M[7][Ubicacion_ficha[3]+1] == Color_Variable2[0]:
                                    lavus_maximous_capture.clear()
                                    lavus_maximous_capture.append(True)


                        #los movimintos 
                        #los movimientos 
                        Movimento_relativo.clear()
                        Movimento_relativo.append(Ubicacion_ficha[2])
                        Movimento_relativo.append(Ubicacion_ficha[3])

                        print(Movimientos_Peon)

                        for i in range(len(Movimientos_Peon)):
                            for j in range(1):
                                if Movimento_relativo[0] == Movimientos_Peon[i][j] and  Movimento_relativo[1] == Movimientos_Peon[i][j+1]:
                                    LLave_cambio_posicion.clear()
                                    LLave_cambio_posicion.append(True)    
                            

                           
                            
                        
                           
                    #EL algoritmo de la torre Torre 
                    elif La_ficha == torre:
                        #La torrre 
                        print("El la Torre esta en ")
                        print(Ubicacion_ficha[0],Ubicacion_ficha[1])
                        print("La Torre se va a mover a ")
                        print(Ubicacion_ficha[2],Ubicacion_ficha[3])

                        #los movimintos 
                        #los movimientos 
                        Movimento_relativo.clear()
                        Movimento_relativo.append(Ubicacion_ficha[2])
                        Movimento_relativo.append(Ubicacion_ficha[3])

                        print(Movimientos_Torre)

                        for i in range(len(Movimientos_Torre)):
                            for j in range(1):
                                if Movimento_relativo[0] == Movimientos_Torre[i][j] and  Movimento_relativo[1] == Movimientos_Torre[i][j+1]:
                                    LLave_cambio_posicion.clear()
                                    LLave_cambio_posicion.append(True) 
                                   

                        
                    elif La_ficha == reina:
                        # #Reina
                        # print("El la Reina esta en ")
                        # print(Ubicacion_ficha[0],Ubicacion_ficha[1])
                        # print("La reina se va a mover a ")
                        # print(Ubicacion_ficha[2],Ubicacion_ficha[3])

                        #los movimientos 
                        Movimento_relativo.clear()
                        Movimento_relativo.append(Ubicacion_ficha[2])
                        Movimento_relativo.append(Ubicacion_ficha[3])

                        print(Movimientos_permitidos_Reina)
                        
                        for i in range(len(Movimientos_permitidos_Reina)):
                            for  j in range(1):
                                # print(Movimientos_permitidos_Reina[i][j] )
                                # print(Movimientos_permitidos_Reina[i][j+1] )
                                # print(Movimientos_permitidos_Reina[i][j]+1)
                                if Movimento_relativo[0] == Movimientos_permitidos_Reina[i][j] and  Movimento_relativo[1] == Movimientos_permitidos_Reina[i][j+1]:
                                    LLave_cambio_posicion.clear()
                                    LLave_cambio_posicion.append(True) 
                                   
                        
                    elif La_ficha == caballo:

                        
                        #los movimintos 
                        #los movimientos 
                        Movimento_relativo.clear()
                        Movimento_relativo.append(Ubicacion_ficha[2])
                        Movimento_relativo.append(Ubicacion_ficha[3])

                        print(Movimiento_caballo)

                        for i in range(len(Movimiento_caballo)):
                            for j in range(1):
                                if Movimento_relativo[0] == Movimiento_caballo[i][j] and  Movimento_relativo[1] == Movimiento_caballo[i][j+1]:
                                    LLave_cambio_posicion.clear()
                                    LLave_cambio_posicion.append(True) 



                        
                    elif La_ficha == rey:
                        # #Rey
                        # print("El rey Está ")
                        # print(Ubicacion_ficha[0],Ubicacion_ficha[1])
                        # print("El rey se va a mover a ")
                        # print(Ubicacion_ficha[2],Ubicacion_ficha[3])

                        #este ba a hacer el enrosque

                        def deciciones_logicas(cor_1,cor_2,ubicacion1,ubicacion2):
                            #esta es la derecha
                            if Ubicacion_ficha[2] == 10  and Ubicacion_ficha[3] == cor_1:
                                
                                M[10][ubicacion1] = M[10][10]
                                M[10][10] = "."
                            #esta es la isquierda
                            if Ubicacion_ficha[2] == 10 and Ubicacion_ficha[3] == cor_2:
                                
                                M[10][ubicacion2] = M[10][3]
                                M[10][3] = "."
                        

                        if Color_Variable1 == Fichas_Blancas:
                            deciciones_logicas(9,5,8,6)

                        if  Color_Variable1 == Fichas_Negras:
                            deciciones_logicas(8,4,7,5)
                        
                        
                        Ubicacion_torre11111.clear()
                        Ubicacion_torre22222.clear()


                        #los movimintos 
                        #los movimientos 
                        Movimento_relativo.clear()
                        Movimento_relativo.append(Ubicacion_ficha[2])
                        Movimento_relativo.append(Ubicacion_ficha[3])

                        print(Movimiento_Rey)

                        for i in range(len(Movimiento_Rey)):
                            for j in range(1):
                                if Movimento_relativo[0] == Movimiento_Rey[i][j] and  Movimento_relativo[1] == Movimiento_Rey[i][j+1]:
                                    LLave_cambio_posicion.clear()
                                    LLave_cambio_posicion.append(True) 
                        
                    elif La_ficha == arfil:
                        #Arfil 
                        #imprime las posiciones 
                        # print("El la Torre esta en ")
                        # print(Ubicacion_ficha[0],Ubicacion_ficha[1])
                        # print("La Torre se va a mover a ")
                        # print(Ubicacion_ficha[2],Ubicacion_ficha[3])

                        #los movimintos 
                        #los movimientos 
                        #guarda los movimientos

                        Movimento_relativo.clear()
                        Movimento_relativo.append(Ubicacion_ficha[2])
                        Movimento_relativo.append(Ubicacion_ficha[3])

                        print(Movimiento_Arfil)

                        #compara cada movimiento permitido de la ficha con el moviento ingresado si coinciden ingresa una llave 
                        for i in range(len(Movimiento_Arfil)):
                            for j in range(1):
                                if Movimento_relativo[0] == Movimiento_Arfil[i][j] and  Movimento_relativo[1] == Movimiento_Arfil[i][j+1]:
                                    LLave_cambio_posicion.clear()
                                    LLave_cambio_posicion.append(True) 
                    
                #pasa la ficha y la posicion de la ficha cuando se selecciona
                Algoritmo(LFicha[0],peon=Colorde_ficha2[0],torre=Colorde_ficha2[1],reina=Colorde_ficha2[2],caballo=Colorde_ficha2[3],rey=Colorde_ficha2[4],arfil=Colorde_ficha2[5])

                #coloca el la ficha en la posicion colocada
                if LLave_cambio_posicion[0] == True:
                    #posiccion anterior
                    M[Posicion_Relativa[0]][Posicion_Relativa[1]] = "."
                    M[Ubicacion_ficha[0]][Ubicacion_ficha[1]] = "."
                    #posicion de movimiento
                    M[fila2][columna2] = LFicha[0]

                    #limpia la llave para la proxima entrada
                    LLave_cambio_posicion.pop(0)
                    LLave_cambio_posicion.append(0)

                    break #si todo está ok pasa esto 

    #condicional supermaestro
    #Se pasqa por parametros las occiones y una llave que activa la opcion de eleccion o la opcion de colocar fica 
    
    Funcion_ingresaFicha("Posicion de ficha >","Ingrese la ",True)
    
    Funcion_ingresaFicha("El movimiento de la ficha > ","Ingrese ",False)
    

Contador_cambio = 2
while True:
    
    #hace que cambien de occion van rotando las acciones...
    if Contador_cambio %2 == 0:
        # se pasa por parametro las poscciones de la letra dentro de la matriz M
        # y el Color de ficha que verifica si le corresponde el juego 
        Accion("Jugador1",3,4,5,6,7,8,9,10,3,4,5,6,7,8,9,10,N,B,Fichas_Blancas,Fichas_Negras)

    else:
        Accion("Jugador2",10,9,8,7,6,5,4,3,10,9,8,7,6,5,4,3,B,N,Fichas_Negras,Fichas_Blancas)
        #limpia La ubicacion del rey
       
    Contador_cambio = Contador_cambio + 1