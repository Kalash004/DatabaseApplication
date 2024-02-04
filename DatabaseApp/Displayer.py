from os import system, name


class Display:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.CHOOSING_STRING = "Please choose using numbers: "
        self.EMPTY_RESULT = "Empty"
        self.SHOWING_TABLE = "Showing data in table"
        pass

    @staticmethod
    def display_start():
        welcome_string = ("Dear client, welcome to this humble, small application. \n\r"
                          "It has an ability to work with a database. \n\r"
                          "Made by Anton Kalashnikov")
        print(welcome_string)

    def display_and_obtain_choices(self, to_choose_from):
        # TODO: Finish
        for i, choice in enumerate(to_choose_from):
            print(f'{i + 1}. {choice}\r')
        try:
            choice = input(self.CHOOSING_STRING)
            choice = int(choice) - 1
            choice = list(to_choose_from)[choice]
            return choice
        except Exception:
            self.clear()
            raise

    @staticmethod
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    @staticmethod
    def display_error(error_msg):
        # TODO: Add red coloring
        print(f"User error happened, please check your inputs: {error_msg}")

    def display_tables(self, to_display, table_name):
        self.clear()
        print(f"{self.SHOWING_TABLE}: {table_name}")
        if len(to_display) < 1:
            print(self.EMPTY_RESULT + "\n")
            return
        for instance in to_display:
            self.__display_item(instance)

    @staticmethod
    def __display_item(item):
        print(f"{item}\r")

    @staticmethod
    def display_message(msg):
        print(msg)

    @staticmethod
    def request(msg):
        return input(msg)
