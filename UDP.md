# Ý tưởng chính:
- UDP: gửi dữ liệu không cần kết nối (gửi là đi luôn)
- Phải gắn kèm địa chỉ đích:
  - IP máy nhận
  - Port ứng dụng nhận
 
## Quá trình trao đổi qua UDP socket:
- Client gửi dữ liệu:
  - gõ văn bản -> gửi kèm IP + port của server
- Server nhận gói tin, xử lý
- Server gửi kết quả cho client
- Client hiển thị kết quả lên màn hình

## Lập trình
- Gồm 2 file:
  - `UPDClient.py`
  - `UDPServer.py`
- Chức năng:
  - Client: gõ 1 dòng văn bản -> gửi qua mạng cho server
  - Server: nhận văn bản -> đổi sang chữ in hoa -> gửi lại cho client
  - Client: nhận data từ server -> hiển thị kết quả


## UDPClient
1. Khai báo địa chỉ IP của server
2. Khai báo cổng mà server đang nghe
3. Tạo socket UDP
4. Nhập tin nhắn
5. Gửi tin nhắn cho server
6. Chờ phản hồi
7. In kết quả
8. Đóng socket



## UDPServer
1. Tạo socket UDP
2. Gán socket vào cổng 12000
3. In thông báo sẵn sàng nhận dữ liệu
4. Bắt đầu vòng lặp vô hạn
5. Nhận tin nhắn từ Client
6. Chuyển thành viết hoa
7. Gửi kết quả về Client
