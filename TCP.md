## TCP là giao thức có kết nối
- Trước khi gửi/nhận dữ liệu, client và server phải thiết lập kết nối TCP (handshake)
- Kết nối này gắn liền với:
  - IP và port của client
  - IP và port của server
 
## Khác với UDP
- UDP: mỗi lần gửi lại phải chỉ rõ địa chỉ đích
- TCP: chỉ cần gửi vào kết nối đã mở, không cần nêu lại địa chỉ

## Tương tác TCP giữa client và server
1. Client là bên chủ động kết nối
- Client gõ cửa Server bằng cách mở một kết nối TCP tới địa chỉ IP và port của server
- Server phải chạy trước và sẵn sàng lắng nghe kết nối

2. Server cần có "cửa chào đón"
- Khi client kết nối -> Server tạo 1 cửa riêng (``connectionSocket``) chỉ để giao tiếp với client đó
- Tưởng tượng:
  - ``serverSocket``: lễ tân
  - ``connectionSocket``: phòng riêng để tiếp khách
