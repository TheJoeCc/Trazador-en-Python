import cv2
import numpy as np

# Lista para almacenar las trayectorias de los círculos
trayectorias = []

def detectar_objetos_circulares(frame):
    global trayectorias

    # Convertir el frame a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar suavizado para reducir el ruido
    suavizado = cv2.GaussianBlur(gris, (9, 9), 2, 2)

    # Detectar círculos utilizando el algoritmo de detección de Hough Circles
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

    # Mostrar el frame resultante
    cv2.imshow('Detección de objetos circulares', frame)

# Crear una instancia para capturar video desde la cámara
captura = cv2.VideoCapture(0)

while True:
    # Leer el frame actual desde la cámara
    ret, frame = captura.read()

    # Llamar a la función para detectar objetos circulares
    detectar_objetos_circulares(frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
captura.release()
cv2.destroyAllWindows()