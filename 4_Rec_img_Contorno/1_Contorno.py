import cv2

image = cv2.imread('c:/Users/edrib/Documents/Repos/Cero.hero.python/4_Rec_img_Contorno/contorno.jpg') # Cargar imagen de la ruta
if image is None:
	raise FileNotFoundError("The image file was not found.")

'''
Luego de tener la imagen se procede a convertirla a escala de grises.
Pero antes de eso se deben encontrar o definir los contornos de la imagen.
para ello se utiliza la función cv2.findContours() que recibe como parámetros
la imagen en escala de grises y el modo de recuperación de contornos.
- Existen varios modos de recuperación de contornos, pero el más común es:
	* APROX_SIMPLE: Aproxima los contornos a una línea recta.
	* APROX_NONE: Devuelve todos los contornos sin aproximar.

Para ello debemos tener una imagen umbralicada, es decir, una imagen en blanco y negro.
'''
# Converir imagen a escala de grises
grises = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convertir imagen a escala de grises

# Aplicar umbralización
tipoUmbral,umbral = cv2.threshold(grises, 100, 255, cv2.THRESH_BINARY) # Puedo crear una variable fictici poniendo un _ ejemplo: _,umbral

# Contornos y jerarquias
contorno, jerarquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos
cv2.drawContours (image, contorno, -1,(0,255,0), 3)


# Mostrar imagen original
cv2.imshow('Original', image) # Mostrar imagen original
#cv2.imshow('Grises', grises) # Mostrar imagen con escala de grises
#cv2.imshow('Umbral', umbral) # Mostrar imagen con umbralización
cv2.waitKey(0) # Esperar a que se presione una tecla
cv2.destroyAllWindows() # Cerrar todas las ventanas


