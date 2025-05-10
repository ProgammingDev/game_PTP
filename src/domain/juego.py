from ppt.core.jugador import JugadorHumano, JugadorCPU,Jugador
from ppt.core.ronda import Ronda
import os

class Juego():
    def __init__(self):
        self.__jugador1 = None
        self.__jugador2 = None
        self.__rondasJugadas = 0
        self.__rondasTotales = 0
        self.__estadisticas = []
        self.__empate= False
        """ self.__establecer_jugadores()
        self.__establecer_reglas() """

    
    #Metodos de control de flujo de datos
    def iniciar_juego(self):                
        while self.__rondasTotales != self.__rondasJugadas:
            self.__jugar_ronda()
            
        self.__mostrar_estadisticas()
   
    def __jugar_ronda(self):
            #Solicita a los jugadores sus manos
            self.__jugador1.elegir()
            self.__jugador2.elegir()
            
            #Devuelve la ronda ya evaluada 
            ronda:Ronda = self.determinar_ronda()

            #Registra la ronda en la memoria
            self.__registrar_ronda(ronda)


            #Muesra los resultados de la ronda 
            self.__mostrar_resultados(ronda)
            
            #Evaluar empate 
            if(self.__empate and self.evaluar_emapte(ronda)):
                return self.__jugar_ronda()

            #Finaliza la ronda
            self.__rondasJugadas += 1
        
        
    def evaluar_emapte(self,ronda:Ronda):
        if(ronda.ganador == ronda.perderdor):
            return True



    def determinar_ronda(self):
        ganador,perdedor = None,None 
        
        #El id devuelve al que esta asociado el nombre de la opcion jugada
        eleccion_j1_id = self.__jugador1.get_eleccion_actual_id()
        eleccion_j1_nombre= self.__jugador1.get_eleccion_actual_nombre()

        eleccion_j2_id = self.__jugador2.get_eleccion_actual_id()
        eleccion_j2_nombre= self.__jugador2.get_eleccion_actual_nombre()
        
        if eleccion_j1_id < eleccion_j2_id :
            ganador,perdedor = self.__jugador1, self.__jugador2
            self.__jugador1.sumar_punto()

       
        elif eleccion_j1_id > eleccion_j2_id:
             ganador,perdedor =self.__jugador2,self.__jugador1
             self.__jugador2.sumar_punto()

        return Ronda(eleccion_j1_nombre,eleccion_j2_nombre,self.__rondasJugadas,ganador,perdedor)
           
   
    def __registrar_ronda(self,ronda):
        self.__estadisticas.append(ronda)

#Metodos de visualizacion
#    def __mostrar_ganador_de_ronda(self,ronda:Ronda):
        ganador,perdedor = ronda.ganador, ronda.perderdor
        
        
        if(ronda.eleccion_j1 == ronda.eleccion_j2 ):
          print('\nParicipantes empatados a jugar de nuevo!!!')
          return
      
        print(f'\nLa ronda numero {self.__rondasJugadas + 1} la gana {ganador.nombre()} felicitaciones!!')
        print(f'\nLa proxima sera {perdedor.nombre()}')
#
#    def __mostrar_resultados(self,ronda):
        self.__mostrar_ganador_de_ronda(ronda)

        print(" ")
        print('Jugador: ',self.__jugador1.get_puntaje())
        print('CPU: ',self.__jugador2.get_puntaje())
        os.system('pause')
        os.system('cls')
#    
#    def __mostrar_estadisticas(self):
#        print('Resumen de la partida: \n')
#        for estadistica in self.__estadisticas :
#            estadistica:Ronda
#            ganador:Jugador=estadistica.ganador
#            print(f'En la ronda numero: {estadistica.numero+1}')
#            print(
#                f"La eleccion del Jugador fue {str(estadistica.eleccion_j1).upper()} y la de la CPU fue {str(estadistica.eleccion_j2).upper()}, "
#                f"por lo tanto el GANADOR es {ganador.get_nombre() if ganador is not None else 'nadie!!'}"
#                )
#            print('\n')
#
##Metodos de establecimientos de partida
#def __establecer_rondas(self):
#    while True:
#        rondas = int(input('Cuantas rondas deseas jugar? '))
#        if(rondas > 0):
#            self.__rondasTotales = rondas
#            os.system('cls')
#            break    
#        else:
#            print("Ronda invalida")
#
#def __establecer_empate(self):
        while True:
            si_no_empate = input('Desea jugar con desempate SI-[S] NO-[N]: ').upper()
            if si_no_empate == 'S':
                self.__empate = not(self.__empate)
                break
            elif si_no_empate == 'N':
                break
#
#def __establecer_jugadores(self):
        os.system("cls")
        self.__jugador1= JugadorHumano(input('Ingrese su nombre jugador: '))
        self.__jugador2= JugadorCPU()
        os.system("cls")
#
#def __establecer_reglas(self):
        self.__establecer_rondas()
        self.__establecer_empate()        
    

    #Estos se pueden parametrizar en un solo metodo
    def asingar_jugadores(self,regJugador1:Jugador,regJugador2:Jugador):
        self.__jugador1 = regJugador1
        self.__jugador2 = regJugador2

    
    
    def asignar_empate(self,opc):
        self.__empate = opc

    def asignar_rondasTotales(self,opc):
        self.__rondasTotales = opc

