from enum import Enum, auto
import mcstatus


class Status(Enum):
    ON = auto()
    OFF = auto()


def get_status(server_adress: str) -> Status:
    try:
        server = mcstatus.JavaServer.lookup(server_adress)
        server.ping()
        return Status.ON

    except Exception:
        return Status.OFF
