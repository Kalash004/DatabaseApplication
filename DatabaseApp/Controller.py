from DatabaseApp import DatabaseClasses as dc
from DatabaseApp import displayCommands as dispC, databaseCommands as dbC
from SimpleSql import Config, Base


class Controller:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        # TODO: INPUT CHECK
        # TODO: remove testing config, read from file
        self.config = Config(username="root", password="Ka32167890", hostname="localhost",
                             port=0,
                             database_name="product_testing", character_set="Testing")
        self.run_loop: bool
        self.commands = {
            # TODO: Add commands from command pattern
            "Cities": dispC.display_and_obtain_action_choice(
                {
                    "Read all": dispC.read_all(dc.cities, self),
                    "Update city": dispC.update(dc.cities, self),
                }
            ),
            "Adresses": dispC.display_and_obtain_action_choice(
                {
                    "Read all": dispC.read_all(dc.adreses, self),
                    "Update": dispC.update(dc.adreses, self),
                }
            ),
            "Houses": dispC.display_and_obtain_action_choice(
                {
                    "Read all": dispC.read_all(dc.houses, self),
                    "Update": dispC.update(dc.houses, self),
                }
            ),
            "Flat": dispC.display_and_obtain_action_choice(
                {
                    "Read all": dispC.read_all(dc.flats, self),
                    "Update": dispC.update(dc.flats, self),
                    # "Add new flat": self.add_flat,  # TODO: Importent
                }
            ),
            "People": dispC.display_and_obtain_action_choice(
                {
                    "Read all": dispC.read_all(dc.people, self),
                    "Update": dispC.update(dc.people, self),
                    # "Add new person": self.add_person
                }
            ),
            "People in flats": dispC.display_and_obtain_action_choice(
                {
                    "Read all": dispC.read_all(dc.people_in_flats, self),  # TODO: Souhrny report
                    "Update": dispC.update(dc.people_in_flats, self),
                    # "Add person to a flat": self.add_person_to_flat
                }
            ),
        }
        self.start()

    def start(self):
        dispC.start_to_displayer_command().execute()
        dbC.start_database(self.config).execute()
        self.__working_loop()

    def __working_loop(self):
        self.run_loop = True
        while self.run_loop:
            table_choice = self.__obtain_table()
            action_choice = self.__obtain_action(table_choice=table_choice)
            action_choice.execute()

    def read_all(self, obj: Base):
        response = dbC.read_all(obj).execute()
        print(response)

    def update(self, obj: Base):
        pass

    def __obtain_table(self):
        table_choice = None
        while table_choice is None:
            try:
                table_choice = dispC.display_and_obtain_choice(self.commands).execute()
            except Exception as err:
                table_choice = None
                dispC.display_user_error(Exception(f"Error happened while enetering table {err}")).execute()
        return table_choice

    def __obtain_action(self, table_choice):
        action_choice = None
        while action_choice is None:
            try:
                action_choice = self.commands[table_choice].execute()
            except Exception as err:
                action_choice = None
                dispC.display_user_error(
                    Exception(f"Error happened while enetering action for table ({table_choice}): {err}")).execute()
        return action_choice
