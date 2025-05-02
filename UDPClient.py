# Import thư viện để dùng socket trong python 
from socket import *

# Địa chỉ của server, localhost = gửi đến chính máy đang chạy (nếu client và server cùng máy)
# nếu gửi đến máy khác thì viết hostname hoặc IP của nó
serverName = 'localhost'

# Cổng server đang mở
serverPort = 12000

# Tạo socket UDP: AF_INET = IPv4, SOCK_DGRAM = UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Nhập data
message = input('Input lowercase sentence:')

# sendto(...) gửi tin nhắn đến server
# message.encode() chuyển chuỗi thành bytes vì socket chỉ truyền bytes
clientSocket.sendto(message.encode(),(serverName, serverPort))

# recvfrom(2048): chờ nhận phản hồi từ server, tối đa 2048 bytes
# modifiedMessage: dữ liệu nhận được
# serverAddress: IP và port của server gửi về 
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode())

clientSocket.close()