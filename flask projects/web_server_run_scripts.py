import http.server
import socketserver
'''
이것은 정적인 파일만을 서비스하는 웹 서버임. CGI 스크립트를 지원하도록 하는 내장 웹서버의 실행은 CGI 스크립트가 있는 디렉토리를 생성해야 함
'''
PORT = 8080  # 어느 포트에서 실행 할 것인지

Handler = http.server.SimpleHTTPRequestHandler  # PORT로 들어오는 요청을 https.serve 모듈이 처리함.

httpd = socketserver.TCPServer(("",PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()  # 소켓 서버가 port로 들어오는 연결을 계속해서 감시하도록 하는 데 사용, 소켓 서버 실행
