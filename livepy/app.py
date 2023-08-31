import cv2
import socket

host = '0.0.0.0'
port = 5787

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print('等待客户端连接...')
client_socket, client_address = server_socket.accept()
print('与客户端连接成功:', client_address)

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    
    encoded_frame = cv2.imencode('.jpg', frame)[1].tobytes()
    
    try:
        client_socket.sendall(encoded_frame)
    except socket.error as e:
        print('发送数据失败:', e)
        break

video_capture.release()

client_socket.close()
server_socket.close()
