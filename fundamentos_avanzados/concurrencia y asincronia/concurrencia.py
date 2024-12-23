import threading
import time


# función que simula procesamiento de una solicitud
def process_request(request_id):
    print(f"Procesando solicitud {request_id}")
    time.sleep(3)
    print(f"Solicitud {request_id} completada")

threads = []

for i in range(3):
    # crear nuevo hilo que ejecutara la funcion
    tread = threading.Thread(target=process_request, args= (i,))
    threads.append(tread)
    tread.start()

# espear que todos los hilos terminen
for thread in threads:
    #asegura del el programa espere que termine cada hilo
    thread.join()

print("todosa las solicitudes completadas")