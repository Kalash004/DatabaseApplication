from os import system, name


class Display:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.CHOOSING_STRING = "Please choose using numbers: "
        pass

    @staticmethod
    def display_start():
        welcome_string = ("Dear client, welcome to this humble, small application. \n\r"
                          "It has an ability to work with a database")
        print(welcome_string)

    def display_and_obtain_choices(self, to_choose_from):
        # TODO: Finish
        for i, choice in enumerate(to_choose_from):
            print(f'{i}. {choice}\r')
        try:
            choice = input(self.CHOOSING_STRING)
            choice = int(choice)
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
