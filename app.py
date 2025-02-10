import datetime 

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
    print("\n---Viaje iniciado!🚕🚕---")
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
        print("------Viaje en pausa ⏸️------")

    else:
        state['stopDuration'] += elapsed
        state['currentStatus'] = "move"
        print("------Viaje reanudado 🚕🚕------")
    state['lastTime'] = now
    return state

def changeStatus(state):
    now = datetime.datetime.now()
    elapsed = (now - state['lastTime']).total_seconds() / 60

    if state['currentStatus'] == "move":
        state['moveDuration'] += elapsed
        state['currentStatus'] = "stop"
        print("------Viaje detenido 🛑------")
    else:
        state['stopDuration'] += elapsed
        state['currentStatus'] = "move"
        print("------Taxi en movimiento------")

    return state   

def finishRide(state):
    elapsed = (datetime.datetime.now() - state['startTime']).total_seconds() / 60
    if state['currentStatus'] == "move":
        state['moveDuration'] += elapsed
    elif state['currentStatus'] == "stop":
        state['stopDuration'] += elapsed

    totalFee = calculateFee(state['moveDuration'], state['stopDuration'])    
    print("\n---Viaje finalizado 🔚---")
    
    print(f"El costo total del viaje es: €{totalFee:.2f}")
    return state

def calculateFee(moveDuration, stopDuration):
    
    feeBase = 3.5
    feeStop = 0.02
    feeMove = 1.5
    stopFee = stopDuration * feeStop
    moveFee = max(0, moveDuration - 10) * feeMove
    return feeBase + stopFee + moveFee


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
                print("------------------------")
                state = createTaximeter()

        elif option == "4":
            print("-----------Adiós y gracias por usar el taxi 👋-----------")
            break

        else:
            print("-----------Opción no válida, por favor elige una opción correcta-----------")
            
        

main()