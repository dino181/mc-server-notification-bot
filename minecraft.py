from enum import Enum, auto
import mcstatus
import time

TRIES = 5


class Status(Enum):
    ON = auto()
    OFF = auto()


def get_status(server_adress: str) -> Status:
    for i in range(TRIES):
        try:
            server = mcstatus.JavaServer.lookup(server_adress)
            server.ping()
            return Status.ON

        except Exception:
            print(f"Failed to ping server: {i + 1}/{TRIES}")

    return Status.OFF
