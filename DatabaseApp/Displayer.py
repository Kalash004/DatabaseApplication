from os import system, name


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

    def display_tables_obtain_choice(self, tables):
        # TODO: Finish
        for i, table in enumerate(tables):
            print(f'{i}. {table}\r\n')
        try:
            choice = input("Please choose using numbers")
            choice = int(choice)
            return tables[choice]
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
