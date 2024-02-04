from DatabaseApp import DataBaseAccess, Commands, DatabaseClasses
from SimpleSql import Config


class Controller:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super.__new__(cls)
        return cls.__instance

    def __init__(self):
        # TODO: INPUT CHECK
        # TODO: remove testing config, read from file
        self.config = Config(username="root", password="Ka32167890", hostname="localhost",
                             port=0,
                             database_name="Testing", character_set="Testing")
        self.tables = {
            # TODO: Add commands from command pattern
            "Cities": Commands.display_table_actions(
                {
                    # TODO: Continue
                }
            ),
            "Adresses": DatabaseClasses.adreses,
            "Houses": DatabaseClasses.houses,
            "Flat": DatabaseClasses.flats,
            "People": DatabaseClasses.people,
            "People in flats":
        }
        self.database = DataBaseAccess(self.config)
        self.start()

    def start(self):
        Commands.start_to_displayer_command().execute()
        self.__working_loop()

    def __working_loop(self):
        pass
        try:
            # Display all avaliable tables
            choice = Commands.display_tables_obtain_choice(self.tables)
            # Obtain table name
        except Exception:
            raise

        # Display all avaliable actions for the table
        # Obtain desired action
        # Do the action

    def
