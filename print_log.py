from colorama import Fore


class Print:

    class PType(object):
        INFO = 0
        WARNING = 1
        ERROR = 2
        OK = 4
        RESET = 5

    @staticmethod
    def print(msg: str, p_type: PType, end='\n'):
        if p_type == Print.PType.INFO:
            color = Fore.WHITE
        elif p_type == Print.PType.WARNING:
            color = Fore.LIGHTYELLOW_EX
        elif p_type == Print.PType.ERROR:
            color = Fore.LIGHTRED_EX
        elif p_type == Print.PType.OK:
            color = Fore.LIGHTGREEN_EX
        else:
            color = Fore.RESET

        print(f"{color}{msg}", end=end)
