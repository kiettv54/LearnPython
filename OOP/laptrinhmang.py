from http.server import BaseHTTPRequestHandler, HTTPServer
class SimpleHTTP(BaseHTTPRequestHandler):
	def do_GET(self):
        # SET http status trả về
		self.send_response(200)
        # Thiết lập header trả về
		self.send_header('Content-type','text/html')
		self.end_headers()
		 # Data
		message = "Hello i am master An "
		# Write data dưới dạng utf8
		self.wfile.write(bytes(message, "utf8"))
		return
# Nhận GET request gửi lên.  
# cấu hình host và cổng port cho server
server_address = ('127.0.0.1', 8000)
# Khởi tạo server với thông số cấu hình ở trên.
httpd = HTTPServer(server_address, SimpleHTTP)
# Tiến hành chạy server
httpd.serve_forever()