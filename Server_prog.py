import pickle
import socket
import cv2
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname(socket.gethostname())
port = 8088
s.bind((ip, port))
s.listen(10)

conn, addr = s.accept()
data = b''
payload_size = struct.calcsize("=I")
print("Connected from " + str(addr))



while True:
    cap=cv2.VideoCapture(0)
    while(cap.isOpened()):
        ret,frame=cap.read()
        data = pickle.dumps(frame)
        message_size = struct.pack("=I", len(data))
        conn.sendall(message_size + data)
        cv2.imshow('Server', frame)
        key=cv2.waitKey(1) & 0xFF
        if key==ord('q'):
            cv2.destroyAllWindows()


conn.close()
