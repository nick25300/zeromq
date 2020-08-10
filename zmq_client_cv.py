import cv2
import zmq
import base64
import numpy as np

context = zmq.Context()
footage_socket = context.socket(zmq.SUB)
footage_socket.bind('tcp://*:5555')
footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

while True:
#for i in range(0,1):
    try:
        frame = footage_socket.recv_string() ###Unicode Format
        
        frame = frame.encode() ###Bytes Format
        #frame = frame[0:len(frame)-1]+"=" + "'"
        #print(frame)
    
        img = base64.b64decode(frame)
        #print(img)
        npimg = np.fromstring(img, dtype=np.uint8)
        
        source = cv2.imdecode(npimg, 1)
        print(source)
        cv2.imshow("image", source)
        cv2.waitKey(1)

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        print("\n\nBye bye\n")
        break
