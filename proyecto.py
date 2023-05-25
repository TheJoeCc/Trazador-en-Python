import cv2
import numpy as np
import time

trayectorias = []

tiempo_inicial = time.time()

def eliminar_trayectoria():
    global trayectorias

    # Limpiar la trayectoria
    mitad = len(trayectorias) // 2
    trayectorias = trayectorias[mitad:]

def detectar_objetos_circulares(frame):
    global trayectorias, tiempo_inicial

    # Usar la escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Suavizado bonito para reducir el ruido en la imagen
    suavizado = cv2.GaussianBlur(gris, (9, 9), 2, 2)

    # Detectar los objetos circulares utilizando el algoritmo de detección de Hough Circles
    circulos = cv2.HoughCircles(suavizado, cv2.HOUGH_GRADIENT, 1, minDist=100,
                               param1=50, param2=30, minRadius=10, maxRadius=200)

    # Verificar si se detectaron círculos
    if circulos is not None:
        circulos = np.round(circulos[0, :]).astype(int)

        # Dibujar y rastrear los círculos detectados
        for (x, y, r) in circulos:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
            trayectorias.append((x, y))  # Agregar posición a la trayectoria

            # Dibujar la trayectoria del círculo
            for i in range(1, len(trayectorias)):
                cv2.line(frame, trayectorias[i-1], trayectorias[i], (0, 255, 0), 2)

    cv2.imshow('GRAVITY TRACKER', frame)

    tiempo_actual = time.time()

    # Verificar si ha pasado 3 segundos
    if tiempo_actual - tiempo_inicial >= 3:
        eliminar_trayectoria()
        tiempo_inicial = tiempo_actual

# Recibir video desde la cámara
captura = cv2.VideoCapture(0)

while True:
    # Leer el frame actual desde la cámara
    ret, frame = captura.read()

    detectar_objetos_circulares(frame)

    # Presionar la tecla 'x' para salir del programa
    if cv2.waitKey(1) == ord('x'):
        break

captura.release()
cv2.destroyAllWindows()
