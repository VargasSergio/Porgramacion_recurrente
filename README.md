# Programación Concurrente: Ejemplos y Aplicaciones

Este repositorio contiene los ejemplos utilizados en el documento "Programación Concurrente", donde se exploran los conceptos básicos y avanzados de este paradigma mediante implementaciones en Python.

## Contenido

1. **[Ejemplo 1: Imprimir mensajes en paralelo](#ejemplo-1-imprimir-mensajes-en-paralelo)**
    - Uso básico de `threading` para ejecutar tareas simultáneamente.

2. **[Ejemplo 2: Cálculo de números primos](#ejemplo-2-cálculo-de-números-primos)**
    - División del trabajo computacional en rangos paralelos.

3. **[Ejemplo 3: Descarga de datos simulada](#ejemplo-3-descarga-de-datos-simulada)**
    - Simulación de tareas de I/O concurrentes.

4. **[Ejemplo 4: Banco de cuentas con sincronización](#ejemplo-4-banco-de-cuentas-con-sincronización)**
    - Uso de `Lock` para evitar condiciones de carrera.

## Ejemplo 1: Imprimir mensajes en paralelo

### Descripción
Este ejemplo muestra cómo utilizar hilos para imprimir dos mensajes simultáneamente.

### Código
```python
import threading

def imprimir_mensaje(mensaje):
    print(mensaje)

hilo1 = threading.Thread(target=imprimir_mensaje, args=("Mensaje desde el hilo 1",))
hilo2 = threading.Thread(target=imprimir_mensaje, args=("Mensaje desde el hilo 2",))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
```

## Ejemplo 2: Cálculo de números primos

### Descripción
Divide la búsqueda de números primos en dos rangos distintos que se procesan simultáneamente.

### Código
```python
import threading

def calcular_primos(inicio, fin):
    for num in range(inicio, fin):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(f"Primo encontrado: {num}")

hilo1 = threading.Thread(target=calcular_primos, args=(1, 500))
hilo2 = threading.Thread(target=calcular_primos, args=(500, 1000))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
```

## Ejemplo 3: Descarga de datos simulada

### Descripción
Simula la descarga de datos desde dos fuentes diferentes al mismo tiempo.

### Código
```python
import threading
import time

def descargar_datos(origen):
    print(f"Iniciando descarga desde {origen}...")
    time.sleep(2)  # Simula el tiempo de descarga
    print(f"Descarga completada desde {origen}")

hilo1 = threading.Thread(target=descargar_datos, args=("Fuente 1",))
hilo2 = threading.Thread(target=descargar_datos, args=("Fuente 2",))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
```

## Ejemplo 4: Banco de cuentas con sincronización

### Descripción
Gestiona de manera segura el acceso concurrente a una cuenta bancaria compartida utilizando un bloqueo (`Lock`).

### Código
```python
import threading

saldo = 1000
lock = threading.Lock()

def depositar(monto):
    global saldo
    with lock:
        nuevo_saldo = saldo + monto
        print(f"Depositando {monto}, saldo nuevo: {nuevo_saldo}")
        saldo = nuevo_saldo

def retirar(monto):
    global saldo
    with lock:
        if saldo >= monto:
            nuevo_saldo = saldo - monto
            print(f"Retirando {monto}, saldo nuevo: {nuevo_saldo}")
            saldo = nuevo_saldo
        else:
            print("Saldo insuficiente")

hilo1 = threading.Thread(target=depositar, args=(500,))
hilo2 = threading.Thread(target=retirar, args=(700,))
hilo3 = threading.Thread(target=retirar, args=(300,))

hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()
```


```bash
python ejemplo1.py
python ejemplo2.py
python ejemplo3.py
python ejemplo4.py
```

## Consideraciones
- Estos ejemplos son demostraciones básicas del paradigma de programación concurrente.
- Se recomienda analizar los resultados y reflexionar sobre los desafíos comunes, como las condiciones de carrera y la sincronización adecuada de tareas.

## Recursos adicionales
- [Documentación oficial de Python - threading](https://docs.python.org/3/library/threading.html)
- [Introducción a la programación concurrente en Python](https://realpython.com/intro-to-python-threading/)
