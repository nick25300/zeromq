import cv2
import zmq
import base64

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
#footage_socket.connect('tcp://localhost:5555')
#footage_socket.connect('tcp://localhost:5555')
footage_socket.connect('tcp://192.168.0.105:8554')

cap = cv2.VideoCapture(0)  # init the camera

while True:
    try:
        ret, frame = cap.read()  
    
        encoded, buffer = cv2.imencode('.jpg', frame)
        buffer=base64.b64encode(buffer) ##Bytes Format
        buffer = buffer.decode('unicode_escape') ##Unicode Format
        #buffer = buffer.encode("utf-8")
        footage_socket.send_string(buffer)

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        print("\n\nBye bye\n")
        break

    


