import datetime 

print("Bienvenid@ al taxímetro")
print("Opciones: ")
print("1. Iniciar el taxímetro")
print("2. Finalizar viaje")
print("3. Ver saldo actual")
print("4. Salir")


feeBase = 3.5
feeStop = 0.02
feeMove = 1.5


def init():
    print("Viaje iniciado!")
    startTime = datetime.datetime.now()
    return startTime

def finish(startTime, duration, distance):
    # endTime = datetime.datetime.now()
    print("Viaje finalizado")
    totalFee = calculateFee(startTime, duration, distance)
    print(f"El costo total del viaje es: €{totalFee:.2f}")
    return totalFee

def calculateFee(startTime, duration = None, distance = None):
    currentTime = datetime.datetime.now()

    if duration is None:
        duration = (currentTime - startTime).total_seconds() / 60

    if distance is None:
        distance = 0

    baseFee = feeBase
    stopFee = duration * feeStop
    moveFee = max(0, duration - 10) * feeMove

    totalFee = baseFee + stopFee + moveFee
    return totalFee
def sale(totalFee):
    actual = 100  
    final = actual - totalFee
    print(f"SALDO ACTUAL: €{actual:.2f}")
    print(f"SALDO FINAL: €{final:.2f}")

def main():
    isStop = False
    startTime = None
    while True:
        print("\nOpciones:")
        print("1. Iniciar viaje")
        print("2. Finalizar viaje")
        print("3. Ver saldo actual")
        print("4. Salir del programa")
        
        option = input("Elige una opción: ")
        # if option == "3":
        #     break
        
        if option == "1":
            if startTime is not None:
                print("Ya hay un viaje iniciado")
            else: 
                startTime = init()
                isStop = True
                print("El taxi está parado")
            # startTime = init()
        
        elif option == "2":
            if startTime is None:
                print("No hay un viaje iniciado")
        duration = (endTime - startTime).total_seconds() / 60
        distance = float(input("Ingrese la distancia recorrida en km: "))

        totalFee = calculateFee(startTime, duration, distance)
        print(f"El costo total del viaje es: ${totalFee:.2f}")
    
