import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QLabel, QMainWindow
from PyQt5.QtGui import QImage, QPixmap

import socketserver, threading

IDX_IMAGE = 1


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        IDX_IMAGE = (IDX_IMAGE + 1) % 4
        print(self.data)


def network_thread():
    HOST, PORT = "0.0.0.0", 4002

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print(f"Listening at: {HOST}:{PORT}")
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()


def main():
    app = QApplication(sys.argv)

    widget = QMainWindow()  # define your widget
    label = QLabel()

    image = QImage(f"patterns/pattern{IDX_IMAGE}.jpg")
    label.setPixmap(QPixmap.fromImage(image))
    
    widget.setCentralWidget(label)

    display_monitor = 1  # the number of the monitor

    monitor = QDesktopWidget().screenGeometry(display_monitor)
    widget.move(monitor.left(), monitor.top())
    widget.showFullScreen()

    # threading.Thread(target=network_thread).start()

    app.exec_()
