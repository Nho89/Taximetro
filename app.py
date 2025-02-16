import datetime 
import logging
import locale

locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")

print("Bienvenid@ al taxímetro")
print("Con este taxímetro, podrás registrar tus viajes de taxi, incluyendo pausas, y calcular el costo total.")
print("Sigue las opciones del menú para controlar el viaje.")
print("\n¿Cuánto cuesta el viaje?:")
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
    print("\n---🚕🚕 Viaje iniciado! 🚕🚕---")
    state['startTime'] = datetime.datetime.now()
    state['lastTime'] = datetime.datetime.now() #state['startTime']
    state['currentStatus'] = 'move'
    return state

def pauseRide(state):
    now = datetime.datetime.now()
    elapsed = (now - state['lastTime']).total_seconds() / 60 
    if state['currentStatus'] == "move":
        state['moveDuration'] += elapsed
        state['currentStatus'] = "pause"
        print("\n------🚖 Viaje en pausa ⏸️------")

    else:
        state['stopDuration'] += elapsed
        state['currentStatus'] = "move"
        print("\n------🚕🚕 Viaje reanudado 🚕🚕------")
    state['lastTime'] = now
    return state
  

def finishRide(state):
    now = datetime.datetime.now()
    elapsed = (now - state['lastTime']).total_seconds()
    if state['currentStatus'] == "move":
        state['moveDuration'] += elapsed
    else:
        state['stopDuration'] += elapsed

    totalFee = calculateFee(state['moveDuration'], state['stopDuration'])    
    
    logEntry = (
        f"\n--- Resumen del viaje 🧳---\n"
        f"📆 Fecha: {state['startTime'].strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"⌛ Duración total del viaje: {round((state['moveDuration'] + state['stopDuration']) / 60, 2)} minutos\n"
        f"🚕 Tiempo en movimiento: {round(state['moveDuration']/60,2)} minutos\n"
        f"⏸️ Tiempo parado: {round(state['stopDuration'] / 60, 2)} minutos\n"
        f"💰 El costo total del viaje es: {locale.currency(totalFee, grouping=True)}\n"
        f"------------------------"
    )
    logging.info(logEntry)
    print("\n---🚖 Viaje finalizado 🔚---")

    return createTaximeter()

def calculateFee(moveDuration, stopDuration):
    
    feeBase = 3.5
    feeStop = 0.02
    feeMove = 0.05
    stopFee = stopDuration * feeStop
    moveFee = moveDuration * feeMove
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
        print("1.🚕 Iniciar viaje")
        print("2.⏸️  Pausar/Reanudar viaje")
        print("3.🔚 Finalizar viaje")
        print("4.💨 Salir del programa\n")
        
        option = input("Elige una opción: ")
    
        if option == "1":
            if state['startTime']:
                print("-----------🚦Ya hay un viaje iniciado, puedes finalizarlo para iniciar otro🚦-----------")
            else: 
                state = initRide(state)
            
        
        elif option == "2":
            if not state['startTime']:
                print("-----------🚦No hay un viaje iniciado🚦-----------")
            else:
                state = pauseRide(state)
                

        elif option == "3":
            if not state['startTime']:
                print("-----------🚦No hay un viaje iniciado🚦-----------")
            else:
                state = finishRide(state)
                

        elif option == "4":
            print("-----------Adiós y gracias por usar el taxi 👋-----------")
            break

        else:
            print("-----------Opción no válida, por favor elige una opción correcta-----------")

main()