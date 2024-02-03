class Display:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        pass

    @staticmethod
    def display_start():
        welcome_string = ("Dear client, welcome to this humble, small application. \n\r"
                          "It has an ability to work with a database")
        print(welcome_string)
