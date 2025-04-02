import cv2 as cv
import numpy as np

def ordenarPuntos(puntos):
    nPuntos = np.concatenate([puntos[0], puntos[1], puntos[2], puntos[3]]).tolist()
    y_order = sorted(nPuntos, key=lambda nPuntos: nPuntos[1])
    x1_order = y_order[0:2]
    x1_order = sorted(x1_order, key=lambda x1_order: x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key=lambda x2_order: x2_order[0])
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

def alineamiento(imagen, ancho, alto):
    imagenAlineada = None
    grises = cv.cvtColor(imagen, cv.COLOR_BGR2GRAY)
    _, umbral = cv.threshold(grises, 150, 255, cv.THRESH_BINARY)
    contorno= cv.findContours(umbral, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
    contorno = sorted(contorno, key=cv.contourArea, reverse=True)[:1]
    for c in contorno:
        epsilon = 0.01*cv.arcLength(c, True)
        aprox = cv.approxPolyDP(c, epsilon, True)
        
        if len(aprox) == 4:
            puntos = ordenarPuntos(aprox)
            puntos1 = np.float32(puntos)
            puntos2 = np.float32([[0,0], [ancho,0], [0,alto], [ancho,alto]])
            M = cv.getPerspectiveTransform(puntos1, puntos2)
            imagenAlineada = cv.warpPerspective(imagen, M, (ancho, alto))
    return imagenAlineada
capturarVideo = cv.VideoCapture(0)

while True:
    ret, frame = capturarVideo.read()
    if ret == False:
        break
    imagenA6 = alineamiento(frame, ancho=480, alto=640)
    if imagenA6 is not None:
        puntos=[]
        imagenGrises = cv.cvtColor(imagenA6, cv.COLOR_BGR2GRAY)
        gaussiana = cv.GaussianBlur(imagenGrises, (5,5), 1)
        _, umbral2 = cv.threshold(gaussiana, 0, 255, cv.THRESH_OTSU+cv.THRESH_BINARY_INV)
        contorno2, _ = cv.findContours(umbral2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        cv.imshow("Imagen Alineada", umbral2)
        cv.drawContours(imagenA6, contorno2, -1, (255,0,0), 2)
        suma1 = 0.0
        suma2 = 0.0
        for c2 in contorno2:
            area = cv.contourArea(c2)
            M = cv.moments(c2)
            if (M["m00"]==0): 
                M["m00"]=1.0
            x = int(M["m10"]/M["m00"])
            y = int(M["m01"]/M["m00"])
                        
            if area<9300 and area>8000:
                font = cv.FONT_HERSHEY_SIMPLEX;
                cv.putText(imagenA6, "Moneda de 1", (x,y), font, 0.75, (0,255,0), 2)
                suma1 += suma1 + 0.2
                
            if area<7800 and area>6500:
                font = cv.FONT_HERSHEY_SIMPLEX;
                cv.putText(imagenA6, "Moneda de 1", (x,y), font, 0.75, (0,255,0), 2)
                
                suma2 += suma2 + 0.1    
        totalSuma = suma1 + suma2
        print("Total: ", round(totalSuma, 2)) 
        cv.imshow("Contador de Monedas", imagenA6)
        cv.imshow("Camara", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
capturarVideo.release()
cv.destroyAllWindows()