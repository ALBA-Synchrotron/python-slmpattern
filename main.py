from socket import INADDR_LOOPBACK
import sys, os, socketserver, threading
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QLabel, QMainWindow
from PyQt5.QtGui import QImage, QPixmap

PATTERNS_PATH = "patterns"
display_monitor = 1  # the number of the monitor
patterns = os.listdir(PATTERNS_PATH)
app = QApplication(sys.argv)
label = QLabel()
IDX_IMAGE = 0


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        global IDX_IMAGE
        # self.request is the TCP socket connected to the client
        while True:
            self.data = self.request.recv(1024).strip()
            print(f"Loading pattern: {PATTERNS_PATH}/{patterns[IDX_IMAGE]}")
            IDX_IMAGE = (IDX_IMAGE + 1) % len(patterns)
            image = QImage(f"{PATTERNS_PATH}/{patterns[IDX_IMAGE]}")
            label.setPixmap(QPixmap.fromImage(image))


def network_thread():
    HOST, PORT = "0.0.0.0", 4002

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print(f"Listening at: {HOST}:{PORT}")
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()


def main():
    widget = QMainWindow()  # define your widget

    image = QImage(f"{PATTERNS_PATH}/{patterns[0]}")
    label.setPixmap(QPixmap.fromImage(image))

    widget.setCentralWidget(label)
    monitor = QDesktopWidget().screenGeometry(display_monitor)
    widget.move(monitor.left(), monitor.top())
    widget.showFullScreen()

    threading.Thread(target=network_thread).start()

    app.exec_()


if __name__ == "__main__":
    main()
