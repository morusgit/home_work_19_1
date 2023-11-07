from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import time

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов.
    """

    def __get_html_code(self):
        html_path = "index.html"
        try:
            with open(html_path, "r", encoding="utf-8") as file:
                code = file.read()
                return code
        except FileNotFoundError:
            return 'File not found'

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        page_content = self.__get_html_code()
        self.send_response(200)  # Отправка кода ответа.
        self.send_header("Content-type", "index.html")  # Отправка типа данных, который будет передаваться.
        self.end_headers()  # Завершение формирования заголовков ответа.
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа.

if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети.
    # Принимать запросы и отправлять их на обработку специальному классу, который был описан выше.
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов.
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал.
    webServer.server_close()
    print("Server stopped.")