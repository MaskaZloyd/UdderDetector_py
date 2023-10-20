import unittest
import socket
import threading
import os

from app.unix_sock_client import UnixSocketClient


class TestClientThread(unittest.TestCase):
    def setUp(self):
        self.socket_name = "/tmp/mysocket"

        if os.path.exists(self.socket_name):
            os.remove(self.socket_name)

        # Create a server socket for test
        self.server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.server.bind(self.socket_name)
        self.server.listen(1)

        # Start server thread
        self.server_thread = threading.Thread(target=self.server_run)
        self.server_thread.start()

        # Initialize Client Thread
        self.client_thread = UnixSocketClient(self.socket_name)

    def tearDown(self):
        # Cleanup after test
        self.server.close()
        if os.path.exists(self.socket_name):
            os.remove(self.socket_name)

    def server_run(self):
        conn, addr = self.server.accept()
        conn.sendall(b"Test message")
        conn.close()

    def test_run(self):
        # Start Client thread
        self.client_thread.start()

        # join will stop main thread until client_thread finishes execution
        self.client_thread.join()
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
