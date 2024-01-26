from enum import Enum


class ConnectionState(Enum):
    CLOSED = 0
    CONNECTED = 1
    CONNECTING = 2
    CLOSING = 3
    ERROR = 4
