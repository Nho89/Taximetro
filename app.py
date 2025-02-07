import datetime 

print("Bienvenid@ al taxímetro")
print("El taxímetro funciona de la siguiente manera:")




def initRide():
    print("\n---Viaje iniciado!---")
    startTime = datetime.datetime.now()
    statusChange = startTime
    currentStatus = "move"
    return startTime, statusChange, currentStatus, 0, 0

def pauseRide(currentStatus, statusChange, moveDuration, stopDuration):
    now = datetime.datetime.now()
    elapsed = (now - statusChange).total_seconds() / 60 
    if currentStatus == "move":
        moveDuration += elapsed
        currentStatus = "pause"
        print("Viaje en pausa")

    else:
        stopDuration += elapsed
        currentStatus = "move"
        print("Viaje reanudado")
    return currentStatus, now, moveDuration, stopDuration

def changeStatus(currentStatus, statusChange, moveDuration, stopDuration):
    now = datetime.datetime.now()
    elapsed = (now - statusChange).total_seconds() / 60

    if currentStatus == "move":
        moveDuration += elapsed
        currentStatus = "stop"
        print("Viaje detenido")
    else:
        stopDuration += elapsed
        currentStatus = "move"
        print("Taxi en movimiento")

    return currentStatus, now, moveDuration, stopDuration    

def finishRide(start_time, currentStatus, statusChange, moveDuration, stopDuration):
    now = datetime.datetime.now()
    elapsed = (now - start_time).total_seconds() / 60
    if currentStatus == "move":
        move_duration += elapsed
    elif currentStatus == "stop":
        stop_duration += elapsed

    totalFee = calculateFee(moveDuration, stopDuration)    
    print("\n---Viaje finalizado---")
    
    print(f"El costo total del viaje es: €{totalFee:.2f}")
    return totalFee, moveDuration, stopDuration

def calculateFee(startTime, duration = None, distance = None):
    currentTime = datetime.datetime.now()

    if duration is None:
        duration = (currentTime - startTime).total_seconds() / 60

    if distance is None:
        distance = 0
    feeBase = 3.5
    feeStop = 0.02
    feeMove = 1.5
    baseFee = feeBase
    stopFee = duration * feeStop
    moveFee = max(0, duration - 10) * feeMove

    totalFee = baseFee + stopFee + moveFee
    return totalFee

def resume(totalFee, duration, distance):
    print("\n--- Resumen del viaje ---")
    print(f"Duración: {duration:.2f} minutos")
    print(f"Distancia: {distance:.2f} km")
    print(f"Tarifa total: €{totalFee:.2f}")
    print("------------------------")

def main():
    # isStop = False
    startTime = None
    while True:
        print("\nOpciones:")
        print("1. Iniciar viaje")
        print("2. Finalizar viaje")
        print("3. Salir del programa")
        
        option = input("Elige una opción: ")
    
        if option == "1":
            if startTime is not None:
                print("Ya hay un viaje iniciado, puedes finalizarlo para iniciar otro")
            else: 
                startTime = initRide()
            
        
        elif option == "2":
            if startTime is None:
                print("No hay un viaje iniciado")
            else:
                endTime = datetime.datetime.now()
                duration = (endTime - startTime).total_seconds() / 60

                while True:
                    try:
                        distance = float(input("\nIngrese la distancia recorrida: "))
                        break
                    except ValueError:
                        print("Debe ingresar un número")

        

                # if isStop:
                #     print("El taxi está parado, se cobrará el precio base")

                #     totalFee = feeBase
                #     print(f"Se le cobrará: {totalFee:.2f}")
                #     sale(totalFee)
                #     startTime = None
                #     isStop = False
                # else:
                totalFee = finishRide(startTime, duration, distance)
                resume(totalFee, duration, distance)
                startTime = None
                

        elif option == "3":
            print("Gracias por usar el taxímetro, adios!")
            break
        else:
            print("Opción no válida, por favor elija una opción válida")

main()