# laptrinh_socket_dongian

Mục tiêu: hiểu các viết chương trình để 2 máy tính giao tiếp qua mạng

Một ứng dụng mạng luôn gồm 2 phần:
- Client: gửi yêu cầu (VD: trình duyệt web)
- Server: nhận và xử lý yêu cầu (VD: máy chủ web)

Giao tiếp qua Socket:
- Socket: ống nối giữa 2 chương trình ở 2 máy khác nhau
- Khi chạy chương trình:
  - Client: tạo **client process**
  - Server: tạo **server process**
- Hai process này đọc và ghi dữ liệu qua socket

Khi lập trình ứng dụng mạng cần:
- Viết code cho Client
- Viết code cho Server
- Chọn giao thức để truyển dữ liệu TCP or UDP
