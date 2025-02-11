import datetime 
import logging

print("Bienvenid@ al taxímetro")
print("El taxímetro funciona de la siguiente manera: en este taxímetro podrás iniciar un viaje y pausarlo cuando desees, así mismo podrás renudar tu viaje, y finalizarlo cuando consideres que debe terminar el viaje, estas son las siguientes opciones")


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
    logging.info("\n---Viaje iniciado!🚕🚕---")
    state['startTime'] = datetime.datetime.now()
    state['statusChange'] = state['startTime']
    state['lastTime'] = state['startTime']
    state['currentStatus'] = 'move'
    return state

def pauseRide(state):
    now = datetime.datetime.now()
    elapsed = (now - state['lastTime']).total_seconds() / 60 
    if state['currentStatus'] == "move":
        state['moveDuration'] += elapsed
        state['currentStatus'] = "pause"
        logging.info("------Viaje en pausa ⏸️------")

    else:
        state['stopDuration'] += elapsed
        state['currentStatus'] = "move"
        logging.info("------Viaje reanudado 🚕🚕------")
    state['lastTime'] = now
    return state

def changeStatus(state):
    now = datetime.datetime.now()
    elapsed = (now - state['lastTime']).total_seconds() / 60

    if state['currentStatus'] == "move":
        state['moveDuration'] += elapsed
        state['currentStatus'] = "stop"
        logging.info("------Viaje detenido 🛑------")
    else:
        state['stopDuration'] += elapsed
        state['currentStatus'] = "move"
        logging.info("------Taxi en movimiento------")

    return state   

def finishRide(state):
    elapsed = (datetime.datetime.now() - state['startTime']).total_seconds() / 60
    if state['currentStatus'] == "move":
        state['moveDuration'] += elapsed
    elif state['currentStatus'] == "stop":
        state['stopDuration'] += elapsed

    totalFee = calculateFee(state['moveDuration'], state['stopDuration'])    
    logging.info("\n---Viaje finalizado 🔚---")
    
    logging.info(f"El costo total del viaje es: €{totalFee:.2f}")
    return state

def calculateFee(moveDuration, stopDuration):
    
    feeBase = 3.5
    feeStop = 0.02
    feeMove = 1.5
    stopFee = stopDuration * feeStop
    moveFee = max(0, moveDuration - 10) * feeMove
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

    while True:
        print("\nOpciones:")
        print("1. Iniciar viaje")
        print("2. Pausar/Reanudar viaje")
        print("3. Finalizar viaje")
        print("4. Salir del programa")
        
        option = input("Elige una opción: ")
    
        if option == "1":
            if state['startTime']:
                logging.warning("-----------Ya hay un viaje iniciado, puedes finalizarlo para iniciar otro-----------")
            else: 
                state = initRide(state)
            
        
        elif option == "2":
            if not state['startTime']:
                logging.warning("-----------No hay un viaje iniciado-----------")
            else:
                state = pauseRide(state)
                

        elif option == "3":
            if not state['startTime']:
                logging.warning("-----------No hay un viaje iniciado-----------")
            else:
                state = finishRide(state)
                logging.info("\n--- Resumen del viaje ---")
                logging.info(f"Duración total del viaje: {round(state['moveDuration'], 2) + round(state['stopDuration'])}")
                logging.info(f"Tiempo parado: {state['stopDuration']:.2f} minutos")
                print("------------------------")
                state = createTaximeter()

        elif option == "4":
            print("-----------Adiós y gracias por usar el taxi 👋-----------")
            break

        else:
            logging.warning("-----------Opción no válida, por favor elige una opción correcta-----------")
            
        

main()