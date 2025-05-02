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
