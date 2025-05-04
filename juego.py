from jugador import JugadorHumano, JugadorCPU,Jugador
from ronda import Ronda
import os

class Juego():
    def __init__(self):
        self.__jugador1 = None
        self.__jugador2 = None
        self.__rondasJugadas = 0
        self.__rondasTotales = 0
        self.__estadisticas = []
        self.__empate= False
        self.__establecer_jugadores()
        self.__establecer_reglas()

    
    #Metodos de control de flujo de datos
    def iniciar_juego(self):                
        while self.__rondasTotales != self.__rondasJugadas:
            self.__jugar_ronda()
            
        self.__mostrar_estadisticas()
   
    def __jugar_ronda(self):
            self.__jugador1.elegir()
            self.__jugador2.elegir()

            eleccion_j1 = list(self.__jugador1.get_eleccion_actual().values())
            eleccion_j2 = list(self.__jugador2.get_eleccion_actual().values())
            
            #Determinar y registrar ganador se tendria que llamar determinarYdevolerGanador
            self.__determinarYregistrar_ganador(eleccion_j1,eleccion_j2)
            # si hay empate se return __jugar_ronda()

            self.mostrar_resultados()
            self.__rondasJugadas = self.__rondasJugadas + 1

    def __determinarYregistrar_ganador(self,eleccion_j1:int,eleccion_cpu:int):
        # Algoritmo que determina el ganador de la ronda 
        # el ganador se almacena en una variable para enviar a registrar la ronda al metodo registrar_ronda

        ganador = None 
        perdedor = None
        if eleccion_j1[1] < eleccion_cpu[1] :
            self.__jugador1.sumar_punto()
            ganador = self.__jugador1
            perdedor = self.__jugador2

        elif eleccion_j1[1] == eleccion_cpu[1]:
            if(self.__empate):
                return self.__reiniciar_ronda()
        else :
             self.__jugador2.sumar_punto()
             ganador =self.__jugador2
             perdedor= self.__jugador1

        self.__registrar_ronda(eleccion_j1[0],eleccion_cpu[0],ganador)
        self.__mostrar_ganador_de_ronda(ganador,perdedor)
       
   
    def __registrar_ronda(self,eleccion_j1,eleccion_j2,ganador):
        ronda = Ronda(eleccion_j1,eleccion_j2,ganador,self.__rondasJugadas)
        self.__estadisticas.append(ronda)

    def __reiniciar_ronda(self):
        self.jugar_ronda()

    #Metodos de visualizacion
    def __mostrar_ganador_de_ronda(self,ganador:Jugador,perdedor:Jugador):
        if(ganador == perdedor):
          print('\nParicipantes empatados a jugar de nuevo!!!')
          return
      
        print(f'\nLa ronda numero {self.__rondasJugadas + 1} la gana {ganador.get_nombre()} felicitaciones!!')
        print(f'\nLa proxima sera {perdedor.get_nombre()}')

    def mostrar_resultados(self):
        print(" ")
        print('Jugador: ',self.__jugador1.get_puntaje())
        print('CPU: ',self.__jugador2.get_puntaje())
        os.system('pause')
        os.system('cls')
    
    def __mostrar_estadisticas(self):
        print('Resumen de la partida: \n')
        for estadistica in self.__estadisticas :
            estadistica:Ronda
            ganador:Jugador=estadistica.ganador
            print(f'En la ronda numero: {estadistica.numero+1}')
            print(
                f"La eleccion del Jugador fue {str(estadistica.eleccion_j1).upper()} y la de la CPU fue {str(estadistica.eleccion_j2).upper()}, "
                f"por lo tanto el GANADOR es {ganador.get_nombre() if ganador is not None else 'nadie!!'}"
                )
            print('\n')

    #Metodos de establecimientos de partida
    def __establecer_rondas(self):
        while True:
            rondas = int(input('Cuantas rondas deseas jugar? '))
            if(rondas > 0):
                self.__rondasTotales = rondas
                os.system('cls')
                break    
            else:
                print("Ronda invalida")

    def __establecer_empate(self):
        si_no_empate = input('Desea jugar con empate por cada ronda SI-[S] NO-[N]')
        if si_no_empate == 'S':
            self.__empate = True
    
    def __establecer_jugadores(self):
        os.system("cls")
        self.__jugador1= JugadorHumano(input('Ingrese su nombre jugador: '))
        self.__jugador2= JugadorCPU()
        os.system("cls")

    def __establecer_reglas(self):
        self.__establecer_rondas()
        """ self.__establecer_empate() """            
 
