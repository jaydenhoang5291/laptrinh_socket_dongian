from socket import *

serverPort = 12000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))

# bắt đầu lắng nghe kết nối TCP từ client
# 1 là chỉ giữ 1 kết nối chờ trong hàng đợi
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    # chấp nhận kết nối từ client
    # tạo 'connectionSocket' - "đường dây riêng" nói chuyện với client này
    # addr: địa chỉ IP và port của client
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()