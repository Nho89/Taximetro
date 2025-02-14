import datetime 
import logging

print("Bienvenid@ al taxímetro")
print("Con este taxímetro, podrás registrar tus viajes de taxi, incluyendo pausas, y calcular el costo total.")
print("Sigue las opciones del menú para controlar el viaje.")
print("\n¿Cuánto cuesta el viaje?")
print("La tarifa se calcula así:")
print(" - Inicio: 3.5€.")
print(" - En movimiento: 0.05€ por segundo.")
print(" - Parado: 0.02€ por segundo.")



def createTaximeter():
    return {
        'startTime' : None,
        'statusTime' : None,
        'currentStatus' : 'move',
        'moveDuration' : 0,
        'stopDuration' : 0,
        'lastTime' : None
    }

def initRide(state):
    print("\n---Viaje iniciado!🚕🚕---")
    state['startTime'] = datetime.datetime.now()
    state['statusChange'] = state['startTime']
    state['lastTime'] = state['startTime']
    state['currentStatus'] = 'move'
    return state

def pauseRide(state):
    now = datetime.datetime.now()
    elapsed = (now - state['lastTime']).total_seconds() #/ 60 
    if state['currentStatus'] == "move":
        state['moveDuration'] += elapsed
        state['currentStatus'] = "pause"
        logging.info("\n------Viaje en pausa ⏸️------")

    else:
        state['stopDuration'] += elapsed
        state['currentStatus'] = "move"
        logging.info("\n------Viaje reanudado 🚕🚕------")
    state['lastTime'] = now
    return state

# def changeStatus(state):
#     now = datetime.datetime.now()
#     elapsed = (now - state['lastTime']).total_seconds() / 60

#     if state['currentStatus'] == "move":
#         state['moveDuration'] += elapsed
#         state['currentStatus'] = "stop"
#         logging.info("\n------Viaje detenido 🛑------")
#     else:
#         state['stopDuration'] += elapsed
#         state['currentStatus'] = "move"
#         logging.info("\n------Taxi en movimiento------")

#     return state   

def finishRide(state):
    elapsed = (datetime.datetime.now() - state['startTime']).total_seconds() / 60
    if state['currentStatus'] == "move":
        state['moveDuration'] += elapsed
    elif state['currentStatus'] == "stop":
        state['stopDuration'] += elapsed

    # totalFee = calculateFee(state['moveDuration'], state['stopDuration'])    
    print("\n---Viaje finalizado 🔚---")
    
    # print(f"El costo total del viaje es: €{totalFee:.2f}")
    return state

def calculateFee(moveDuration, stopDuration):
    
    feeBase = 3.5
    feeStop = 0.02
    feeMove = 0.05
    stopFee = stopDuration * feeStop
    moveFee = max(0, moveDuration) * feeMove
    return feeBase + stopFee + moveFee


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler(".taximeter.log", mode="a", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

def main():
    
    state = createTaximeter()
    totalFee = calculateFee(state['moveDuration'], state['stopDuration'])
    while True:
        print("\nOpciones:")
        print("1. Iniciar viaje")
        print("2. Pausar/Reanudar viaje")
        print("3. Finalizar viaje")
        print("4. Salir del programa\n")
        
        option = input("Elige una opción: ")
    
        if option == "1":
            if state['startTime']:
                print("-----------Ya hay un viaje iniciado, puedes finalizarlo para iniciar otro-----------")
            else: 
                state = initRide(state)
            
        
        elif option == "2":
            if not state['startTime']:
                print("-----------No hay un viaje iniciado-----------")
            else:
                state = pauseRide(state)
                

        elif option == "3":
            if not state['startTime']:
                print("-----------No hay un viaje iniciado-----------")
            else:
                state = finishRide(state)
                print("\n--- Resumen del viaje ---")
                print(f"Duración total del viaje: {round(state['moveDuration'], 2) + round(state['stopDuration'])}")
                print(f"Tiempo parado: {state['stopDuration']:.2f} minutos")
                print(f"El costo total del viaje es: €{totalFee:.2f}")
                print("------------------------")
                state = createTaximeter()

        elif option == "4":
            print("-----------Adiós y gracias por usar el taxi 👋-----------")
            break

        else:
            print("-----------Opción no válida, por favor elige una opción correcta-----------")
            
        

main()