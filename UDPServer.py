from socket import *

# gán cổng giao tiếp cho server là 12000
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# gán socket với port 12000 để chờ nhận dữ liệu
# ' ': chuỗi rỗng, đại diện cho IP mặc định của máy chủ -> chấp nhận kết nối từ tất cả các địa chỉ IP của máy tính này
serverSocket.bind(('', serverPort))

print('The server is ready to receive')

#
while True:
 message, clientAddress = serverSocket.recvfrom(2048)
 modifiedMessage = message.decode().upper()
 serverSocket.sendto(modifiedMessage.encode(), clientAddress)