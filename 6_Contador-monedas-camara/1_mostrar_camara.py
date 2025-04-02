import cv2 as cv

capturarVideo = cv.VideoCapture(0)

if not capturarVideo.isOpened():
    print("Error al abrir la cámara")
    exit()
    
while True:
    ret, frame = capturarVideo.read()
    #grises = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #cv.imshow("cam grises", grises)
    cv.imshow("Camara", frame)
    if cv.waitKey(1) == ord('q'):
        break
    
capturarVideo.release()
cv.destroyAllWindows()    
    
