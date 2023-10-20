import socket
import threading
import queue
from typing import List
import time
import app.command as cmd
import app.command_types as cmdtype
from app.logger import Logger


class UnixSockClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.buffer = b""
        self.commands = queue.Queue()
        self.is_writing = False

    def connect_to_socket(self, socket_path: str):
        self.client.connect(socket_path)
        self.sock_read_thread = threading.Thread(target=self.on_socket_ready_read)
        self.sock_read_thread.start()

    def disconnect_from_socket(self):
        self.client.close()

    def on_socket_ready_read(self):
        while True:
            response = self.client.recv(1024)
            if not response:
                break
            self.buffer += response
            command = self.parse_command(self.buffer.decode())
            # Assume we have method command_parsed that needs to be triggered.
            # self.command_parsed(command)
            self.buffer = b""

    def write_to_socket(self, command: str):
        self.commands.put(command)
        if not self.is_writing:
            self.is_writing = True
            self.write_next_command()

    def write_next_command(self):
        if not self.commands.empty():
            command = self.commands.get()
            time.sleep(0.1)
            formatted_command = self.format_command(command).encode()
            self.client.send(formatted_command)
            if not self.commands.empty():
                self.write_next_command()

    def format_command(self, command: cmd.Command) -> str:
        result_string_command = cmdtype.OUTPUT_COMMANDS[command.command_name]
        result_string_command += "("

        for i in range(len(command.params)):
            result_string_command += command.params[i]
            if i < len(command.params) - 1:
                result_string_command += ";"

        result_string_command += ")"
        return result_string_command

    def parse_command(self, message: str) -> str:
        open_brace_pos = message.find("(")
        close_brace_pos = message.find(")")

        if open_brace_pos == -1 or close_brace_pos == -1:
            return cmd.Command(cmdtype.InputCommandType.BAD_COMMAND, [])

        string_command_name = message[:open_brace_pos].strip()
        string_params = message[open_brace_pos + 1 : close_brace_pos].split(";")

        vec_params = [param.strip() for param in string_params]

        command_name_enum = None
        for command in cmdtype.INPUT_COMMANDS:
            if command.value == string_command_name:
                command_name_enum = command

        if not command_name_enum:
            Logger.logger.error("invalid command name")

        return cmd.Command(command_name_enum, vec_params)
