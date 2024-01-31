class ConnectionException(Exception):
    def __init__(self, message):
        self.exception = "Execption happened during connection initiation"
        self.message = message
        super(message)

    def __repr__(self):
        return f"{self.exception} : {self.message}"
