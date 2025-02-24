import cv2
import numpy as np

original = cv2.imread('c:/Users/edrib/Documents/Repos/Cero.hero.python/5_Contador_monedas/monedassoles.jpg')
grises = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

#GaussianBlur
'''
    El método GaussianBlur se utiliza para reducir el ruido de la imagen.
    El primer argumento es la imagen de entrada.
    El segundo argumento es el tamaño del kernel, que debe ser un número impar.
    El tercer argumento es la desviación estándar en X.
    ó en otras palabras suaaviza la imagen. para una mejor visualización.
'''
valorMatrix = 1
valorKernel = 33
desviacionEnX = 0
desenfoque = cv2.GaussianBlur(grises, (valorMatrix, valorMatrix), desviacionEnX)

# Canny
'''
    El método Canny se utiliza para detectar bordes en la imagen.
    El primer argumento es la imagen de entrada.
    El segundo argumento es el umbral mínimo.
    El tercer argumento es el umbral máximo.
'''
umbralMinimo = 30
umbralMaximo = 100
bordes = cv2.Canny(desenfoque, umbralMinimo, umbralMaximo)

# Tomar solamente el contorno extene y omitir los internos
kernel = np.ones((valorKernel, valorKernel), np.uint8)

'''
    Se toma la imagen de los bordes y se aplica un cierre
    El cierre es una operación que combina dilatación y erosión.
    Se utiliza para cerrar pequeños agujeros dentro de los objetos o pequeños puntos en la superficie del objeto.
    El primer argumento es la imagen de entrada.
    El segundo argumento es el tipo de operación de cierre.
    El tercer argumento es el kernel que se utilizará durante la operación.
'''
cierreContorno = cv2.morphologyEx(bordes, cv2.MORPH_CLOSE, kernel)
contornos, jerarquia = cv2.findContours(cierreContorno.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('Monedas encontradas: {}'.format(len(contornos)))
# Mostrar imagen
cv2.imshow('Imagen en escala de grises', grises)
cv2.imshow('Imagen sin ruido - Gauss', desenfoque)
cv2.imshow('Bordes', bordes)
cv2.imshow('Cierre', cierreContorno)
cv2.drawContours(original, contornos, -1, (0, 0, 255), 2)
cv2.imshow('Contornos', original)
cv2.waitKey(0)