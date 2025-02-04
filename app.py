import datetime 

print("Bienvenid@ al taxímetro")
print("Opciones: ")
print("1. Iniciar el taxímetro")
print("2. Finalizar viaje")
print("3. Salir")

while True:
    print("Opciones:")
    print("1. Iniciar viaje")
    print("2. Finalizar viaje")
    print("3. Salir")

    option = input("Elige una opción: ")

    if option == "1":
        start_time = datetime.datetime.now()


def init():
    feeBase = 3.5
    feeStop = 0.2
    feeKm = 0.3
    initViaje = []

    initViaje = datetime.datetime.now()
    