
#EJERCICIO BÁSICO CON HILOS
# Importa el módulo threading, que permite la creación y manejo de hilos en Python
import threading

# Define una función que toma un mensaje como argumento y lo imprime
def imprimir_mensaje(mensaje):
    print(mensaje)

# Crea un hilo (hilo1) que ejecutará la función imprimir_mensaje con el argumento "Mensaje desde el hilo 1"
hilo1 = threading.Thread(target=imprimir_mensaje, args=("Mensaje desde el hilo 1",))

# Crea otro hilo (hilo2) que ejecutará la función imprimir_mensaje con el argumento "Mensaje desde el hilo 2"
hilo2 = threading.Thread(target=imprimir_mensaje, args=("Mensaje desde el hilo 2",))

# Inicia la ejecución de hilo1
hilo1.start()

# Inicia la ejecución de hilo2
hilo2.start()

# Espera a que hilo1 termine su ejecución antes de continuar
hilo1.join()

# Espera a que hilo2 termine su ejecución antes de continuar
hilo2.join()




# EJERCICIO NÚMEROS PRIMOS
####################################################################################
# Importa el módulo threading, que permite la creación y manejo de hilos en Python
import threading

# Define una función que calcula números primos en un rango dado
def calcular_primos(inicio, fin):
    # Itera sobre cada número en el rango especificado
    for num in range(inicio, fin):
        # Verifica si el número es mayor que 1 (ya que 1 no es primo)
        if num > 1:
            # Itera desde 2 hasta la raíz cuadrada del número para verificar si es primo
            for i in range(2, int(num ** 0.5) + 1):
                # Si el número es divisible por cualquier i, no es primo
                if num % i == 0:
                    break
            else:
                # Si no se encontró ningún divisor, el número es primo
                print(f"Primo encontrado: {num}")

# Crea un hilo (hilo1) que ejecutará la función calcular_primos con el rango de 1 a 500
hilo1 = threading.Thread(target=calcular_primos, args=(1, 500))

# Crea otro hilo (hilo2) que ejecutará la función calcular_primos con el rango de 500 a 1000
hilo2 = threading.Thread(target=calcular_primos, args=(500, 1000))

# Inicia la ejecución de hilo1
hilo1.start()

# Inicia la ejecución de hilo2
hilo2.start()

# Espera a que hilo1 termine su ejecución antes de continuar
hilo1.join()

# Espera a que hilo2 termine su ejecución antes de continuar
hilo2.join()



#EJERCICIO DESCARGA DE DATOS A DOS HILOS
####################################################################################
# Importa el módulo threading, que permite la creación y manejo de hilos en Python
import threading

# Importa el módulo time, que permite trabajar con funciones relacionadas con el tiempo
import time

# Define una función que simula la descarga de datos desde una fuente dada
def descargar_datos(origen):
    # Imprime un mensaje indicando el inicio de la descarga desde la fuente especificada
    print(f"Iniciando descarga desde {origen}...")
    # Simula el tiempo de descarga con una pausa de 2 segundos
    time.sleep(2)
    # Imprime un mensaje indicando que la descarga se ha completado desde la fuente especificada
    print(f"Descarga completada desde {origen}")

# Crea un hilo (hilo1) que ejecutará la función descargar_datos con el argumento "Fuente 1"
hilo1 = threading.Thread(target=descargar_datos, args=("Fuente 1",))

# Crea otro hilo (hilo2) que ejecutará la función descargar_datos con el argumento "Fuente 2"
hilo2 = threading.Thread(target=descargar_datos, args=("Fuente 2",))

# Inicia la ejecución de hilo1
hilo1.start()

# Inicia la ejecución de hilo2
hilo2.start()

# Espera a que hilo1 termine su ejecución antes de continuar
hilo1.join()

# Espera a que hilo2 termine su ejecución antes de continuar
hilo2.join()



# EJERCICIO TRANSFERENCIA DE DINERO CON LOCK
####################################################################################
# Importa el módulo threading, que permite la creación y manejo de hilos en Python
import threading

# Variable global que representa el saldo inicial de una cuenta bancaria
saldo = 1000

# Crea un objeto Lock para asegurar que solo un hilo pueda modificar el saldo a la vez
lock = threading.Lock()

# Define una función para depositar una cantidad de dinero en la cuenta
def depositar(monto):
    global saldo
    # Utiliza el lock para asegurar que solo un hilo pueda ejecutar este bloque de código a la vez
    with lock:
        # Calcula el nuevo saldo después del depósito
        nuevo_saldo = saldo + monto
        # Imprime un mensaje indicando la cantidad depositada y el nuevo saldo
        print(f"Depositando {monto}, saldo nuevo: {nuevo_saldo}")
        # Actualiza el saldo global con el nuevo saldo
        saldo = nuevo_saldo

# Define una función para retirar una cantidad de dinero de la cuenta
def retirar(monto):
    global saldo
    # Utiliza el lock para asegurar que solo un hilo pueda ejecutar este bloque de código a la vez
    with lock:
        # Verifica si hay suficiente saldo para realizar el retiro
        if saldo >= monto:
            # Calcula el nuevo saldo después del retiro
            nuevo_saldo = saldo - monto
            # Imprime un mensaje indicando la cantidad retirada y el nuevo saldo
            print(f"Retirando {monto}, saldo nuevo: {nuevo_saldo}")
            # Actualiza el saldo global con el nuevo saldo
            saldo = nuevo_saldo
        else:
            # Imprime un mensaje indicando que no hay suficiente saldo para realizar el retiro
            print("Saldo insuficiente")

# Crea un hilo (hilo1) que ejecutará la función depositar con el argumento 500
hilo1 = threading.Thread(target=depositar, args=(500,))

# Crea un hilo (hilo2) que ejecutará la función retirar con el argumento 700
hilo2 = threading.Thread(target=retirar, args=(700,))

# Crea un hilo (hilo3) que ejecutará la función retirar con el argumento 300
hilo3 = threading.Thread(target=retirar, args=(300,))

# Inicia la ejecución de hilo1
hilo1.start()

# Inicia la ejecución de hilo2
hilo2.start()

# Inicia la ejecución de hilo3
hilo3.start()

# Espera a que hilo1 termine su ejecución antes de continuar
hilo1.join()

# Espera a que hilo2 termine su ejecución antes de continuar
hilo2.join()

# Espera a que hilo3 termine su ejecución antes de continuar
hilo3.join()