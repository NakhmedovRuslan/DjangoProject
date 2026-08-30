# Импорт встроенной библиотеки для работы веб-сервера

from http.server import BaseHTTPRequestHandler, HTTPServer

from cfg import *

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
    Специальный класс, который отвечает за
    обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        try:
            with open(f"{HTML_FILES}/contacts.html", "r", encoding="utf-8") as file:
                html = file.read()
                self.send_response(200)  # Отправка кода ответа

        except FileNotFoundError:
            with open(f"{HTML_FILES}/404.html", "r", encoding="utf-8") as file:
                html = file.read()
                self.send_response(404)  # Отправка кода ответа

        except Exception:
            with open(f"{HTML_FILES}/500.html", "r", encoding="utf-8") as file:
                html = file.read()
                self.send_response(500)  # Отправка кода ответа

        self.send_header(
            "Content-type", "text/html"
        )  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(html.encode("utf-8"))  # Тело ответа


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрах в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
