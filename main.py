from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"  # Адрес для доступа по сети
serverPort = 5000  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):

    @staticmethod
    def __get_html_content():
        """Метод для открытия файла HTML"""
        html_file = open('https://github.com/dikiypes/dz6-1.git/index.html', 'r', encoding='utf-8')
        source_code = html_file.read()
        return source_code

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        name = query_components.get('firstName', [''])[0]
        email = query_components.get('eMail', [''])[0]
        print(f"Имя: {name}")
        print(f"Почта: {email}")
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    # Инициализация веб-сервера
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

